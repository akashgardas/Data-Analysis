def check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        

year = int(input('Enter year: '))

print(f'{year} is {'a' if leap_year(year) else 'not a'} leap year')