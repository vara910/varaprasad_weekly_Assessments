# •	3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
class Book():
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        return f"book_name:{self.title}\nauthor:{self.author}\nisbn_number:{self.isbn}"
        
bookss=Book("call of duty","varaprasad","ic3434")
print(bookss.display())