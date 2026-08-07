#Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(n):
    if n == 0:
        return 0
    digit = n % 10
    return digit ** 3 + armstrong(n // 10)
num = int(input("Enter a number: "))

if armstrong(num) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")