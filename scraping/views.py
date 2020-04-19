from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from django_filters import rest_framework as filters

from scraping.models import Employee
from scraping.serializers import EmployeeSerializer, mockup_employee_serializer


class EmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    #serializer_class = mockup_employee_serializer
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('position',)
