#Write a program to calculate the percentage of student based on marks of any 5 subjects.
subject1 = int(input("Enter the marks of subject 1: "))
subject2 = int(input("Enter the marks of subject 2: "))
subject3 = int(input("Enter the marks of subject 3: "))
subject4 = int(input("Enter the marks of subject 4: "))
subject5 = int(input("Enter the marks of subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

print("The percentage of the student is:", percentage)