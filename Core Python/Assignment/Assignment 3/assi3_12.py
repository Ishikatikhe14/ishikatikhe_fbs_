#Write a program to check if given 3 digit number is a palindrome or not.

num = input("Enter a 3-digit number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome")