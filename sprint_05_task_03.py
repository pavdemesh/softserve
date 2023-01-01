class MyError(Exception):
    def __init__(self, message):
        self.data = message

    def __str__(self):
        return repr(self.data)


def check_positive(number):
    try:
        number = int(number)
    except ValueError:
        print("Error Type: Value Error")
        return

    if number > 0:
        print(f"you input positive number: {int(number)}")

    else:
        raise MyError(f"You input negative number: {int(number)}. Try again.")


check_positive('-ab')
