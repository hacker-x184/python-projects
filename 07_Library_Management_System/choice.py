from Book import Book
from borrow import borrow_book
from database import *
import random
from members import *
def choice_1():
    try:
        title = input("Enter Your Book title here :-")
        category = input("Enter Your book category here:-")
        while True:
            isbn = str(random.randint(10000000,99999999))
            temp = db_query(
                f"SELECT isbn FROM book WHERE isbn='{isbn}'"
            )
            if not temp:
                break 
        quantity = int(input("Enter Your book quantity here:-"))
        book = Book(title,category,isbn,quantity)
        book.add_book()
        print("Your Book is successfully added in library!")
    except Exception as e:
            print(e)          
def choice_2():
    try:
        isbn = input("Enter Your Book isbn Number Here :- ")
        if isbn:
            result = db_query(f"SELECT quantity FORM book WHERE isbn='{isbn}';")
            qn = result[0][0]-1
            if qn >=0:
                borrow_book(isbn,qn)
            else:
                print("This book are currently not available in library")
    except Exception as e:
        print(e)
def choice_3():
    try:
        isbn = int(input("Enter Your Book isbn :--"))
        temp = db_query(f"""SELECT isbn FROM book WHERE isbn = '{isbn}'""")
        if temp:
            Book.remove_book(isbn)
        else:
            print(f"Your book {isbn} are not available in library")
    except Exception as e:
        print(e)
def choice_4():
    print()
def choice_5():
    try:
        isbn = int(input("Enter Your Book isbn :--"))
        temp = db_query(f"""SELECT isbn FROM book WHERE isbn = '{isbn}'""")
        if temp:
            Book.search_book(isbn)
        else:
            print(f"Your book {isbn} are not available in library")
    except Exception as e:
        print(e)
def choice_6():
    Book.display_book()
def choice_7():
    name = input("Please Enter your name here:--")
    phone = input("Please Enter your Phone number here:--")
    city = input("Please Enter your City here:--")
    member = Members.add_member(name,phone,city)
def choice_8():
    member_id = int(input("Please Enter your members here:--"))
    Members.remove_member(member_id)
    