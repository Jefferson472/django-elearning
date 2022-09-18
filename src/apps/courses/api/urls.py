from urllib.parse import urlparse
from django.urls import path

from apps.courses.api.views import SubjectListView, SubjectDetailView


app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
]
