# wap to check if person is eligible to marry or not (male age>=21 and female age>=18)

gender = input("Enter gender (m/f): ")
age = int(input("Enter age: "))

if(gender == 'f'):
    if(age >= 18):
        print("Girl is eligible for Marriage.")
    else:
        print("Not eligible.")
else:
    if(age >= 21):
        print("Boy is eligible for Marriage.")
    else:
        ("Not eligible.")