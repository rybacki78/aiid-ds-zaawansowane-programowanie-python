class Rectangle:

    width = 0
    height = 0

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def info(self):
        return f"Szerokość: {self.width}, Wysokość: {self.height}, Pole: {self.area()}, Obwód: {self.perimeter()}"


p1 = Rectangle()
p1.width = 12
p1.height = 15

print(p1.area())
print(p1.perimeter())
print(p1.info())