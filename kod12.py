class Person:
    name = "Jan"

    def __str__(self):
        return f"Nazwa {self.name}"

p1 = Person()
p1.name="Sylwia"
print(p1)