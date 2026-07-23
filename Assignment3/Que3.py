# WAP TO INPUT ANGLES OF TRIANGLE AND CHECK WHETHER TRIANGLE IS VAILD OR NOT.

a = float(input("Ente first angle: "))
b = float(input("Ente Second angle: "))
c = float(input("Ente Third angle: "))

if a + b + c == 180:
    print("Triangle is Valid.")
else:
    print("Triangle is Not Valid.")