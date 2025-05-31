class Book:

    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __repr__(self):
        return f"Title: {self.title}, author: {self.author}, publisher: {self.publisher}, pages: {self.year}."

    def __str__(self):
        return self.__repr__()

book = [
    Book("Jeden", "Jedyneczek", "Jedynek", 1),
    Book("Dwa", "Dwójeczek", "Dwójek", 2),
    Book("Trzy", "Trójeczek", "Trójek", 3),
    Book("Cztery", "Czwóreczek", "Czwórek", 4),
]

print(book[1])
