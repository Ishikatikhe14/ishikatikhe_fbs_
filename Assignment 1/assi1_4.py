#Write a program to enter P, T, R and calculate simple Interest.

P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time Period: "))
R = int(input("Enter Rate of Interest: "))
SI = (P * T * R) / 100


print("Simple Interest is:", SI)