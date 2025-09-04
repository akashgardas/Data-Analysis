def sum_div(n):
    sum = 0
    
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
    
    return sum

def is_perfect_num(n):
    if n == sum_div(n):
        return True
    
    return False

def print_perfect_num(n):
    for i in range(n):
        if is_perfect_num(i):
            print(i, end=', ')

print_perfect_num(5000)