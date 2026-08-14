#3. Write a program to find the second largest element in the list.
a = [10, 25, 5, 40, 15]

largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest =", second)