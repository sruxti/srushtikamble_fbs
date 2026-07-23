# WAP TO INPUT ALL SIDES OF A TRIANGLE AND CHECK WHETHER TRIANGLE IS VALID OR NOT.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if(a+b>c)and(a+c>b)and(b+c>a):
    print("Triangle is Valid.")
else:
    print("Triangle is Not Valid.")