#Write a program to enter P, T, R and calculate Compound Interest.
P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time Period: "))   
R = int(input("Enter Rate of Interest: "))

CI = P * (1 + R / 100) ** T - P

print("Compound Interest is:", CI)