class Book:
    def __init__(self, bid=0, bname="Unknown", price=0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    def __del__(self):
        print("Book object destroyed")
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

b1 = Book(101, "Python", 500, "James")
b1.ShowBook()
b2 = Book()
b2.ShowBook()