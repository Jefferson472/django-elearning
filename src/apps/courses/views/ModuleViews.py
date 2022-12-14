from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View

from braces.views import CsrfExemptMixin, JsonRequestResponseMixin

from apps.courses.models import Course
from apps.courses.forms import ModuleFormSet
from apps.courses.models.Module import Module

# o template mixin foi utilizado para renderizar mais de uma model na mesma view
class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'course': self.course,
            'formset': formset
        })
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({
            'course': self.course,
            'formset': formset
        })


class ModuleContentListView(TemplateResponseMixin, View):
    """Lê o objeto Module com ID especificado e renderiza um template com esse módulo"""
    template_name = 'courses/manage/module/content_list.html'

    def get(self, request, module_id):
        module = get_object_or_404(
            Module, id=module_id, course__owner=request.user)
        return self.render_to_response({'module': module})


class ModuleOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    """Lida com uma requisição post para reordenar o conteúdo"""
    def post(self, request):
        for id, order in self.request_json.items():
            Module.objects.filter(
                id=id, course__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'Ok'})
