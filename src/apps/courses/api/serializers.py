from rest_framework import serializers

from apps.courses.models.Course import Course
from apps.courses.models.Module import Module
from apps.courses.models.Subject import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True) # serializando vários objetos

    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug', 'overview'
            'created', 'owner', 'modules'
        ]
