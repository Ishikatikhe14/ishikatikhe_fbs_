#6. Write a program to remove duplicates from the list.

a = [10, 20, 10, 30, 20, 40]

b = []

for i in a:
    if i not in b:
        b.append(i)

print("List after removing duplicates:", b)