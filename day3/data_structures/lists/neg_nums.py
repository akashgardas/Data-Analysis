from random import randint

nums = [randint(-100, 100) for _ in range(10)]

print(f'List: {nums}')

for i in nums: 
    if i < 0:
        print(i, end=', ')