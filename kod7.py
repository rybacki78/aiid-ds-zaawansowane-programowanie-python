import math


class Point:
    x = 4
    y = 2

    def reset(self):
        self.x = 0
        self.y = 0

    def left(self, move):
        self.x -= move

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def dist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


p1 = Point()
p1.reset()
print(p1.x, p1.y)
print(p1.dist())
p1.move(3, 4)
print(p1.x, p1.y)
print(p1.dist())