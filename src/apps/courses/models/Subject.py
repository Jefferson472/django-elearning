from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = 'tb_subject'
        ordering = ['title']

    def __str__(self):
        return self.title
