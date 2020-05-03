from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)

    class Meta: 
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Course(models.Model):
    SOURCE_CHOICES = (
        ('coursera', 'www.coursera.org'),
        ('edx', 'www.edx.org'),
    )

    LANG_CHOICES = (
        ('en', 'English'),
        ('ru', 'Russian'),
    )

    source = models.CharField(max_length=200, choices=SOURCE_CHOICES)
    lang = models.CharField(max_length=2, choices=LANG_CHOICES)
    link = models.CharField(max_length=200, null=True, default='')