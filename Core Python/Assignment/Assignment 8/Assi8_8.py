# Write a program find reverse of a number

def reverse_number(num):
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
        
    return reversed_num

num = int(input("Enter a number: "))
print("Reverse of the number =", reverse_number(num))