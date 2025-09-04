def print_alphabet(n):
    alpha = 'A'
    for _ in range(n):
        print(alpha, end=', ')
        alpha = chr(ord(alpha) + 1)

n = int(input('Enter a number: '))
print_alphabet(n)