from django.urls import path

from scraping.views import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('employees/', EmployeeView.as_view())
]