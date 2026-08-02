from register import *
from bank import *
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
status = True      
while status:
    try:
        facility = int((input("1. Balance Enquiry\n2. Cash Deposit\n3. Cash Withdraw\n4. Fund Transition   :--")))
        if facility == 1 :
            username = input("Enter your Username here :-")
            account_number = input("Enter your Account Number here :-")
            Bank.check_balance(username,account_number)
        elif facility == 2:
            
            
    except ValueError:
        print("Invalid Input Try Again With valid input")