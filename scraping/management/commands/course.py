from datetime import datetime
import scraping.management.parse_courses

from django.core.management import BaseCommand

from scraping.management.parse_courses import fill_courses_from_rutracker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('site', type=str,
                            help='Site for parsing courses. Available: rutracker'
                            )
        parser.add_argument('-c', '--count', type=int,
                            help='Number of courses for parsing',
                            )

    def handle(self, *args, **options):
        site_for_parsing = options.get('site')
        elements_for_parsing = options.get('count') or 20
        available_sites = ['rutracker']

        if site_for_parsing not in available_sites:
            raise Exception(
                f"Wrong site for parsing. Available variants: {', '.join(available_sites)}"
            )

        if site_for_parsing == "rutracker":
            fill_courses_from_rutracker()
