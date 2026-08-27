# wap to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter the same. 
# If user enters the same number then show her success message otherwise failed. (Something like captcha)



import random
userID = input("Enter the userid: ")
password = input("Enter password: ")

if(userID == "srushti" and password == "srushh05"):
    captch = random.randint(1000,9999)
    print("captch: ", captch)

    user = int(input("Enter User: "))
    if(user == captch):
        print("Login Successful.")
    else:
        print("Captch Failed.")
else:
    print("Invalid userID and Password.")