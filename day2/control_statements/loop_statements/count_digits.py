import math

def count_digits(n):
    count = math.floor(math.log(n, 10)) + 1
    return count

n = 2323
print(f'{n} has {count_digits(n)} digits')