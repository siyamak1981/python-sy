class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
# >>> from test import Book
# >>> x = Book("s","f")
# >>> x
# <test.Book object at 0x0000027D22FE9AC8>
# >>> x.title
# 's'
# >>> x.author
# 'f'
# >>>
    def __str__(self):
        return '{} by {}'.format(self.title,self.author)        

class BookCase:
    def __init__(self, books = None):
    # def __init__(self, books = True):فرقی نمی کنه فقط میخایم فعلا لیستمون خالی باشه
        self.books = books

    @classmethod    
    def create_bookcase(cls,book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title,author))
        return cls(books)
    
# >>> from classmethod import BookCase
# >>> b =BookCase.create_bookcase([("kjshef", "og"),("idg","jhf")])
# >>> b
# <test.BookCase object at 0x00000203A8A31630>
# >>> b.books
# [<test.Book object at 0x00000203A8A316A0>, <test.Book object at 0x00000203A8A316D8>]
# >>> str(b.books[0])
# 'kjshef by og'
# #########################################
عکسی که در این بخش گداشته شده مربوز به ابسترک هستش 
و قرار نیست از کلاس پدر اینستنس ساخته بشه باید از کلاس بچه ساخته بشه
و فقط برای ارث بری هستش