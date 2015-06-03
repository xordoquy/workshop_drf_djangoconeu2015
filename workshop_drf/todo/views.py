from rest_framework import viewsets
from . import serializers, models


class Category(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category


class Task(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Task

