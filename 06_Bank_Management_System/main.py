from register import *
from bank import *
# from bank import *
print("Welcome to our Banking System")
status = False
while True:
    try:
        register = int((input("1. SignUp\n2. SignIn     :--")))
        if register == 1 or register==2:
            if register == 1:
                SingUp()
            else:
                acc_no = SingIn()
                user = db_query(f"SELECT username FROM customers WHERE account_number = {acc_no} ")
                status = True
            break
        else:
            print("Please enter a valid input From Options")
            break
            
    except ValueError:
        print("Invalid Input Try Again With valid input")   
while status:
    try:
        facility = int((input("1. Balance Enquiry\n2. Cash Deposit\n3. Cash Withdraw\n4. Fund Transition\n5. Exit   :--")))
        if facility == 1 :
            Bank.check_balance(user[0][0],acc_no)
        elif facility == 2:
            amount = int(input("Enter the account you want to deposit :-"))
            Bank.cash_deposit(user[0][0],acc_no,amount)
        elif facility == 3:
            amount = int(input("Enter the account you want to Withdraw :-"))
            Bank.cash_withdraw(user[0][0],acc_no,amount)
        elif facility == 4:
            amount = int(input("Enter the amount you want to transfer :-"))
            acc_no2 = print("Enter the account number that you want to transfer Your money")
            Bank.fund_transition(acc_no,acc_no2,amount)
        elif facility == 5:
            print("Thanks For Coming Our Bank")
            break
        else:
            print("You select the invaild Option")
    except ValueError:
        print("Invalid Input Try Again With valid input")