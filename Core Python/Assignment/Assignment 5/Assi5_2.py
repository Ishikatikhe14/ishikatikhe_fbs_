# #2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input("Enter the no of student :"))
s1 =int(input ("Enter the mark s1: "))
s2=int(input("Enter the mark s2:"))
s3 =int(input("Enter the mark s3:"))
s4 =int(input("Enter the mark s4:"))
s5 =int(input("Enter the mark s5:"))

total = s1+s2+s3+s4+s5
percentage = total/5
average =n/total

print("total mark =",total)
print("percentage =",percentage)
print("average =",average)