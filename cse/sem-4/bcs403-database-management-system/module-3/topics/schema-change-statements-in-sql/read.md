# Schema Change Statements in SQL

## Table of Contents

- [Schema Change Statements in SQL](#schema-change-statements-in-sql)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [ALTER TABLE Statement](#alter-table-statement)
  - [DROP Statement](#drop-statement)
  - [TRUNCATE Statement](#truncate-statement)
  - [Index Management](#index-management)
  - [View Management](#view-management)
  - [RENAME Statement](#rename-statement)
  - [COMMENT Statement](#comment-statement)
- [Examples](#examples)
  - [Example 1: Evolving a Customer Table](#example-1-evolving-a-customer-table)
  - [Example 2: Database Normalization](#example-2-database-normalization)
  - [Example 3: Complete Schema Restructuring](#example-3-complete-schema-restructuring)
- [Exam Tips](#exam-tips)

## Introduction

Schema change statements in SQL are Data Definition Language (DDL) commands that allow database administrators and developers to modify the structure of database objects after they have been initially created. In real-world database environments, requirements evolve over time, and the database schema must adapt accordingly without losing existing data. Schema change statements provide the mechanism to make structural modifications to tables, indexes, views, and other database objects efficiently and safely.

Understanding schema change statements is crucial for database professionals because schema modifications are common operations in software development lifecycles. Whether adding a new column to track customer phone numbers, removing an obsolete field, creating an index to improve query performance, or restructuring tables for better normalization, these DDL commands form the backbone of database evolution. In the context of the university's Database Management System curriculum, this topic demonstrates how SQL not only supports data manipulation but also provides robust tools for managing database structure dynamically.

## Key Concepts

### ALTER TABLE Statement

The ALTER TABLE statement is the most frequently used schema change command. It modifies an existing table structure without requiring the table to be recreated. The primary operations include adding new columns, modifying existing column definitions, dropping columns, and adding or removing constraints.

**Adding a Column:**

```sql
ALTER TABLE Employee
ADD COLUMN PhoneNumber VARCHAR(15);
```

When adding a column, the new column is appended to the end of the table. If a default value is specified, all existing rows receive that default value. Without a default, existing rows contain NULL values for the new column.

**Modifying Column Definition:**

```sql
ALTER TABLE Employee
MODIFY COLUMN Salary DECIMAL(12,2) NOT NULL;
```

Column modification capabilities vary among database systems. MySQL uses MODIFY, Oracle and PostgreSQL use MODIFY COLUMN, while SQL Server uses ALTER COLUMN. The modification can change data type, size, nullability, and default values.

**Dropping a Column:**

```sql
ALTER TABLE Employee
DROP COLUMN PhoneNumber;
```

Dropping a column permanently removes the column and all its data from the table. This operation cannot be undone unless you have a backup. Some database systems require you to drop related constraints before dropping the column.

**Adding Constraints:**

```sql
ALTER TABLE Employee
ADD CONSTRAINT PK_Employee PRIMARY KEY (EmployeeID);
```

### DROP Statement

The DROP statement completely removes database objects from the system.

**DROP TABLE:**

```sql
DROP TABLE Employee;
```

This command removes the table structure and all data permanently. The IF EXISTS clause prevents errors if the table doesn't exist:

```sql
DROP TABLE IF EXISTS Employee;
```

**DROP DATABASE:**

```sql
DROP DATABASE CompanyDB;
```

This removes the entire database and all its contents. This is a destructive operation that requires careful consideration.

### TRUNCATE Statement

TRUNCATE TABLE removes all rows from a table efficiently:

```sql
TRUNCATE TABLE Employee;
```

Unlike DELETE, TRUNCATE is a DDL operation that deallocates data pages rather than deleting rows individually, making it significantly faster for large tables. TRUNCATE resets identity columns and cannot be rolled back in some database systems without proper transaction handling.

### Index Management

**Creating Indexes:**

```sql
CREATE INDEX idx_Dept ON Employee(DepartmentID);
CREATE UNIQUE INDEX idx_Email ON Employee(Email);
```

**Dropping Indexes:**

```sql
DROP INDEX idx_Dept ON Employee;
```

Index syntax varies significantly across database systems. MySQL uses the table name in the DROP INDEX command, while PostgreSQL and Oracle require specifying the schema.

### View Management

**Creating Views:**

```sql
CREATE VIEW EmployeeDetails AS
SELECT EmployeeID, Name, DepartmentName, Salary
FROM Employee E
JOIN Department D ON E.DepartmentID = D.DepartmentID;
```

**Dropping Views:**

```sql
DROP VIEW EmployeeDetails;
```

### RENAME Statement

Renaming database objects:

```sql
ALTER TABLE Employee RENAME TO Staff;
RENAME TABLE Employee TO Staff;
```

The syntax varies by database system. MySQL uses RENAME TABLE, while Oracle uses ALTER TABLE with RENAME.

### COMMENT Statement

Adding documentation to database objects:

```sql
COMMENT ON TABLE Employee IS 'Contains staff information including salary and department';
COMMENT ON COLUMN Employee.Salary IS 'Annual salary in INR';
```

Comments are stored in the data dictionary and help other developers understand the purpose of tables and columns.

## Examples

### Example 1: Evolving a Customer Table

Consider a scenario where an e-commerce application initially tracks customers with basic information, then requirements expand to include loyalty program data.

**Initial Table:**

```sql
CREATE TABLE Customer (
 CustomerID INT PRIMARY KEY,
 Name VARCHAR(100),
 Email VARCHAR(100) UNIQUE
);
```

**Adding Loyalty Program Fields:**

```sql
ALTER TABLE Customer
ADD COLUMN LoyaltyPoints INT DEFAULT 0,
ADD COLUMN MembershipDate DATE,
ADD COLUMN MembershipLevel VARCHAR(20) DEFAULT 'Bronze';
```

**Adding Index for Performance:**

```sql
ALTER TABLE Customer
ADD INDEX idx_Email (Email);
```

**Modifying for Business Rule Change:**

```sql
ALTER TABLE Customer
MODIFY COLUMN Name VARCHAR(150) NOT NULL;
```

### Example 2: Database Normalization

Moving from 1NF to 3NF by splitting a denormalized table:

**Original Table:**

```sql
CREATE TABLE Orders (
 OrderID INT PRIMARY KEY,
 CustomerName VARCHAR(100),
 CustomerEmail VARCHAR(100),
 CustomerAddress VARCHAR(200),
 ProductName VARCHAR(100),
 ProductPrice DECIMAL(10,2),
 Quantity INT
);
```

**Normalization Process:**

```sql
-- Create Customer table
CREATE TABLE Customer (
 CustomerID INT PRIMARY KEY,
 Name VARCHAR(100),
 Email VARCHAR(100),
 Address VARCHAR(200)
);

-- Create Product table
CREATE TABLE Product (
 ProductID INT PRIMARY KEY,
 Name VARCHAR(100),
 Price DECIMAL(10,2)
);

-- Modify Orders table
ALTER TABLE Orders
DROP COLUMN CustomerName,
DROP COLUMN CustomerEmail,
DROP COLUMN CustomerAddress,
DROP COLUMN ProductName,
DROP COLUMN ProductPrice,
ADD COLUMN CustomerID INT REFERENCES Customer(CustomerID),
ADD COLUMN ProductID INT REFERENCES Product(ProductID);
```

### Example 3: Complete Schema Restructuring

A company restructuring requires renaming tables and columns:

```sql
-- Rename table
RENAME TABLE Employee TO Staff;

-- Add new column for reporting structure
ALTER TABLE Staff
ADD COLUMN ReportsTo INT NULL,
ADD CONSTRAINT FK_ReportsTo FOREIGN KEY (ReportsTo) REFERENCES Staff(StaffID);

-- Drop obsolete column
ALTER TABLE Staff
DROP COLUMN OldEmployeeID;

-- Add computed column (if supported)
ALTER TABLE Staff
ADD COLUMN FullName VARCHAR(200) GENERATED ALWAYS AS (CONCAT(FirstName, ' ', LastName));
```

## Exam Tips

1. **Understand DDL vs DML**: Remember that schema change statements are DDL commands (ALTER, DROP, TRUNCATE) which automatically commit, unlike DML commands (INSERT, UPDATE, DELETE) which can be rolled back within transactions.

2. **DROP vs TRUNCATE vs DELETE**: Know the differences - DROP removes table structure entirely, TRUNCATE removes all data but keeps structure, DELETE removes rows conditionally and can be rolled back.

3. **Column Modification Limitations**: Not all column modifications are possible. You typically cannot reduce column size if data exists, change to incompatible data types, or remove columns that are part of primary or foreign keys without first dropping the constraint.

4. **CASCADE and RESTRICT**: When dropping objects with dependencies, use CASCADE to drop dependent objects or RESTRICT to prevent dropping if dependencies exist.

5. **IF EXISTS Clause**: Always use DROP TABLE IF EXISTS or CREATE TABLE IF NOT EXISTS to make scripts idempotent and avoid errors when running multiple times.

6. **Index Naming Conventions**: Follow consistent naming like idx_tablename_column for regular indexes and uk_tablename_column for unique indexes.

7. **Order of Operations**: When making multiple schema changes, consider dependencies. Add columns before adding constraints that reference them, and drop dependent constraints before dropping referenced columns.

8. **Data Preservation**: ALTER TABLE operations generally preserve data, but always backup before major schema changes. Test in development environment first.
