# Objective: Showcase inheritance with Book, EBook, PrintBook classes
#   and composition with a Library class managing books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
        # EBook: Snow Crash by Neal Stephenson, File Size: 500KB

    def __str__(self):
        return (f"EBook: {self.title} by {self.author}, "
                f"File Size: {self.file_size}KB")


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return (f"PrintBook: {self.title} by {self.author}, "
                f"Page Count: {self.page_count}")


class Library:
    def __init__(self):
        # self.base = Book()
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
