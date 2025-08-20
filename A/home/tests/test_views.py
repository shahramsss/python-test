from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from home.forms import UserRegistrationForm
from home.views import HomeView


class TestUserRegistration(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_registration_GET(self):
        response = self.client.get(reverse("home:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")
        self.assertIsInstance(response.context["form"], UserRegistrationForm)

    def test_user_registration_valid_post(self):
        response = self.client.post(
            reverse("home:register"),
            data={
                "username": "s2",
                "email": "s2@email.com",
                "password1": "Test12345!",
                "password2": "Test12345!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home:home"))
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_invalid_post(self):
        response = self.client.post(
            reverse("home:register"),
            data={
                "username": "s2",
                "email": "ss2",
                "password1": "Test12345!",
                "password2": "Test12345!",
            },
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
        self.assertFormError(
            form=form, field="email", errors=["Enter a valid email address."]
        )


class TestWriter(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="root", email="root@email.com", password="root"
        )
        self.client = Client()
        self.client.login(username="root", password="root")

    def test_writers(self):
        response = self.client.get(reverse("home:writers"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/writers.html")


"""
برای تست مستقیم viewها در جنگو، بدون اجرای کامل چرخهٔ درخواست-پاسخ، می‌تونی از کلاس RequestFactory استفاده کنی.
 این ابزار بهت اجازه می‌ده یک شیء درخواست بسازی و اون رو مستقیماً به view مورد نظر ارسال کنی، مثل یک تابع معمولی.
"""


class TestHome(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="root", email="root@email.com", password="root"
        )
        self.factory = RequestFactory()

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse("home:home"))
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse("home:home"))
        request.user = AnonymousUser()
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
