#Write a program to find sum of n numbers using recursion.

def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

num = int(input("Enter a number: "))
print("Sum =", sum(num))