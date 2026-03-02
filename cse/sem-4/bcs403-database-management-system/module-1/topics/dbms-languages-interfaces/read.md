# Database Languages and Interfaces

## Table of Contents

- [Database Languages and Interfaces](#database-languages-and-interfaces)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Data Definition Language (DDL)](#data-definition-language-ddl)
  - [Data Manipulation Language (DML)](#data-manipulation-language-dml)
  - [Data Control Language (DCL)](#data-control-language-dcl)
  - [Transaction Control Language (TCL)](#transaction-control-language-tcl)
  - [Database Interfaces](#database-interfaces)
- [Examples](#examples)
  - [Example 1: Creating a Complete Database Schema](#example-1-creating-a-complete-database-schema)
  - [Example 2: Performing DML Operations with Transaction Control](#example-2-performing-dml-operations-with-transaction-control)
  - [Example 3: Implementing Security with DCL](#example-3-implementing-security-with-dcl)
- [Exam Tips](#exam-tips)

## Introduction

Database Management Systems (DBMS) serve as the backbone of modern data-driven applications, enabling efficient storage, retrieval, and manipulation of data. A crucial component of any DBMS is its database language, which provides the interface through which users and applications interact with the database. Understanding database languages and interfaces is fundamental for computer science students, as these concepts form the foundation for effective database design and development.

Database languages can be categorized into several types based on their functionality: Data Definition Language (DDL) for defining database structure, Data Manipulation Language (DML) for manipulating data, Data Control Language (DCL) for controlling access, and Transaction Control Language (TCL) for managing transactions. Each serves a distinct purpose in database operations. Additionally, various interfaces including command-line interfaces, graphical user interfaces, and application programming interfaces provide different ways to interact with the database system. This topic is particularly important for the university's BCS403 syllabus as it establishes the groundwork for understanding how databases operate in real-world scenarios.

## Key Concepts

### Data Definition Language (DDL)

Data Definition Language is a subset of SQL (Structured Query Language) used to define and manage database objects such as tables, indexes, views, and schemas. DDL commands are auto-committed, meaning changes are automatically saved to the database. The primary DDL commands include:

**CREATE**: This command is used to create new database objects. The most common usage is creating tables to store data. When creating a table, you must define the table name, column names, data types, and constraints.

```sql
CREATE TABLE Student (
 Student_ID INT PRIMARY KEY,
 Name VARCHAR(50) NOT NULL,
 Age INT,
 Department VARCHAR(30),
 CGPA DECIMAL(3,2)
);
```

**ALTER**: This command modifies existing database objects. You can add, modify, or delete columns from a table, as well as add or drop constraints.

```sql
-- Add a new column
ALTER TABLE Student ADD Email VARCHAR(100);

-- Modify column data type
ALTER TABLE Student MODIFY Age SMALLINT;

-- Drop a column
ALTER TABLE Student DROP COLUMN Email;
```

**DROP**: This command deletes database objects permanently. When you drop a table, all data within it is lost permanently.

```sql
DROP TABLE Student;
DROP DATABASE CollegeDB;
```

**TRUNCATE**: This command removes all rows from a table quickly but preserves the table structure for future use.

```sql
TRUNCATE TABLE Student;
```

**RENAME**: This command is used to rename database objects.

```sql
RENAME TABLE Student TO Undergraduate;
```

### Data Manipulation Language (DML)

Data Manipulation Language commands are used to manipulate data within existing database objects. Unlike DDL, DML operations require explicit commit or rollback to save changes. The four primary DML commands are:

**SELECT**: This is the most frequently used command in SQL, used to retrieve data from one or more tables. It forms the foundation of query operations.

```sql
-- Simple select
SELECT * FROM Student;

-- Select specific columns
SELECT Name, Department, CGPA FROM Student WHERE CGPA > 8.0;

-- Complex query with join
SELECT s.Name, d.Dept_Name
FROM Student s
JOIN Department d ON s.Dept_ID = d.Dept_ID
WHERE s.CGPA >= 8.5;
```

**INSERT**: This command adds new rows of data into a table.

```sql
-- Insert single row
INSERT INTO Student (Student_ID, Name, Age, Department, CGPA)
VALUES (101, 'Raj Kumar', 20, 'Computer Science', 8.7);

-- Insert multiple rows
INSERT INTO Student (Student_ID, Name, Age, Department, CGPA)
VALUES
(102, 'Priya Sharma', 21, 'Information Science', 8.9),
(103, 'Amit Patel', 20, 'Computer Science', 7.8);
```

**UPDATE**: This command modifies existing data in a table.

```sql
UPDATE Student
SET CGPA = 9.1
WHERE Student_ID = 101;

UPDATE Student
SET Department = 'Artificial Intelligence'
WHERE CGPA > 9.0;
```

**DELETE**: This command removes specific rows from a table based on conditions.

```sql
DELETE FROM Student WHERE Student_ID = 103;
DELETE FROM Student WHERE CGPA < 5.0;
```

### Data Control Language (DCL)

Data Control Language deals with security permissions and access control in databases. It ensures that only authorized users can access or modify database data.

**GRANT**: This command provides specific privileges to database users.

```sql
-- Grant select permission
GRANT SELECT ON Student TO user1;

-- Grant multiple privileges
GRANT SELECT, INSERT, UPDATE ON Student TO user2;

-- Grant with grant option
GRANT ALL ON Student TO user3 WITH GRANT OPTION;
```

**REVOKE**: This command removes previously granted privileges from users.

```sql
REVOKE INSERT ON Student FROM user2;
REVOKE ALL ON Student FROM user3;
```

### Transaction Control Language (TCL)

Transaction Control Language manages transactions in the database to ensure data integrity. A transaction is a logical unit of work that must be completed entirely or not at all.

**COMMIT**: This command saves all pending transactions permanently to the database.

```sql
INSERT INTO Student VALUES (104, 'Vikram', 22, 'CSE', 8.5);
COMMIT;
```

**ROLLBACK**: This command undoes all uncommitted changes, restoring the database to its previous state.

```sql
DELETE FROM Student WHERE Student_ID = 104;
ROLLBACK;
```

**SAVEPOINT**: This command creates checkpoint markers within transactions, allowing partial rollback to specific points.

```sql
SAVEPOINT sp1;
INSERT INTO Student VALUES (105, 'Ananya', 20, 'ISE', 8.2);
SAVEPOINT sp2;
ROLLBACK TO sp1; -- Undoes changes after sp1
```

**SET TRANSACTION**: This command sets transaction properties like isolation level.

```sql
SET TRANSACTION READ ONLY;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### Database Interfaces

Database interfaces provide various methods for users and applications to interact with the database system.

**Command-Line Interface (CLI)**: Tools like SQL\*Plus (Oracle), mysql command-line client, and psql (PostgreSQL) allow users to type SQL commands directly. This is preferred by database administrators and developers for direct database manipulation.

**Graphical User Interface (GUI)**: Tools like Oracle Enterprise Manager, MySQL Workbench, SQL Server Management Studio, and phpMyAdmin provide visual interfaces for database operations. These are user-friendly and ideal for beginners.

**Application Programming Interface (API)**: Programming languages provide APIs to interact with databases. Database APIs include ODBC (Open Database Connectivity), JDBC (Java Database Connectivity), and ADO.NET. These enable application programs to connect to databases programmatically.

**Web-Based Interfaces**: Modern databases provide web consoles for administration and query execution. Examples include phpMyAdmin for MySQL and Oracle Cloud Console.

## Examples

### Example 1: Creating a Complete Database Schema

Consider a college database scenario where we need to create tables for students, courses, and enrollments.

**Step 1: Create Tables using DDL**

```sql
-- Create Department table
CREATE TABLE Department (
 Dept_ID INT PRIMARY KEY,
 Dept_Name VARCHAR(50) NOT NULL,
 HOD VARCHAR(50)
);

-- Create Student table with constraints
CREATE TABLE Student (
 Student_ID INT PRIMARY KEY,
 Name VARCHAR(50) NOT NULL,
 Email VARCHAR(100) UNIQUE,
 Phone VARCHAR(15),
 Dept_ID INT,
 Admission_Year INT,
 FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);

-- Create Course table
CREATE TABLE Course (
 Course_ID VARCHAR(10) PRIMARY KEY,
 Course_Name VARCHAR(50) NOT NULL,
 Credits INT CHECK (Credits BETWEEN 1 AND 6),
 Dept_ID INT,
 FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);

-- Create Enrollment table
CREATE TABLE Enrollment (
 Enroll_ID INT PRIMARY KEY,
 Student_ID INT,
 Course_ID VARCHAR(10),
 Grade CHAR(1),
 Semester INT,
 FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
 FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);
```

### Example 2: Performing DML Operations with Transaction Control

```sql
-- Start transaction
BEGIN TRANSACTION;

-- Insert department data
INSERT INTO Department VALUES (1, 'Computer Science', 'Dr. Smith');

-- Insert student data
INSERT INTO Student VALUES (1001, 'John Doe', 'john@college.edu', '1234567890', 1, 2022);

-- Insert course data
INSERT INTO Course VALUES ('CS101', 'Data Structures', 4, 1);

-- Insert enrollment
INSERT INTO Enrollment VALUES (5001, 1001, 'CS101', 'A', 1);

-- Check data
SELECT * FROM Enrollment;

-- Commit the transaction
COMMIT;
-- If error occurs, use ROLLBACK instead
```

### Example 3: Implementing Security with DCL

```sql
-- Create a new user for an application
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'password123';

-- Grant appropriate privileges
GRANT SELECT, INSERT, UPDATE ON CollegeDB.Student TO 'app_user'@'localhost';
GRANT SELECT ON CollegeDB.Course TO 'app_user'@'localhost';

-- Create admin user with more privileges
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON CollegeDB.* TO 'admin'@'localhost' WITH GRANT OPTION;

-- Verify privileges
SHOW GRANTS FOR 'app_user'@'localhost';

-- Revoke privileges if needed
REVOKE UPDATE ON CollegeDB.Student FROM 'app_user'@'localhost';
```

## Exam Tips

1. **Understand the Difference Between DDL and DML**: Remember that DDL commands (CREATE, ALTER, DROP, TRUNCATE, RENAME) are auto-committed, while DML commands (SELECT, INSERT, UPDATE, DELETE) require explicit COMMIT or ROLLBACK operations.

2. **Know the Order of SQL Execution**: In SELECT queries, the logical order is: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. This is frequently tested in university exams.

3. **Constraints Are Important**: Remember primary key (unique + not null), foreign key (references), unique (unique values), check (condition), and default (default value) constraints.

4. **TCL Requires Transaction Awareness**: Understand how COMMIT saves changes permanently while ROLLBACK undoes uncommitted changes. SAVEPOINT allows partial rollbacks within a transaction.

5. **DCL for Security**: Grant and Revoke are essential for database security. Remember that privileges can be granted at table level or database level.

6. **Practice SQL Queries**: Most exam questions require writing SQL queries. Practice SELECT with WHERE, JOINs, aggregate functions, and subqueries.

7. **Difference Between DROP, DELETE, and TRUNCATE**: DROP removes table structure permanently, DELETE removes rows conditionally with transaction support, TRUNCATE removes all rows but keeps structure.
