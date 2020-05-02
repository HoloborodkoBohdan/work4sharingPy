from django.urls import path
from django.conf.urls import url

from scraping.views import EmployeeView, JobView, match_view, api_main_page

urlpatterns = [
    path('', api_main_page),
    path('employees/', EmployeeView.as_view(), name="employee-list"),
    path('vacancy/', JobView.as_view(), name="vacancy-list"),
    path('match/', match_view, name='match-endpoint'),
]