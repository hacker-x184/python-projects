from register import *
# from bank import *
print("Welcome to our Banking System")
while True:
    try:
        register = int((input("1. SignUp\n2. SignIn     :--")))
        if register == 1 or register==2:
            if register == 1:
                SingUp()
            else:
                SingIn()
            break
        else:
            print("Please enter a valid input From Options")
            break
            
    except ValueError:
        print("Invalid Input Try Again With valid input")