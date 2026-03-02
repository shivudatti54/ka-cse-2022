# **Database Management System Study Material: Ch 7.1 to 7.3**

## **Module: 8 Hours**

### Overview

In this module, we will cover the following topics:

- Data Definition Language (DDL)
- Data Control Language (DCL)
- Data Manipulation Language (DML)
- Data Query Language (DQL)

### 7.1: Data Definition Language (DDL)

**Definition:** Data Definition Language (DDL) is a set of commands used to define the structure of a database.

**Types of DDL Commands:**

- **CREATE**: Used to create a new database, table, or index.
- **ALTER**: Used to modify the structure of a database, table, or index.
- **DROP**: Used to drop a database, table, or index.
- **TRUNCATE**: Used to truncate a table, deleting all of its rows.

**Example DDL Commands:**

- `CREATE TABLE customers (id INT PRIMARY KEY, name VARCHAR(255));`
- `ALTER TABLE customers ADD COLUMN email VARCHAR(255);`
- `DROP TABLE customers;`
- `TRUNCATE TABLE customers;`

**Key Concepts:**

- **Primary Key (PK)**: A unique identifier for each record in a table.
- **Foreign Key (FK)**: A field in a table that references the primary key of another table.
- **Index**: A data structure that improves the speed of data retrieval.

### 7.2: Data Control Language (DCL)

**Definition:** Data Control Language (DCL) is a set of commands used to control access to a database.

**Types of DCL Commands:**

- **GRANT**: Used to grant privileges to users.
- **REVOKE**: Used to revoke privileges from users.
- **CREATE ROLE**: Used to create a new role.
- **ALTER ROLE**: Used to modify the privileges of a role.

**Example DCL Commands:**

- `GRANT SELECT ON customers TO user1;`
- `REVOKE SELECT ON customers FROM user1;`
- `CREATE ROLE admin;`
- `ALTER ROLE admin ADD PRIVILEGE SELECT ON customers;`

**Key Concepts:**

- **Privileges**: Special permissions granted to users, such as SELECT, INSERT, UPDATE, and DELETE.
- **Roles**: Groups of users with specific privileges.

### 7.3: Data Manipulation Language (DML)

**Definition:** Data Manipulation Language (DML) is a set of commands used to modify the data in a database.

**Types of DML Commands:**

- **INSERT**: Used to add new records to a table.
- **UPDATE**: Used to modify existing records in a table.
- **DELETE**: Used to delete records from a table.

**Example DML Commands:**

- `INSERT INTO customers (id, name, email) VALUES (1, 'John Doe', 'john.doe@example.com');`
- `UPDATE customers SET name = 'Jane Doe' WHERE id = 1;`
- `DELETE FROM customers WHERE id = 1;`

**Key Concepts:**

- **Primary Key (PK)**: A unique identifier for each record in a table.
- **Foreign Key (FK)**: A field in a table that references the primary key of another table.
- **Constraints**: Rules that enforce data consistency, such as primary keys and foreign keys.

### Conclusion

In this module, we covered the fundamental concepts of DDL, DCL, and DML, which are essential for managing a database. We learned how to define database structures, control access to data, and manipulate data using these powerful commands. By mastering these concepts, you will be well-equipped to design, implement, and maintain a database system.
