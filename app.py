from abc import ABC, abstractmethod
from math import pi, sqrt
import random
# import prepare_data.triangle.gen_random
from prepare_data.triangle import gen_random

import prepare_data.triangle.gen_randint
import prepare_data.square.gen_randint


# triangle_dt_1 = prepare_data.triangle.gen_random.generate_data_1()
triangle_dt_1 = gen_random.generate_data_1()

triangle_dt_2 = prepare_data.triangle.gen_randint.generate_data_1()
triangle_dt_3 = prepare_data.triangle.gen_randint.generate_data_2()
square_dt_1 = prepare_data.square.gen_randint.generate_data_1()

class Figure(ABC):
    """
    A class related to geometrical shapes
    """

    @abstractmethod
    def print_area(self):
        print("Info about figure area:")

    @abstractmethod
    def print_perimeter(self):
        pass

    def print_info(self):
        print("This class is about geometrical shapes")

    def print_edges(self, *args):
        print('Specified edges {}'.format(args))


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a * self.b
        return area

    def print_area(self):
        super().print_area()
        print('The area is {}'.format(round(self.calculate_area(), 2)))

    def print_perimeter(self):
        perimeter = self.a * 2 + self.b * 2
        print('The perimeter is {}'.format(round(perimeter, 2)))

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
        super().print_area()
        area = 0.5 * self.a * self.h
        print('The area is: {}'.format(round(area, 2)))

    def print_perimeter(self):
        perimeter = self.a + 2 * sqrt(self.h ** 2 + 0.25 * self.a ** 2)
        print('The perimeter is: {}'.format(round(perimeter, 2)))


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def print_area(self):
        area = pi * self.r ** 2
        print('The area is: {}'.format(round(area), 2))

    def print_perimeter(self):
        perimeter = 2 * pi * self.r
        print('The perimeter is: {}'.format(round(perimeter, 2)))


square1 = Square(square_dt_1)
square1.print_edges()
square1.print_area()
square1.print_perimeter()
square1.print_info()

triangle1 = Triangle(*triangle_dt_1)
triangle1.print_area()
triangle1.print_perimeter()

circle1 = Circle(3)
circle1.print_area()
circle1.print_perimeter()

# An example of polimorphism:
if random.random() >= 0.5:
    f = Triangle(3, 3)
else:
    f = Square(7)
f.print_area()


