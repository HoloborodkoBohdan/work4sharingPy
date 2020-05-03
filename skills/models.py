from django.db import models


SOURCE_CHOICES = (
    ('coursera', 'www.coursera.org'),
    ('edx', 'www.edx.org'),
)
LANG_CHOICES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    aliases = models.TextField(default='')

    class Meta: 
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    source = models.CharField(max_length=200, choices=SOURCE_CHOICES)
    lang = models.CharField(max_length=2, choices=LANG_CHOICES)
    link = models.CharField(max_length=200, null=True, default='') # We need courses without link?
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.skill}: {self.link} ({self.lang})"