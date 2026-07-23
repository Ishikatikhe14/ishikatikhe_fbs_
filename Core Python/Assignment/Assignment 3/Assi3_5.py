#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter the value"))
b = int(input("enter the value"))
c = int(input("Enter the value"))
if(a==b==c):
    print("Trialgle is equilateral")
elif (a==b and b==c and a==c):
    print("triangle is isosceles")
else:
    print("trianglr is scalene")
