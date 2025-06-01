class Book():

    def __init__(self, title, author, publisher, year):
        self.__title = title if isinstance(title, str) else ""
        self.__author = author if isinstance(author, str) else ""
        self.publisher = publisher
        self.__year = year if isinstance(year, int) and 0 < year <= 2025 else 2025

    def __str__(self):
        return f"{self.__title}, {self.__author}, {self.publisher}, {self.__year}"

    def __eq__(self, other):
        return (self.__title == other.__title and self.__author == other.__author and self.publisher == other.publisher
                and self.__year == other.__year)


b1 = Book("HS", "PR", "YT", "2020")
b2 = Book("HS", "PR", "YT", "2020")

print(b1 == b2)
print(b1 is b2)
