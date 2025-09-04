def print_ascii():
    print('Value    Character')
    for i in range(128):
        print(f'{i}     {chr(i)}')
        
print_ascii()