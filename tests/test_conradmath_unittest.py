import sys
import unittest
from src.conradmath import Calculator

class TestConradMath(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.cadd(5,6), 11, "Should be 11")

    def test_subtract(self):
        self.assertEqual(self.calc.csubtract(20,10), 10, "Should be 10")

    def test_multiply(self):
        self.assertEqual(self.calc.cmultiply(5,6), 30, "Should be 30")

    def test_divide(self):
        self.assertEqual(self.calc.cdivide(30,6), 5, "Should be 5")

if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)