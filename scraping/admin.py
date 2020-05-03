from django.contrib import admin
from scraping.models import Employee, Job, Request


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['title', 'site', 'company_name', 'location', 'industry', 'date_created']
    search_fields = ['title', 'company_name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['__str__', 'status', 'conformity']
    raw_id_fields = ['related_request', 'related_vacancy']
    filter_horizontal = ['skills',]


admin.site.register(Request)
