def factorial(n):
    fact = 1
    while n > 0: 
        fact *= n
        n -= 1
    
    return fact
        
n = 7
print(f'Factorial of {n}: {factorial(n)}')

# https://shorturl.at/ozKij