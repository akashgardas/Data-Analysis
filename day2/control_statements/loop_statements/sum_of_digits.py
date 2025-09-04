def sum_digits(n):
    sum = 0
    temp = n
    
    while temp > 0:
        sum += temp % 10
        temp //= 10
    
    return sum

n = 123456789
print(sum_digits(n))