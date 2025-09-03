char = input('Enter a character: ')

if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
    print(f'{char} is an alphabet')
else:
    print(f'{char} is not an alphabet')