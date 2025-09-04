def factors(n):
    factors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

def is_prime(n):
    if n < 2:
        return None
    
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    
    return factors

print(factors(24))
print(prime_factors(24))