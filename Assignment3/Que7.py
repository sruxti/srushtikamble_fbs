# WAP TO CHECK IF USER HAS ENTERED CORRECT USERID AND PASSWORD.

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "srushti" and password == "2005":
    print("Login Successful")
else:
    print("Invalid User ID or Password")