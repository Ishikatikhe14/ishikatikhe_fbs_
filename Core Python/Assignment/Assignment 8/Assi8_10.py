#Write a program to check if entered year is a leap year or not.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

year = int(input("Enter a year: "))
leap_year(year)