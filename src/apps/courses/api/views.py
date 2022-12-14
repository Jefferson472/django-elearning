from xmlrpc.client import ResponseError
from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.courses.models.Course import Course
from apps.courses.models.Subject import Subject
from apps.courses.api.serializers import SubjectSerializer, CourseSerializer
from apps.courses.api.serializers import CourseWithContentsSerializer
from apps.courses.api.permissions import IsEnrolled


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
    """Essa class foi commitada para exemplicar que a CourseViewSet faz a mesma coisa"""
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Essa ViewSet irá gerar automaticamente a url para inscrição no curso"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(
        detail=True, # ação executada em um único objeto
        methods=['post'],
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated],
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(
        detail=True, # ação executada em um único objeto
        methods=['get'],
        serializer_class=CourseWithContentsSerializer,
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated, IsEnrolled], # IsEnrolled garante somente alunos inscritos no curso
    )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
