from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status

CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")
payload = {
    "email": 'canhazn@gmail.com',
    "password": '23',
    "name": "Tuan Anh"
}


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = Client()

    def test_create_user(self):
        """Test creating user is successfull"""
        payload = {
            "email": 'canhazn@gmail.com',
            "password": 'test123123',
            "name": "Tuan Anh"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_exited_user(self):
        """Test creating exited user"""
        payload = {
            "email": 'canhazn@gmail.com',
            "password": 'test123123',
            "name": "Tuan Anh"
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test password too short"""
        payload = {
            "email": 'canhazn@gmail.com',
            "password": '23',
            "name": "Tuan Anh"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test create token for user"""
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
