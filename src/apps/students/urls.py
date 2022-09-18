from django.views.decorators.cache import cache_page
from django.urls import path

from apps.students import views


urlpatterns = [
    path('register/',
        views.StudentRegistrationView.as_view(),
        name='student_registration'
    ),
    
    path('enroll-course/',
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'
    ),

    path('course/',
        views.StudentCourseListView.as_view(), 
        name='student_course_list'
    ),
    
    path('course/<pk>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'
    ),
    
    path('course/<pk>/<module_id>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), # armazena cache da página por 15 min
        name='student_course_detail_module'
    ),
]
