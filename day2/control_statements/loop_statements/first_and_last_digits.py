def find_first_last(n):
    temp = n 
    first = temp%10
    
    while temp > 9:
        temp //= 10
    
    last = temp
    
    return first, last

def first_last_sum(n):
    first, last = find_first_last(n)
    
    return first + last

n = 23455391
print(first_last_sum(n))