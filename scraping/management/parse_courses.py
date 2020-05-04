from skills.models import Skill
from scraping.management.rutracker import Rutracker

from JobParser.local_settings import RUTRACKER_LOGIN as login
from JobParser.local_settings import RUTRACKER_PASSWORD as password


def fill_courses_from_rutracker():
    """Finds skills without courses and tries to fill courses"""
    skills = Skill.objects.filter(learn_materials=False)
    rutracker = Rutracker(login, password)
    for skill in skills:
        search_term = skill.name
        search_results = rutracker.search(search_term)
        print(search_results)
