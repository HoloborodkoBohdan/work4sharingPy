from django.contrib import admin
from scraping.models import Employee, Job, Request

admin.site.register(Request)
admin.site.register(Employee)
admin.site.register(Job)
