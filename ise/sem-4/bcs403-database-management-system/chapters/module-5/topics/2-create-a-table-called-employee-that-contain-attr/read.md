# **Database Management System**

## **Module: 08 - Creating Tables**

## **Topic: 2 Create a table called Employee**

### Introduction

In a database management system, a table is a collection of related data that is stored in rows and columns. Each column represents an attribute of the data, and each row represents a single record. In this topic, we will learn how to create a table called "Employee" that contains attributes such as EMPNO.

### What is a Table?

A table is a fundamental concept in database management systems. It is a collection of related data that is stored in rows and columns. Each column represents an attribute of the data, and each row represents a single record.

**Key Characteristics of a Table:**

- **Rows**: Represent individual records
- **Columns**: Represent attributes of the data
- **Primary Key**: A unique identifier for each record

### Creating a Table: EMPNO

In this topic, we will create a table called "Employee" that contains attributes such as EMPNO.

**Employee Table Attributes:**

- **EMPNO**: Unique identifier for each employee
- **ENAME**: Employee name
- **JTITLE**: Job title
- **MGRNO**: Manager's EMPNO (for hierarchical relationships)
- **DEPTNO**: Department number
- **SALARY**: Employee salary

**Example Employee Table:**

| EMPNO | ENAME       | JTITLE    | MGRNO | DEPTNO | SALARY |
| ----- | ----------- | --------- | ----- | ------ | ------ |
| 101   | John Smith  | Manager   | 202   | 1      | 50000  |
| 102   | Jane Doe    | Sales Rep | 201   | 2      | 40000  |
| 103   | Bob Johnson | Engineer  | 202   | 1      | 60000  |

### SQL Syntax for Creating a Table

To create a table called "Employee", we use the following SQL syntax:

```sql
CREATE TABLE Employee (
  EMPNO INT PRIMARY KEY,
  ENAME VARCHAR(20),
  JTITLE VARCHAR(20),
  MGRNO INT,
  DEPTNO INT,
  SALARY DECIMAL(10,2)
);
```

### Example Use Case:

Suppose we want to insert a new employee record into the "Employee" table.

```sql
INSERT INTO Employee (EMPNO, ENAME, JTITLE, MGRNO, DEPTNO, SALARY)
VALUES (104, 'Mike Brown', 'Sales Rep', 201, 2, 45000);
```

This will add a new row to the "Employee" table with the specified attributes.

### Best Practices for Table Design:

- Identify the primary key attribute: Ensure that each table has a primary key attribute that uniquely identifies each record.
- Use meaningful attribute names: Use descriptive names for attributes to improve data readability and maintainability.
- Use data types effectively: Choose the most suitable data type for each attribute to prevent data inconsistencies and improve performance.
