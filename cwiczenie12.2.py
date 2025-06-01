from math import pi


class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


figures = [Rectangle(10, 10), Circle(5)]

for fig in figures:
    print(f"{fig.name}, {fig.area()}")
