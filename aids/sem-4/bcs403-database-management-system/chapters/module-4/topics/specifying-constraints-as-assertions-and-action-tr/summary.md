# **Specifying Constraints as Assertions and Action Triggers**

### Overview

Constraints in a database management system are used to enforce data integrity and relationships between tables. Specifying constraints as assertions and action triggers is a crucial aspect of database design.

### Key Points

- **Assertions**: A declarative statement that specifies the desired state of the database.
- **Action Triggers**: A procedural statement that executes when a constraint is violated.
- **Types of Constraints**:
  - **Primary Key (PK)**: Unique identifier for each record.
  - **Foreign Key (FK)**: Reference to a primary key in another table.
  - **Unique (UN)**: No duplicate values allowed.
  - **Check (CK)**: Enforces a specific condition for each record.
  - **Default (DF)**: Assigns a default value to a field if no value is provided.
  - **NotNull (NN)**: Fields cannot be null.
- **Constraints as Assertions**:
  - **Example**: ASSERT (emp_id INT, PRIMARY KEY); specifies that employee_id must be unique and serve as a primary key.
- **Constraints as Action Triggers**:
  - **Example**: WHEN NOT EXISTS (SELECT 1 FROM employees WHERE employee_id = NEW.emp_id); BEFORE INSERT ON employees FOR EACH ROW;
    - checks if the employee_id already exists in the employees table before inserting a new record.
- **SQL Formula**:
  - `CREATE TABLE employees (emp_id INT PRIMARY KEY, name VARCHAR(255) NOT NULL);`

### Important Formulas, Definitions, and Theorems

- **Inclusion-Exclusion Principle**: Used to calculate the total number of tuples in a database.
- **Normalization Theorem**: States that third-normal form is a necessary condition for a database to be in first-normal form.

### Quick Revision Tips

- Understand the difference between assertions and action triggers.
- Familiarize yourself with common constraints (PK, FK, UN, CK, DF, NN).
- Practice specifying constraints as assertions and action triggers.
