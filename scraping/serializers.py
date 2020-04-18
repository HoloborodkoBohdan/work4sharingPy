from rest_framework.serializers import ModelSerializer, BaseSerializer

from scraping.models import Employee
from random import randint

class EmployeeSerializer(ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('id', 'status', 'skills', 'position')


def mockup_employee_serializer(employee_view, *args, **kwargs):
    '''
    Мокап для вывода данных.
    Когда будут связи между моделями - лучше использовать ModelSerializer
    '''

    my_obj = type('MyObject', (), {})
    d = my_obj()
    d.data = list()

    for item in args[0]:
        if item.skills:
            skills = item.skills.split()
        else: 
            skills = []

        d.data.append({
            'id': item.id,
            'position': item.position,
            'status': item.status,
            'vacancy': '',
            'conformity': randint(2, 10) * 10,
            'skills': [{'name': skill, 'isset': True, 'link': 'https://google.com'} for skill in skills],
        }) 

    return d

