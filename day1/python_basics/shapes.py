PI = 3.14

class Shape:
    def __init__(self):
        pass

    def circle(self, radius):
        '''
        returns (area, circumference)
        '''
        return PI * radius ** 2, 2 * PI * radius

    def rectangle(self, length, breadth):
        '''
        returns (area, perimeter)
        '''
        return length * breadth, 2 * (length + breadth)

    def cube(self, length):
        '''
        returns volumne
        '''
        return length**3

    def cylinder(self, radius, height):
        '''
        returns volume
        '''
        return PI * radius ** 2 * height

shape = Shape()

radius = float(input("Enter Radius: "))
length = float(input("Enter Length: "))
breadth = float(input('Enter Breadth: '))

area, circum = shape.circle(radius)
print(f"Area = {area}, Circumference = {circum}")


area, peri = shape.rectangle(length, breadth)
print(f'Area: {area}, Perimeter: {peri}')