# SQLite Database in Android: Revision Notes (Chapters 8)

=============================================

### Introduction

---

- SQLite is a self-contained, file-based database that can be used in Android applications.
- It is a popular choice for mobile application development due to its ease of use and flexibility.

### Key Points

---

- **What is SQLite?**
  - A lightweight, file-based database management system.
  - Designed for mobile and embedded devices.
- **SQLite Database Creation**
  - Create a new database file using `sqlite_create_database()` function.
  - Specify the database name, location, and size.
- **Connecting to SQLite Database**
  - Use `sqlite_open()` function to establish a connection to the database.
  - Pass the database name and mode (e.g., `SQLITE_OPEN_READWRITE`).
- **SQL Statements**
  - Use SQL statements to create, read, update, and delete data in the database.
  - Examples:
    - `CREATE TABLE`: create a new table.
    - `INSERT INTO`: insert data into a table.
    - `SELECT *`: retrieve data from a table.
- **Database Schema**
  - Define the structure of the database using tables, columns, and data types.
  - Use `CREATE TABLE` statement to create a new table.

### Important Formulas and Definitions

---

- **SQL Syntax**
  - `SELECT * FROM table_name;`: retrieve all data from a table.
  - `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`: insert data into a table.
- **Database Modes**
  - `SQLITE_OPEN_READWRITE`: read and write access.
  - `SQLITE_OPEN_READONLY`: read-only access.

### Important Theorems

---

- **ACID (Atomicity, Consistency, Isolation, Durability)**: ensures database transactions are processed reliably.
- **Normalization**: ensures data is stored in a structured and organized manner.

### Quick Revision Tips

---

- Familiarize yourself with SQL syntax and database schema.
- Understand the importance of ACID and normalization.
- Practice creating and connecting to SQLite databases using Android.
