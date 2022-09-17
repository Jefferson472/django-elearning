from django.urls import path

from apps.courses.views import CourseViews, ModuleViews, ContentViews

urlpatterns = [
    path('mine/', CourseViews.ManageCourseListView.as_view(),
        name='manage_course_list'),

    path('create/', CourseViews.CourseCreateView.as_view(),
        name='course_create'),

    path('<pk>/edit/', CourseViews.CourseUpdateView.as_view(),
        name='course_edit'),

    path('<pk>/delete/', CourseViews.CourseDeleteView.as_view(),
        name='course_delete'),
         
    path('<pk>/module/', ModuleViews.CourseModuleUpdateView.as_view(),
        name='course_module_update'),

    path('module/<int:module_id>/content/<model_name>/create/',
        ContentViews.ContentCreateUpdateView.as_view(),
        name='module_content_create'),

    path('module/<int:module_id>/content/<model_name>/<id>/',
        ContentViews.ContentCreateUpdateView.as_view(),
        name='module_content_update'),

    path('content/<int:id>/delete/', ContentViews.ContentDeleteView.as_view(),
        name='module_content_delete'),

    path('module/<int:module_id>/', ModuleViews.ModuleContentListView.as_view(),
        name='module_content_list'),

    path('module/order/', ModuleViews.ModuleOrderView.as_view(),
        name='module_order'),

    path('content/order/', ContentViews.ContentOrderView.as_view(),
        name='content_order'),
]
