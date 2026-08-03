#Library DATABASE
import psycopg2 as sql
mydb = sql.connect(
    host="localhost",
    database="library",
    user="postgres",      # PostgreSQL username
    password="1234",      # Your PostgreSQL password
    port="5001"           # Default PostgreSQL port
)
cursor = mydb.cursor()
def create_tables_book():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book(
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            category varchar(50),
            isbn VARCHAR(20),
            quantity INT,
            available BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            
        );
    """)
    mydb.commit()
    print("Library Table Created Successfully!")
def db_query(query):
    cursor.execute(query)
    if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
    else:
        mydb.commit()
        return "Query executed successfully."
def create_tables_member():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS member(
            member_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(15),
            city VARCHAR(20),
            joined_on DATE DEFAULT CURRENT_DATE,
            status BOOLEAN DEFAULT TRUE
        );
    """)
    mydb.commit()
    print("Members Table Created Successfully!")
def create_tables_borrow():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrow(
            borrow_id SERIAL PRIMARY KEY,
            book_id INT REFERENCES book(book_id),
            member_id INT REFERENCES member(member_id),
            borrow_date DATE DEFAULT CURRENT_DATE,
            due_date DATE,
            return_date DATE,
            status boolean
        );
    """)
    mydb.commit()
    print("Borrow Table Created Successfully!")
def create_database():
    create_tables_book()
    create_tables_member()
    create_tables_borrow()
    print("Database Created Successfully!")
if __name__ == "__main__":
    create_database()