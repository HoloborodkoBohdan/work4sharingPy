from rest_framework.serializers import ModelSerializer, BaseSerializer, SerializerMethodField
from django.core import serializers
from django.forms.models import model_to_dict

from scraping.models import Employee, Request, Job


class EmployeeSerializer(ModelSerializer):
    vacancy = SerializerMethodField(source='get_vacancy')
    position = SerializerMethodField(source='get_position')
    skills = SerializerMethodField(source='get_skills')

    class Meta:
        model = Employee
        fields = ('id', 'status', 'position', 'vacancy', 'conformity', 'skills', 'related_request', 'related_vacancy')

    def get_vacancy(self, obj):
        return serializers.serialize('json', obj.related_vacancy.all())

    def get_position(self, obj):
        return obj.related_request.all()[0].position

    def get_skills(self, obj):
        return obj.get_skills_for_vacancy()


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
        'id': request_obj.position,
        'status': request_obj.status,
        'skills_text': request_obj.skills_text,
        'vacancies': []
    }

    for employee in request_obj.employee_set.all():
        item['vacancies'].append({
            'id': employee.id,
            'status': employee.status,
            'conformity': employee.conformity,
            'vacancy_full': model_to_dict(employee.related_vacancy),
            'skills': employee.get_skills_for_vacancy(),
        })

    d.data.append(item)
    return d


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

