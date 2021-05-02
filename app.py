from math import pi, sqrt

class Figure:
    """
    A class related to geometrical shapes
    """
    def print_info(self):
        print("This class is about geometrical shapes")

    def print_edges(self, *args):
        # pass
        print('Specified edges {}'.format(args))

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print_area(self):
        area = self.a * self.b
        print('The area is '.format(round(area, 2)))
    def print_perimeter(self):
        perimeter = self.a * 2 + self.b * 2
        print('The perimeter is '.format(round(perimeter, 2)))
    def print_edges(self):
        print('My edges are {} and {}.'.format(self.a, self.b))
        super().print_edges(self.a, self.b)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.square_color = 'blue'

class Triangle(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def print_area(self):
        area = 0.5 * self.a * self.h
        print('The area is: {}'.format(round(area, 2)))
    def print_perimeter(self):
        perimeter = self.a + 2 * sqrt(self.h**2 + 0.25 * self.a**2)
        print('The perimeter is: {}'.format(round(perimeter, 2)))

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def print_area(self):
        area = pi * self.r**2
        print('The area is: {}'.format(round(area), 2))
    def print_perimeter(self):
        perimeter = 2 * pi * self.r
        print('The perimeter is: {}'.format(round(perimeter, 2)))

square1 = Square(3)
square1.print_edges()

triangle1 = Triangle(1,3)
triangle1.print_area()
triangle1.print_perimeter()

circle1 = Circle(3)
circle1.print_area()
circle1.print_perimeter()

