#Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter the value of n: "))

print("a. Sum of series (1 + 2 + ... + n) =", sum_numbers(n))


# b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# def sum_factorials(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += factorial(i)
#     return total

n = int(input("Enter the value of n: "))

print("b. Sum of series (1! + 2! + ... + n!) =", sum_factorials(n))


# c. 1^1 + 2^2 + 3^3+ ...... n^n
def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter the value of n: "))

print("c. Sum of series (1^1 + 2^2 + ... + n^n) =", sum_powers(n))