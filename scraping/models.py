from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    ('active', 'active'),
    ('archive', 'archive'),
]

WORK_TYPES = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
]


class Employee(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    conformity = models.IntegerField(default=0)
    position = models.CharField(max_length=255)
    vacancy = models.TextField(default='')
    skills_text = models.TextField(default='')

    def skills(self):
        return str(self.skills_text).splitlines()

    def __str__(self):
        return self.position + " (" + self.status + ")"


class Request(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    position = models.CharField(max_length=255)
    skills_text = models.TextField(default='')

    def skills(self):
        return str(self.skills_text).splitlines()

    def __str__(self):
        return self.position + " (" + self.status + ")"


class Job(models.Model):
    # Vacancy
    site = models.TextField(default='')
    url = models.TextField(default='')
    title = models.TextField(default='')
    work_type = models.TextField(default='')
    contract = models.TextField(default='')
    description = models.TextField(default='')
    skills = models.TextField(default='')
    date_created = models.DateField(default=timezone.now().date())

    # Company
    company_name = models.TextField(default='')
    location = models.TextField(default='')
    industry = models.TextField(default='')
    email = models.TextField(default='')
    phone = models.TextField(default='')
    address = models.TextField(default='')

    def __str__(self):
        return self.title + " - " + self.company_name + " (" + self.location + ") " + self.email
