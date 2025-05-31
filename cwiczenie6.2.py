class Product:

    def __init__(self, name, price, quality, tax):
        self.name = name if isinstance(name, str) else ""
        self.price = price if isinstance(price, (int, float)) and price >= 0 else 0
        self.quality = (
            quality if isinstance(quality, (int, float)) and quality >= 0 else 0
        )
        self.tax = tax if isinstance(tax, (int, float)) and tax >= 0 else 0


p1 = Product("Jaja", -1.5, 24, -5.5)

print(p1.name, p1.price, p1.quality, p1.tax)
