# Insert, Delete, and Update Statements in SQL

## Introduction

Structured Query Language (SQL) is the standard language for managing relational databases. After creating database tables using Data Definition Language (DDL) commands, the next fundamental operation is manipulating the data stored within those tables. This module covers the three primary Data Manipulation Language (DML) statements: INSERT, DELETE, and UPDATE. These statements form the backbone of any database-driven application, enabling users to add new records, modify existing data, and remove unwanted information.

In real-world scenarios, databases are rarely static. E-commerce platforms continuously add new products, social media applications insert new user posts, banking systems update account balances, and outdated records are periodically removed. Understanding how to properly implement these manipulation statements is essential for any database professional or software developer. This topic becomes particularly important for university examinations, where practical SQL queries and theoretical understanding of DML commands are frequently tested.

This comprehensive guide explores the syntax, variations, and best practices for INSERT, DELETE, and UPDATE statements in SQL, with particular emphasis on exam-relevant concepts and real-world applications.

## Key Concepts

### 1. INSERT Statement

The INSERT statement adds new rows of data into a table. SQL provides two primary variations for inserting data.

**Syntax for Single Row Insert:**

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**Syntax for Multiple Row Insert:**

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES
 (value1, value2, value3, ...),
 (value1, value2, value3, ...),
 (value1, value2, value3, ...);
```

**Key Points About INSERT:**

- Column list is optional if values are provided for all columns in the order they were defined
- String and date values must be enclosed in single quotes
- Numeric values can be written without quotes
- NULL values can be inserted using the NULL keyword (without quotes)
- DEFAULT keyword can be used to insert default values defined during table creation
- Numeric expressions can be used as values

**Inserting Data from Another Table:**

```sql
INSERT INTO target_table (column1, column2)
SELECT column1, column2
FROM source_table
WHERE condition;
```

This variation is particularly useful for data migration, archiving, and creating backup tables.

### 2. DELETE Statement

The DELETE statement removes one or more rows from a table based on specified conditions.

**Syntax:**

```sql
DELETE FROM table_name
WHERE condition;
```

**Critical Considerations:**

- The WHERE clause is crucial to avoid accidentally deleting all rows
- Without a WHERE clause, all rows from the table are deleted
- DELETE removes rows one by one and can be rolled back within a transaction
- TRUNCATE is faster but cannot be rolled back in many database systems
- The number of rows affected can be checked using SQL%ROWCOUNT in PL/SQL

**DELETE vs TRUNCATE:**

- DELETE is DML (can be rolled back), TRUNCATE is DDL
- DELETE fires triggers, TRUNCATE does not
- TRUNCATE deallocates space, DELETE does not
- DELETE can have WHERE clause, TRUNCATE cannot

### 3. UPDATE Statement

The UPDATE statement modifies existing values in one or more rows of a table.

**Syntax:**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

**Advanced UPDATE Features:**

- Multiple columns can be updated in a single statement
- Expressions can be used in SET clause (arithmetic operations, string concatenation)
- UPDATE can use subqueries to derive values from other tables
- CASE expressions can be used for conditional updates

**UPDATE with CASE Expression:**

```sql
UPDATE employees
SET salary = CASE
 WHEN dept_id = 1 THEN salary * 1.10
 WHEN dept_id = 2 THEN salary * 1.15
 ELSE salary * 1.05
END;
```

### 4. Transaction Control

SQL operations can be grouped into transactions for atomicity:

```sql
BEGIN TRANSACTION;

INSERT INTO accounts (id, balance) VALUES (101, 5000);
UPDATE accounts SET balance = balance - 1000 WHERE id = 101;
UPDATE accounts SET balance = balance + 1000 WHERE id = 102;

COMMIT; -- Makes changes permanent
-- ROLLBACK; -- Undoes all changes if something goes wrong
```

## Examples

### Example 1: Insert Statement with Multiple Variations

Consider a student database with the following table:

```sql
CREATE TABLE students (
 student_id INT PRIMARY KEY,
 student_name VARCHAR(50) NOT NULL,
 email VARCHAR(50) UNIQUE,
 age INT DEFAULT 20,
 join_date DATE DEFAULT CURRENT_DATE,
 cgpa DECIMAL(3,2)
);
```

**Inserting a single row with all values:**

```sql
INSERT INTO students (student_id, student_name, email, age, join_date, cgpa)
VALUES (1, 'John Smith', 'john@example.com', 21, '2023-01-15', 8.5);
```

**Inserting using DEFAULT keyword:**

```sql
INSERT INTO students (student_id, student_name, email)
VALUES (2, 'Alice Johnson', 'alice@example.com');
```

_Result: age becomes 20 (default), join_date becomes current date (default)_

**Inserting NULL value:**

```sql
INSERT INTO students (student_id, student_name, email, cgpa)
VALUES (3, 'Bob Williams', 'bob@example.com', NULL);
```

**Inserting multiple rows at once:**

```sql
INSERT INTO students (student_id, student_name, email, age, cgpa)
VALUES
 (4, 'Carol Davis', 'carol@example.com', 22, 7.8),
 (5, 'David Brown', 'david@example.com', 20, 9.1),
 (6, 'Eve Wilson', 'eve@example.com', 23, 8.2);
```

### Example 2: Update Statement with Calculations

Given an employee table:

```sql
CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(50),
 salary DECIMAL(10,2),
 bonus DECIMAL(10,2),
 dept_id INT
);

-- Insert sample data
INSERT INTO employees VALUES
(101, 'Ravi Kumar', 50000, 5000, 1),
(102, 'Priya Sharma', 60000, 6000, 2),
(103, 'Amit Patel', 55000, 5500, 1),
(104, 'Sneha Reddy', 65000, 6500, 3);
```

**Update salary with 10% increase for dept_id = 1:**

```sql
UPDATE employees
SET salary = salary * 1.10
WHERE dept_id = 1;
```

_Result: Ravi's salary becomes 55000, Amit's salary becomes 60500_

**Update multiple columns:**

```sql
UPDATE employees
SET salary = salary + 5000,
 bonus = bonus + 1000
WHERE emp_id = 102;
```

_Result: Priya's salary becomes 65000, bonus becomes 7000_

**Update using subquery:**

```sql
UPDATE employees
SET salary = (SELECT AVG(salary) FROM employees)
WHERE emp_id = 104;
```

### Example 3: Delete Statement with Conditions

```sql
-- Delete employees from dept_id = 3
DELETE FROM employees
WHERE dept_id = 3;
```

**Delete with multiple conditions:**

```sql
DELETE FROM employees
WHERE salary < 50000 AND dept_id = 1;
```

**Delete all rows (use with caution):**

```sql
DELETE FROM employees;
-- All records deleted but structure remains
```

### Example 4: Transaction Control Example

```sql
-- Start a transaction for fund transfer
BEGIN TRANSACTION;

-- Deduct from account 101
UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 101;

-- Add to account 102
UPDATE accounts
SET balance = balance + 5000
WHERE account_id = 102;

-- Check balance (if insufficient funds, rollback)
DECLARE @balance DECIMAL(10,2);
SELECT @balance = balance FROM accounts WHERE account_id = 101;

IF @balance < 0
 ROLLBACK;
ELSE
 COMMIT;
```

## Exam Tips

1. **Remember the ORDER**: INSERT comes before UPDATE, and UPDATE comes before DELETE in terms of common usage patterns - this helps in remembering syntax sequence.

2. **WHERE Clause Importance**: For UPDATE and DELETE, always emphasize the WHERE clause in answers - omitting it affects all rows, which is rarely the intended operation.

3. **INSERT without column list**: When inserting without specifying columns, values must match the exact column order in table definition - mention this as a caution in exams.

4. **DEFAULT and NULL**: Know the difference between DEFAULT (uses table's default value) and NULL (explicitly inserts null) - this is a common exam question.

5. **Transaction Control**: COMMIT makes changes permanent, ROLLBACK undoes them - understand when each is used in database operations.

6. **Multiple Row INSERT**: Most modern databases support inserting multiple rows in a single INSERT statement, which improves performance.

7. **Data Types**: Remember to use single quotes for strings and dates, while numeric values don't require quotes - this is essential for writing correct SQL.

8. **Subqueries in UPDATE**: UPDATE statements can use subqueries in both SET and WHERE clauses - this advanced feature is often tested in university exams.

9. **Difference between DELETE and TRUNCATE**: DELETE is DML (can rollback), TRUNCATE is DDL (cannot rollback in most systems), and TRUNCATE is faster for deleting all rows.

10. **RETURNING Clause**: Some databases support RETURNING clause with INSERT/UPDATE/DELETE to get the affected rows - be aware of this feature for practical applications.
