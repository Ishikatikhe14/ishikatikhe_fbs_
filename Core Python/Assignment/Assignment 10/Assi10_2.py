#2. Write a program to find maximum and minimum element in a list.

a = [10, 25, 5, 40, 15]

maximum = a[0]
minimum = a[0]

for i in a:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)