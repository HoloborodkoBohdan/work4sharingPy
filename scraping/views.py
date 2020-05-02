from django.core.management import call_command
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from JobParser.local_settings import API_MATCH_VACANCIES_COUNTER, API_MATCH_VACANCIES_PERCENT

from scraping.models import Employee
from scraping.serializers import (
    RequestSerializer, EmployeeSerializer, RequestCheckSerializer,
    request_create_serializer, mockup_employee_serializer
)


class EmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    # serializer_class = mockup_employee_serializer # Delete if match api ok
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('position',)


class RequestView(CreateAPIView):
    serializer_class = RequestSerializer


@api_view(['GET', 'POST'])
def match_view(request):
    if request.method == 'GET':
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data) # Нет фильтра по позиции

    if request.method == 'POST':
        serializer = RequestCheckSerializer(data=request.data)
        if serializer.is_valid():
            save = serializer.save()
            # Call manage.py match command for matching for just created Request
            call_command(
                'match', 
                f"--top={str(API_MATCH_VACANCIES_COUNTER)}", 
                f"--percent={str(API_MATCH_VACANCIES_PERCENT)}", 
                f"--id={str(save.id)}"
            )

            data = request_create_serializer(save,  many=True).data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
