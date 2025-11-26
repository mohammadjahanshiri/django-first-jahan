from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        exclude = ['profile']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        exclude = ['profile']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class ProfileSerializer(serializers.Serializer):
    class Meta:
        models = Profile
        fields = "__all__"