import unittest
from person import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("sss", "shah")
        self.p2 = Person("a1", "f1")
    def tearDown(self):
        print('OK Down ...')

        
    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), "sss shah")
        self.assertEqual(self.p2.fullname(), "a1 f1")

    def test_email(self):
        self.assertEqual(self.p1.email(), "sssshah@email.com")
        self.assertEqual(self.p2.email(), "a1f1@email.com")


if __name__ == "__main__":
    unittest.main()


# command: python3 -m unittest test_person.py
