def count_alp_digits(s):
    alp = 0
    digits = 0
    spl_chars = 0
    
    for char in s.lower():
        if ord('a') <= ord(char) <= ord('z'):
            alp += 1
        elif char.isdigit():
            digits += 1
        else:
            spl_chars += 1
    
    return alp, digits, spl_chars
    
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_count = 0
    consonant_count = 0
    
    for char in s.lower():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    return vowel_count, consonant_count

def count_words(s):
    word_count = s.split(' ')
    return word_count

s = input('Enter a string: ')
alp, digits, spl_chars = count_alp_digits(s)
vowel_count, consonant_count = count_vowels(s)
word_count = count_words(s)
print('Count')
print(f'Alphabet: {alp}')
print(f'Digits: {digits}')
print(f'Special Characters: {spl_chars}')
print(f'Vowels: {vowel_count}')
print(f'Consonants: {consonant_count}')
print(f'Words: {word_count}')
