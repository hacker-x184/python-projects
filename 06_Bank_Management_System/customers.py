from database import *
class Customer:
    def __init__(self, username, password, name, age, city, balance,account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__balance = balance
        self.__account_number = account_number
        self.createuser()
    def createuser(self):
        db_query(f"INSERT INTO customers VALUES ('{self.__username}', '{self.__password}', '{self.__name}', '{self.__age}', '{self.__city}','{self.__balance}', '{self.__account_number}',True  );")
        mydb.commit()