def is_prime(n):
    if n < 2:
        return None
    
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(n):
        if is_prime(i):
            print(i, end=', ')

n = 100
print_primes(n)