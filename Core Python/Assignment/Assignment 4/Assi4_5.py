#WAP to print Fibonacci series upto n.
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c