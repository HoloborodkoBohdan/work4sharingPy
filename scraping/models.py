import json

from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from skills.models import Skill

STATUS_CHOICES = [
    ('active', 'active'),
    ('archive', 'archive'),
]

WORK_TYPES = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
]

class Request(models.Model):
    ''' All requests from company to find vacancy and learning skills '''
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    position = models.CharField(max_length=255)
    skills_text = models.TextField(default='')

    def skills(self):
        return str(self.skills_text).splitlines()

    def __str__(self):
        return self.position + " (" + self.status + ") # " + ', '.join(self.skills())


class Job(models.Model):
    ''' All vacancies in our database '''
    # Vacancy
    site = models.TextField(default='')
    url = models.TextField(default='')
    title = models.TextField(default='')
    work_type = models.TextField(default='')
    contract = models.TextField(default='')
    description = models.TextField(default='')
    skills = models.TextField(default='')
    date_created = models.DateField(default=timezone.now().date()) # use DateTimeField with auto=now?

    # Company
    company_name = models.TextField(default='')
    location = models.TextField(default='')
    industry = models.TextField(default='')
    email = models.TextField(default='')
    phone = models.TextField(default='')
    address = models.TextField(default='')

    def __str__(self):
        return self.title + " - " + self.company_name + " (" + self.location + ") # " + self.email

class Employee(models.Model):
    ''' 
    Result of match.py for new Request.
    Should return skills to learn for related vacancy 
    with percent of conformity.
    '''
    related_request = models.ManyToManyField(Request)
    related_vacancy = models.ManyToManyField(Job)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active') # How we use it?
    conformity = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill)

    def set_skills(self, x):
        self.skills = json.dumps(x)

    def get_position(self):
        return self.related_request.all()[0].position

    def get_skills(self):
        return json.loads(self.skills)

    def get_skills_for_vacancy(self):
        tmp = {}
        for skill in self.skills.all():
            tmp[skill.name] = skill.get_links_for_courses()
        return tmp

    def __str__(self):
        return self.get_position() + " (" + self.status + ") - " + str(self.conformity) + "%"
