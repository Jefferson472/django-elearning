from django.db import models
from django.contrib.auth.models import User


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User, related_name='%(class)s_related', on_delete=models.CASCADE) # o related name será criado auto, ex: text_related
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
