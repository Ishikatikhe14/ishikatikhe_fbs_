# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
    
    # Static member
    size_increment = 10

    # Constructor
    def __init__(self, sid=0, sname="Unknown", type="Unknown",
                 price=0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object deleted")

    # ShowBook method
    def ShowBook(self):

        final_price = self.price

        if self.size.lower() == "small":
            final_price = self.price

        elif self.size.lower() == "medium":
            final_price = self.price + (self.price * Shirt.size_increment / 100)

        elif self.size.lower() == "large":
            final_price = self.price + (self.price * Shirt.size_increment * 2 / 100)

        elif self.size.lower() == "xlarge":
            final_price = self.price + (self.price * Shirt.size_increment * 3 / 100)

        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", final_price)


# Parameterized object
s1 = Shirt(101, "Formal Shirt", "Formal", 1000, "Small")
s2 = Shirt(102, "Formal Shirt", "Formal", 1000, "Medium")
s3 = Shirt(103, "Formal Shirt", "Formal", 1000, "Large")
s4 = Shirt(104, "Formal Shirt", "Formal", 1000, "Xlarge")

print("Small Shirt:")
s1.ShowBook()

print("\nMedium Shirt:")
s2.ShowBook()

print("\nLarge Shirt:")
s3.ShowBook()

print("\nXlarge Shirt:")
s4.ShowBook()