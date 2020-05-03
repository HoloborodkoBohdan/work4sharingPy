from rest_framework.serializers import ModelSerializer
from skills.models import Skill, Course


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
