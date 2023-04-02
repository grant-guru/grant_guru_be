from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class TestListCreateUsers(APITestCase):
    
    def test_creates_user(self):
        sample_user = {'first_name': 'Kaylah Rose', 'last_name': 'Mitchell'}
        response = self.client.post('users', sample_user)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)