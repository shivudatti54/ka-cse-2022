# Transaction Support in SQL

## Table of Contents

- [Transaction Support in SQL](#transaction-support-in-sql)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [ACID Properties of Transactions](#acid-properties-of-transactions)
  - [Transaction States](#transaction-states)
  - [SQL Transaction Control Statements](#sql-transaction-control-statements)
  - [Concurrency Control](#concurrency-control)
  - [Isolation Levels](#isolation-levels)
- [Examples](#examples)
  - [Example 1: Bank Fund Transfer with Transaction Management](#example-1-bank-fund-transfer-with-transaction-management)
  - [Example 2: Using Savepoints for Partial Rollback](#example-2-using-savepoints-for-partial-rollback)
  - [Example 3: Setting Transaction Isolation Level](#example-3-setting-transaction-isolation-level)
- [Exam Tips](#exam-tips)

## Introduction

A database transaction is a fundamental concept in Database Management Systems that represents a logical unit of work containing one or more SQL operations. Transactions ensure data integrity and consistency even when multiple users access the database concurrently. In real-world applications, operations rarely occur in isolation; consider a banking system where transferring money between accounts involves debiting one account and crediting another. Both operations must succeed together or fail together to maintain data consistency.

SQL provides robust transaction support through a set of control statements that enable developers to manage the atomicity, consistency, isolation, and durability (ACID) properties of database operations. Understanding transaction support in SQL is crucial for developing reliable database applications, particularly in systems where data integrity is paramount. This topic covers the theoretical foundations of transactions, the practical SQL commands for transaction control, and the various isolation levels that determine how concurrent transactions interact with each other.

## Key Concepts

### ACID Properties of Transactions

The ACID properties form the foundation of reliable transaction processing:

1. **Atomicity**: This property ensures that a transaction is treated as a single atomic unit of work. Either all operations within a transaction are successfully completed and applied to the database, or none of them are applied. If any operation fails, the entire transaction is rolled back, leaving the database in its original state. For example, in a fund transfer, both debit and credit operations must complete successfully.

2. **Consistency**: A transaction must transform the database from one consistent state to another consistent state. All integrity constraints, triggers, and business rules must be satisfied after the transaction completes. If a transaction violates any constraint, it should be rolled back entirely.

3. **Isolation**: This property ensures that concurrent transactions appear to execute serially, one after another. The intermediate state of one transaction is not visible to other transactions until the transaction commits. Isolation prevents interference between concurrent transactions.

4. **Durability**: Once a transaction commits, its effects must persist permanently in the database, even in the case of system failure. This is typically achieved through write-ahead logging and recovery mechanisms.

### Transaction States

A transaction can exist in several states throughout its lifecycle:

- **Active**: The transaction is currently being executed, and SQL statements are being processed.
- **Partially Committed**: All statements have been executed, but the transaction has not yet been committed.
- **Committed**: The transaction has been successfully completed, and all changes are permanently saved in the database.
- **Failed**: The transaction cannot proceed further due to an error or user intervention.
- **Aborted**: After failure, the transaction is rolled back, and the database returns to its consistent state.

### SQL Transaction Control Statements

SQL provides three primary commands for transaction control:

**COMMIT**: The COMMIT statement permanently saves all changes made during the current transaction to the database. After committing, the transaction ends, and a new transaction begins automatically. All locks held by the transaction are released.

```sql
-- Example: Committing a transaction
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance - 5000
WHERE AccountID = 'ACC001';
UPDATE Accounts SET Balance = Balance + 5000
WHERE AccountID = 'ACC002';
COMMIT;
```

**ROLLBACK**: The ROLLBACK statement undoes all changes made since the beginning of the current transaction or since the last SAVEPOINT. It restores the database to its state before the transaction started.

```sql
-- Example: Rolling back a transaction
BEGIN TRANSACTION;
INSERT INTO Employees (ID, Name, Salary)
VALUES (101, 'John Doe', 50000);
-- Something went wrong
ROLLBACK;
-- Database remains unchanged
```

**SAVEPOINT**: Savepoints allow creating intermediate points within a transaction to which you can partially rollback without losing the entire transaction.

```sql
-- Example: Using savepoints
BEGIN TRANSACTION;
INSERT INTO Orders (OrderID, CustomerID)
VALUES (1001, 'C001');
SAVEPOINT OrderInserted;

INSERT INTO OrderItems (OrderID, ProductID, Quantity)
VALUES (1001, 'P001', 5);
-- If something fails here
ROLLBACK TO SAVEPOINT OrderInserted;

-- Continue with other operations
COMMIT;
```

### Concurrency Control

When multiple transactions execute simultaneously, concurrency control mechanisms ensure that the ACID properties are maintained. The two primary approaches are:

**Locking**: Locks are mechanisms that prevent concurrent transactions from accessing the same data item simultaneously.

- **Shared Lock (S)**: Allows reading data but not writing
- **Exclusive Lock (X)**: Allows both reading and writing

**Timestamp-Based Ordering**: Each transaction receives a timestamp, and operations are scheduled based on these timestamps to ensure serializability.

### Isolation Levels

SQL defines four standard isolation levels that determine how transactions interact:

1. **READ UNCOMMITTED**: The lowest isolation level where transactions can read uncommitted data from other transactions. This can lead to dirty reads, non-repeatable reads, and phantom reads.

2. **READ COMMITTED**: Transactions can only read committed data. This prevents dirty reads but may allow non-repeatable reads (same query returning different results within the same transaction).

3. **REPEATABLE READ**: Ensures that if a transaction reads data, it will see the same data if it reads again. Prevents dirty reads and non-repeatable reads but may allow phantom reads.

4. **SERIALIZABLE**: The highest isolation level ensures that transactions execute as if they were running sequentially. Prevents all concurrency problems but may reduce concurrency significantly.

```sql
-- Setting isolation level in SQL
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

## Examples

### Example 1: Bank Fund Transfer with Transaction Management

Consider a banking scenario where we need to transfer ₹10,000 from account A1001 to account A1002.

**Initial State:**

- Account A1001: Balance = ₹50,000
- Account A1002: Balance = ₹25,000

**Transaction Implementation:**

```sql
BEGIN TRANSACTION;

-- Step 1: Debit from source account
UPDATE Accounts
SET Balance = Balance - 10000
WHERE AccountID = 'A1001';

-- Step 2: Credit to destination account
UPDATE Accounts
SET Balance = Balance + 10000
WHERE AccountID = 'A1002';

-- Step 3: Check if both operations succeeded
IF @@ERROR = 0
 COMMIT;
ELSE
 ROLLBACK;
```

**After Successful Commit:**

- Account A1001: Balance = ₹40,000
- Account A1002: Balance = ₹35,000

If any UPDATE fails (e.g., insufficient funds), the ROLLBACK ensures neither account is modified, maintaining data integrity.

### Example 2: Using Savepoints for Partial Rollback

A university registration system where we need to register a student for a course, but if course capacity is full, we want to save the student information:

```sql
BEGIN TRANSACTION;

-- Insert student information
INSERT INTO Students (StudentID, Name, Email)
VALUES ('S105', 'Alice Smith', 'alice@example.com');
SAVEPOINT StudentInserted;

-- Attempt to enroll in a course
INSERT INTO Enrollments (StudentID, CourseID, Semester)
VALUES ('S105', 'CS301', 'Fall2024');

-- Check if enrollment failed (capacity full)
IF @@ERROR <> 0
BEGIN
 -- Rollback only the enrollment, keep student data
 ROLLBACK TO SAVEPOINT StudentInserted;
 PRINT 'Course full. Student registered but not enrolled.';
END

COMMIT;
```

### Example 3: Setting Transaction Isolation Level

A reporting application that requires consistent reads across multiple queries:

```sql
-- Set isolation level for the transaction
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

BEGIN TRANSACTION;

-- First query
SELECT COUNT(*) FROM Orders
WHERE OrderDate = '2024-01-15';
-- Returns: 150

-- Another transaction inserts new orders
-- With REPEATABLE READ, this won't affect our transaction

-- Second query (will return same count)
SELECT COUNT(*) FROM Orders
WHERE OrderDate = '2024-01-15';
-- Still returns: 150

COMMIT;
```

## Exam Tips

1. **Remember ACID Properties**: In exams, always associate Atomicity with "all or nothing," Consistency with "valid state," Isolation with "concurrent execution appears serial," and Durability with "permanent changes."

2. **COMMIT vs ROLLBACK**: COMMIT makes changes permanent and visible to other transactions, while ROLLBACK undoes all uncommitted changes.

3. **Savepoints are Transactional**: Remember that SAVEPOINT must be used within a transaction that has not been committed or rolled back.

4. **Isolation Levels Hierarchy**: Know the order from lowest to highest: READ UNCOMMITTED → READ COMMITTED → REPEATABLE READ → SERIALIZABLE.

5. **Phantom Reads**: Understand that phantom reads occur when new rows match the search condition during a transaction, typically prevented only at SERIALIZABLE level.

6. **Default Isolation Level**: Most database systems default to READ COMMITTED (e.g., SQL Server, PostgreSQL).

7. **Transaction in SQL Server**: Remember that in SQL Server, BEGIN TRANSACTION starts the transaction, while Oracle uses implicit BEGIN for the first DML statement.

8. **@@ERROR Variable**: In SQL Server, check @@ERROR immediately after each statement to detect failures, as it resets after each statement.
