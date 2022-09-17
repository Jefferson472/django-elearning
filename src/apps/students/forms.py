from django import forms

from apps.courses.models import Course


class CourseEnrollForm(forms.Form):
    course = forms.modelChoiceField(
        queryset=Course.objects.all(), widget=forms.HiddenInput)