from operator import itemgetter

from JobParser import settings
from scraping.management import email_thread
from scraping.management.matcher import *
from scraping.models import Employee, Skill


class EmployeeProcessor:

    def __init__(self, jobs):
        self.jobs = jobs

    def _process(self, employee):
        pass


    def _send_email(self, email, job_title):
        title = f'Regarding your "{job_title}" position'
        text = 'We have a candidate that might fit your position, please contact us if you are interested'
        print(email, ' -> ',title)
        email = settings.EMAIL_HOST_USER
        email_thread.send_html_mail(title, text, [email], settings.EMAIL_HOST_USER)

    def run(self, request, is_send_mails, top_count, min_percent):
        print("###", request.position)
        recommendations = self.load_csv()
        variants = list()
        # Skills of our candidate. Transform from text to list
        request_skills = request.skills_text.splitlines()
        # TO_FIX: Jobs пиходит как dict из match.py
        for job in self.jobs:
            if job.get('site') is None:
                continue
            percentage, must_have_skills = vacancy_percentage(request_skills, job.get('description', ''))
            skill_courses, names = courses_advice(recommendations, must_have_skills)
            variants.append((percentage, job, skill_courses, names))

        if len(variants) > 0:
            top_list = sorted(variants, key=itemgetter(0), reverse=True)
            for variant in top_list[:top_count]:
                percentage = variant[0]
                if percentage >= min_percent:

                    job = variant[1]
                    skill_courses = variant[2]
                    names = variant[3]
                    email = job.get('email')
                    print(percentage, '% -', email, job.get('title', ''), '\n', variant[3])

                    skills = []
                    for skill_name in request_skills:
                        # Create only missing skills
                        link = ''
                        if skill_name in names:
                            # Search missing skill for learning materials
                            for course in skill_courses:
                                # Search in CSV by eng/de skill name 
                                if course[0] == skill_name or course[1] == skill_name:
                                    link = course[2]
                                    break
                            s = Skill(name=skill_name, isset=False, link=link)
                            s.save()
                            skills.append(s)

                    print('SKILLS TO LEARN', skills)
                    employee = Employee.objects.create()
                    employee.status = request.status
                    employee.conformity = percentage
                    employee.position = request.position
                    employee.vacancy = job
                    employee.save()

                    employee.related_request.add(request.id)
                    employee.related_vacancy.add(job.get('id'))
                    employee.skills.set(skills)

                    if is_send_mails:
                        if not(email is None) & (email != ''):
                            self._send_email(email, job.get('title', ''))


    # csv_file = "Вакансии - Словарь скиллы.csv"
    def load_csv(self):
        with open("skills.csv", 'r', encoding="UTF-8") as fin:
            reader = csv.reader(fin, lineterminator='\n')
            recommendations = list(reader)
        return recommendations