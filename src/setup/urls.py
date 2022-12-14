from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from apps.courses.views.CourseViews import CourseListView


urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('apps.courses.urls')),
    path('students/', include('apps.students.urls')),
    path('api/', include('apps.courses.api.urls')),
    path('chat/', include('apps.chat.urls', namespace='chat')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
