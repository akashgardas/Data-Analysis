fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.append('papaya')
print(fruits)

fruits.sort()
print(fruits)

print(f'Count of apples: {fruits.count("apple")}')

fruits.reverse()
print(f'Reversed List: {fruits}')

print(f'Pop: {fruits.pop()}')

# List comprehensions
squares = [i**2 for i in range(10)]
nested_com = [[i*j for i in range(3)] for j  in range(4)]
print(f'Squares: {squares}')
print(f'Nested Comprehension: {nested_com}')