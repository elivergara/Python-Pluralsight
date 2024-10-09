class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Implementing the __str__ method
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# Creating an instance of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Using the print() function will call the __str__ method
print(book1)  # Output: 'To Kill a Mockingbird' by Harper Lee (1960)
