# Relational Model Constraints and Relational Database Schemas

## Table of Contents

- [Relational Model Constraints and Relational Database Schemas](#relational-model-constraints-and-relational-database-schemas)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Domain Constraints](#1-domain-constraints)
  - [2. Key Constraints and Superkeys](#2-key-constraints-and-superkeys)
  - [3. Entity Integrity Constraint](#3-entity-integrity-constraint)
  - [4. Referential Integrity Constraint](#4-referential-integrity-constraint)
  - [5. Relational Database Schemas](#5-relational-database-schemas)
  - [6. Database State and Instance](#6-database-state-and-instance)
- [Examples](#examples)
  - [Example 1: Identifying Constraints in a Banking Database](#example-1-identifying-constraints-in-a-banking-database)
  - [Example 2: Handling Referential Integrity Violations](#example-2-handling-referential-integrity-violations)
  - [Example 3: Defining Constraints in SQL](#example-3-defining-constraints-in-sql)
- [Exam Tips](#exam-tips)

## Introduction

The relational model, introduced by Edgar F. Codd in 1970, forms the theoretical foundation for modern database management systems. One of the most critical aspects of designing a reliable database is defining appropriate constraints that maintain data integrity and accuracy. Without constraints, databases would become repositories of inconsistent and unreliable data, rendering them useless for practical applications.

Constraints in the relational model serve as rules that govern what data values are permitted in a database. They act as the "guardians" of data integrity, ensuring that only valid and meaningful data can be inserted, updated, or deleted. When working with relational databases, understanding these constraints is fundamental to creating robust and maintainable systems.

In this module, we will explore the various types of constraints supported by the relational model, including domain constraints, key constraints, entity integrity constraints, and referential integrity constraints. We will also examine how these constraints are used in defining relational database schemas and how database systems handle constraint violations during update operations.

## Key Concepts

### 1. Domain Constraints

Domain constraints define the permissible values for each attribute in a relation. A domain is essentially a set of atomic values that share the same data type. For example, the domain of the attribute "age" might consist of all positive integers between 1 and 150, while the domain of "email" might be all valid email address strings.

Domain constraints ensure that:

- Each attribute contains only values from its defined domain
- All values in an attribute are of the correct data type
- Value comparisons are meaningful (e.g., you cannot compare a string to an integer)

Common domain types include:

- Numeric domains (integer, float, decimal)
- Character domains (fixed-length strings, variable-length strings)
- Date and time domains
- Boolean domains
- User-defined domains (enumerations, ranges)

### 2. Key Constraints and Superkeys

A key constraint is one of the most important constraints in the relational model. A **superkey** is a set of attributes that uniquely identifies each tuple in a relation. In other words, no two tuples can have the same combination of values for the attributes in a superkey.

A **candidate key** is a minimal superkey—meaning it is a superkey but removing any attribute from it would destroy the uniqueness property. A relation can have multiple candidate keys, and the database designer chooses one of these to be the **primary key**.

Key constraints require that:

- No two tuples in a relation can have the same primary key value
- The primary key value cannot be NULL (this is enforced by entity integrity)

For example, in a STUDENT relation with attributes (student_id, name, email, phone), both {student_id} and {email} could be candidate keys if each student has a unique ID and unique email address.

### 3. Entity Integrity Constraint

The entity integrity constraint states that the primary key of a relation cannot contain NULL values. This constraint ensures that each tuple in a relation can be uniquely identified. If the primary key were NULL, we would have no way of distinguishing between different tuples.

The rationale behind this constraint is:

- Every relation must represent an entity from the real world
- Each entity must have a unique identifier
- Without a unique identifier, we cannot reliably reference or update tuples

For instance, in an EMPLOYEE relation with primary key emp_id, every tuple must have a non-NULL emp_id value. A tuple with a NULL emp_id would violate entity integrity.

### 4. Referential Integrity Constraint

The referential integrity constraint maintains consistency between relations. It ensures that a foreign key value in one relation must either match the primary key value of a related tuple in another relation or be NULL.

Consider two relations: DEPARTMENT(dept_id, dept_name, manager_id) and EMPLOYEE(emp_id, emp_name, dept_id). Here, dept_id in EMPLOYEE is a foreign key referencing DEPARTMENT(dept_id). Referential integrity requires that every dept_id value in the EMPLOYEE table must either:

- Match an existing dept_id in the DEPARTMENT table, or
- Be NULL (meaning the employee is not assigned to any department)

This constraint prevents "dangling references"—situations where a record references another record that doesn't exist.

### 5. Relational Database Schemas

A relational database schema is the logical structure of the entire database. It defines:

- All relations (tables) in the database
- Attributes for each relation
- Primary keys and foreign keys
- Domain definitions for each attribute
- Integrity constraints

The schema is typically created during the database design phase and remains relatively stable. There are two types of schema:

- **Conceptual schema**: Describes the logical structure of the entire database
- **External schema**: Describes specific user views of the database

A relation schema is denoted as R(A1, A2, ..., An) where R is the relation name and A1, A2, ..., An are the attributes.

### 6. Database State and Instance

A database schema is static, defining the structure, while a database instance or state is the actual data stored at a particular moment. When we perform INSERT, UPDATE, or DELETE operations, we change the database state, but the schema remains unchanged unless altered through DDL commands.

For example, the schema for STUDENT(student_id, name, age, department) is fixed, but the actual data in the table (the instance) changes as students are added, modified, or removed.

## Examples

### Example 1: Identifying Constraints in a Banking Database

Consider a BANK database with the following relations:

```
CUSTOMER(CustomerID, Name, Email, Phone, Address)
ACCOUNT(AccountNumber, CustomerID, Balance, AccountType)
TRANSACTION(TransactionID, AccountNumber, Amount, Date, Type)
```

**Domain Constraints:**

- CustomerID must be a 10-digit integer
- Balance must be a decimal value greater than or equal to zero
- AccountType must be one of: 'Savings', 'Current', 'Fixed Deposit'

**Key Constraints:**

- CustomerID is the primary key of CUSTOMER
- AccountNumber is the primary key of ACCOUNT
- TransactionID is the primary key of TRANSACTION

**Entity Integrity:**

- No customer can have a NULL CustomerID
- No account can have a NULL AccountNumber

**Referential Integrity:**

- CustomerID in ACCOUNT must reference an existing CustomerID in CUSTOMER
- AccountNumber in TRANSACTION must reference an existing AccountNumber in ACCOUNT

### Example 2: Handling Referential Integrity Violations

Given the relations:

```
DEPT(DId, DName, Location)
EMP(EId, EName, DId)
```

Where DId in EMP is a foreign key referencing DEPT(DId).

**Scenario 1: Attempting to delete a department with employees**

If we try to delete a department from DEPT that has employees in EMP, this would violate referential integrity. The database system typically handles this in one of several ways:

- **RESTRICT**: Reject the delete operation
- **CASCADE**: Delete all related employees as well
- **SET NULL**: Set the DId in related employees to NULL
- **SET DEFAULT**: Set the DId in related employees to a default value

**Scenario 2: Inserting an employee with invalid department**

```sql
-- This would fail if DEPT does not contain DId = 50
INSERT INTO EMP VALUES (101, 'John', 50);
-- Error: Foreign key constraint violation
```

### Example 3: Defining Constraints in SQL

```sql
CREATE TABLE STUDENT (
 StudentID INT PRIMARY KEY,
 Name VARCHAR(50) NOT NULL,
 Email VARCHAR(100) UNIQUE,
 Age INT CHECK (Age >= 18 AND Age <= 100),
 DepartmentID INT REFERENCES DEPARTMENT(DepartmentID)
);

CREATE TABLE DEPARTMENT (
 DepartmentID INT PRIMARY KEY,
 DepartmentName VARCHAR(50) NOT NULL
);
```

In this SQL example:

- PRIMARY KEY enforces entity integrity on StudentID
- NOT NULL enforces domain constraint on Name
- UNIQUE enforces a candidate key constraint on Email
- CHECK enforces domain constraint on Age
- REFERENCES enforces referential integrity on DepartmentID

## Exam Tips

1. **Remember the three primary integrity constraints**: Entity integrity, referential integrity, and domain constraints are the three main integrity constraints in the relational model.

2. **Primary key cannot be NULL**: This is a key point in entity integrity. In exams, remember that primary keys must have unique, non-NULL values.

3. **Foreign key can be NULL**: Unlike primary keys, foreign keys can have NULL values (unless explicitly defined as NOT NULL), representing that the relationship is optional.

4. **Candidate keys vs. primary key**: All candidate keys can uniquely identify tuples, but only one is chosen as the primary key. The others become alternate keys.

5. **Superkeys contain candidate keys**: Every candidate key is a superkey, but not every superkey is a candidate key. Candidate keys are minimal.

6. **Referential integrity violations**: When deleting or updating a parent tuple, consider CASCADE, SET NULL, RESTRICT, and NO ACTION as handling mechanisms.

7. **Schema vs. instance**: Schema is the structure (permanent), instance is the data (changes with operations). This distinction is often tested.

8. **Domain constraints are attribute-level**: They define what values an individual attribute can take, while key constraints work at the tuple level.

9. **NULL has special meaning**: NULL means "unknown or missing" and is not the same as zero or empty string. Any comparison with NULL yields UNKNOWN, not TRUE or FALSE.

10. **Integrity constraints are enforced by the DBMS**: The database management system automatically enforces these constraints, preventing invalid data from entering the database.
