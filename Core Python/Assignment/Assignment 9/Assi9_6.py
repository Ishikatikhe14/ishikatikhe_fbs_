#Write a program to print Fibonacci series using recursion.

def fibinacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibinacci(n - 1) + fibinacci(n - 2)

n=int(input("Enter n: "))

for i in range(n):
    print(fibinacci(i), end=" ")