#Write a program to reverse a number using recursion.

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    rev = rev * 10 + (n % 10)
    return reverse_number(n // 10, rev)

num = int(input("Enter a number: "))
print("Reversed number =", reverse_number(num))