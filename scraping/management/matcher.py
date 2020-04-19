import csv


def vacancy_percentage(employer_skills, vacancy_description):
    if (employer_skills == None):
        skills = set()
    else:
        skills = set(employer_skills)
    shared = set()
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
        percentage = (len(shared) / len(skills)) * 100
    return percentage, must_have_skills


def courses_advice(recommendations, skills):
    skill_courses = []
    names = []
    for skill in recommendations[1:]:
        if skill[0] in skills or skill[1] in skills:
            skill_courses.append(skill)
            names.append(skill[0])
    return skill_courses, names

    # one element of skill_courses is like
    # ['Eigenständig', 'Work Independently', 'https://www.coursera.org/learn/positive-psychiatry', 'https://www.coursera.org/learn/learning-how-to-learn?index=prod_all_products_term_optimization']
    # DE, EN, ref1, ref2