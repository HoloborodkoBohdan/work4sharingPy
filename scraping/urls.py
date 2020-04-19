from django.urls import path

from scraping.views import EmployeeView, RequestView

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('employees/', EmployeeView.as_view()),
    path('request/', RequestView.as_view())
]