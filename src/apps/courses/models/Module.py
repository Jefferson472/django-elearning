from django.db import models

from apps.courses.models.Course import Course


class Module(models.Model):
    courses = models.ForeignKey(Course, related_name="module", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "tb_module"

    def __str__(self):
        return self.title
