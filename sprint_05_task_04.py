def day_of_week(day):
    day_numbers = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    try:
        day = int(day)
        if 0 < day < 8:
            print(f"{day_numbers[day]}")
        else:
            print(f'There is no such day!')

    except ValueError:
        print('You did not enter a number')


day_of_week(12)
day_of_week(5)
day_of_week('friday')
