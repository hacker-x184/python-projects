from database import *
import numpy as np
class Book:
    def __init__(self,title,category,isbn,quantity):
        self.__title = title
        self.__category = category
        self.__isbn = isbn
        self.__quantity = quantity
    def add_book(self):
        db_query(f"""INSERT INTO book (title,category,isbn,quantity)
                 VALUES(
                     '{self.__title}',
                     '{self.__category}',
                     '{self.__isbn}',
                     {self.__quantity}
                     );
                     
        """)
    def remove_book(isbn):    
        db_query(f"DELETE FROM book where isbn = '{isbn}';")
    def update_book(isbn):
        try:   
            user_update = int(input("==== Update Book ====\n\nEnter Select the number that you want to update the value:-\n\n1. -  Update the title of the book\n2.  -  Update the Category of the book\n3.  -  Update the quantity of the book\n4. -  Update the isbn of the book\n\nEnter your Choice :--"))
            if user_update==1:
                print("You Want to update your title")
                isbn = input("Enter your isbn Number :-")
                temp = input("Enter the new title :--")
                db_query(f"""UPDATE book
                        SET title = '{temp}'
                        WHERE isbn = '{isbn}'""")
            elif user_update==2:
                print("You Want to update your Category")
                isbn = input("Enter your isbn Number :-")
                temp = input("Enter the new Category :--")
                db_query(f"""UPDATE book
                        SET title = '{temp}'
                        WHERE isbn = '{isbn}'""")
            elif user_update==3:
                print("You Want to update your Quantity")
                isbn = input("Enter your isbn Number :-")
                temp = int(input("Enter the new Quantity :--"))
                db_query(f"""UPDATE book
                        SET title = {temp}
                        WHERE isbn = '{isbn}'""")
            elif user_update==4:
                print("You Want to update your isbn")
                temp = input("Enter the new book_id :--")
                isbn = input("Enter your isbn Number :-")
                db_query(f"""UPDATE book
                        SET isbn = '{isbn}'
                        WHERE book_id = {temp}""")
            else:
                print("You Can't Update other than this four things")
        except Exception as e:
            print(e)
    def display_book():
        table = db_query("""SELECT * FROM book;""")
        np.array(table)
        print(table)
    def search_book(isbn):
        try:    
            table = db_query(f"""SELECT * FROM book WHERE isbn = '{isbn}'""")
            if table:
                np.array(table)
                print(table)
            else:
                print("Your Entered Book isbn Is not avaiable in library")
        except Exception as e:
            print(e)
