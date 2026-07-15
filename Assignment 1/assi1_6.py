#Write a Program to input two angles from user and find third angle of the triangle.
A1 = int(input("Enter the first angle of the triangle: "))
A2 = int(input("Enter the second angle of the triangle: "))     

A3 = 180 - (A1 + A2)

print("The third angle of the triangle is:", A3)