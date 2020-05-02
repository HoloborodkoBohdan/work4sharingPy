from django.urls import path

from scraping.views import EmployeeView, RequestView, match_view

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('employees/', EmployeeView.as_view()),
    path('request/', RequestView.as_view()),
    path('match/', match_view),
]