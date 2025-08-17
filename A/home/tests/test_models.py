from django.test import TestCase
from home.models import Writer


class TestWriterModel(TestCase):
    def test_model_str(self):
        writer = Writer.objects.create(
            first_name="sss",
            last_name="shah",
            email="shah@email.com",
            password="shah",
        )
        self.assertEqual(str(writer) , 'sss shah')
    