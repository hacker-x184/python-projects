# 📚 Library Management System

A console-based **Library Management System** built using **Python**, **Object-Oriented Programming (OOP)**, and **PostgreSQL**. This project demonstrates CRUD operations, relational database management, and modular programming concepts.

---

## 🚀 Features

### 📖 Book Management
- ➕ Add New Book
- ❌ Remove Book
- ✏️ Update Book Details
- 🔍 Search Book by ISBN
- 📋 Display All Books

### 👤 Member Management
- ➕ Add Member
- ❌ Remove Member
- ✏️ Update Member Details
- 🔍 Search Member
- 📋 Display All Members

### 🔄 Borrow Management
- 📚 Borrow Book
- ↩️ Return Book
- 📜 Borrow History
- ⏰ Check Overdue Books

### 🗄️ Database
- PostgreSQL Integration
- Relational Database Design
- Foreign Key Relationships
- Automatic Table Creation

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| PostgreSQL | Database |
| psycopg2 | PostgreSQL Connector |
| SQL | Database Queries |
| OOP | Project Structure |

---

# 📂 Project Structure

```
Library_Management_System/
│
├── database.py          # Database connection & table creation
├── book.py              # Book CRUD operations
├── members.py           # Member CRUD operations
├── borrow.py            # Borrow & Return operations
├── choice.py            # Menu logic
├── main.py              # Entry point
├── requirements.txt
└── README.md
```

---

# 🗃️ Database Schema

## 📚 Book Table

| Column | Type |
|---------|------|
| book_id | SERIAL PRIMARY KEY |
| title | VARCHAR(100) |
| category | VARCHAR(50) |
| isbn | VARCHAR(20) |
| quantity | INT |
| available | BOOLEAN |
| created_at | TIMESTAMP |

---

## 👤 Member Table

| Column | Type |
|---------|------|
| member_id | SERIAL PRIMARY KEY |
| name | VARCHAR(50) |
| phone | VARCHAR(15) |
| city | VARCHAR(20) |
| joined_on | DATE |
| status | BOOLEAN |

---

## 🔄 Borrow Table

| Column | Type |
|---------|------|
| borrow_id | SERIAL PRIMARY KEY |
| book_id | Foreign Key |
| member_id | Foreign Key |
| borrow_date | DATE |
| due_date | DATE |
| return_date | DATE |
| status | BOOLEAN |

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/hacker-x184/Library-Management-System.git
```

### 2️⃣ Move into the Project

```bash
cd Library-Management-System
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL

Open `database.py` and update:

```python
host="localhost"
database="library"
user="postgres"
password="your_password"
port="5001"
```

### 5️⃣ Run the Project

```bash
python main.py
```

The database tables will be created automatically if they do not already exist.

---

# 🎯 Learning Outcomes

Through this project, I practiced:

- Object-Oriented Programming (OOP)
- Python Modules & Packages
- PostgreSQL Integration
- SQL CRUD Operations
- Foreign Key Relationships
- Exception Handling
- Modular Project Structure
- Database Design
- Problem Solving

---

# 📸 Sample Menu

```
=========================================
      📚 Library Management System
=========================================

1. Add Book
2. Borrow Book
3. Remove Book
4. Return Book
5. Search Book
6. Display Books
7. Add Member
8. Exit

=========================================
```

---

# 🚧 Future Improvements

- User Authentication
- Fine Calculation for Overdue Books
- ISBN Validation
- Better Console UI
- Search by Book Title
- Member Login
- Export Reports
- Django Web Interface

---

# 👨‍💻 Author

**Mohd Inzamam**

🎓 B.Tech CSE (AI & ML)

🌱 Currently Learning:
- Django
- Machine Learning
- Data Science
- Full Stack Development

GitHub: https://github.com/hacker-x184

---

# ⭐ If you like this project

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.