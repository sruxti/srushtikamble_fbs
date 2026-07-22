#WAP TO FIND THE ROOTS OF A QUADRATIC EQUATION

import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
d=(b*b)-(4*a*c)

root1 = (-b + math.sqrt(d))/(2*a)
root2 = (-b - math.sqrt(d))/(2*a)

print("first root: ",root1)
print("second root: ",root2)