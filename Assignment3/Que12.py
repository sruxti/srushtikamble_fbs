# wap to check if given 3 digit number is a palidrome or not.

num = int(input("Enter a 3-digit number: "))

d1 = num % 10
d2 = (num // 10) % 10
d3 = num // 100

reverse = d1 * 100 + d2 * 10 + d3

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Pallindrome Number")