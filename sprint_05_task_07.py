
def check_odd_even(number):
    try:
        number = int(number)
    except ValueError:
        print("You entered incorrect data. Please try again.")
        return

    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

    return


check_odd_even('-ab')
check_odd_even(15)
check_odd_even("10")
