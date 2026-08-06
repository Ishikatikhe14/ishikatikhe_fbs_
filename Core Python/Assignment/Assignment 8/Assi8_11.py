#WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def checkArmstrong(num):
    sum= 0
    temp = num
    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    if sum == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

num = int(input("Enter a number: "))
checkArmstrong(num)