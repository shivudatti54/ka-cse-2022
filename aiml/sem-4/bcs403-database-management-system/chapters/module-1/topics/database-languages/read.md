# Database Languages (DBMS)

## Introduction

A Database Management System (DBMS) is a software system designed to store, manage, and facilitate access to databases. For users to interact with a database—be it to define its structure, manipulate its data, or control access to it—a precise and structured method of communication is essential. This is where **database languages** come into play. They provide the set of commands and syntax that act as an interface between the user and the DBMS, enabling all database operations.

Database languages are primarily categorized based on their functionality. The most fundamental categorization divides them into Data Definition Language (DDL) and Data Manipulation Language (DML). Other important types include Data Control Language (DCL) and Transaction Control Language (TCL).

## Core Concepts

### 1. Data Definition Language (DDL)

DDL is used to define the database schema, i.e., the structure of the database. It deals with the description of the database objects and is used to create, modify, and delete the structure of database objects like tables, indexes, and constraints. DDL commands are auto-committed, meaning they permanently save all changes to the database. Common DDL commands include:

*   **CREATE:** Used to create new database objects like tables, views, or indexes.
    *   Example: `CREATE TABLE Student (Roll_No INT, Name VARCHAR(50), Marks INT);`
*   **ALTER:** Used to modify the structure of an existing database object, such as adding, dropping, or modifying a column in a table.
    *   Example: `ALTER TABLE Student ADD COLUMN Address VARCHAR(100);`
*   **DROP:** Deletes an existing database object from the database. This removes the table structure and all its data.
    *   Example: `DROP TABLE Student;`
*   **TRUNCATE:** Removes all records from a table, including freeing up the space allocated to the table. Unlike DROP, it does not destroy the table's structure.
    *   Example: `TRUNCATE TABLE Student;`
*   **RENAME:** Used to rename an existing database object.
    *   Example: `RENAME TABLE Student TO Student_Info;`

### 2. Data Manipulation Language (DML)

DML is used for managing data within the database objects. It allows users to insert, update, delete, and retrieve data from the database. DML commands are not auto-committed; changes can be rolled back. The most common DML command is SELECT for querying data.

*   **INSERT:** Adds new rows of data into a table.
    *   Example: `INSERT INTO Student VALUES (101, 'Alice', 85);`
*   **UPDATE:** Modifies existing data in a table.
    *   Example: `UPDATE Student SET Marks = 90 WHERE Roll_No = 101;`
*   **DELETE:** Removes one or more rows from a table based on a condition.
    *   Example: `DELETE FROM Student WHERE Roll_No = 101;`
*   **SELECT:** Retrieves data from one or more tables. It is the most frequently used DML command.
    *   Example: `SELECT Name, Marks FROM Student WHERE Marks > 75;`

### 3. Data Control Language (DCL)

DCL is used to control access to the data stored in the database. It handles the authorization and permissions for users and roles.

*   **GRANT:** Gives user(s) specific privileges to perform certain tasks on database objects.
    *   Example: `GRANT SELECT, INSERT ON Student TO user1;`
*   **REVOKE:** Takes back privileges granted to a user.
    *   Example: `REVOKE INSERT ON Student FROM user1;`

### 4. Transaction Control Language (TCL)

TCL commands are used to manage transactions within a database. A transaction is a single logical unit of work that consists of one or more DML operations. TCL ensures the integrity and consistency of the database.

*   **COMMIT:** Permanently saves all changes made during the current transaction.
    *   Example: After several UPDATE statements, `COMMIT;` makes the changes permanent.
*   **ROLLBACK:** Undoes all changes made in the current transaction, reverting the database to its last committed state.
    *   Example: If an error occurs, `ROLLBACK;` cancels all changes since the last COMMIT.
*   **SAVEPOINT:** Sets a point within a transaction to which you can later roll back.
    *   Example: `SAVEPOINT S1;` ... later `ROLLBACK TO SAVEPOINT S1;`

## Summary of Key Points

| Category | Purpose | Key Commands |
| :--- | :--- | :--- |
| **DDL** | To define and modify the database structure/schema. | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** | To manipulate (insert, update, delete, retrieve) data within the defined objects. | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | To control user access and permissions for data security. | `GRANT`, `REVOKE` |
| **TCL** | To manage transactions and ensure data integrity. | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

**Conclusion:** Database languages are the fundamental tools for interacting with a DBMS. While **DDL** shapes the skeleton of the database, **DML** works with the data inside it. **DCL** acts as a security gatekeeper, and **TCL** ensures that data operations are processed reliably as complete units. Understanding these languages is the first step toward effectively managing and utilizing any relational database system like MySQL, Oracle, or PostgreSQL.