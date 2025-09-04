def factorial(n):
    fact = 1
    while n > 0: 
        fact *= n
        n -= 1
    
    return fact

def is_strong(n):
    temp = n
    sum = 0
    
    while temp > 0:
        sum += factorial(temp % 10)
        temp //= 10
    
    return n == sum

def print_strong(n):
    for i in range(n):
        if is_strong(i):
            print(i, end=', ') 

print_strong(400)