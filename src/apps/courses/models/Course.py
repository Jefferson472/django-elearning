from django.db import models
from django.contrib.auth.models import User

from apps.courses.models.Subject import Subject


class Course(models.Model):
    owner = models.ForeignKey(
        User, related_name="courses_created", on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, related_name="courses", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(
        User, related_name='courses_joined', blank=True)
    

    class Meta:
        db_table = "tb_courses"
        ordering = ["-created"]

    def __str__(self):
        return self.title
