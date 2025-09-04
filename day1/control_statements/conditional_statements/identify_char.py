def char_check(char):
    if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
        return 'Alphabet'
    elif char.isdigit():
        return 'Digit'
    else:
        return 'Special Character'
    
char = input('Enter a character: ')
print(f'You entered {char_check(char)}' if len(char) == 1 else 'Character not a String')