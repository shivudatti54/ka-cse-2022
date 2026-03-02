# Constraints On Relationships in Database Management Systems

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#introduction-and-real-world-relevance)
2. [Classification of Constraints](#classification-of-constraints)
3. [Domain Constraints](#domain-constraints)
4. [Key Constraints](#key-constraints)
5. [Entity Integrity Constraints](#entity-integrity-constraints)
6. [Referential Integrity Constraints](#referential-integrity-constraints)
7. [Participation Constraints](#participation-constraints)
8. [Cardinality Constraints](#cardinality-constraints)
9. [Update and Delete Rules](#update-and-delete-rules)
10. [Weak Entities and Identifying Relationships](#weak-entities-and-identifying-relationships)
11. [CHECK Constraints](#check-constraints)
12. [Practical Examples with SQL](#practical-examples-with-sql)
13. [Key Takeaways](#key-takeaways)
14. [Assessment Section](#assessment-section)
    - [Multiple Choice Questions](#multiple-choice-questions)
    - [Flashcards](#flashcards)
    - [Short Answer Questions](#short-answer-questions)

---

## Introduction and Real-World Relevance

### What Are Constraints on Relationships?

In Database Management Systems (DBMS), **constraints on relationships** are rules and restrictions that govern how data in different tables (relations) can relate to each other. These constraints ensure the **integrity, accuracy, and consistency** of data within a database. Without these constraints, databases would become prone to anomalies, redundant data, and logical inconsistencies that could severely impact applications relying on them.

### Why This Topic Matters in the Real World

Consider a banking system where customers have accounts, and accounts make transactions. Without proper constraints:

- A transaction could reference a non-existent account
- Deleting a customer might leave orphaned records of their accounts
- Multiple customers could have the same account number
- Negative balances could be recorded

**Real-world applications** of relationship constraints include:

1. **E-commerce platforms**: Ensuring orders reference valid customers and products
2. **Hospital Management Systems**: Linking patient records to valid diagnoses and treatments
3. **University Databases**: Maintaining relationships between students, courses, and grades
4. **Social Networks**: Ensuring friend connections are between valid user accounts

### Delhi University Syllabus Context

This topic aligns with the **Database Management Systems** paper for BSc (Hons) Computer Science under NEP 2024 UGCF. Students are expected to understand:

- Various types of integrity constraints
- How constraints maintain data quality
- Implementation of constraints in SQL
- Theoretical foundations as per E.F. Codd's relational model

---

## Classification of Constraints

Constraints in relational databases can be classified into the following categories:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONSTRAINT CATEGORIES                       │
├─────────────────────────────────────────────────────────────────┤
│  1. Domain Constraints (Type Constraints)                      │
│  2. Key Constraints (Uniqueness)                               │
│  3. Entity Integrity Constraints                               │
│  4. Referential Integrity Constraints                         │
│  5. Participation Constraints (Total vs Partial)              │
│  6. Cardinality Constraints (1:1, 1:N, M:N)                   │
│  7. CHECK Constraints                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Domain Constraints

### Definition

**Domain constraints** define the allowable values for each attribute. They ensure that each attribute in a relation holds values from a valid domain (set of permissible values).

### Components of Domain Constraints

1. **Data Type**: Specifies the type of data (INTEGER, VARCHAR, DATE, etc.)
2. **Format**: Specific pattern or format (e.g., phone numbers, email)
3. **Range**: Valid range of values (e.g., marks between 0-100)
4. **Nullability**: Whether NULL values are allowed

### Examples

```sql
-- Creating a domain with CHECK constraint
CREATE DOMAIN GradeType AS VARCHAR(2)
CHECK (VALUE IN ('A+', 'A', 'B+', 'B', 'C', 'D', 'F'));

-- Table with domain constraints
CREATE TABLE Student (
    student_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) CHECK (email LIKE '%@%.%'),
    age INTEGER CHECK (age >= 18 AND age <= 35),
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O'))
);
```

---

## Key Constraints

### What Is a Key?

A **key** is a set of one or more attributes that uniquely identifies a tuple (row) in a relation. Keys are fundamental to relational databases as they enforce uniqueness.

### Types of Keys

| Key Type | Description | Example |
|----------|-------------|---------|
| **Candidate Key** | Minimal superkey; any minimal unique attribute | roll_no, email |
| **Primary Key (PK)** | Selected candidate key to identify tuples | roll_no |
| **Alternate Key** | Unused candidate keys | email (if roll_no is PK) |
| **Composite Key** | Key with multiple attributes | (course_id, student_id) |
| **Foreign Key (FK)** | References PK of another relation | dept_id references Department |

### Properties of Keys

1. **Uniqueness**: No two tuples can have the same key value
2. **Minimality**: No proper subset of a candidate key can be a superkey
3. **Not Null**: Primary key cannot contain NULL values

```sql
-- Primary Key
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50) UNIQUE NOT NULL,
    location VARCHAR(50)
);

-- Composite Primary Key
CREATE TABLE Enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id)
);

-- Unique Key (Alternate Key)
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_email VARCHAR(100) UNIQUE,
    emp_name VARCHAR(50)
);
```

---

## Entity Integrity Constraints

### Definition

**Entity integrity** ensures that the primary key of a relation is never NULL and must have a unique value. This constraint guarantees that each tuple can be uniquely identified.

### Rules

1. **Primary Key ≠ NULL**: No component of the primary key can be NULL
2. **Primary Key = Unique**: Each primary key value must be unique

### Why Entity Integrity Matters

Without entity integrity:
- You cannot uniquely identify records
- Duplicate or null records would corrupt data
- Relational algebra operations would fail

```sql
-- Entity Integrity enforced by PRIMARY KEY
CREATE TABLE Product (
    product_id INTEGER PRIMARY KEY,  -- Cannot be NULL, must be unique
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2)
);

-- Attempting to insert NULL in PK will fail
-- INSERT INTO Product VALUES (NULL, 'Test', 100); -- ERROR
```

---

## Referential Integrity Constraints

### Definition

**Referential integrity** (also called **entity referential integrity**) ensures that relationships between tables remain consistent. A foreign key in a referencing table must always reference a valid primary key value in the referenced table.

### Foreign Key Rules

```
Referencing Table (Child)          Referenced Table (Parent)
┌─────────────────────┐            ┌─────────────────────┐
│ foreign_key --------┼────────----►│ primary_key         │
│ (must match PK     │            │ (of parent table)   │
│  of parent or     │            └─────────────────────┘
│  be NULL)         │
└─────────────────────┘
```

### Example Scenario

```sql
-- Parent Table
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Child Table with Foreign Key
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INTEGER REFERENCES Department(dept_id),
    salary DECIMAL(10,2)
);

-- Valid insert: dept_id = 1 exists in Department
INSERT INTO Employee VALUES (101, 'John Smith', 1, 50000);

-- Invalid insert: dept_id = 99 does not exist
-- INSERT INTO Employee VALUES (102, 'Jane Doe', 99, 45000);
-- ERROR: foreign key constraint violation
```

---

## Participation Constraints

### Definition

**Participation constraints** specify whether the existence of an entity depends on its being related to another entity through a relationship. There are two types:

### 1. Total Participation (Mandatory)

Every entity in the entity set **must** participate in the relationship. Denoted by double line in ER diagrams.

**Example**: Every student **must** enroll in at least one course.

```sql
-- Total participation enforced by NOT NULL on FK
CREATE TABLE Enrollment (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
```

### 2. Partial Participation (Optional)

An entity may or may not participate in the relationship. Denoted by single line in ER diagrams.

**Example**: An employee may or may not manage a department.

```sql
-- Partial participation: manager_id can be NULL
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50),
    manager_id INTEGER REFERENCES Employee(emp_id)  -- Optional
);
```

### Visual Representation

```
Total Participation:           Partial Participation:

    ┌───────┐                      ┌───────┐
    │  A    │                      │  A    │
    └───────┘                      └───────┘
      ╱   ╲                          ╱   ╲
     ╱     ╲                        ╱     ╲
    ╱       ╲                      ╱       ╲
┌───────┐                      ┌───────┐
│   B   │                      │   B   │
└───────┘                      └───────┘
(must have A)                (may have A)
```

---

## Cardinality Constraints

### Definition

**Cardinality** specifies the number of instances of one entity that can be associated with each instance of another entity through a relationship.

### Types of Cardinality

| Cardinality | Description | ER Notation |
|-------------|-------------|-------------|
| **One-to-One (1:1)** | Each entity in A relates to exactly one in B | 1────────1 |
| **One-to-Many (1:N)** | One entity in A relates to many in B | 1─────────N |
| **Many-to-One (N:1)** | Many entities in A relate to one in B | N─────────1 |
| **Many-to-Many (M:N)** | Many entities in A relate to many in B | M─────────N |

### Implementation Examples

```sql
-- 1:1 Relationship - Employee manages one Department
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50),
    manager_id INTEGER UNIQUE REFERENCES Employee(emp_id)
);

-- 1:N Relationship - One Department has many Employees
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INTEGER REFERENCES Department(dept_id)
);

-- M:N Relationship - Students enroll in many Courses
-- Implemented via junction table
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE Course (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE Enrollment (
    student_id INTEGER,
    course_id INTEGER,
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
```

---

## Update and Delete Rules

### What Are Referential Actions?

When a parent (referenced) row is updated or deleted, we must define what happens to the corresponding child (referencing) rows. These are called **referential integrity actions** or **update/delete rules**.

### Types of Referential Actions

| Action | Behavior |
|--------|----------|
| **NO ACTION** | Prevents change if child rows exist (default) |
| **CASCADE** | Automatically updates/deletes child rows |
| **SET NULL** | Sets foreign key to NULL |
| **SET DEFAULT** | Sets foreign key to default value |

### Detailed Explanation with Examples

#### 1. CASCADE

```sql
-- If parent department is deleted, all employees are deleted
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

**Scenario**: If Department 10 is deleted, all employees in department 10 are automatically deleted.

#### 2. SET NULL

```sql
-- If parent department is deleted, employee's dept_id becomes NULL
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
        ON UPDATE SET NULL
);
```

**Scenario**: If Department 10 is deleted, employees previously in dept 10 now have dept_id = NULL.

#### 3. NO ACTION

```sql
-- Prevents deletion/update if child rows exist
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);
```

**Scenario**: Cannot delete Department 10 if employees exist in it.

### Practical Example: E-Commerce System

```sql
-- Parent Table: Categories
CREATE TABLE Category (
    cat_id INTEGER PRIMARY KEY,
    cat_name VARCHAR(50) NOT NULL
);

-- Child Table: Products with CASCADE and SET NULL
CREATE TABLE Product (
    prod_id INTEGER PRIMARY KEY,
    prod_name VARCHAR(100) NOT NULL,
    cat_id INTEGER,
    price DECIMAL(10,2),
    FOREIGN KEY (cat_id) REFERENCES Category(cat_id)
        ON DELETE SET NULL      -- Product exists without category
        ON UPDATE CASCADE       -- Product sees category ID change
);

-- Child Table: OrderItems with CASCADE
CREATE TABLE OrderItem (
    order_id INTEGER,
    prod_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, prod_id),
    FOREIGN KEY (prod_id) REFERENCES Product(prod_id)
        ON DELETE CASCADE       -- Deleting product removes order items
);
```

---

## Weak Entities and Identifying Relationships

### Weak Entity

A **weak entity** is an entity that cannot be uniquely identified by its own attributes alone. It depends on another entity (called the **owner** or **identifying entity**) for its identity.

### Characteristics of Weak Entities

1. Does not have a primary key of its own
2. Uses a **partial key** (discriminator) along with the owner's primary key
3. Existence depends on the owner entity (total participation)
4. Identified through an **identifying relationship**

### Example: Bank Account System

```
┌──────────────┐                         ┌──────────────┐
│   Customer   │ 1          N            │    Account   │
├──────────────┤◄────────────────────────►├──────────────┤
│ customer_id  │    owns                 │ account_no   │
│ name         │                         │ balance      │
│ phone        │                         │ account_type │
└──────────────┘                         └──────────────┘
         │                                        │
         │              Identifying              │
         └────────────────────────────────────────┘
```

### Implementation in SQL

```sql
-- Owner Entity
CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(50),
    phone VARCHAR(15)
);

-- Weak Entity with identifying relationship
CREATE TABLE Account (
    account_number VARCHAR(20),
    customer_id INTEGER NOT NULL,  -- Part of composite key
    balance DECIMAL(15,2),
    account_type VARCHAR(20),
    PRIMARY KEY (account_number, customer_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
        ON DELETE CASCADE
);
```

In this case:
- Account is a weak entity
- (account_number, customer_id) together form the primary key
- customer_id is both a foreign key and part of the primary key
- Deleting a customer cascades to delete all their accounts

---

## CHECK Constraints

### Definition

The **CHECK constraint** allows you to specify conditions that must be true for each row in a table. It restricts the values that can be inserted or updated.

### Syntax

```sql
CREATE TABLE table_name (
    column_name datatype CHECK (condition),
    ...
);
```

### Examples

```sql
-- Basic CHECK constraint
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER CHECK (age >= 18),
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    marks DECIMAL(5,2) CHECK (marks >= 0 AND marks <= 100),
    status VARCHAR(20) CHECK (status IN ('Active', 'Inactive', 'Graduated'))
);

-- Multiple conditions with AND
CREATE TABLE Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2) CHECK (salary > 0),
    hire_date DATE CHECK (hire_date <= CURRENT_DATE),
    bonus DECIMAL(10,2) CHECK (bonus <= salary * 0.5)
);

-- Complex CHECK with CASE
CREATE TABLE Order (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    shipped_date DATE,
    status VARCHAR(20) CHECK (
        status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')
    ),
    CHECK (
        CASE 
            WHEN status = 'Shipped' THEN 
                shipped_date IS NOT NULL AND shipped_date >= order_date
            ELSE TRUE
        END
    )
);
```

### CHECK vs Other Constraints

| Constraint | Purpose | Example |
|------------|---------|---------|
| **NOT NULL** | Column cannot be NULL | name VARCHAR(50) NOT NULL |
| **UNIQUE** | No duplicate values | email VARCHAR(100) UNIQUE |
| **PRIMARY KEY** | Unique + NOT NULL | PRIMARY KEY(id) |
| **FOREIGN KEY** | Reference integrity | FOREIGN KEY(dept_id) REFERENCES Dept |
| **CHECK** | Custom condition | CHECK(age >= 18) |

---

## Practical Examples with SQL

### Example 1: University Database

```sql
-- Complete University Database Schema

-- Department (Parent Entity)
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(50) UNIQUE NOT NULL,
    establishment_year INTEGER CHECK (establishment_year >= 1900)
);

-- Course (Weak Entity - dependent on Department)
CREATE TABLE Course (
    course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    dept_id INTEGER NOT NULL,
    credits INTEGER CHECK (credits BETWEEN 1 AND 6),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Student (Entity with various constraints)
CREATE TABLE Student (
    roll_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE CHECK (email LIKE '%@%.%'),
    phone VARCHAR(15),
    dob DATE CHECK (dob >= '1990-01-01'),
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
);

-- Enrollment (M:N relationship with attributes)
CREATE TABLE Enrollment (
    roll_no VARCHAR(10),
    course_id VARCHAR(10),
    semester INTEGER CHECK (semester BETWEEN 1 AND 8),
    year INTEGER CHECK (year >= 2020),
    grade CHAR(2) CHECK (grade IN ('A+', 'A', 'B+', 'B', 'C', 'D', 'F', 'P')),
    PRIMARY KEY (roll_no, course_id, semester),
    FOREIGN KEY (roll_no) REFERENCES Student(roll_no)
        ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
        ON DELETE CASCADE
);

-- Teacher (Entity)
CREATE TABLE Teacher (
    teacher_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2) CHECK (salary > 0),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
);

-- Teaching (M:N between Teacher and Course)
CREATE TABLE Teaching (
    teacher_id INTEGER,
    course_id VARCHAR(10),
    semester INTEGER,
    PRIMARY KEY (teacher_id, course_id, semester),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
        ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
        ON DELETE CASCADE
);
```

### Example 2: Hospital Management System

```sql
-- Hospital Database with comprehensive constraints

-- Ward (Entity)
CREATE TABLE Ward (
    ward_id INTEGER PRIMARY KEY,
    ward_name VARCHAR(50) NOT NULL,
    ward_type VARCHAR(20) CHECK (ward_type IN ('General', 'ICU', 'Emergency', 'Pediatric')),
    total_beds INTEGER CHECK (total_beds > 0),
    occupied_beds INTEGER DEFAULT 0,
    CHECK (occupied_beds <= total_beds)
);

-- Doctor (Entity)
CREATE TABLE Doctor (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    qualification VARCHAR(50),
    experience_years INTEGER CHECK (experience_years >= 0),
    consultation_fee DECIMAL(10,2) CHECK (consultation_fee > 0),
    ward_id INTEGER,
    FOREIGN KEY (ward_id) REFERENCES Ward(ward_id)
        ON DELETE SET NULL
);

-- Patient (Weak Entity - identified by Patient + Admission)
CREATE TABLE Patient (
    patient_id INTEGER PRIMARY KEY,
    patient_name VARCHAR(50) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    dob DATE CHECK (dob < CURRENT_DATE),
    blood_group VARCHAR(5) CHECK (blood_group IN ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')),
    phone VARCHAR(15),
    address VARCHAR(200)
);

-- Admission (Weak entity dependent on Patient)
CREATE TABLE Admission (
    admission_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    ward_id INTEGER,
    doctor_id INTEGER NOT NULL,
    admission_date DATE DEFAULT CURRENT_DATE,
    discharge_date DATE,
    diagnosis VARCHAR(200),
    status VARCHAR(20) DEFAULT 'Admitted' CHECK (status IN ('Admitted', 'Discharged', 'Transferred')),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
        ON DELETE CASCADE,
    FOREIGN KEY (ward_id) REFERENCES Ward(ward_id)
        ON DELETE SET NULL,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
    CHECK (discharge_date IS NULL OR discharge_date >= admission_date)
);

-- Treatment (M:N between Doctor and Patient)
CREATE TABLE Treatment (
    treatment_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    treatment_date DATE NOT NULL,
    treatment_type VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
        ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
        ON DELETE CASCADE
);
```

---

## Key Takeaways

### Summary of Constraints

1. **Domain Constraints**: Define valid values for attributes (data type, format, range)

2. **Key Constraints**: 
   - Ensure uniqueness through PRIMARY KEY, UNIQUE
   - Composite keys for multi-attribute identification

3. **Entity Integrity**: Primary key must be NOT NULL and unique

4. **Referential Integrity**: Foreign keys must reference valid primary keys

5. **Participation Constraints**:
   - Total: Every entity must participate (NOT NULL)
   - Partial: Participation is optional

6. **Cardinality**: Defines relationship ratios (1:1, 1:N, M:N)

7. **Update/Delete Rules**:
   - CASCADE: Propagate changes
   - SET NULL: Set foreign key to NULL
   - NO ACTION: Prevent changes

8. **Weak Entities**: Use owner's key + partial key for identification

9. **CHECK Constraints**: Custom business rules for data validation

### Best Practices

- Always define appropriate constraints at table creation
- Use meaningful constraint names for debugging
- Choose appropriate referential actions based on business logic
- Document all constraints in database documentation
- Test constraint violations during development

---

## Assessment Section

### Multiple Choice Questions

#### Easy Level

**Question 1:** Which constraint ensures that each tuple in a relation can be uniquely identified?
- A) Domain Constraint
- B) Entity Integrity Constraint
- C) Referential Integrity Constraint
- D) CHECK Constraint

**Answer:** B

---

**Question 2:** In an ER diagram, a double line connecting an entity to a relationship represents:
- A) Partial participation
- B) Total participation
- C) Identifying relationship
- D) Cardinality ratio

**Answer:** B

---

**Question 3:** What is the default action when deleting a parent row that has child references?
- A) CASCADE
- B) SET NULL
- C) NO ACTION
- D) RESTRICT

**Answer:** C

---

**Question 4:** Which SQL constraint is used to enforce entity integrity?
- A) FOREIGN KEY
- B) UNIQUE
- C) PRIMARY KEY
- D) CHECK

**Answer:** C

---

**Question 5:** A weak entity must have:
- A) A primary key of its own
- B) A partial key with the owner's primary key
- C) No relationship with any other entity
- D) Only one attribute

**Answer:** B

---

#### Medium Level

**Question 6:** Consider the following SQL statement:

```sql
CREATE TABLE OrderItem (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
        ON DELETE CASCADE ON UPDATE SET NULL
);
```

What happens when a product is deleted?
- A) All order items for that product are deleted
- B) The product_id in order items becomes NULL
- C) The delete operation fails
- D) Order items are set to default values

**Answer:** A

---

**Question 7:** In a one-to-many relationship between Department and Employee, where should the foreign key be placed?
- A) In the Department table
- B) In the Employee table
- C) In a separate junction table
- D) Both tables

**Answer:** B

---

**Question 8:** Which of the following is NOT a valid cardinality type?
- A) 1:1
- B) 1:N
- C) N:M
- D) 0:1

**Answer:** D

---

**Question 9:** What does the CHECK constraint in the following do?

```sql
CHECK (salary > 0 AND salary <= 1000000)
```
- A) Allows salary to be 0
- B) Allows salary to be NULL
- C) Requires salary between 1 and 1,000,000
- D) Requires salary to be exactly 1000000

**Answer:** C

---

**Question 10:** A student can enroll in multiple courses, and each course can have multiple students. This is an example of:
- A) 1:1 relationship
- B) 1:N relationship
- C) N:1 relationship
- D) M:N relationship

**Answer:** D

---

#### Hard Level

**Question 11:** Given the schema:

```sql
CREATE TABLE A (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE B (
    bid INTEGER PRIMARY KEY,
    aid INTEGER REFERENCES A(id) ON DELETE SET NULL
);

INSERT INTO A VALUES (1, 'Alpha'), (2, 'Beta');
INSERT INTO B VALUES (100, 1), (101, 1), (102, 2);
```

After executing `DELETE FROM A WHERE id = 1;`, what will be the contents of table B?
- A) (100, 1), (101, 1), (102, 2)
- B) (102, 2)
- C) (100, NULL), (101, NULL), (102, 2)
- D) (100, 1), (101, 1)

**Answer:** C

---

**Question 12:** Which constraint combination correctly represents a weak entity with total participation in an identifying relationship?
- A) Primary key + Foreign key (partial participation)
- B) Primary key + Foreign key (total participation)
- C) Composite primary key with foreign key (total participation)
- D) Unique key + Foreign key (partial participation)

**Answer:** C

---

**Question 13:** Consider a scenario where you need to ensure that a student's age is at least 18, and they must be enrolled in at least one course. Which constraints apply?
- A) CHECK (age >= 18) for entity, total participation for relationship
- B) NOT NULL for age, partial participation for relationship
- C) UNIQUE for age, foreign key constraint
- D) CHECK (age >= 18), foreign key with total participation

**Answer:** A

---

**Question 14:** In a ternary relationship R(A, B, C), what is the minimum number of foreign keys needed to implement it?
- A) 1
- B) 2
- C) 3
- D) Depends on cardinality

**Answer:** C

---

**Question 15:** What will happen if we try to insert the following in a table with the constraint `CHECK (status IN ('Active', 'Inactive'))`?

```sql
INSERT INTO Table VALUES ('ACTIVE');
```
- A) Insert succeeds
- B) Insert fails (case sensitivity)
- C) Insert fails (value not in list)
- D) Depends on database settings

**Answer:** C (in standard SQL, 'ACTIVE' ≠ 'Active')

---

### Flashcards

#### Flashcard 1
**Term:** Referential Integrity
**Definition:** A database rule that ensures relationships between tables remain consistent. A foreign key must always reference a valid primary key value.
---

#### Flashcard 2
**Term:** CASCADE
**Definition:** A referential action that automatically propagates changes (updates/deletes) from parent table to child table.
---

#### Flashcard 3
**Term:** Weak Entity
**Definition:** An entity that cannot be uniquely identified by its own attributes alone and depends on another entity (owner) for identification.
---

#### Flashcard 4
**Term:** Total Participation
**Definition:** A participation constraint where every entity must participate in the relationship; represented by a double line in ER diagrams.
---

#### Flashcard 5
**Term:** Composite Key
**Definition:** A primary key consisting of two or more attributes that together uniquely identify a tuple.
---

#### Flashcard 6
**Term:** Cardinality
**Definition:** The number of instances of one entity that can be associated with each instance of another entity (1:1, 1:N, M:N).
---

#### Flashcard 7
**Term:** Entity Integrity
**Definition:** The rule that states the primary key cannot be NULL and must have a unique value for each tuple.
---

#### Flashcard 8
**Term:** Foreign Key
**Definition:** An attribute (or set of attributes) in one table that references the primary key of another table to enforce referential integrity.
---

#### Flashcard 9
**Term:** CHECK Constraint
**Definition:** A constraint that specifies a condition that must be true for each row in a table, allowing custom business rules.
---

#### Flashcard 10
**Term:** Identifying Relationship
**Definition:** A relationship where the child entity is weak and is identified by combining its partial key with the parent's primary key.
---

#### Flashcard 11
**Term:** Domain Constraint
**Definition:** Rules that define the permissible values for an attribute, including data type, format, and range.
---

#### Flashcard 12
**Term:** Alternate Key
**Definition:** A candidate key that is not selected as the primary key but still enforces uniqueness.
---

### Short Answer Questions

1. **Explain the difference between CASCADE and SET NULL with practical examples.**

2. **Why is entity integrity important in relational databases?**

3. **How would you implement a many-to-many relationship in SQL? Explain with an example.**

4. **What are the different types of keys in DBMS? Explain with examples.**

5. **Differentiate between total participation and partial participation with ER diagram examples.**

6. **What is a weak entity? How does it differ from a regular entity?**

7. **Explain the concept of referential integrity with the help of an example.**

8. **How do CHECK constraints differ from other constraints?**

9. **What are the various cardinalities in relationships? Explain each with an example.**

10. **Discuss the importance of constraints in maintaining database integrity.**

---

## Conclusion

This comprehensive study material covers all aspects of **Constraints On Relationships** as required for the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF curriculum. The content provides:

- ✅ Detailed explanations of all constraint types
- ✅ Real-world examples with SQL code
- ✅ Coverage of domain, key, entity integrity, referential integrity, participation, cardinality, and CHECK constraints
- ✅ Update/delete rules (CASCADE, SET NULL, NO ACTION)
- ✅ Weak entities and identifying relationships
- ✅ 15 MCQs (easy, medium, and hard levels)
- ✅ 12 flashcards for quick revision
- ✅ 10 short answer questions for practice

**Word Count:** ~2,800 words