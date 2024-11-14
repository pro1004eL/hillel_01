
from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area_of_figure(self):
        pass
    @abstractmethod
    def perimeter_of_figure(self):
        pass


class Rectangle(Figure):
    def __init__(self, height, width):

        self.height = height
        self.width = width

    def area_of_figure(self):
        return self.height * self.width

    def perimeter_of_figure(self):
        return 2 * (self.height + self.width)


class Circle(Figure):
    def __init__(self, radius):

        self.radius = radius

    def area_of_figure(self):
        return math.pi * self.radius ** 2

    def perimeter_of_figure(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area_of_figure(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter_of_figure(self):
        return self.side_a + self.side_b + self.side_c


figure_list = [
    Rectangle(5, 105),
    Triangle(15, 15, 6),
    Circle(60)
]


for figure in figure_list:
    print(f"{figure.__class__.__name__}:")
    print(f'Area: {figure.area_of_figure():.2f} ')
    print(f'Perimeter: {figure.perimeter_of_figure():.2f}\n ')



