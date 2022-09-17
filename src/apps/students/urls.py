from django.urls import path

from apps.students.views import StudentRegistrationView


urlpatterns = [
    path('register/',
        StudentRegistrationView.as_view(), name='student_registration'),
]
