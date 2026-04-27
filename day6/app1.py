username = input("Username: ")
password = input("Password: ")

if username == "Bijoy":
    if password == "1234":
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")