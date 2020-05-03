from django.urls import path
from django.conf.urls import url

from scraping.views import EmployeeView, JobView, match_view, api_main_page
from skills.views import SkillView, CourseView

urlpatterns = [
    path('', api_main_page),
    path('employees/', EmployeeView.as_view(), name="employee-list"), # Need? GET in match is the same without filter
    path('vacancies/', JobView.as_view(), name="vacancy-list"),
    path('skills/', SkillView.as_view(), name='skill-list'),
    path('courses/', CourseView.as_view(), name='course-list'),
    path('match/', match_view, name='match-endpoint'),

]