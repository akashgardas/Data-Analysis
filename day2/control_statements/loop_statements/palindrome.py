def reverse_num(n):
    temp = n
    reverse = 0
    
    while temp > 0:
        reverse *= 10
        reverse += temp % 10
        temp //= 10
    
    return reverse

def is_palindrome(n):
    if n == reverse_num(n):
        return True
    
    return False

def print_palindrome(n):
    for i in range(n):
        if is_palindrome(i):
            print(i, end=', ')

print_palindrome(500)