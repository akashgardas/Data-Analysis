def print_sqaure(n):
    for _ in range(n):
        print('* ' * n)
        
def print_sqaure_dollar(n):
    for i in range(n):
        for j in range(n):
            print('* ' if i != j else '$ ', end='')
        print()
        
def print_square_dollar_cross(n):
    for i in range(n):
        for j in range(n):
            print('$ ' if i == j or i + j == n-1 else '* ', end='')
        print()

print('Square')
print_sqaure(6)

print()
print('Dollar Square')
print_sqaure_dollar(6)

print()
print('Cross Dollar Square')
print_square_dollar_cross(6)