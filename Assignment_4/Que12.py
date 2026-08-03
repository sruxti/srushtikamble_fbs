#wap to check if given number is Armstrong number or not.

n = int(input("Enter a number: "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")