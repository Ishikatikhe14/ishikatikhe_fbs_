#Write a program to check whether a number is prime or not using recursion.

def prime(n, i=2):
    if n <=2 :
        return n == 2
    if n % i == 0:
        return False    
    if i * i > n:
        return True
    return prime(n, i + 1)

num = int(input("Enter a number: "))
if prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")