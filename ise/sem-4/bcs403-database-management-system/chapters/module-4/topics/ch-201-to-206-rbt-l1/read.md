# **DATABASE MANAGEMENT SYSTEM (DBMS) Study Material**

**Module:** 8 hours
**Topic:** Ch 20.1 to 20.6 RBT: L1

## **1. Introduction to DBMS (20.1)**

### Definition:

A Database Management System (DBMS) is a software system that allows for the definition, creation, maintenance, and manipulation of databases.

### Characteristics of a DBMS:

- Provides a way to store and retrieve data
- Supports data independence
- Supports data integrity
- Supports data security
- Supports data backup and recovery

### Types of DBMS:

- Relational DBMS (RDBMS)
- Object-Oriented DBMS (OODBMS)
- Hierarchical DBMS (HDBMS)
- Network DBMS (NDBMS)

## **2. Relational Database Management System (RDBMS)**

### Definition:

A Relational Database Management System (RDBMS) is a type of DBMS that stores data in tables with well-defined relationships between them.

### Characteristics of RDBMS:

- Tables are used to store data
- Data is organized into rows and columns
- Relationships between tables are established using keys
- Supports data integrity and security

### Features of RDBMS:

- Supports multiple users
- Supports transactions
- Supports subqueries
- Supports views

## **3. Normalization of Database**

### Definition:

Normalization is the process of organizing data in a database to minimize data redundancy and dependency.

### Types of Normalization:

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Boyce-Codd Normal Form (BCNF)

### Normalization Rules:

- Each cell in a table should contain a single value
- Each row should contain a unique combination of values
- Each column should contain a single value

### Example:

| Customer ID | Customer Name | Order ID | Product ID | Quantity |
| ----------- | ------------- | -------- | ---------- | -------- |
| 1           | John          | 1        | 101        | 2        |
| 1           | John          | 1        | 102        | 3        |
| 2           | Jane          | 2        | 101        | 1        |

## **4. Relational Algebra**

### Definition:

Relational Algebra is a formal language used to manipulate and query relational databases.

### Operations:

- Selection
- Projection
- Union
- Intersection
- Difference
- Join
- Divide

### Examples:

- Selection: `σ Name = 'John' (Customers)`
- Projection: `π Name (Customers)`
- Union: `σ Name = 'John' ∨ σ Name = 'Jane' (Customers)`

## **5. SQL**

### Definition:

SQL (Structured Query Language) is a programming language used to manipulate and query relational databases.

### Syntax:

- SELECT
- FROM
- WHERE
- GROUP BY
- HAVING
- ORDER BY

### Examples:

- SELECT \* FROM Customers WHERE Name = 'John'
- CREATE TABLE Customers (Name VARCHAR(50), Address VARCHAR(100))

## **6. Data Types**

### Definition:

Data types are the categorization of data into different types such as numeric, string, date, etc.

### Types of Data Types:

- Numeric
- String
- Date
- Time
- Boolean
- Decimal

### Examples:

- Numeric: `INT`, `FLOAT`, `DOUBLE`
- String: `VARCHAR`, `CHAR`
- Date: `DATE`, `TIME`
- Boolean: `BOOL`

## **7. Indexing**

### Definition:

Indexing is the process of creating a data structure that improves the speed of data retrieval.

### Types of Indexing:

- B-Tree Index
- Hash Index
- Full-Text Index

### Benefits:

- Improved query performance
- Reduced data retrieval time
- Increased data security

### Example:

| Customer ID | Customer Name | Order ID | Product ID | Quantity |
| ----------- | ------------- | -------- | ---------- | -------- |
| 1           | John          | 1        | 101        | 2        |
| 1           | John          | 1        | 102        | 3        |
| 2           | Jane          | 2        | 101        | 1        |

## **8. Database Security**

### Definition:

Database security refers to the measures taken to protect the database from unauthorized access, modification, or deletion.

### Types of Database Security:

- Authentication
- Authorization
- Encryption
- Access Control

### Examples:

- Authentication: Using a username and password
- Authorization: Giving access to specific tables or columns
- Encryption: Encrypting data to prevent unauthorized access
- Access Control: Limiting access to certain database objects

By following this study material, you will be able to understand the concepts of Database Management System, Relational Database Management System, Normalization, Relational Algebra, SQL, Data Types, Indexing, and Database Security.
