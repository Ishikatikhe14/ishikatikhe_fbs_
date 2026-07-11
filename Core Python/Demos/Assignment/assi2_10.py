#Write a program to reverse three-digit number.

number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

# Reversing the number
reversed = units * 100 + tens * 10 + hundreds
print("The reversed number is:", reversed)

