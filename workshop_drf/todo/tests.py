from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()

class TestTask(APITestCase):

    def test_task_creation(self):
        user = User.objects.create(username="admin")
        category = models.Category.objects.create(name="Django")
        url = reverse('task-list')
        data = {
            "name": "demo",
            "owner": user.id,
            "categories": [category.id],
            "done": False,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, response.content)
        data['id'] = 1
        self.assertEqual(response.data, data)
        self.assertEqual(category.tasks.count(), 1)

