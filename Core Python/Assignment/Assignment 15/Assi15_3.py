# #3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    # Constructor - supports parameterized and parameterless
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # ShowBook method
    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Shirt Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)


# Parameterized constructor
s1 = Shirt(101, "Peter England", "Formal", 1500, "Large")
s1.ShowBook()

print()

# Parameterless constructor
s2 = Shirt()
s2.ShowBook()