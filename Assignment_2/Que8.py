# WAP TO SWAP TWO NUMBERS USING THIRD VARIABLE.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After Swapping: ")
print("First Number= ",a)
print("Second Number= ",b)