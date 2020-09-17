from django.test import TestCase

from app.count import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are correctly added"""
        self.assertEqual(add(3,8),11)
