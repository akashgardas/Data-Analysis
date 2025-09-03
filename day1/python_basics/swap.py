def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b

a, b = map(float, input("Enter a, b: ").split())
print('-'*30)

print('Before')
print(f'a = {a}, b = {b}')
print('-'*30)

a, b = swap(a, b)
print('After')
print(f'a = {a}, b = {b}')