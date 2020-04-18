from django.urls import path

from scraping.views import EmployeeView

urlpatterns = [
    path('employees/', EmployeeView.as_view())
]