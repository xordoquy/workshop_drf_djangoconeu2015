from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Task(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    categories = models.ManyToManyField(
        Category, related_name="tasks")
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

