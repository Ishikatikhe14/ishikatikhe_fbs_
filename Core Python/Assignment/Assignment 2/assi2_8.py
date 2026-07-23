#Write a program to swap two numbers using third variable.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a =", a, "b =", b)
c = a
a = b
b = c
print("After swapping: a =", a, "b =", b)