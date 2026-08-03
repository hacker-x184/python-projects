from database import db_query
def borrow_book(isbn,qn):
    title = db_query(f"SELECT title FROM book WHERE isbn = '{isbn}';")
    db_query(f"UPDATE book SET quantity={qn} WHERE isbn = '{isbn}'; ")
    print(f"Now you borrow the {title[0][0]}")
    db_query(f"")
    



"""borrow_book()

return_book()

borrow_history()

overdue_books()"""