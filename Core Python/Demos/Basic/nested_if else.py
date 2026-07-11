gender = (input("Enter your gender(M/F): "))
age = int(input("Enter your age: "))

if (gender == 'f'):
    if (age >= 18):
        print("You are eligible for marriage.")
    else:
        print('pahele padhai kae lo.')
else:
    if (age>=21):
        print('boy is eligible for marringe.')
    else:
        print('pahele kama lo.')