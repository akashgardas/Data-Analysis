num = int(input('Enter a number: '))

if num == 0:
    print('You entered zero')
else:
    print(f'You entered {'positive' if num > 0 else 'negative'} number')