import csv

from operator import and_
from django.db.models import Q
from itertools import chain

from skills.models import Skill



def vacancy_percentage(employer_skills, vacancy_description):
    if (employer_skills == None):
        skills = set()
    else:
        skills = set(employer_skills)
    shared = set()
    # must_have_skills должен содержать только те скилы, 
    # которые требуются к вакансии но отсутствуют у соискателя.
    # DO_FIX после того как будет понятно как определять ключевые скилы вакансии
    must_have_skills = set()
    for skill in skills:
        if vacancy_description.find(skill) == -1:
            must_have_skills.add(skill)
        else:
            shared.add(skill)

    # Percentage algorithm is worth reviewing
    if len(skills) == 0:
        percentage = 0
    else:
        percentage = int((len(shared) / len(skills)) * 100)
    return percentage, must_have_skills


def courses_advice(skills):
    skills_to_learn = []
    for skill in skills:
        # Не ищет по альтернативным именам + уйти от формата когда на каждый 
        # скил генерируется отдельный запрос
        skill_query = Skill.objects.filter(name__icontains=skill, learn_materials=True)
        if len(skill_query) > 0:
            if skills_to_learn:
                skills_to_learn = skills_to_learn | skill_query
            else:
                skills_to_learn = skill_query
        else:
            # Создаем скил который есть у сотрудника но нет у нас в базе
            s = Skill(name=skill, learn_materials=False)
            s.save()

    print('STL', skills_to_learn)
    return skills_to_learn