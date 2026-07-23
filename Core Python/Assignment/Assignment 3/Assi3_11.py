    
# #Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1 = int(input("Enter the age of person 1: "))
tkprice1 = float(input("Enter the ticket price for person 1: "))
totalPrice = 0
if age1<12:
    totalPrice = totalPrice + (tkprice1 * 0.30)
elif age1>59:
    totalPrice = totalPrice + (tkprice1 * 0.50)
else:
    totalPrice = totalPrice + tkprice1
#First person end here.....

age2 = int(input("Enter the age of person 2: "))
tkprice2 = float(input("Enter the ticket price for person 2: "))
if age2<12:
    totalPrice = totalPrice + (tkprice2 * 0.30)
elif age2>59:
    totalPrice = totalPrice + (tkprice2 * 0.50)
else:
    totalPrice = totalPrice + tkprice2
#Second Person Ends here.....

age3 = int(input("Enter the age of person 3: "))
tkprice3 = float(input("Enter the ticket price for person 3: "))
if age3<12:
    totalPrice = totalPrice + (tkprice3 * 0.30)
elif age3>59:
    totalPrice = totalPrice + (tkprice3 * 0.50)
else:
    totalPrice = totalPrice + tkprice3  
#Third Person Ends here.....

age4 = int(input("Enter the age of person 4: "))
tkprice4 = float(input("Enter the ticket price for person 4: "))
if age4<12:
    totalPrice = totalPrice + (tkprice4 * 0.30)
elif age4>59:
    totalPrice = totalPrice + (tkprice4 * 0.50)
else:
    totalPrice = totalPrice + tkprice4
#Fourth Person Ends here.....

age5 = int(input("Enter the age of person 5: "))
tkprice5 = float(input("Enter the ticket price for person 5: "))
if age5<12:
    totalPrice = totalPrice + (tkprice5 * 0.30)
elif age5>59:
    totalPrice = totalPrice + (tkprice5 * 0.50)
else:
    totalPrice = totalPrice + tkprice5
#Fifth Person Ends here.....

print("Total ticket price for all five persons is:", totalPrice)
    