def char_freq(s, c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    
    return count

s = input("Enter a string: ")
char = input("Enter a character: ")

count = char_freq(s, char)
print(f'"{char}" occurs {count} times in "{s}"')
