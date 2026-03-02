# DDL: CREATE TABLE & Constraints
## Database Management Systems (Delhi University - NEP 2024 UGCF)

### Introduction
Data Definition Language (DDL) is a subset of SQL used to define and manage database structures. The CREATE TABLE statement is fundamental for establishing the schema, while constraints enforce data integrity rules at the table level.

---

### Key Concepts

**DDL Commands Overview**
- **CREATE**: Used to create database objects (tables, indexes, views)
- **ALTER**: Modifies existing table structures
- **DROP**: Deletes database objects permanently
- **TRUNCATE**: Removes all rows from a table

**CREATE TABLE Syntax**
```sql
CREATE TABLE table_name (
    column_name data_type [constraints],
    ...
);
```

**Table Constraints (Primary Constraints)**

- **PRIMARY KEY**: Uniquely identifies each row; only one per table; automatically enforces NOT NULL
  ```sql
  PRIMARY KEY (column_name)
  ```

- **FOREIGN KEY**: Establishes relationship between tables; references PRIMARY KEY of another table
  ```sql
  FOREIGN KEY (column_name) REFERENCES parent_table(column)
  ```

- **UNIQUE**: Ensures all values in a column are distinct (multiple allowed per table)

- **NOT NULL**: Prevents NULL values in a column (mandatory field)

- **CHECK**: Validates that values satisfy a specific condition
  ```sql
  CHECK (column_name >= 0)
  ```

- **DEFAULT**: Provides a default value when no value is specified

**Constraint Levels**
- **Column-level**: Applied to single column within column definition
- **Table-level**: Applied across multiple columns; defined after all columns

**ALTER TABLE Operations**
- ADD/DROP/MODIFY columns
- ADD/DROP constraints
- RENAME table

---

### Important Notes for Exam
- Constraints are automatically enforced by the DBMS
- Referential integrity is maintained through FOREIGN KEY
- CASCADE option propagates changes across related tables
- Constraints can be named for easier management

---

### Conclusion
DDL commands and constraints form the foundation of database design. Understanding CREATE TABLE with various constraints is essential for implementing data integrity and relationships in relational database systems, a core topic in Delhi University BSc (Hons) CS syllabus.