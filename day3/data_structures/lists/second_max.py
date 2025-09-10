import math

def get_second_largest(nums):
    largest = sec_largest = -math.inf
    
    for i in nums:
        if i > largest:
            sec_largest = largest
            largest = i
    
    return sec_largest

nums = [-2, -28, -82, -53, -10, 5, -29, 21, 23, -14]
sec_largest = get_second_largest(nums)
print(f'List: {nums}')
print(f'Second Largest: {sec_largest}')
