"""Module YAML_TESTING.src
Basic arithmatic functions
"""


class Calculator():
    """Calculator class"""

    def __init__(self):
        self._last_answser = 0.0

    def cadd(self, first_number, second_number):
        """Function to add two numbers"""
        return first_number + second_number

    def csubtract(self, first_number, second_number):
        """Function to subtract one number from another"""
        return first_number - second_number

    def cmultiply(self, first_number, second_number):
        """Function to multiply two numbers"""
        return first_number * second_number

    def cdivide(self, first_number, second_number):
        """Function to divide one number by another"""
        return first_number / second_number
