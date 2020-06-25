from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successfull(self):
        """ Test createing a new user is successfull"""
        email = "canhazn@gmail.com"
        password = "123456789"
        user = get_user_model().objects.create_user(

            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizer(self):
        """Test the email for new user is normalize"""
        email = 'canhazn@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_supper_user(self):
        """Test createing super user"""
        user = get_user_model().objects.create_superuser(
            "canhazn@gmail.com",
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
