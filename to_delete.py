class Shape:
    def area(self):
        print('Cannot calculate area of abstract shape.')

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        print('The area is equal to {}.'.format(self.a*self.b))

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

square1 = Square(5)
square1.area()




