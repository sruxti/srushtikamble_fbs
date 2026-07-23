# WAP TO CALCULATE SELLING PRICE OF BOOK BASED ON COST PRICE AND DISCOUNT.

cp = float(input("Enter Cost Price: "))
d = float(input("Enter Discount(%): "))

discount = (cp * d) / 100
sp = cp - discount

print("Selling Price =", sp)