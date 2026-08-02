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
        temp = db_query(f"SELECT balance")
    
    def check_balance(self,username,account_number):
        balance = db_query(f"SELECT {username} from {username}_transaction")
        print(f"Your Account {account_number} has the total Balance {balance}")