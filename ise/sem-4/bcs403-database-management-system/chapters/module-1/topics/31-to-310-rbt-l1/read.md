# **DATABASE MANAGEMENT SYSTEM**

**Module:** No. of Hours: 8
**Topic:** RBT: L1 (3.1 to 3.10)

## **Table of Contents**

1. [3.1: Data Management](#31-data-management)
2. [3.2: Database Design](#32-database-design)
3. [3.3: Database Implementation](#33-database-implementation)
4. [3.4: Database Administration](#34-database-administration)
5. [3.5: Data Security](#35-data-security)
6. [3.6: Database Normalization](#36-database-normalization)
7. [3.7: Data Integrity](#37-data-integrity)
8. [3.8: Transactions](#38-transactions)
9. [3.9: Concurrency Control](#39-concurrency-control)
10. [3.10: Data Recovery](#30-data-recovery)

### 3.1: Data Management

**Definition:** Data management refers to the process of planning, organizing, and maintaining the data in a database.

**Key Concepts:**

- **Data Management Life Cycle**: The stages of data management include data definition, data development, data implementation, data maintenance, and data evaluation.
- **Data Definition Language (DDL)**: A language used to define the structure of a database.
- **Data Control Language (DCL)**: A language used to control access to a database.

**Example:**
A company may have a database that stores information about its customers. The data management process would include defining the structure of the database, developing the database schema, implementing the database, maintaining the database, and evaluating the effectiveness of the database.

### 3.2: Database Design

**Definition:** Database design refers to the process of creating a conceptual and logical model of a database.

**Key Concepts:**

- **Entity Relationship Model (ERM)**: A model that represents the relationships between entities in a database.
- **Normalization**: The process of organizing the data in a database to minimize data redundancy and improve data integrity.
- **Denormalization**: The process of organizing the data in a database to improve data retrieval efficiency.

**Example:**
A university may have a database that stores information about its students. A database design would include creating an entity relationship model to represent the relationships between students, courses, and grades.

### 3.3: Database Implementation

**Definition:** Database implementation refers to the process of creating a physical database from a conceptual and logical model.

**Key Concepts:**

- **Database System**: A system that provides a set of tools and facilities for defining, implementing, and managing a database.
- **Database Management System (DBMS)**: A software system that manages a database.
- **Database Engine**: The component of a DBMS that executes SQL commands.

**Example:**
A company may have a database that stores information about its products. The database implementation process would include creating a database system and DBMS, and designing the database engine.

### 3.4: Database Administration

**Definition:** Database administration refers to the process of managing and maintaining a database.

**Key Concepts:**

- **Database Administrator (DBA)**: A person responsible for managing and maintaining a database.
- **Database Security**: The process of protecting a database from unauthorized access.
- **Backup and Recovery**: The process of creating backups of a database and recovering the database in case of failure.

**Example:**
A university may have a database that stores information about its students. A database administrator would be responsible for managing and maintaining the database, ensuring database security, and creating backups and recovering the database in case of failure.

### 3.5: Data Security

**Definition:** Data security refers to the process of protecting a database from unauthorized access.

**Key Concepts:**

- **Access Control**: The process of controlling who has access to a database.
- **Authentication**: The process of verifying the identity of a user.
- **Authorization**: The process of granting access to a database based on a user's identity.

**Example:**
A company may have a database that stores sensitive financial information. A data security strategy would include implementing access control, authentication, and authorization to protect the database from unauthorized access.

### 3.6: Database Normalization

**Definition:** Database normalization refers to the process of organizing the data in a database to minimize data redundancy and improve data integrity.

**Key Concepts:**

- **First Normal Form (1NF)**: A normalization rule that states that each table cell must contain a single value.
- **Second Normal Form (2NF)**: A normalization rule that states that each non-key attribute in a table must depend on the entire primary key.
- **Third Normal Form (3NF)**: A normalization rule that states that if a table has a composite key, then each non-key attribute must depend on the entire key.

**Example:**
A university may have a database that stores information about its students. A database normalization process would include normalizing the database to minimize data redundancy and improve data integrity.

### 3.7: Data Integrity

**Definition:** Data integrity refers to the process of ensuring that the data in a database is accurate and consistent.

**Key Concepts:**

- **Validation**: The process of checking data to ensure that it meets the requirements of the database.
- **Constraints**: Rules that define the valid values for a column or a set of columns.
- **Triggers**: Events that occur when a row in a table is modified.

**Example:**
A company may have a database that stores information about its products. A data integrity strategy would include implementing validation, constraints, and triggers to ensure that the data in the database is accurate and consistent.

### 3.8: Transactions

**Definition:** Transactions refer to a sequence of operations that are executed as a single, all-or-nothing unit.

**Key Concepts:**

- **Atomicity**: The property that ensures that a transaction is executed as a single, all-or-nothing unit.
- **Consistency**: The property that ensures that the database remains in a consistent state after a transaction is executed.
- **Isolation**: The property that ensures that multiple transactions can occur concurrently without interfering with each other.

**Example:**
A university may have a database that stores information about its students. A transaction would include a series of operations, such as adding a new student, updating the student's grade, and saving the changes.

### 3.9: Concurrency Control

**Definition:** Concurrency control refers to the process of managing multiple transactions that occur concurrently.

**Key Concepts:**

- **Locking**: The process of acquiring exclusive access to a resource.
- **Timeouts**: The process of terminating a transaction if it takes too long to complete.
- **Rollback**: The process of reverting a transaction to its previous state.

**Example:**
A company may have a database that stores information about its products. A concurrency control strategy would include implementing locking, timeouts, and rollback to manage multiple transactions that occur concurrently.

### 3.10: Data Recovery

**Definition:** Data recovery refers to the process of restoring a database to its original state after a failure or disaster.

**Key Concepts:**

- **Backup and Restore**: The process of creating backups of a database and restoring it in case of failure.
- **Data Recovery Procedures**: Procedures that are used to recover data from a backup.
- **Data Archiving**: The process of storing data in a separate location for long-term preservation.

**Example:**
A university may have a database that stores information about its students. A data recovery strategy would include implementing backup and restore procedures to ensure that the database can be recovered in case of failure.
