from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.forms import UserRegistrationForm


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_registration_GET(self):
        response = self.client.get(reverse("home:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")
        self.assertIsInstance(response.context["form"], UserRegistrationForm)

    def test_user_registration_post(self):
        response = self.client.post(
            reverse("home:register"),
            data={
                "username": "s2",
                "email": "s2@email.com",
                "password1": "Test12345!",
                "password2": "Test12345!",
            },
        )
        # print('*'*90)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home:home"))
        self.assertEqual(User.objects.count() , 1)
