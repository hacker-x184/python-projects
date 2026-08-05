from database import db_query
def borrow_book(isbn,member_id,qn):
    title = db_query(f"SELECT title FROM book WHERE isbn = '{isbn}';")
    db_query(f"UPDATE book SET quantity={qn} WHERE isbn = '{isbn}'; ")
    print(f"Now you borrow the {title[0][0]}")
    book_id  = db_query(f"SELECT book_id FROM book WHERE isbn = '{isbn}';")
    db_query(f"INSERT INTO borrow(book_id,member_id,due_date,status)VALUES ({book_id},{member_id},CURRENT_DATE + 7,TRUE);")
def return_book(book_id):
    try:            
        temp = db_query(f"SELECT * FROM borrow WHERE book_id = {book_id};")
        if temp:
            db_query(f"UPDATE borrow SET return_date = CURRENT_DATE,status = FALSE WHERE book_id = {temp[0][0]};")
            print("Your book return successful")
        else:
            print("Your book id are not Avaiable")
    except Exception as e:
        print(e)
def borrow_history(member_id):
    try:
        temp = db_query(f"SELECT * FROM borrow WHERE member_id = {member_id};")
        print("here is your history:-\n",temp)
    except Exception as e:
        print(e)
def check_overdue():
    try:
        temp = db_query(f"SELECT * FROM borrow WHERE due_date < CURRENT_DATE;")
        print("Here is th data of the member of the overdue book")
        for due in temp:
            print(due)
    except Exception as e:
        print(e)
"""borrow_book()
return_book()
borrow_history()
overdue_books()"""