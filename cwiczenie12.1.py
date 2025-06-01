class Animal:

    def speak(self):
        return "Animal speaks"


class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"


animals = (Animal(), Dog(), Cat())

for animal in animals:
    print(animal.speak())
