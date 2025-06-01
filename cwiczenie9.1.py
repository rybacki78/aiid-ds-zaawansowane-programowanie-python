class Book:

    def __init__(self, title, author, publisher, year):
        self.__title = title if isinstance(title, str) else ""
        self.__author = author if isinstance(author, str) else ""
        self.publisher = publisher
        self.__year = (
            year if isinstance(year, int) and 0 < year <= 2025 else 2025
        )

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @title.setter
    def title(self, value):
        self.__title = value if isinstance(value, str) else self.__title

    @author.setter
    def author(self, value):
        self.__author = value if isinstance(value, str) else self.__author

    @year.setter
    def year(self, value):
        self.__year = (
            value
            if isinstance(value, int) and 0 < value <= 2025
            else self.__year
        )

    def __str__(self):
        return f"{self.__title}, {self.__author}, {self.publisher}, {self.__year}"


b1 = Book("Miś", "Ja", "Ty", -3)
print(b1)

b1.title = 1
print(b1)

b1.author = 1
print(b1)

b1.year = 2026
print(b1)

b1.year = -1
print(b1)

b1.title = "Miś2"
print(b1)
