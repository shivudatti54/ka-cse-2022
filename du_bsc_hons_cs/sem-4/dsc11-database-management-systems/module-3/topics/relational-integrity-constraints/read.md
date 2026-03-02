# Relational Integrity Constraints

## Introduction

Relational Integrity Constraints are the backbone of any well-designed relational database management system. These constraints define the rules and conditions that must be satisfied by the data stored in a database, ensuring data accuracy, consistency, and reliability throughout the database's lifecycle. In the context of the University of Delhi's Computer Science program, understanding integrity constraints is fundamental to mastering database design and implementation.

In real-world applications, databases often contain millions of records accessed by multiple users simultaneously. Without proper integrity constraints, data can become corrupted, inconsistent, or meaningless. For example, consider a university database where a student record references a non-existent department, or where the same student is enrolled twice with conflicting grades. Such anomalies can lead to erroneous results in academic reporting, financial calculations, and administrative decisions. Integrity constraints prevent these problems by enforcing business rules at the database level, making them an essential component of any enterprise application.

The relational model, pioneered by E.F. Codd in 1970, provides a theoretical foundation for maintaining database integrity through various types of constraints. These constraints operate at different levels—from individual column values to relationships between tables—and form the basis for what is commonly referred to as "data integrity." For DU students preparing for semester examinations, a thorough understanding of these constraints is crucial, as they frequently appear in both theoretical questions and practical SQL implementations.

## Key Concepts

### 1. Domain Constraints

Domain constraints define the set of permissible values for an attribute (column) in a relation. Each attribute must belong to a specific domain, which specifies its data type and valid range. Domain constraints ensure that only meaningful data enters the database.

A domain is characterized by:
- **Data Type**: Integer, varchar, date, float, boolean, etc.
- **Format**: Specific patterns or formats (e.g., phone numbers, email addresses)
- **Range**: Minimum and maximum acceptable values
- **Constraints**: Additional rules like NOT NULL, UNIQUE

For instance, a student's age attribute might have a domain of integers between 15 and 100, while a grade attribute might be restricted to values 'A', 'B', 'C', 'D', or 'F'. SQL implements domain constraints through CHECK constraints and user-defined data types.

### 2. Key Constraints

Key constraints are fundamental to the relational model and ensure entity integrity—the uniqueness of records within a relation.

**Candidate Key**: An attribute or set of attributes that uniquely identifies each tuple in a relation. A relation can have multiple candidate keys. For example, in a Student relation, both RegistrationNumber and EmailID could be candidate keys.

**Primary Key**: The candidate key selected to uniquely identify records in a relation. A primary key must have unique, non-null values. For example, StudentID is commonly used as the primary key in a Students table.

**Composite Key**: A candidate key consisting of two or more attributes. For example, in an Enrollment relation, the combination of (StudentID, CourseID) might form the primary key, as a student can enroll in multiple courses.

**Foreign Key**: An attribute in one relation that references the primary key of another relation. Foreign keys establish referential integrity between tables. For example, DeptID in a Faculty table references the primary key of a Department table.

**Superkey**: A set of attributes that uniquely identifies tuples. Every relation has at least one superkey (the set of all attributes). Primary keys and candidate keys are special types of superkeys.

### 3. Entity Integrity Constraint

The entity integrity constraint states that no primary key value can be NULL. This ensures that each record in a relation can be uniquely identified. Since primary keys uniquely identify rows, they cannot contain null values—otherwise, we would have no way to distinguish between different rows.

The entity integrity rule can be formally stated as: For every tuple in a base relation, the primary key attribute(s) must have a non-null value. This constraint is enforced by the database system automatically when a primary key is defined.

### 4. Referential Integrity Constraint

Referential integrity ensures that relationships between tables remain consistent. It requires that every foreign key value must either match a primary key value in the referenced table or be NULL (if allowed).

Formally: If relation R1 has a foreign key FK that references the primary key of relation R2, then every non-null value of FK in R1 must equal some primary key value in R2.

**Referential Actions**: When a referenced row is deleted or its primary key is updated, the database must specify how to handle dependent rows:

- **RESTRICT**: Prevents deletion/update if dependent rows exist
- **CASCADE**: Automatically deletes/updates dependent rows
- **SET NULL**: Sets foreign key values to NULL
- **SET DEFAULT**: Sets foreign key values to their default values
- **NO ACTION**: Similar to RESTRICT but checked after attempting the operation

### 5. Null Constraints

Null constraints specify whether an attribute can contain NULL values. A NULL value represents missing or unknown information, distinct from zero or empty string. The NOT NULL constraint ensures that a column must have a value—essential for critical fields like primary keys or mandatory attributes.

### 6. Check Constraints

Check constraints allow users to define custom conditions that must be satisfied by data in a column or row. The condition must evaluate to TRUE for the operation to succeed. For example: `CHECK (Age >= 18)` ensures only adults are stored, or `CHECK (Gender IN ('M', 'F', 'Other'))` restricts gender to valid values.

### 7. Assertion Constraints

Assertions are table-level or database-level constraints that involve multiple tables. Unlike column-level CHECK constraints, assertions are defined separately and can enforce complex business rules. For example, an assertion might ensure that no student can enroll in more than six courses in a semester.

### 8. Trigger-Based Integrity

Triggers are database objects that automatically execute in response to certain events (INSERT, UPDATE, DELETE). While not pure integrity constraints, triggers can enforce complex business rules that cannot be expressed through other constraint types. For instance, automatically updating a student's CGPA when new grades are entered.

## Examples

### Example 1: Creating Tables with Multiple Constraints

Consider a university database with three tables: Departments, Faculty, and Courses.

```sql
-- Departments Table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL UNIQUE,
    Location VARCHAR(30) DEFAULT 'Delhi'
);

-- Faculty Table
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY,
    FacultyName VARCHAR(100) NOT NULL,
    DeptID INT NOT NULL,
    Salary DECIMAL(10,2) CHECK (Salary > 0),
    JoinDate DATE,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Courses Table
CREATE TABLE Courses (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(50) NOT NULL,
    Credits INT CHECK (Credits BETWEEN 1 AND 6),
    DeptID INT,
    InstructorID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (InstructorID) REFERENCES Faculty(FacultyID)
        ON DELETE SET NULL ON UPDATE CASCADE
);
```

In this example:
- Entity integrity: Primary keys (DeptID, FacultyID, CourseID) cannot be NULL
- Referential integrity: Foreign keys ensure DeptID references valid Departments
- Domain constraints: Salary must be positive, Credits between 1 and 6
- Null constraint: Faculty.DeptID is NOT NULL
- Unique constraint: DeptName must be unique

### Example 2: Violating and Maintaining Referential Integrity

```sql
-- Attempting to insert a faculty member for a non-existent department
INSERT INTO Faculty VALUES (101, 'Dr. Sharma', 99, 75000, '2020-01-15');
-- This will fail because DeptID=99 does not exist in Departments

-- Correct approach: First insert the department
INSERT INTO Departments VALUES (10, 'Computer Science', 'Building A');

-- Now the faculty insertion succeeds
INSERT INTO Faculty VALUES (101, 'Dr. Sharma', 10, 75000, '2020-01-15');

-- Deleting a department with CASCADE delete
DELETE FROM Departments WHERE DeptID = 10;
-- All faculty in DeptID=10 will also be deleted automatically
```

### Example 3: Complex Check Constraint

```sql
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT NOT NULL,
    CourseID VARCHAR(10) NOT NULL,
    EnrollmentDate DATE DEFAULT CURRENT_DATE,
    Grade CHAR(1),
    CHECK (Grade IS NULL OR Grade IN ('A', 'B', 'C', 'D', 'E', 'F')),
    CHECK (EnrollmentDate <= CURRENT_DATE),
    UNIQUE (StudentID, CourseID)  -- A student cannot enroll in the same course twice
);
```

This table enforces:
- Grade must be NULL or one of the valid letter grades
- Enrollment date cannot be in the future
- Composite uniqueness: Each student can enroll in each course only once

## Exam Tips

1. **Remember the three fundamental integrity constraints**: Entity integrity (primary key cannot be NULL), Referential integrity (foreign key must match or be NULL), and Domain integrity (values must be from valid domains).

2. **Difference between DELETE and DROP**: DELETE removes tuples (rows) and triggers referential actions; DROP removes the entire table structure.

3. **Foreign key actions in order of evaluation**: RESTRICT and NO ACTION prevent the operation if dependent rows exist. CASCADE propagates changes. SET NULL requires the foreign key column to allow NULL values.

4. **Primary key vs. Unique key**: Primary key enforces entity integrity (one per table, cannot be NULL), while unique key ensures distinct values but can have NULL values (except in some DBMS implementations).

5. **Composite keys**: Remember that all attributes in a composite key must be non-NULL for entity integrity to hold, as the entire combination identifies the tuple.

6. **CHECK constraint behavior**: A CHECK constraint passes if the condition evaluates to TRUE or UNKNOWN (NULL); it only fails when the condition is FALSE.

7. **Real-world example preparation**: Be ready to analyze scenarios like "In a hospital database, how would you ensure a patient is assigned to an existing ward?" This tests referential integrity understanding.

8. **SQL syntax mastery**: Know how to add constraints using ALTER TABLE (ADD CONSTRAINT) and how to name constraints for better error identification.

9. **Difference between assertion and trigger**: Assertions are checked at statement level and are declarative; triggers are procedural and fire before/after events.

10. **NULL handling**: Remember that NULL = NULL evaluates to UNKNOWN, not TRUE. This affects how constraints and queries handle NULL values.