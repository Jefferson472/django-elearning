from django.urls import path
from apps.courses.views import CourseViews

urlpatterns = [
    path('mine/', CourseViews.ManageCourseListView.as_view(),
        name='manage_course_list'),

    path('create/', CourseViews.CourseCreateView.as_view(),
        name='course_create'),

    path('<pk>/edit/', CourseViews.CourseUpdateView.as_view(),
        name='course_edit'),

    path('<pk>/delete/', CourseViews.CourseDeleteView.as_view(),
        name='course_delete'),
         
    # path('<pk>/module/', CourseViews.CourseModuleUpdateView.as_view(),
    #     name='course_module_update'),

    # path('module/<int:module_id>/content/<model_name>/create/',
    #     CourseViews.ContentCreateUpdateView.as_view(),
    #     name='module_content_create'),

    # path('module/<int:module_id>/content/<model_name>/<id>/',
    #     CourseViews.ContentCreateUpdateView.as_view(),
    #     name='module_content_update'),

    # path('content/<int:id>/delete/', CourseViews.ContentDeleteView.as_view(),
    #     name='module_content_delete'),

    # path('module/<int:module_id>/', CourseViews.ModuleContentListView.as_view(),
    #     name='module_content_list'),

    # path('module/order/', CourseViews.ModuleOrderView.as_view(),
    #     name='module_order'),

    # path('content/order/', CourseViews.ContentOrderView.as_view(),
    #     name='content_order'),

]