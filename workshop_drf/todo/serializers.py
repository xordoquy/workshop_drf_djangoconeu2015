from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class Task(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        'task-detail', source='id', read_only=True)
    owner = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)
    categories = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Category.objects.all(),
        many=True)

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'owner', 'categories', 'done', 'url')

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        task = models.Task.objects.create(**validated_data)
        task.categories = categories
        return task

