digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def num_to_words(n):
    words = ''
    temp = n
    while temp > 0:
        words = digits[temp%10 - 1] + ' ' + words
        temp //= 10
    
    return words

n = 3235
print(num_to_words(n))