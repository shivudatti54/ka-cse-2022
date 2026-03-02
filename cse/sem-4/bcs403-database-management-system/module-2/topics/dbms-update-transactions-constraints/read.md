# Update Operations, Transactions, and Dealing with Constraint Violations

## Table of Contents

- [Update Operations, Transactions, and Dealing with Constraint Violations](#update-operations-transactions-and-dealing-with-constraint-violations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Update Operations in Relational Database](#1-update-operations-in-relational-database)
  - [2. Transaction Concept](#2-transaction-concept)
  - [3. Constraint Violations and Handling](#3-constraint-violations-and-handling)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

Database Management Systems (DBMS) must not only store and retrieve data but also ensure data integrity and consistency at all times. The relational model provides a theoretical foundation for data manipulation through relational algebra, while the practical implementation involves **update operations** that modify the database state. These operations—INSERT, DELETE, and UPDATE—form the backbone of dynamic data management.

When executing these update operations, the DBMS must enforce **integrity constraints** defined in the database schema. However, constraint violations may occur during updates, and the system must handle them appropriately. Furthermore, to ensure atomicity and consistency even in the face of system failures, databases employ the concept of **transactions**—logical units of work that transform the database from one consistent state to another.

This topic explores three interrelated concepts: the mechanics of update operations in relational databases, the transaction concept with its ACID properties, and strategies for dealing with constraint violations during database modifications.

## Key Concepts

### 1. Update Operations in Relational Database

Update operations modify the content of database relations. The three fundamental update operations are:

**INSERT Operation**
The INSERT operation adds new tuples to a relation. The general syntax is:

```
INSERT INTO relation_name VALUES (value1, value2, ..., valuen)
```

or

```
INSERT INTO relation_name (column1, column2, ...) VALUES (value1, value2, ...)
```

The INSERT operation can also use a query to insert multiple tuples:

```
INSERT INTO relation_name SELECT ... FROM ...
```

**DELETE Operation**
The DELETE operation removes existing tuples from a relation based on a condition:

```
DELETE FROM relation_name WHERE condition
```

If no WHERE clause is specified, all tuples are deleted (emptying the relation).

**UPDATE (or MODIFY) Operation**
The UPDATE operation modifies values of one or more attributes in existing tuples:

```
UPDATE relation_name SET attribute = new_value WHERE condition
```

### 2. Transaction Concept

A **transaction** is a logical unit of work that consists of one or more database operations. It transforms the database from one consistent state to another. Transactions are essential for maintaining data integrity.

**ACID Properties of Transactions:**

1. **Atomicity**: A transaction is atomic—it either completes entirely or has no effect at all. If any operation fails, the entire transaction is rolled back.

2. **Consistency**: A transaction must preserve the database's consistency constraints. Upon completion, the database must be in a valid state satisfying all integrity constraints.

3. **Isolation**: Concurrent transactions appear to execute sequentially. Each transaction is unaware of other concurrent transactions.

4. **Durability**: Once a transaction commits, its effects are permanently stored in the database, even if system failure occurs.

**Transaction States:**

- **Active**: Transaction is being executed
- **Partially Committed**: Final operation has been executed, but commit not yet complete
- **Committed**: Transaction successfully completed
- **Aborted**: Transaction failed and is being rolled back
- **Terminated**: Transaction has ended (committed or aborted)

### 3. Constraint Violations and Handling

Integrity constraints define the rules that data must satisfy. During update operations, constraint violations may occur. The DBMS must handle these appropriately.

**Types of Constraints:**

1. **Key Constraints**: Primary key, unique key
2. **Referential Integrity**: Foreign key constraints
3. **Domain Constraints**: Attribute values must belong to the defined domain
4. **Check Constraints**: User-defined conditions
5. **Null Constraints**: NOT NULL specifications

**Handling Constraint Violations:**

For **INSERT violations**:

- Domain violation: Reject the insert with an error message
- Key violation (duplicate primary key): Reject the insert
- Referential integrity violation (invalid foreign key): Reject the insert or cascade update

For **DELETE violations**:

- When deleting a parent tuple with dependent child records: Reject, cascade, set to null, or set to default (based on referential action defined)

For **UPDATE violations**:

- Updating primary key: Check for duplicates, enforce constraints
- Updating foreign key: Verify referenced key exists
- Updating to violate check constraints: Reject the update

**Deferred vs. Immediate Constraint Checking:**

- **Immediate checking**: Constraints are checked after each operation
- **Deferred checking**: Constraints are checked only at transaction commit time

## Examples

**Example 1: INSERT Operation with Constraint Violation**

Consider a relation:

```
EMPLOYEE(EID: integer PRIMARY KEY, Name: varchar, Salary: integer CHECK Salary > 0, DeptID: integer)
```

Attempting to insert:

```sql
INSERT INTO EMPLOYEE VALUES (101, 'John', -5000, 10);
```

This violates the CHECK constraint (Salary > 0). The DBMS rejects this insert with an appropriate error message.

**Example 2: DELETE with Referential Integrity**

Consider relations:

```
DEPT(DID: integer PRIMARY KEY, DName: varchar)
EMP(EID: integer PRIMARY KEY, Name: varchar, DeptID: integer REFERENCES DEPT(DID))
```

When deleting a department:

```sql
DELETE FROM DEPT WHERE DID = 10;
```

Options for handling (defined in referential action):

- **NO ACTION**: Reject the delete if employees exist
- **CASCADE**: Also delete all employees in department 10
- **SET NULL**: Set DeptID to NULL for all employees in department 10
- **SET DEFAULT**: Set DeptID to default value

**Example 3: Transaction with Rollback**

```sql
BEGIN TRANSACTION;
 UPDATE ACCOUNT SET Balance = Balance - 1000 WHERE AccountID = 'A1';
 UPDATE ACCOUNT SET Balance = Balance + 1000 WHERE AccountID = 'A2';
-- If any operation fails, ROLLBACK
-- If both succeed, COMMIT
```

If the second UPDATE fails (e.g., Account A2 doesn't exist), the first update must be undone to maintain atomicity.

## Exam Tips

1. **Remember ACID properties**: Atomicity, Consistency, Isolation, Durability—each is equally important and frequently tested.

2. **Understand constraint types**: Know the difference between key, referential, domain, and check constraints.

3. **Know referential actions**: CASCADE, SET NULL, SET DEFAULT, and NO ACTION for handling foreign key violations.

4. **Transaction states diagram**: Be familiar with the state transition diagram (Active → Partially Committed → Committed; Active → Aborted).

5. **Immediate vs. Deferred checking**: Understand when each type is appropriate and how they affect transaction behavior.

6. **INSERT vs. DELETE vs. UPDATE**: Know what each operation does and what violations can occur with each.

7. **Constraint violation handling**: Understand that the DBMS automatically rejects or modifies operations that would violate constraints.

8. **Atomicity in transactions**: Remember that partial transaction execution is not allowed—a transaction either fully succeeds or fully fails.
