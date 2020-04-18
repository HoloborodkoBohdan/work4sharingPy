from django.shortcuts import render
from .models import Employee
from rest_framework.generics import ListCreateAPIView
from django_filters import rest_framework as filters

from scraping.serializers import EmployeeSerializer


class EmployeeView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('position',)
