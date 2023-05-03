import conradmath

def main():

    x = int(input("Input the first value: "))

    y = int(input("Input the second value: "))

    result_add = print("Result of adding: ", conradmath.cadd(x,y))
    result_subtract = print("Result of subtracting: ", conradmath.csubtract(x,y))
    result_multiply = print("Result of multiplying: ", conradmath.cmultiply(x,y))
    result_divide = print("Result of dividing: ", conradmath.cdivide(x,y))

if __name__ == "__main__":
    main()
