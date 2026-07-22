#WAP TO INPUT TWO ANGLES FROM USER AND FIND THIRD ANGLE OF THE TRIANGLE

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))

c = 180 - (a + b)

print("Third angle =", c)