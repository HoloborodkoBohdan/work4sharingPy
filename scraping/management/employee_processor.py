from operator import itemgetter

from JobParser import settings
from scraping.management import email_thread
from scraping.management.matcher import *
from scraping.models import Employee
from skills.models import Skill


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
        variants = list()
        # Skills of our candidate. Transform from text to list
        request_skills = request.skills_text.splitlines()
        # TO_FIX: Jobs пиходит как dict из match.py
        for job in self.jobs:
            if job.get('site') is None:
                continue
            percentage, must_have_skills = vacancy_percentage(request_skills, job.get('description', ''))
            skill_courses = courses_advice(must_have_skills)
            variants.append((percentage, job, skill_courses))

        if len(variants) > 0:
            top_list = sorted(variants, key=itemgetter(0), reverse=True)
            for variant in top_list[:top_count]:
                percentage = variant[0]
                if percentage >= min_percent:
                    job = variant[1]
                    skill_courses = variant[2]
                    email = job.get('email')
                    print(percentage, '% -', email, job.get('title', ''), '\n')

                    employee = Employee.objects.create()
                    employee.status = request.status
                    employee.conformity = percentage
                    employee.save()

                    employee.related_request.add(request.id)
                    employee.related_vacancy.add(job.get('id'))
                    employee.skills.set(skill_courses)

                    if is_send_mails:
                        if not(email is None) & (email != ''):
                            self._send_email(email, job.get('title', ''))
