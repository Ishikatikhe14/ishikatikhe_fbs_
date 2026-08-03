# #a
# n = 5
# # Upper half of the diamond  
# for i in range(n):
#         for j in range(n - i - 1):
#             print(" ", end="")
#         for j in range(2 * i + 1):
#             if j == 0 or j == 2 * i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# # Lower half of the diamond

# for i in range(n - 1, -1, -1):
#     for j in range(n - i - 1):
#             print(" ", end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#                 print("*", end="")
#         else:
#                 print(" ", end="")
#     print()


#b
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end =' ')
    print()

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=' ')
    print()