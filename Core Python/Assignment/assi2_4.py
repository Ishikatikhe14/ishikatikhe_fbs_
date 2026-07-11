#WAP to calculate area of triangle and rectangle

# Area of triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area_triangle = 1/2 * base * height

# Area of rectangle
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area_rectangle = length * breadth

print("The area of the triangle is:", area_triangle)
print("The area of the rectangle is:", area_rectangle)