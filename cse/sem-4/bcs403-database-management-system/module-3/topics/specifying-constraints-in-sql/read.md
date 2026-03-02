# Specifying Constraints in SQL

## Table of Contents

- [Specifying Constraints in SQL](#specifying-constraints-in-sql)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What Are Database Constraints?](#what-are-database-constraints)
  - [Types of SQL Constraints](#types-of-sql-constraints)
  - [Adding Constraints to Existing Tables](#adding-constraints-to-existing-tables)
- [Examples](#examples)
  - [Example 1: Creating a Student Information System Database](#example-1-creating-a-student-information-system-database)
  - [Example 2: Creating an Online Shopping Order System](#example-2-creating-an-online-shopping-order-system)
  - [Example 3: Modifying Constraints on Existing Tables](#example-3-modifying-constraints-on-existing-tables)
- [Exam Tips](#exam-tips)

## Introduction

Database Management Systems (DBMS) form the backbone of modern data-driven applications, and ensuring data integrity is paramount for any reliable database design. When creating and managing databases, one of the most critical aspects is defining rules that restrict what data can be inserted, updated, or deleted from tables. These rules are implemented through **constraints** in Structured Query Language (SQL).

Constraints are database objects that enforce data integrity by defining conditions that must be satisfied by the data in a database. They prevent invalid or inconsistent data from entering the database, thereby maintaining the accuracy and reliability of the stored information. Without proper constraints, databases would become susceptible to duplicate records, orphaned data, and various forms of data corruption that could lead to serious application failures.

In the context of the university's BCS403 Database Management System syllabus, understanding how to specify constraints in SQL is essential for designing robust database schemas. This topic covers the various types of constraints available in SQL, their syntax, and practical implementation strategies. Whether you are creating a simple student database or a complex enterprise resource planning system, proper constraint specification ensures that your data remains consistent and meaningful throughout the application's lifecycle.

## Key Concepts

### What Are Database Constraints?

Constraints are declarative statements that specify rules about the values that can be assigned to a column in a table. They are enforced by the database management system automatically and ensure that data modifications comply with defined business rules. Constraints can be defined at the column level (applying to a single column) or at the table level (applying to multiple columns or the entire table).

When a constraint is violated due to an INSERT, UPDATE, or DELETE operation, the database system rejects the operation and returns an error message. This automatic enforcement eliminates the need for manual validation in application code, making data integrity more reliable and maintainable.

### Types of SQL Constraints

#### 1. NOT NULL Constraint

The NOT NULL constraint ensures that a column cannot contain NULL values. By default, SQL columns can accept NULL values unless explicitly restricted. This constraint is particularly important for fields that are mandatory for business operations, such as customer email addresses, employee identification numbers, or product prices.

```sql
-- Column-level NOT NULL constraint
CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL,
 salary DECIMAL(10, 2)
);
```

#### 2. UNIQUE Constraint

The UNIQUE constraint ensures that all values in a column or a group of columns are different from each other. Unlike PRIMARY KEY, a table can have multiple UNIQUE constraints. The UNIQUE constraint allows NULL values (in most database systems, only one NULL is permitted in a unique column, though this varies by DBMS).

```sql
-- Table-level UNIQUE constraint
CREATE TABLE products (
 product_id INT PRIMARY KEY,
 product_name VARCHAR(100),
 product_code VARCHAR(50),
 price DECIMAL(10, 2),
 UNIQUE (product_code)
);

-- Multiple columns as unique (composite unique key)
CREATE TABLE student_enrollments (
 student_id INT,
 course_id INT,
 enrollment_date DATE,
 UNIQUE (student_id, course_id)
);
```

#### 3. PRIMARY KEY Constraint

The PRIMARY KEY constraint uniquely identifies each row in a table. A primary key column must contain unique values and cannot contain NULLs. Each table should have exactly one primary key, which can consist of one or multiple columns (composite primary key). Primary keys are automatically indexed by most database systems for efficient data retrieval.

```sql
-- Single column primary key
CREATE TABLE customers (
 customer_id INT PRIMARY KEY,
 customer_name VARCHAR(100),
 contact_number VARCHAR(20)
);

-- Composite primary key
CREATE TABLE order_items (
 order_id INT,
 item_id INT,
 quantity INT,
 PRIMARY KEY (order_id, item_id)
);
```

#### 4. FOREIGN KEY Constraint

The FOREIGN KEY constraint establishes a relationship between two tables. A foreign key in a child table references the primary key or a unique key in the parent table. This constraint ensures referential integrity—meaning that values in the foreign key column must either match a value in the referenced table or be NULL (if the column allows NULLs).

```sql
-- Creating parent and child tables
CREATE TABLE departments (
 dept_id INT PRIMARY KEY,
 dept_name VARCHAR(100)
);

CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(100),
 dept_id INT,
 FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

The FOREIGN KEY constraint supports several actions when referenced data is modified:

- **ON DELETE CASCADE**: Automatically deletes rows from the child table when the parent row is deleted
- **ON DELETE SET NULL**: Sets the foreign key column to NULL when the parent row is deleted
- **ON UPDATE CASCADE**: Updates foreign key values when the parent key is updated

```sql
CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(100),
 dept_id INT,
 FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
 ON DELETE CASCADE
 ON UPDATE CASCADE
);
```

#### 5. CHECK Constraint

The CHECK constraint allows you to specify a condition that must be true for each row in the table. The condition can use logical operators and compare values against constants, column values, or expressions. This constraint is invaluable for enforcing business rules directly at the database level.

```sql
CREATE TABLE products (
 product_id INT PRIMARY KEY,
 product_name VARCHAR(100),
 price DECIMAL(10, 2) CHECK (price > 0),
 quantity INT CHECK (quantity >= 0),
 discount_rate DECIMAL(5, 2) CHECK (discount_rate BETWEEN 0 AND 100)
);

-- Table-level CHECK constraint
CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(100),
 hire_date DATE,
 salary DECIMAL(10, 2),
 CHECK (hire_date <= CURRENT_DATE)
);
```

#### 6. DEFAULT Constraint

The DEFAULT constraint provides a default value for a column when no value is explicitly specified during an INSERT operation. This is useful for fields that have a common default value, such as order status, subscription type, or country code.

```sql
CREATE TABLE orders (
 order_id INT PRIMARY KEY,
 order_date DATE DEFAULT CURRENT_DATE,
 status VARCHAR(20) DEFAULT 'Pending',
 shipping_address VARCHAR(200)
);
```

### Adding Constraints to Existing Tables

Constraints can also be added to existing tables using the ALTER TABLE statement:

```sql
-- Add NOT NULL to existing column (requires column to not null)
ALTER TABLE employees MODIFY salary DECIMAL(10, 2) NOT NULL;

-- Add CHECK constraint
ALTER TABLE products ADD CONSTRAINT chk_price CHECK (price > 0);

-- Add FOREIGN KEY constraint
ALTER TABLE employees ADD CONSTRAINT fk_dept
FOREIGN KEY (dept_id) REFERENCES departments(dept_id);

-- Drop a constraint
ALTER TABLE products DROP CONSTRAINT chk_price;
```

## Examples

### Example 1: Creating a Student Information System Database

Consider a scenario where we need to create a database for a college student information system with the following requirements:

- Each student has a unique student ID
- Student name and email are mandatory
- Email must be unique across all students
- Phone number is optional but must be unique if provided
- Age must be at least 17
- Department ID must reference an existing department

```sql
-- Create departments table (parent table)
CREATE TABLE departments (
 dept_id INT PRIMARY KEY,
 dept_name VARCHAR(50) NOT NULL,
 hod_name VARCHAR(100)
);

-- Create students table (child table)
CREATE TABLE students (
 student_id INT PRIMARY KEY,
 student_name VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL UNIQUE,
 phone VARCHAR(20) UNIQUE,
 age INT CHECK (age >= 17),
 dept_id INT NOT NULL,
 FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert sample data
INSERT INTO departments VALUES (1, 'Computer Science', 'Dr. Smith');
INSERT INTO departments VALUES (2, 'Information Science', 'Dr. Johnson');

-- This will succeed
INSERT INTO students VALUES (101, 'John Doe', 'john@example.com', '9876543210', 19, 1);

-- This will FAIL (duplicate email)
INSERT INTO students VALUES (102, 'Jane Smith', 'john@example.com', '9876543211', 20, 1);
-- Error: Duplicate key 'john@example.com'

-- This will FAIL (age < 17)
INSERT INTO students VALUES (103, 'Baby Doe', 'baby@example.com', '9876543212', 15, 1);
-- Error: CHECK constraint violation

-- This will FAIL (invalid department)
INSERT INTO students VALUES (104, 'Mike Brown', 'mike@example.com', '9876543213', 21, 99);
-- Error: Foreign key constraint violation
```

### Example 2: Creating an Online Shopping Order System

Design an order management system with the following constraints:

- Orders must have positive amounts
- Order date cannot be in the future
- Quantity must be positive
- Payment status must be one of: 'Pending', 'Paid', 'Cancelled', 'Refunded'

```sql
CREATE TABLE orders (
 order_id INT PRIMARY KEY,
 customer_id INT NOT NULL,
 order_date DATE NOT NULL CHECK (order_date <= CURRENT_DATE),
 total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount > 0),
 payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('Pending', 'Paid', 'Cancelled', 'Refunded')),
 shipping_address VARCHAR(200)
);

CREATE TABLE order_items (
 order_id INT NOT NULL,
 item_id INT NOT NULL,
 product_name VARCHAR(100),
 quantity INT NOT NULL CHECK (quantity > 0),
 unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price > 0),
 PRIMARY KEY (order_id, item_id),
 FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Test constraints
INSERT INTO orders VALUES (1, 101, '2024-01-15', 2500.00, 'Pending', 'Bangalore');

-- This will FAIL (future date)
INSERT INTO orders VALUES (2, 101, '2025-01-15', 1500.00, 'Pending', 'Mysore');

-- This will FAIL (negative amount)
INSERT INTO orders VALUES (3, 101, '2024-01-15', -500.00, 'Paid', 'Delhi');

-- This will FAIL (invalid status)
INSERT INTO orders VALUES (4, 101, '2024-01-15', 3000.00, 'Complete', 'Chennai');
```

### Example 3: Modifying Constraints on Existing Tables

```sql
-- Create table without constraints first
CREATE TABLE employees (
 emp_id INT,
 emp_name VARCHAR(100),
 salary DECIMAL(10, 2),
 dept_id INT
);

-- Add PRIMARY KEY constraint
ALTER TABLE employees ADD CONSTRAINT pk_emp PRIMARY KEY (emp_id);

-- Add NOT NULL constraints
ALTER TABLE employees MODIFY emp_name VARCHAR(100) NOT NULL;
ALTER TABLE employees MODIFY salary DECIMAL(10, 2) NOT NULL;

-- Add CHECK constraint for salary range
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary >= 10000 AND salary <= 500000);

-- Add foreign key reference
CREATE TABLE departments (
 dept_id INT PRIMARY KEY,
 dept_name VARCHAR(50)
);

ALTER TABLE employees ADD CONSTRAINT fk_dept FOREIGN KEY (dept_id) REFERENCES departments(dept_id);

-- Verify constraints
SELECT * FROM user_constraints WHERE table_name = 'EMPLOYEES';
```

## Exam Tips

1. **Remember the difference between PRIMARY KEY and UNIQUE**: PRIMARY KEY cannot have NULL values and there can be only one per table, while UNIQUE allows one NULL value (in most DBMS) and there can be multiple per table.

2. **CHECK constraints can reference multiple columns**: Unlike other constraints, CHECK can validate conditions involving multiple columns in the same row, such as checking that end_date is after start_date.

3. **FOREIGN KEY actions matter**: Understand the difference between CASCADE, SET NULL, and RESTRICT actions for referential integrity enforcement.

4. **Constraint naming**: Always name your constraints explicitly using the CONSTRAINT keyword for better error messages and easier management.

5. **Order of table creation matters**: When using foreign keys, create the parent (referenced) table before the child (referencing) table to avoid constraint violations.

6. **DEFAULT vs NOT NULL**: Remember that DEFAULT provides a value when none is specified, while NOT NULL prohibits NULL values entirely—they serve different purposes.

7. **Composite keys**: Multiple columns can be combined to form a PRIMARY KEY or UNIQUE constraint, useful for scenarios like student enrollment where (student_id, course_id) must be unique.
