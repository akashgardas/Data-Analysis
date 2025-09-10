def count_freq(l):
    elements = []
    freq = []
    
    for i in l:
        if i in elements:
            freq[elements.index(i)] += 1
        else:
            elements.append(i)
            freq.append(1)
    
    return elements, freq
    
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
elements, freq = count_freq(fruits)

for i in range(len(elements)):
    print(f'{elements[i]} => {freq[i]}')
