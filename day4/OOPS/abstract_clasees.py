from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return math.PI * self.radius ** 2
    

rec = Rectangle(3, 4)
print(f'Area of Rectangle is {rec.area()}')
print(f'Perimeter of Rectangle is {rec.perimeter()}')

circle = Circle(5)
print(f'Area of Circle is {circle.area()}')