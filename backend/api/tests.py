# backend/api/tests.py
from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from api import models


class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.tasks_url = reverse('tasks-list') 

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get(self.tasks_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи."""
        data = {
            'title': 'Test',
            'description': 'Test'
        }

        response = self.guest_client.post(
            self.tasks_url,
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(
            models.Task.objects.filter(title='Test').exists()
        )
