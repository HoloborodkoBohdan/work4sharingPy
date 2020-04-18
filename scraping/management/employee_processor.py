from django.core.mail import send_mail

from JobParser import settings


class EmployeeProcessor:

    def __init__(self, jobs):
        self.jobs = jobs

    def _process(self, employee):
        pass

    def _send_email(self, company_name, job_title):
        email = f'info@{"".join(company_name.split(" "))}'
        print(email, " : ", f'Regarding your {job_title} position')
        #send_mail(
        #    f'Regarding your {job_title} position',
        #    'We have a candidate that might fit your position, please contact us if you are interested',
        #    settings.EMAIL_HOST_USER,
        #    [email],
        #    fail_silently=False,
        #)

    def run(self, employee):
        employee_position = employee.position
        for job in self.jobs:
            if set(job.get('title','').split(' ')).intersection(set(employee_position.split(' '))):
                self._send_email(job.get('company_name',''), job.get('title',''))
