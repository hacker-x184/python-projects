from Book import Book
from database import *
import random
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
            title = db_query(f"SELECT title FROM book where isbn = '{isbn}';")
            Book.remove_book(isbn)
            print(f"Your {title[0][0]} are Remove from the data base")
        else:
            print("Your book are not available in library")
    except Exception as e:
        print(e)
    
    
    
    
def choice_3():
    print()
def choice_4():
    print()
def choice_5():
    print()
def choice_6():
    print()