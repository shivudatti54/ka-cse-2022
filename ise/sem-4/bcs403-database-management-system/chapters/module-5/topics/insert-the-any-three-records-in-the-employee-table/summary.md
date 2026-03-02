# **Database Management System Revision Notes**

## **Topic: Inserting Records into the Employee Table**

### Key Points

- **Employee Table**: A relational database schema that stores information about employees.
  - Attributes:
    - EMPNO: Employee number
    - ENAME: Employee name
    - JOB: Job title
    - MANAGER_NO: Manager's employee number
    - SAL: Salary
    - COMMISSION: Commission amount
- **Insert Statement**: Used to add new records to a database table.
  - Syntax: `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`
- **Rollback**: A database transaction that can be undone in case of errors or inconsistencies.
  - Used with `INSERT` statements to ensure data integrity.

### Important Formulas and Definitions

- **Primary Key (PK)**: A unique identifier for each record in a table.
- **Foreign Key (FK)**: A field that references the primary key of another table.
- **Referential Integrity**: Ensures that data in one table is consistent with data in another table.

### Important Theorems

- **ACID Properties**: Ensures that database transactions are processed reliably and securely.
  - Atomicity: Ensures that transactions are treated as a single, indivisible unit.
  - Consistency: Ensures that data remains consistent throughout the transaction.
  - Isolation: Ensures that transactions do not interfere with each other.
  - Durability: Ensures that once a transaction is committed, its effects are permanent.

### Revision Tips

- Practice writing `INSERT` statements to insert records into the Employee table.
- Understand the importance of rollback in ensuring data integrity.
- Review the ACID properties to ensure reliable database transactions.
