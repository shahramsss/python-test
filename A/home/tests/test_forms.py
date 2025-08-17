from django.test import TestCase
from home.forms import UserRegistrationForm
from django.contrib.auth.models import User


class TestRegistrationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="s", email="s1@email.com", password="Test12345!"
        )

    def test_valid_data(self):
        form = UserRegistrationForm(
            data={
                "username": "s2",
                "email": "s2@email.com",
                "password1": "Test12345!",
                "password2": "Test12345!",
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_exist_email(self):
        form = UserRegistrationForm(
            data={
                "username": "s3",
                "email": "s1@email.com",  # ایمیل تکراری
                "password1": "Test12345!",
                "password2": "Test12345!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error("email"))

    def test_unmatch_password(self):
        form = UserRegistrationForm(
            data={
                "username": "s4",
                "email": "s4@email.com",
                "password1": "Test12345!",
                "password2": "Wrong12345!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error)
