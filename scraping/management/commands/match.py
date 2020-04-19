from django.core.management import BaseCommand
from django.forms import model_to_dict

from scraping.management.employee_processor import EmployeeProcessor
from scraping.models import Job, Employee


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-m', '--mail', type=bool,
                            help='Send mails after matching'
                            )
        parser.add_argument('-t', '--top', type=int,
                            help='Maximum number of most suitable vacancies to found',
                            )
        parser.add_argument('-p', '--percent', type=int,
                            help='Minimum percentage of suitable vacancies to found',
                            )

    def handle(self, *args, **options):
        is_send_mails = options.get('mail') or False
        top_count = options.get('top') or 10
        min_percent = options.get('percent') or 70
        jobs = []
        for job in Job.objects.all():
            jobs.append(model_to_dict(job))

        employee_processor = EmployeeProcessor(jobs)
        for employee in Employee.objects.filter(status='active'):
            employee_processor.run(employee, is_send_mails, top_count, min_percent)
