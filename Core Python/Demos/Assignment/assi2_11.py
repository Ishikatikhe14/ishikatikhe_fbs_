# #Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# amount = int(input("Enter the amount: "))
# # Denominations of notes    
# denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# note_count = {}
# for denomination in denominations:
#     note_count[denomination] = amount // denomination
#     amount %= denomination

# for denomination, count in note_count.items():
#     if count > 0:
#         print(f"Number of {denomination} notes needed: {count}")

amount = int(input("Enter amount: "))

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print("500 Notes =", n500)
print("200 Notes =", n200)
print("100 Notes =", n100)
print("50 Notes =", n50)
print("20 Notes =", n20)
print("10 Notes =", n10)