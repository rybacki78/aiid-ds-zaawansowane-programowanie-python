class Person:

    first_name = "John"
    last_name = "Smith"
    age = 31
    eye_color = "brown"
    hair_color = "black"

    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def colors(self):
        return f'has {self.eye_color} eyes and {self.hair_color} hair.'
    

p1 = Person()
p2 = Person()

p2.first_name = "Jane"
p2.last_name = "Doe"
p2.age = 18
p2.eye_color = "blue"
p2.hair_color = "blonde"

print(p1.full_name(),f"({p1.age})", p1.colors())
print(p2.full_name(),f"({p2.age})", p2.colors())

