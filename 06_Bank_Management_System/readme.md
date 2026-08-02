# 🏦 Bank Management System

A **Python-based Bank Management System** that uses **PostgreSQL** as its database. This project simulates basic banking operations such as account creation, customer authentication, deposits, withdrawals, fund transfers, and balance inquiries.

This project was built to strengthen my understanding of **Python**, **Object-Oriented Programming (OOP)**, **PostgreSQL**, and **Database Connectivity using psycopg2**.

---

## 🚀 Features

### 👤 Customer Management

- Register New Customer
- Secure Login (Username & Password)
- Store Customer Information
- Unique Account Number Generation
- Account Status Management

### 💰 Banking Operations

- Balance Enquiry
- Cash Deposit
- Cash Withdrawal
- Fund Transfer
- Transaction History

### 🗄 Database Features

- PostgreSQL Integration
- Automatic Customer Table Creation
- Transaction Table Management
- SQL CRUD Operations
- Persistent Data Storage

---

# 🛠 Technologies Used

- Python 3
- PostgreSQL
- psycopg2
- Object-Oriented Programming (OOP)
- SQL

---

# 📂 Project Structure

```
06_Bank_Management_System/
│
├── main.py
├── database.py
├── bank.py
├── customers.py
├── register.py
├── README.md
```

---

# 🗄 Database Tables

## Customers

| Column | Type |
|----------|---------|
| username | VARCHAR(20) |
| password | VARCHAR(20) |
| name | VARCHAR(20) |
| age | INTEGER |
| city | VARCHAR(20) |
| account_number | INTEGER |
| status | BOOLEAN |

---

## Transactions

| Column | Type |
|----------|---------|
| timedate | TIMESTAMP |
| account_number | INTEGER |
| remarks | VARCHAR(30) |
| amount | INTEGER |

---

# 📋 Functionalities

## 1️⃣ Register Customer

- Create New Bank Account
- Save Customer Details
- Generate Account Number

---

## 2️⃣ Login

Authenticate customer using

- Account Number
- Password

---

## 3️⃣ Balance Enquiry

Displays the current account balance.

---

## 4️⃣ Cash Deposit

Deposit money into the account.

Example

```
Current Balance : ₹5000

Deposit Amount : ₹2000

New Balance : ₹7000
```

---

## 5️⃣ Cash Withdrawal

Withdraw money from the account.

Validation

- Sufficient Balance
- Valid Account

---

## 6️⃣ Fund Transfer

Transfer money from one account to another.

Checks

- Sender Exists
- Receiver Exists
- Sufficient Balance

---

## 7️⃣ Transaction History

Displays all transactions performed by the customer.

Example

```
Deposit      ₹5000

Withdraw     ₹2000

Transfer     ₹1000
```

---

# ▶️ How to Run

## Step 1

Clone the repository

```bash
git clone https://github.com/hacker-x184/python-Library.git
```

---

## Step 2

Move into the project

```bash
cd python-Library
```

---

## Step 3

Install PostgreSQL

Download and install PostgreSQL from the official website.

---

## Step 4

Install psycopg2

```bash
pip install psycopg2
```

---

## Step 5

Configure Database

Update your PostgreSQL credentials in **database.py**

```python
mydb = sql.connect(
    host="localhost",
    database="bank",
    user="postgres",
    password="YOUR_PASSWORD",
    port="5432"
)
```

---

## Step 6

Run the application

```bash
python main.py
```

---

# 🖥 Menu

```
========== Bank Management System ==========

1. Register Customer

2. Login

3. Balance Enquiry

4. Cash Deposit

5. Cash Withdrawal

6. Fund Transfer

7. Transaction History

8. Exit
```

---

# 📚 Concepts Practiced

- Python Fundamentals
- Object-Oriented Programming
- Classes & Objects
- Functions
- Loops
- Conditional Statements
- Exception Handling
- PostgreSQL
- SQL CRUD Operations
- Database Connectivity
- psycopg2
- Modular Programming

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Connect Python with PostgreSQL.
- Execute SQL queries using psycopg2.
- Build a menu-driven application.
- Implement user authentication.
- Design relational database tables.
- Perform CRUD operations.
- Manage customer and transaction records.
- Organize a Python project into multiple modules.

---

# 🚀 Future Improvements

- 🔐 Password Hashing using bcrypt
- 📧 Email Verification
- 📱 OTP Login
- 💳 ATM PIN Authentication
- 📊 Monthly Transaction Report
- 📈 Interest Calculation
- 📂 Export Transactions to PDF
- 📄 Export Transactions to Excel
- 🌐 Flask/Django Web Version
- 📱 Mobile App Version
- ☁ Cloud Database Support
- 🔔 SMS/Email Transaction Notifications

---

# 📸 Preview

```
========== Bank Management System ==========

1. Register Customer
2. Login
3. Balance Enquiry
4. Cash Deposit
5. Cash Withdrawal
6. Fund Transfer
7. Transaction History
8. Exit

Enter Choice :
```

---

# 👨‍💻 Author

**Mohd Inzamam**

- 🎓 B.Tech (AI/ML)
- 💻 Skills: Python, HTML, CSS, JavaScript, C++
- 🌱 Currently Learning: AI/ML, PostgreSQL, Ethical Hacking
- 🚀 Goal: Build AI-powered products and become an AI Engineer.

---

# 🔗 GitHub

**Repository**

https://github.com/hacker-x184/python-Library

---

# ⭐ Support

If you found this project helpful, consider giving the repository a **⭐ Star**.

It motivates me to keep learning, building, and sharing more Python, AI/ML, and Database projects.