from rest_framework import serializers
from . import models


class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category


class Task(serializers.ModelSerializer):
    class Meta:
        model = models.Task

