class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("File Size:", self.size, "MB")


e = EBook("Python Basics", "James", 15)
e.display()