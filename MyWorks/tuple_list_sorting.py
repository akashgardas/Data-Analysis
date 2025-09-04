values = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# sorting based on the last element in each list
sorted_values = sorted(values, key=lambda value:value[1])
print(sorted_values)