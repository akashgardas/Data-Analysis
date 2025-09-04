import math

square = lambda x: x * x

def calc_hypothenuse(side1, side2):
    side3 = math.sqrt(square(side1) + square(side2))
    return side3

a, b = 3, 4
print(f'Hypotenuse with sides {a, b} is {calc_hypothenuse(a, b)}')