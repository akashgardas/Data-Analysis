def count(nums):
    evens = 0
    odds = 0
    
    for i in nums:
        if i % 2:
            odds += 1
        else:
            evens += 1
    
    return evens, odds

nums = [33, 98, 8, 2, 5, 97]
evens, odds = count(nums)
print(f'Evens: {evens}, Odds: {odds}')