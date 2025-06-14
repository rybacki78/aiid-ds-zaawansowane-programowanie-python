class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __lt__(self, other):
        return len(self.title) < len(other.title)

    def __repr__(self):
        return f"{self.title}, {self.author}, {self.price}\n"


books = [Book("BBBBB", "BBBBB", 20),
         Book("GGGG", "GGGG", 15),
         Book("CCCCCC", "CCCCCC", 10),
         Book("HH", "UUUU", 200),
         Book("HHH", "HHH", 200),
         Book("RRRRRRHHH", "HHH", 210),
         Book("RRRRRRHHHTTT", "HHH", 215),
         Book("RRRRJRRHHHH", "HHH", 220),
         Book("EE", "UIO", 2),
         Book("EEED", "UIO", 2)]

books.sort()

print(books)
