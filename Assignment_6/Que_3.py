for i in range(1, 5):
    for j in range(4-i-1):
        print(" ", end=" ")

    if i == 0:
        print(" 1 ")

    elif i == 1:
        print("1 1")

    elif i == 2:
        print("1 2 1")

    elif i == 3:
        print("1 3 3 1")