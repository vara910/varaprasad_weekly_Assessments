class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.author)
            
    def __str__(self):
        return f"'{self.title}' by {self.author}"

book1 = Book("rich dad poor dad", "robert")
book2 = Book("psychology of money", "morgan")

series = book1 + book2
print(series)