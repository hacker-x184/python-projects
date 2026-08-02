# Database Management Banking

import psycopg2 as sql

mydb = sql.connect(
    host="localhost",
    database="bank",
    user="postgres",      # PostgreSQL username
    password="1234",      # Your PostgreSQL password
    port="5001"           # Default PostgreSQL port
)

cursor = mydb.cursor()

def create_customer_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20),
            password VARCHAR(20),
            name VARCHAR(20),
            age INTEGER,
            city VARCHAR(20),
            balance INTEGER,
            account_number INTEGER NOT NULL,
            status BOOLEAN
        );
    """)
    mydb.commit()
    print("Customer table created successfully!")

if __name__ == "__main__":
    create_customer_table()
def db_query(query):
    cursor.execute(query)

    if query.strip().upper().startswith("SELECT"):
        return cursor.fetchall()
    else:
        mydb.commit()
        return "Query executed successfully."