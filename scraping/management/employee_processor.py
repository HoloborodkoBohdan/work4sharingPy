from operator import itemgetter

from django.core.mail import send_mail

from JobParser import settings
from scraping.management.matcher import *


class EmployeeProcessor:

    def __init__(self, jobs):
        self.jobs = jobs

    def _process(self, employee):
        pass


    def _send_email(self, email, job_title, percentage):
        title = f'Regarding your {job_title} position ({percentage}%)'
        text = 'We have a candidate that might fit your position, please contact us if you are interested'
        print(email, "\n", title)
        email = settings.EMAIL_HOST_USER
        #send_mail(title, text, settings.EMAIL_TEST_USER, [email], fail_silently=False)

    def run(self, employee):
        print("###", employee.position)
        recommendations = self.load_csv()
        variants = list()
        for job in self.jobs:
            if job.get('site') is None:
                continue
            percentage, must_have_skills = vacancy_percentage(employee.skills, job.get('description', ''))
            skill_courses = courses_advice(recommendations, must_have_skills)
            variants.append((percentage, job, skill_courses))

        if len(variants) > 0:
            top_list = sorted(variants, key=itemgetter(0), reverse=True)
            for variant in top_list:
                percentage = variant[0]
                job = variant[1]
                email = job.get('email')
                if not(email is None) & (email != ''):
                    self._send_email(email, job.get('title', ''), percentage)


    # csv_file = "Вакансии - Словарь скиллы.csv"
    def load_csv(self):
        with open("skills.csv", 'r', encoding="UTF-8") as fin:
            reader = csv.reader(fin, lineterminator='\n')
            recommendations = list(reader)
        return recommendations