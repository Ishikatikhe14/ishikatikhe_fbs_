#WAP to calculate selling price of book based on cost price and discount.

cp = int(input("Enter the cost price of the book: "))
discount = int(input("Enter the discount percentage: "))  

sp = cp - (cp * discount / 100)

print("The selling price of the book is:", sp)