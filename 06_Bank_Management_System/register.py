#User Registration
import random
from database import *
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
        while True:
            acc_num = random.randint(10000000,999999999)
            temp = db_query(f"SELECT account_number FROM customers where account_number = '{acc_num}';")
            if temp:
                continue
            else:
                pass
SingUp()
