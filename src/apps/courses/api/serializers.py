from rest_framework import serializers

from apps.courses.models.Course import Course
from apps.courses.models.Content import Content
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
            'id', 'subject', 'title', 'slug', 'overview',
            'created', 'owner', 'modules',
        ]


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value): # sobreescrevendo o método to_representation
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    """Esta class está sendo utilizada para lidar com os diferentes tipso de conteúdos"""
    item = ItemRelatedField(read_only=True) # método personalizado anteriormente, usamos como chave estrangerira genérica

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']

    
class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug', 'overview',
            'created', 'owner', 'modules',
        ]