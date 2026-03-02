# **Revision Notes: SQLite Database in Android (Chapters 8)**

## **Key Points**

- **What is SQLite?**
  - A self-contained, serverless, zero-configuration database.
  - A lightweight disk-based database that allows for fast and efficient data storage.
- **Advantages of SQLite**
  - Fast and efficient data retrieval.
  - Easy to use and implement.
  - Zero configuration required.
- **Creating a SQLite Database**
  - Use the `sqlite3` command-line tool or the `SQLiteOpenHelper` class in Android.
  - Create a database file with a `.db` extension.
- **Connecting to a SQLite Database**
  - Use the `SQLiteDatabase` class in Android.
  - Create a `Connection` object to establish a connection to the database.
- **Database Object Model**
  - `Cursor`: A read-only reference to a row in a database table.
  - `RowId`: A unique identifier for each row in a database table.
  - `SQLiteOpenHelper`: A helper class that simplifies the process of creating a database.
- **SQL Queries**
  - `SELECT`: Retrieve data from a database table.
  - `INSERT`: Insert data into a database table.
  - `UPDATE`: Update data in a database table.
  - `DELETE`: Delete data from a database table.

## **Important Formulas and Definitions**

- **SQL Query Syntax**
  - `SELECT * FROM table_name;` - Retrieve all data from a table.
  - `INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');` - Insert data into a table.
- **Relationship Between Tables**
  - **Primary Key**: A unique identifier for each row in a table.
  - **Foreign Key**: A field in one table that references the primary key of another table.

## **Important Theorems**

- **ACID Properties**
  - Atomicity: Ensure that database transactions are processed as a single unit.
  - Consistency: Ensure that database data remains consistent and valid.
  - Isolation: Ensure that database transactions are executed independently.
  - Durability: Ensure that database transactions are persisted even in the event of a failure.
