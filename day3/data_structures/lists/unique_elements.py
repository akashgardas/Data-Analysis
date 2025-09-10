def filter_unique_elements(l):
    unique = []
    for i in l:
        if i not in unique:
            unique.append(i)
    
    return unique

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
unique_fruits = filter_unique_elements(fruits)
print(f'Fruits: {fruits}')
print(f'Unique Fruits: {unique_fruits}')
