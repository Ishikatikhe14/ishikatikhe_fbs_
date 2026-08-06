#Write a program to check if entered number is a palindrome or not.

def is_palindrome(num):
    temp = num
    reversed_num = 0
    
    while temp > 0:
        digit = temp % 10
        reversed_num = (reversed_num * 10) + digit
        temp //= 10
        
    if temp == reversed_num:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
        
num = int(input("Enter a number: "))
is_palindrome(num)