#Write a program to reverse a given number using recursive function.
rev =0
def reverse(n):
    global rev
    if n == 0:
        return 
    digit = n % 10
    rev = rev * 10 + digit
    reverse(n // 10)    
    
num = int(input("Enter a number: "))
reverse(num)
print("Reversed Number: ", rev)