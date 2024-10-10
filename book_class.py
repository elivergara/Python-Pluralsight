class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Implementing the __str__ method
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_yr):
        self._year = new_yr


# Creating an instance of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)


print(book1.year)
print(book2.year)
book1.year = 2021
book2.year = 2024   
print(book1.year)
print(book2.year)


