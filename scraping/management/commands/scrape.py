from datetime import datetime

from django.core.management import BaseCommand

from scraping.management.parse import get_jobs_glassdoor, get_jobs_stepstone
from scraping.models import Job


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('site', type=str, 
            help='Site for parsing. Available: glassdoor, stepstone'
        )
        parser.add_argument('-c', '--count', type=int, 
            help='Number of jobs for parsing', 
        )

    def handle(self, *args, **options):
        site_for_parsing = options.get('site')
        elements_for_parsing = options.get('count') or 20
        available_sites = ['glassdoor', 'stepstone']
        site = 'www.example.com'

        if site_for_parsing not in available_sites:
            raise Exception(
                f"Wrong site for parsing. Available variants: {', '.join(available_sites)}"
            )

        if site_for_parsing == 'glassdoor':
            site = 'www.glassdoor.com'
            jobs = get_jobs_glassdoor(elements_for_parsing, False)
        elif site_for_parsing == 'stepstone':
            site = 'www.stepstone.de'
            jobs = get_jobs_stepstone(elements_for_parsing, False)

        model_jobs = []
        for job in jobs:
            model_jobs.append(Job(
                site = site,
                url = job['url'],
                title = job['title'],
                work_type = job['work_type'],
                contract = job['contract'],
                description = job['description'],
                skills = job['skills'],
                date_created = datetime.today(),
                company_name = job['company_name'],
                location = job['location'],
                industry = job['industry'],
                email = job['email'],
                phone = job['phone'],
                address = job['address'],
            ))
        Job.objects.bulk_create(model_jobs)
