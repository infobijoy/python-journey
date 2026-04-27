#Both conditions must be True.
age = 20
verified = True

if age >= 18 and verified:
    print("Access Allowed")
else:
    print("Access Denied")

#At least one condition must be True.
role = "manager"

if role == "admin" or role == "manager":
    print("Dashboard Access")
else:
    print("No Access")


#Reverses True/False.
banned = False

if not banned:
    print("User Can Enter")


#Log in
username = input("Username: ")
password = input("Password: ")

if username == "Bijoy":
    if password == "1234":
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")