#8. Write a program to create a duplicate of an existing list. It should not point to same list.

a = [10, 20, 30, 40]

b = []

for i in a:
    b.append(i)

print("Original list =", a)
print("Duplicate list =", b)