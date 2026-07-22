#WAP TO ENTER P,T,R AND CALCULATE COMPOUND INTEREST

p = float(input("Enter principle: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

amount = p * (1 + r / 100)** t
ci = amount - p

print("Compound Interest=", ci)