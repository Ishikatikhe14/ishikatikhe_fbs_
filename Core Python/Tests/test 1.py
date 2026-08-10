#2 Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time Period: "))
R = int(input("Enter Rate of Interest: "))
SI = (P * T * R) / 100


print("Simple Interest is:", SI)