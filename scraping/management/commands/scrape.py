from datetime import datetime

from django.core.management import BaseCommand

from scraping.management.parse import get_jobs
from scraping.models import Job


class Command(BaseCommand):

    def handle(self, *args, **options):
        jobs = get_jobs(2, False)
        model_jobs = []
        for job in jobs:
            model_jobs.append(Job(
                url='example.com',
                title=job['Job Title'],
                company_name=job['Company Name'],
                location=job['Location'],
                industry=job['Industry'],
                date_created=datetime.today(),
            ))
        Job.objects.bulk_create(model_jobs)
