def sum_cubes(n):
    temp = n
    sum = 0
    
    while temp > 0:
        sum += (temp % 10) ** 3
        temp //= 10
    
    return sum

def is_armstrong(n):
    if n == sum_cubes(n):
        return True
    
    return False

def print_armstrong(n):
    for i in range(n):
        if is_armstrong(i):
            print(i, end=', ')

print_armstrong(5000)