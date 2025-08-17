from django.test import SimpleTestCase, TestCase
from home.views import HomeView, AboutView
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse("home:home")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_About(self):
        url = reverse("home:about", args=("sss",))
        self.assertEqual(resolve(url).func.view_class, AboutView)
