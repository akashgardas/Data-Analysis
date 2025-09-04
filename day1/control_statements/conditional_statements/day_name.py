def get_day(day):
    if day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Wednesday'
    elif day == 4:
        return 'Thursday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    elif day == 7:
        return 'Sunday'
    else:
        return None
    
day = int(input('Enter day number: '))
print(f'Day {day} in a week is {get_day(day)}' if day in range(1, 8) else 'Invalid day Number')