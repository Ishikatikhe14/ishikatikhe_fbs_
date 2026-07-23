#Find the sum of three-digit number.

num=379
 
d1 = num % 100
num = num // 100

d2 = num % 10
d3 = num // 10    

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3
print("The sum of the digits is:", sum)