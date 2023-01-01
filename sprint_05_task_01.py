def divide(a, b):
    try:
        print(f"Result is {a / b}")
    except ZeroDivisionError:
        print(f"Oops, {a} / {b} denominator! Division by 0 is error!!!")
    except TypeError:
        print("Value Error! You did not enter a number!!!")


divide(5, 0)
divide("5", 16)
divide(5, 10)
