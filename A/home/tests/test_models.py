from django.test import TestCase
from home.models import Writer
from model_bakery import baker


class TestWriterModel(TestCase):
    def test_model_str(self):
        # writer = Writer.objects.create(
        #     first_name="sss",
        #     last_name="shah",
        #     email="shah@email.com",
        #     password="shah",
        # )
        writer = baker.make(
            Writer,
            first_name="sss",
            last_name="shah",
        )
        self.assertEqual(str(writer), "sss shah")
