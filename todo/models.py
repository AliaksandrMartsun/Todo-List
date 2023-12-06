from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=False)
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 null=True)
    owner = models.ForeignKey(User,
                              related_name='todos',
                              on_delete=models.CASCADE,
                              null=True)

    def __str__(self):
        return self.title
