#Write a program to input angles of a triangle and check whether triangle is valid or not.
# angles = [ ]
# if angles[0] > 0 and angles[1] > 0 and angles[2] > 0:
#     if angles[0] + angles[1] + angles[2] == 180:
#         print("Triangle is valid.")
#     else:
#         print("Triangle is not valid.")
# else:
#     print("Triangle is not valid.")

a = int(input("Enter first angle = "))
b = int(input("Enter second angle = "))
c = int(input("Enter third angle = "))
if  a+b+c==180 :
    print("It is Valid Triangle")
else:
    print("Invalid")