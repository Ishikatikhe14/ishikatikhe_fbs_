#WAP to check if given number Strong Number.
n = int(input("Enter a number: "))
temp = n
sum = 0

for i in range(1, n + 1):
    digit = n % 10

    fact = 1
    for j in range(1, digit + 1):
        fact = fact * j

    sum = sum + fact
    n = n // 10

    if n == 0:
        break

if sum == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")