#wap to print all numbers in range divisible by a given number.

n = int(input("Enter n: "))
d = int(input("Enter divisor: "))

for i in range(1, n + 1):
    if i % d == 0:
        print(i)