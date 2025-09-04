def calc_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    return sum

n = 10
print(f'Sum of {n} natural numbers is {calc_sum(n)}')