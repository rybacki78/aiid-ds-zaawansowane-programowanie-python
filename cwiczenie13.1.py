class Product:

    def __init__(self, name, price, quality, tax):
        self.name = name if isinstance(name, str) else ""
        self.price = price if isinstance(price, float) and price >= 0 else 0
        self.quality = quality if isinstance(quality, int) and quality >= 0 else 0
        self.tax = tax if isinstance(tax, float) and tax >= 0 else 0

    def __str__(self):
        return f"{self.__class__.__name__}. {self.name}. {round(self.price,2)}. {self.quality}. {self.tax}."

    @staticmethod
    def check_quality(obj):
        if isinstance(obj, Product) and obj.quality > 5:
            obj.price *= 1.1

p1 = Product("Apple", 3.5, 5,1.0)
p2 = Product("Banana", 3.5, 6,1.0)

Product.check_quality(p1)
Product.check_quality(p2)

print(p1)
print(p2)