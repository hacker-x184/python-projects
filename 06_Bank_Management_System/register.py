#User Registration
import random
from database import *
from customers import *
from bank import *
def SingUp():
    username=input("Enter Your name here :-")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username Already Exists")
        SingUp()
    else:
        print("Username is Available please Proceed")
        password = input("Enter your password here:- ")
        name = input("Enter your name:-")
        age = int(input("Enter your age here:-"))
        city = input("Enter your city:-")
        balance = int(input("Enter your current balance:-"))
        isvalue = True
        while isvalue:
            acc_num = random.randint(10000000,999999999)
            temp = db_query(f"SELECT account_number FROM customers where account_number = '{acc_num}';")
            num = db_query(f"SELECT account_number FROM customers")
            if temp in num:
                continue
            else:
                print(f"Your account number is {acc_num}")
                isvalue = False
    cobj = Customer(username,password,name,age,city,balance,acc_num)
    bobj = Bank(username,acc_num)
def SingIn():
    acc_no = int(input("Enter Your account number here :-"))
    password = input("Enter Your Password here :-")
    temp_acc = db_query(f"select account_number from customers where account_number = {acc_no}")
    temp_pass = db_query(f"select password from customers where password = '{password}'")
    if temp_acc and temp_pass:
        if password == temp_pass[0][0]:
            print("Sign In Successful ")   
            return acc_no
        else:
            print("Wrong Password")
    else:
        print("Your Account Number not found")