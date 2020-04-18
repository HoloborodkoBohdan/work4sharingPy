from django.db import models

# Create your models here.

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
    skills = models.TextField(null=True)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position + " (" + self.status + ")"


class Job(models.Model):
    # Vacancy
    site = models.TextField(null=True)
    url = models.TextField(null=True)
    title = models.TextField(null=True)
    work_type = models.CharField(max_length=20, choices=WORK_TYPES, null=True)
    contract = models.TextField(null=True)
    description = models.TextField(null=True)
    skills = models.TextField(null=True)
    date_created = models.DateField(null=True)

    # Company
    company_name = models.TextField(null=True)
    location = models.TextField(null=True)
    industry = models.TextField(null=True)
    email = models.TextField(null=True)
    phone = models.TextField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.title + " - " + self.company_name + " (" + self.location + ")"
