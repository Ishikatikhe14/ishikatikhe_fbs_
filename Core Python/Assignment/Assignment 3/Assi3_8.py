#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
userId =input("enter the user id=")
password =input("enter the password=")
if userId=="admin" and password=="virat@123":
    captcha=random.randint(1000,9999)
    print(f"your captcha = {captcha}")
    chuser = int (input("enter the captcha=>"))
    if chuser==captcha:
        print("User login successfully")
    else:
        print("Invalid captcha")
else:
    print("User is Invalid ")
    