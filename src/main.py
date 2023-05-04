"""
Module YAML_TESTING.src
Check code functionality without complete build
"""

from src.conradmath import Calculator

def main():
    """Main function for checking that code is functional"""

    calc = Calculator()

    first_number = int(input("Input the first value: "))

    second_number = int(input("Input the second value: "))

    print("Result of adding: ", calc.cadd(first_number, second_number))
    print("Result of subtracting: ", calc.csubtract(first_number, second_number))
    print("Result of multiplying: ", calc.cmultiply(first_number, second_number))
    print("Result of dividing: ", calc.cdivide(first_number, second_number))

if __name__ == "__main__":
    main()
