from django.urls import path

from apps.students.views import StudentRegistrationView
from apps.students.views import StudentEnrollCourseView


urlpatterns = [
    path('register/',
        StudentRegistrationView.as_view(), name='student_registration'),
    
    path('enroll-course/',
        StudentEnrollCourseView.as_view(), name='student_course_detail')
]
