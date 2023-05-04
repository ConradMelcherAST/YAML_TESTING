"""
Module tests
Test functions in conradmath.py
"""

import unittest
from src.conradmath import Calculator


class TestConradMath(unittest.TestCase):
    """Calculator class test"""

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """Test the adding function"""
        self.assertEqual(self.calc.cadd(5, 6), 11, "Should be 11")

    def test_subtract(self):
        """Test the subtracting function"""
        self.assertEqual(self.calc.csubtract(20, 10), 10, "Should be 10")

    def test_multiply(self):
        """Test the multiplying function"""
        self.assertEqual(self.calc.cmultiply(5, 6), 30, "Should be 30")

    def test_divide(self):
        """Test the dividing function"""
        self.assertEqual(self.calc.cdivide(30, 6), 5, "Should be 5")
