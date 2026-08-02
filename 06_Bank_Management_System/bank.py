#Bank Services
from database import *
import datetime
class Bank:
    def __init__(self,username,account_number):
        self.__username = username
        self.__account_number = account_number
        self.create_transaction_table()
        
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                f"( timedate VARCHAR(30),"
                f"account_number INTEGER,"
                f"remarks VARCHAR(30),"
                f"amount INTEGER )")
    def deposit(self,amount):
        temp = db_query(f"SELECT balance,account_number FROM customer WHERE username = '{self.__username}'")
    
    def check_balance(username,account_number):
        balance = db_query(f"SELECT balance from customers where username = '{username}'")
        print(f"Your Account {account_number} has the total Balance {balance[0][0]}")
    def cash_deposit(username,account_number,amount):
            balance = db_query(f"SELECT balance from customers where username = '{username}'")
            amount = balance[0][0]+amount
            db_query(f"UPDATE customers SET balance = '{amount}' WHERE account_number = {account_number}")
            print(f"Now  Account {account_number} have total Balance {balance[0][0]}")
    def cash_withdraw(username,account_number,amount):
            balance = db_query(f"SELECT balance from customers where username = '{username}'")
            amount = balance[0][0]-amount
            db_query(f"UPDATE customers SET balance = '{amount}' WHERE account_number = {account_number}")
            print(f"Now  Account {account_number} have total Balance {balance[0][0]}")
    def fund_transition(account_number,account_number2,amount):
        balance = db_query(f"SELECT balance from customers where account_number = {account_number}")
        temp = balance[0][0]-amount
        db_query(f"UPDATE customers SET balance = '{temp}' WHERE account_number = {account_number}")
        print(f"Now  Account {account_number} have total Balance {temp}")
        balance = db_query(f"SELECT balance from customers where account_number = {account_number2}")
        temp = balance[0][0]+amount
        db_query(f"UPDATE customers SET balance = '{temp}' WHERE account_number = {account_number2}")
        print(f"Now  Account {account_number2} have total Balance {temp}")
        