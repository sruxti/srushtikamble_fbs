# Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12)+ inches
centimeters = total_inches * 2.54
meters = centimeters / 100

print("Meters =", meters)
print("Centimeters =", centimeters)