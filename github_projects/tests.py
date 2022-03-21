from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient


class ProjectEntryAPIViewTestCase(APITestCase):
    url = reverse("github_projects:projectentry-list")

    def setUp(self):
        self.user = User.objects.create_user("user", "user@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.test_payload = {'name': 'one', 'link': 'http://localhost/stars', 'rating': 5}

    def test_create(self):
        response = self.client.post(self.url, self.test_payload)
        self.assertEqual(201, response.status_code)

    def test_response_is_paginated(self):
        response = self.client.get(self.url).json()
        for field in ('count', 'next', 'previous', 'results'):
            self.assertIn(field, response)

    def test_required_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(400, response.status_code)
        for field in ('name', 'link'):
            self.assertIn(field, response.json())
