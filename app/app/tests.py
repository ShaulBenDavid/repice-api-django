"""
Calculator functions
"""
from django.test import SimpleTestCase

from app.calc import add, subtract


class ClacTests(SimpleTestCase):

    def test_add_numbers(self):
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = subtract(10, 15)
        self.assertEqual(res, 5)
