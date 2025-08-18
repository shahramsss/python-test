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
        self.assertIsInstance(response.context['form'], UserRegistrationForm)
