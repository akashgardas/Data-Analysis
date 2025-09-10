def char_freq(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1
    
    return dict(sorted(freq.items()))

# s = 'aaabbca'
s = input('Enter a string: ')   

char_freq = char_freq(s)
for k, v in char_freq.items():
    print(f'{k}{v}', end='')

