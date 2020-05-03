from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from skills.serializers import SkillSerializer, CourseSerializer
from django_filters import rest_framework as filters

from skills.models import Skill, Course


class SkillView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name',)


class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
