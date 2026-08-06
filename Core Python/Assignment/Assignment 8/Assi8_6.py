# #Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci_series(n):
    a=1
    b=1
    
    if n>= 1:
        print(a, end=" ")
    if n>= 2:
        print(b, end=" ")
    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

n= int(input("Enter the number of terms: "))
fibonacci_series(n)