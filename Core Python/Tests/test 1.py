#1. Write a program to find the area and perimeter of following figure (Accept the length, 
# breadth and radius from user:
import math

length =int(input("Enter the length of the rectangle :"))
breadth = int(input("Enter the breadth of the rectangle :"))
redius = float(input("Enter the radius of the semi-circle :"))

#Area:
area_rectangle =length * breadth
area_semicircle = 0.5 * math.pi(redius ** 2)
total_area = area_rectangle + area_semicircle

#perimeter
perimeter_semicircle_arc = math.pi *redius
total_perimeter =(2*length)+breadth + perimeter_semicircle_arc

print(f"\ntotal Area :{total_area : 2f}")
print(f"Total Perimeter : {total_perimeter :.2f}")


#2 Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time Period: "))
R = int(input("Enter Rate of Interest: "))
SI = (P * T * R) / 100


print("Simple Interest is:", SI)

#3 Write a program to accept distance in km and convert it into meters and centimeters both.
km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)

## 4Calculate the cost of painting the following building’s walls (both interior and exterior). 
# You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

area = int(input('Enter the area of one wall: '))
int_cost = int(input('Enter the cost for interior wall: '))
ext_cost = int(input('Enter the cost for exterior wall: '))

