def del_element(l, index):
    new_list =[l[i] for i in range(len(l)) if i != index]
    return new_list

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del_index = 3

print(len(fruits))
new_fruits = del_element(fruits, del_index)

print(len(new_fruits))
print(new_fruits)
