from django.apps import apps
from django.forms.models import modelformset_factory
from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import get_object_or_404, redirect

from apps.courses.models import Module, Content


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None
    
    def get_form(self, model, *args, **kwargs):
        Form = modelformset_factory(model, exclude=[
            'owner', 'order', 'created', 'updated'
        ])
        return Form(*args, **kwargs)
    
    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(
            Module, id=module_id, course__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(
                self.model, id=id, owner=request.user)
        return super().dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({
            'form': form,
            'object': self.obj
        })

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(
            self.model, instance=self.obj,
            data=request.POST, files=request.FILES
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                # novo conteúdo
                Content.objects.create(module=self.module, item=obj)
            return redirect('module_content_list', self.module.id)
        return self.render_to_response({
            'form': form,
            'object': self.obj
        })
