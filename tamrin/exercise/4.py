class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class BookCase():
    def __init__(self,books = None):
        self.books = books
        super().__init__()
    @classmethod
    def create_bookcase(cls, booklist):
        books=[]
        for title, author in booklist:
            books.append(Book(title,author))
        return cls(books)


b = BookCase.create_bookcase([("menu","siyamak"),("submenu","saed")])
print(b.books[0])