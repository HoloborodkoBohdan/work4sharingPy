from rest_framework.serializers import ModelSerializer, BaseSerializer

from scraping.models import Employee, Request, Skill, Job


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'position', 'status', 'vacancy', 'conformity', 'skills')


class RequestCheckSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'position', 'status', 'skills_text', 'skills')

def request_create_serializer(request_obj, *args, **kwargs):
    my_obj = type('MyObject', (), {})
    d = my_obj()
    d.data = list()

    item = {
        'id': request_obj.id,
        'status': request_obj.status,
        'skills_text': request_obj.skills_text,
        'vacancies': []
    }

    for employee in request_obj.employee_set.all():
        item['vacancies'].append({
            'id': employee.id,
            'status': employee.status,
            'conformity': employee.conformity,
            'vacancy_full': employee.vacancy,
            'skills': []
        })

    d.data.append(item)
    return d