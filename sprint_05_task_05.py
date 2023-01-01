class ToSmallNumberGroupError(Exception):
    def __init__(self, message):
        self.data = message

    def __str__(self):
        return repr(self.data)


def check_number_group(number):
    try:
        number = int(number)
    except ValueError:
        print("You entered incorrect data. Please try again.")
        return

    if number > 10:
        print(f"Number of your group {int(number)} is valid")

    else:
        raise ToSmallNumberGroupError(f"We obtain Error. Number of your group can't be less than 10.")


check_number_group('-ab')
check_number_group(16)
check_number_group("10")
