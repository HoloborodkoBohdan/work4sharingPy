from django.urls import path

<<<<<<< HEAD
from scraping.views import EmployeeView

urlpatterns = [
    path('employees/', EmployeeView.as_view())
=======
from scraping.views import EmployeeView, RequestView, match_view

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('employees/', EmployeeView.as_view()),
    path('request/', RequestView.as_view()),
    path('match/', match_view),
>>>>>>> last
]