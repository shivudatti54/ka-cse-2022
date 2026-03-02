# **Specifying Constraints as Assertions and Action Triggers**

**Definitions:**

- **Assertion**: A declarative statement that specifies a constraint on the database.
- **Action Trigger**: A procedural statement that specifies an action to be performed when a constraint is violated.

**Key Points:**

- **Types of Constraints:**
  - **Referential Integrity Constraint**: Ensures referential integrity between tables.
  - **Unique Constraint**: Ensures uniqueness of values in a column.
  - **Primary Key Constraint**: Ensures uniqueness and integrity of a column.
  - **Foreign Key Constraint**: Ensures referential integrity between tables.
- **Syntax:**
  - `ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_type (column1, column2);`
  - `ALTER TABLE table_name DROP CONSTRAINT constraint_name;`
- **Assertions:**
  - Example: `ASSERT that column1 = column2;`
- **Action Triggers:**
  - Example: `WHEN NOT EXISTS (SELECT 1 FROM table2 WHERE column2 = 'value') THEN INSERT INTO table1 (column1, column2);`

**Important Formulas and Theorems:**

- **Data Integrity Theorem**: If a constraint is not enforced, the data may become inconsistent.

**Revision Tips:**

- Understand the difference between assertions and action triggers.
- Know the syntax for specifying constraints.
- Be able to identify and create assertions and action triggers.
- Understand the importance of data integrity.
