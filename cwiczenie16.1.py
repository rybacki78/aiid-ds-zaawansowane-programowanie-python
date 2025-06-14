class Model:
    def __init__(self, dane, wynik, nazwa):
        self.dane = dane
        self.wynik = wynik
        self.nazwa = nazwa

    def __add__(self, other):
        if isinstance(other, Model):
            return Model(
                [a + b for a, b in zip(self.dane, other.dane)],
                self.wynik + other.wynik,
                self.nazwa + other.nazwa
            )
        elif isinstance(other, int):
            return Model(
                [a + other for a in self.dane], self.wynik, self.nazwa,
            )
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Model(self.dane, self.wynik + other, self.nazwa)
        else:
            return NotImplemented

    def __repr__(self):
        return f"{self.dane}, {self.wynik}, {self.nazwa}"


m1 = Model([1, 3, 3.4], 2.5, "m1")
m2 = Model([2, 8, 4.4], 1.3, "m2")

print(m1 + m2)
print(m2 + 100)
print(100 + m2)
