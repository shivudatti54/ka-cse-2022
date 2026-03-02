# Employee (EMPNO)

**Definition:** A unique identifier for an employee in a database.

**Key Points:**

- **Data Type:** Typically an integer or a character string (e.g., VARCHAR2)
- **Purpose:** To uniquely identify each employee in the database
- **Length:** Varies depending on the database system (e.g., 6 digits in Oracle)
- **Nullability:** Can be nullable (if no employee data exists)
- **Primary Key:** Often used as a primary key in employee tables

**Formulas:**

- None specific to EMPNO, but used in conjunction with other employee data (e.g., salary, department)

**Theorems:**

- **Normalization Theorem:** EMPNO should be a unique identifier for each employee to ensure data integrity
- **Referential Integrity Theorem:** EMPNO should be used as a foreign key to link to the employee table

**Important Concepts:**

- **Primary Key:** A unique identifier for each record in a table
- **Foreign Key:** A field that links to the primary key of another table
- **Data Integrity:** The accuracy and consistency of data in a database

**Revision Tips:**

- EMPNO is a unique identifier for each employee
- EMPNO is often used as a primary key or foreign key
- EMPNO is used to ensure data integrity in employee tables
