#User Registration
import random
from database import *
from customers import *
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
    cobj = Customer(username,password,name,age,city,acc_num)
def SingIn():
    acc_no = int(input())
    password = input("Enter Your Password here :-")
    temp_acc = db_query(f"select account_number from customers where {acc_no} = account_number")
    temp_pass = db_query(f"select password from customers where {password} = password")
    if acc_no == temp_acc and password == temp_pass:
        print("SignIn Successful ")
    else:
        print("Your Account Number and Password are wrong")
