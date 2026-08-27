# Input 5 subjects from user and display grade(First class,Second class..)

m1 = int(input("Entter marks of Subject 1: "))
m2 = int(input("Entter marks of Subject 2: "))
m3 = int(input("Entter marks of Subject 3: "))
m4 = int(input("Entter marks of Subject 4: "))
m5 = int(input("Entter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total/5

print("Total MArks =", total)
print("Percentage =", per)

if per > 90:
    print("First Class")
elif per > 75:
    print("Second Class")
elif per > 35:
    print("Pass Class")
else:
    print("Fail")