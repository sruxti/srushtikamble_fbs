#WAP TO CALCULATE THE PERCENTAGE OF STUDENT BASED ON MARKS OF ANY 5 SUBJECTS.

m1 = float(input("Enter marks 1:"))
m2 = float(input("Enter marks 2:"))
m3 = float(input("Enter marks 3:"))
m4 = float(input("Enter marks 4:"))
m5 = float(input("Enter marks 5:"))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Percentage =",percentage)