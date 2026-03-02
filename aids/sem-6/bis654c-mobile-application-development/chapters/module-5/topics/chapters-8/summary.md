# SQLite Database in Android: Chapters 8

===========================================

## Key Points

---

- **What is SQLite?**
  - A self-contained, file-based database engine
  - Supports SQL (Structured Query Language)
- **Creating a SQLite Database in Android**
  - Create a new database using `SQLiteDatabase` class
  - Specify database name, version, and size
- **Connecting to a SQLite Database in Android**
  - Create a connection using `SQLiteOpenHelper` class
  - Use `openDatabase()` method to get a connection
- **SQLiteDatabase Methods**
  - `create()`: Create a new database
  - `insert()`: Insert data into a table
  - `update()`: Update data in a table
  - `delete()`: Delete data from a table
  - `query()`: Retrieve data from a table

## Important Formulas and Definitions

---

- **SQL Syntax**
  - `CREATE TABLE table_name (column1 data_type, column2 data_type);`
  - `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`
- **Database Schema**
  - A schema is a blueprint for the database structure

## Relevant Theorems

---

- **First Normal Form (1NF)**: Each table cell must contain a single value
- **Second Normal Form (2NF)**: Each non-key attribute must depend on the entire primary key

## Revision Tips

---

- Practice creating and connecting to SQLite databases
- Familiarize yourself with SQLiteDatabase methods
- Review SQL syntax and database schema
