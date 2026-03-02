# SQL Data Definition and Data Types

## Table of Contents

- [SQL Data Definition and Data Types](#sql-data-definition-and-data-types)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [SQL Data Types](#sql-data-types)
  - [CREATE Statement](#create-statement)
  - [ALTER Statement](#alter-statement)
  - [DROP Statement](#drop-statement)
  - [Constraints in SQL](#constraints-in-sql)
- [Examples](#examples)
  - [Example 1: Creating a Complete Employee Database Table](#example-1-creating-a-complete-employee-database-table)
  - [Example 2: Modifying Table Structure](#example-2-modifying-table-structure)
  - [Example 3: Creating Related Tables with Foreign Keys](#example-3-creating-related-tables-with-foreign-keys)
- [Exam Tips](#exam-tips)

## Introduction

Structured Query Language (SQL) is the standard language for managing relational databases. Data Definition Language (DDL) is a subset of SQL used to define and manage database structures, including tables, indexes, and constraints. Understanding DDL commands and SQL data types is fundamental for any database professional, as these form the foundation upon which data storage and manipulation rest.

The Data Definition component of SQL allows database administrators and developers to create, modify, and delete database objects in a systematic manner. Without proper data definition, even the most sophisticated queries cannot retrieve meaningful information. In the context of the the syllabus for BCS403-Database Management System, this module serves as a prerequisite for understanding subsequent topics like query processing and transaction management.

This module covers essential DDL commands including CREATE, ALTER, and DROP, along with the comprehensive study of SQL data types. Mastery of these concepts enables students to design robust database schemas that ensure data integrity, optimize storage, and support efficient query execution.

## Key Concepts

### SQL Data Types

SQL data types determine the type of data that can be stored in each column of a table. Choosing appropriate data types is crucial for data integrity, storage efficiency, and query performance.

**Numeric Data Types:**

- **INTEGER/INT**: Stores whole numbers ranging from -2,147,483,648 to 2,147,483,647 (4 bytes). Used for primary keys, counters, and quantities.
- **SMALLINT**: Stores integers from -32,768 to 32,767 (2 bytes). Suitable for smaller numeric values.
- **BIGINT**: Stores large integers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (8 bytes). Used for very large counting needs.
- **DECIMAL(p,s) or NUMERIC(p,s)**: Exact numeric type with precision p (total digits) and scale s (digits after decimal). For example, DECIMAL(5,2) can store values like 123.45.
- **FLOAT(n)**: Approximate numeric with n bits of precision. Used for scientific calculations where exact precision is not critical.
- **REAL**: Single-precision floating-point (approximately 7 digits).
- **DOUBLE PRECISION**: Double-precision floating-point (approximately 15 digits).

**Character/String Data Types:**

- **CHAR(n)**: Fixed-length character string of length n. Pads with spaces if data is shorter. Maximum 255 bytes.
- **VARCHAR(n)**: Variable-length string with maximum n characters. More storage-efficient than CHAR.
- **TEXT**: Variable-length character string for large text data (up to 65,535 bytes in MySQL, similar in other databases).
- **NVARCHAR**: Unicode variable-length string supporting multilingual characters.

**Date and Time Data Types:**

- **DATE**: Stores date in YYYY-MM-DD format (3 bytes).
- **TIME**: Stores time in HH:MM:SS format.
- **DATETIME/TIMESTAMP**: Stores both date and time (YYYY-MM-DD HH:MM:SS).
- **YEAR**: Stores year values (1 byte).

**Other Data Types:**

- **BOOLEAN/BOOL**: Stores TRUE or FALSE values.
- **BLOB/BINARY**: Stores binary data like images, audio, or video files.
- **NULL**: Represents missing or unknown values. Important: NULL is not zero or empty string.

### CREATE Statement

The CREATE statement is used to create database objects like tables, indexes, views, and databases.

**Creating a Database:**

```sql
CREATE DATABASE university_db;
USE university_db;
```

**Creating a Table:**

```sql
CREATE TABLE students (
 student_id INT PRIMARY KEY,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(50) NOT NULL,
 email VARCHAR(100) UNIQUE,
 date_of_birth DATE,
 cgpa DECIMAL(3,2),
 enrollment_year INT
);
```

**Key Components in CREATE TABLE:**

- **PRIMARY KEY**: Uniquely identifies each row
- **NOT NULL**: Column must contain a value
- **UNIQUE**: No duplicate values allowed
- **DEFAULT**: Provides default value if none specified
- **CHECK**: Validates values against a condition

### ALTER Statement

The ALTER statement modifies existing database objects.

**Adding a Column:**

```sql
ALTER TABLE students ADD phone_number VARCHAR(15);
```

**Modifying a Column:**

```sql
ALTER TABLE students MODIFY COLUMN cgpa DECIMAL(4,2);
```

**Dropping a Column:**

```sql
ALTER TABLE students DROP COLUMN phone_number;
```

**Adding Constraints:**

```sql
ALTER TABLE students ADD CONSTRAINT chk_cgpa CHECK (cgpa >= 0 AND cgpa <= 10);
```

### DROP Statement

The DROP statement permanently removes database objects.

**Dropping a Table:**

```sql
DROP TABLE students;
```

**Dropping a Database:**

```sql
DROP DATABASE university_db;
```

**Truncating a Table:**

```sql
TRUNCATE TABLE students; -- Removes all rows, keeps structure
```

### Constraints in SQL

Constraints enforce rules at the table level:

1. **PRIMARY KEY Constraint**: Combination of NOT NULL and UNIQUE. Only one per table.
2. **FOREIGN KEY Constraint**: Maintains referential integrity between tables.
3. **UNIQUE Constraint**: Ensures all values in a column are different.
4. **NOT NULL Constraint**: Prevents NULL values.
5. **CHECK Constraint**: Limits values based on condition.
6. **DEFAULT Constraint**: Provides default value.

**Example with Multiple Constraints:**

```sql
CREATE TABLE enrollments (
 enrollment_id INT PRIMARY KEY,
 student_id INT NOT NULL,
 course_code VARCHAR(10) NOT NULL,
 enrollment_date DATE DEFAULT CURRENT_DATE,
 grade CHAR(2),
 FOREIGN KEY (student_id) REFERENCES students(student_id),
 CHECK (grade IN ('A', 'B', 'C', 'D', 'E', 'F'))
);
```

## Examples

### Example 1: Creating a Complete Employee Database Table

**Problem:** Create a table 'employees' with the following requirements:

- Employee ID (primary key, integer)
- First name (required, max 30 characters)
- Last name (required, max 30 characters)
- Email (unique, max 50 characters)
- Phone number (optional, max 15 characters)
- Hire date (required)
- Salary (positive decimal with 2 decimal places)
- Department ID (integer foreign key)

**Solution:**

```sql
CREATE TABLE employees (
 employee_id INT PRIMARY KEY,
 first_name VARCHAR(30) NOT NULL,
 last_name VARCHAR(30) NOT NULL,
 email VARCHAR(50) UNIQUE,
 phone VARCHAR(15),
 hire_date DATE NOT NULL,
 salary DECIMAL(10,2) CHECK (salary > 0),
 department_id INT
);
```

**Explanation:**

- DECIMAL(10,2) allows salary up to 99999999.99
- CHECK constraint ensures salary is always positive
- UNIQUE on email prevents duplicate email addresses

### Example 2: Modifying Table Structure

**Problem:** Given the employees table, perform the following modifications:

1. Add a new column 'manager_id'
2. Change salary column to allow larger values
3. Add a constraint that hire_date cannot be in the future

**Solution:**

```sql
-- Step 1: Add manager_id column
ALTER TABLE employees ADD manager_id INT;

-- Step 2: Modify salary column
ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12,2);

-- Step 3: Add check constraint for hire_date
ALTER TABLE employees
ADD CONSTRAINT chk_hire_date CHECK (hire_date <= CURRENT_DATE);
```

### Example 3: Creating Related Tables with Foreign Keys

**Problem:** Create a department table and modify employees table to include foreign key reference to departments.

**Solution:**

```sql
-- Create departments table first
CREATE TABLE departments (
 department_id INT PRIMARY KEY,
 department_name VARCHAR(50) NOT NULL,
 location VARCHAR(50)
);

-- Now add foreign key to employees
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id);
```

**Explanation:** The foreign key constraint ensures that every department_id in employees table must either be NULL or exist in the departments table, maintaining referential integrity.

## Exam Tips

1. **Difference between CHAR and VARCHAR**: Remember CHAR is fixed-length (pads with spaces), VARCHAR is variable-length. VARCHAR is more storage-efficient.

2. **NULL vs Empty String**: NULL represents absence of value, while empty string is a value. NULL ≠ NULL (requires IS NULL or IS NOT NULL).

3. **PRIMARY KEY vs UNIQUE**: PRIMARY KEY allows only one per table and cannot be NULL. UNIQUE can have multiple columns and can have NULL (depending on database).

4. **DROP vs TRUNCATE vs DELETE**: DROP removes table structure completely. TRUNCATE removes all data but keeps structure. DELETE removes rows conditionally with WHERE clause.

5. **Data Type Selection**: Choose INT for identifiers, DECIMAL for monetary values, VARCHAR for variable text, DATE for dates. Avoid using TEXT for small strings.

6. **CASCADE and RESTRICT**: When dropping tables with foreign keys, use ON DELETE CASCADE to automatically remove child records, or ON DELETE RESTRICT to prevent deletion.

7. **Constraint Order**: When creating tables with multiple constraints, define constraints after all columns are specified.

8. **Database Object Naming**: Use meaningful names. Follow conventions like tbl*students or students_table for tables, pk* for primary keys, fk\_ for foreign keys.

9. **FOREIGN KEY Requirements**: The foreign key column data type must match the referenced primary key column data type.

10. **DEFAULT Values**: DEFAULT can use system functions like CURRENT_DATE, CURRENT_TIMESTAMP, or USER.
