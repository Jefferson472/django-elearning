from django.db import models

from apps.courses.fields import OrderField
from apps.courses.models.Course import Course


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        db_table = "tb_module"
        ordering = ['order']

    def __str__(self):
        return f'{self.order}.{self.title}'
