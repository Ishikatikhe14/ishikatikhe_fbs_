#9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list =", even)
print("Odd list =", odd)