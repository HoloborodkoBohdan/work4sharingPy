from django.contrib import admin
from skills.models import Skill, Course


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ['name', 'learn_materials', 'aliases']
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['skill', 'link', 'source', 'lang']
    search_fields = ['skill__name', 'link']