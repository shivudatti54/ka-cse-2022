# Relational Model Constraints and Relational Database Schemas

## Introduction

The relational model's power lies not just in its simple tabular structure but in its ability to maintain **data integrity** and **consistency**. This is achieved through a set of rules called **constraints**. These constraints are applied to a **relational database schema**, which is the logical blueprint of the entire database. Understanding these concepts is fundamental to designing robust and error-free databases.

## Core Concepts

### 1. Relational Database Schema

A relational database schema is the logical structure of the database. It defines:
*   **Relations:** The tables (e.g., `Student`, `Course`).
*   **Attributes:** The columns within each table (e.g., `USN`, `Name`, `Course_Code`).
*   **Domains:** The set of allowable values for each attribute (e.g., the `Grade` attribute's domain might be `{A, B, C, D, F}`).
*   **Constraints:** The rules that the data must always satisfy.

A **database instance** is a snapshot of the data in the database at a given moment. The schema remains constant, while the instance changes every time data is inserted, updated, or deleted.

### 2. Relational Model Constraints

Constraints are conditions that must hold true for any valid database instance. They are primarily used to prevent invalid data from being entered into the database, thus enforcing business rules and data correctness.

#### Key Constraints

These are the most critical integrity constraints.

*   **Domain Constraint:** Specifies that the value of each attribute must be an **atomic value** (indivisible) from its declared domain.
    *   *Example:* The `Age` attribute of a `Student` table must be a positive integer. The value `-25` or `"twenty"` would violate this constraint.

*   **Key Constraint:** A **superkey** is a set of one or more attributes that uniquely identifies a tuple in a relation. A **candidate key** is a minimal superkey (no subset of it is a superkey). The **primary key** is the candidate key chosen by the database designer to uniquely identify tuples.
    *   *Example:* In a `Student` table, `USN` is a natural primary key. The combination of `Name` and `Phone_Number` could be a candidate key, but it's less reliable than `USN`.

*   **Entity Integrity Constraint:** States that no primary key attribute can be **NULL**. This ensures that every tuple is uniquely identifiable.
    *   *Example:* A `Student` tuple cannot be inserted if its `USN` value is NULL.

*   **Referential Integrity Constraint:** This defines relationships between tables. It requires that a **foreign key** value in one relation must either match a primary key value in another relation or be entirely NULL.
    *   A **foreign key** is an attribute (or set of attributes) in one table that references the primary key of another table.
    *   *Example:* An `Enrollment` table has a `Course_Code` attribute. This is a foreign key that references the `Course_Code` primary key in the `Course` table. You cannot enroll a student in a course (`CSE101`) that does not exist in the `Course` table. This preserves the integrity of the relationship between `Enrollment` and `Course`.

#### Other Important Constraints

*   **Semantic Integrity Constraints (Business Rules):** These are application-specific rules that go beyond the built-in key and referential constraints. They are often enforced using `CHECK` clauses and triggers.
    *   *Example:* "A student's CGPA must be between 0 and 10." This can be implemented as a `CHECK (CGPA >= 0 AND CGPA <= 10)` constraint on the `Student` table.

## Example Scenario

Let's define schemas for two relations with constraints:

**Schema: `Course`**
*   `Course_Code` VARCHAR(10) **PRIMARY KEY**
*   `Title` VARCHAR(50) **NOT NULL**
*   `Credits` INT **CHECK (Credits > 0)**

**Schema: `Enrollment`**
*   `USN` VARCHAR(15) **NOT NULL**
*   `Course_Code` VARCHAR(10) **FOREIGN KEY REFERENCES Course(Course_Code)**
*   `Sem` INT
*   **PRIMARY KEY (USN, Course_Code)** -- Composite primary key

**Valid Instance:**
`Course`: (`'CSE101'`, `'DBMS'`, `4`)
`Enrollment`: (`'01VTU123'`, `'CSE101'`, `3`) -- **Valid:** `CSE101` exists in `Course`.

**Invalid Instance:**
`Enrollment`: (`'01VTU123'`, `'ECE205'`, `4`) -- **Invalid:** Violates **Referential Integrity** because `'ECE205'` does not exist in the `Course` table. The DBMS will reject this insertion.

## Key Points / Summary

*   **Relational Schema:** The logical blueprint (`intension`) of the database, defining relations, attributes, domains, and constraints.
*   **Database Instance:** The actual data (`extension`) stored in the database at a specific time.
*   **Constraints:** Rules enforced to maintain data integrity and consistency.
*   **Domain Constraint:** Ensures attribute values are atomic and from a predefined set.
*   **Key Constraint:** Ensures unique identification of tuples via primary keys.
*   **Entity Integrity:** Ensures the primary key value is never `NULL`.
*   **Referential Integrity:** Ensures a valid relationship between tables through foreign keys, preventing orphaned records.
*   These constraints are **automatically enforced** by the DBMS, shielding users and applications from underlying data inconsistencies.