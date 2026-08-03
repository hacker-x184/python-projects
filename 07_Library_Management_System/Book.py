from database import *
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


"""add_book()

remove_book()

update_book()

display_books()

search_book()"""