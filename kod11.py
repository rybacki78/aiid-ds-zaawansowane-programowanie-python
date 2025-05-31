import math


class Point:
    name = "W"

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def dist(self, other=None):
        if other is None:
            return math.sqrt(self.x ** 2 + self.y ** 2)
        else:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(2, 2)
p1.name = "A"
p1.move(-1, 1)
p2 = Point(3, 4)
p3 = Point(2, 0)
p1.name = "R"
Point.name = "T"
p3.name = "g"
Point.name = "v" 