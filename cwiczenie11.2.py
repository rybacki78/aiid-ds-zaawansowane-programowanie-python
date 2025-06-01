class Product:

    def __init__(self, name, price, quality, tax):
        self.name = name if isinstance(name, str) else ""
        self.price = price if isinstance(price, float) and price >= 0 else 0
        self.quality = quality if isinstance(quality, int) and quality >= 0 else 0
        self.tax = tax if isinstance(tax, float) and tax >= 0 else 0

    def __str__(self):
        return f"{self.__class__.__name__}. {self.name}. {self.price}. {self.quality}. {self.tax}."


class Book(Product):

    def __init__(self, name, price, quality, tax, authors, title):
        super().__init__(name, price, quality, tax)
        self.authors = authors if isinstance(authors, list) else ["Adam Mickiewicz"]
        self.title = title if isinstance(title, str) else ""
        self.tax = 0

    def __str__(self):
        return super().__str__() + f" {self.authors}. {self.title}."


p1 = Product("Apple", 4.5, 5, 3)
print(p1)

b1 = Book("Novel", 3.4, 1, 0.07, ["PP", "yy"], "XZZZ")
print(b1)
