# Module 4: Transaction and System Concepts in DBMS

## Introduction

In a multi-user Database Management System (DBMS), multiple transactions (e.g., withdrawing money, booking a ticket) can occur simultaneously. This concurrency, while essential for performance, can lead to inconsistencies and data corruption if not managed properly. Furthermore, system failures can occur at any time. The concepts of **Transactions** and associated **System Concepts** form the bedrock of ensuring data integrity, consistency, and reliability in such an environment. This module delves into the fundamental properties of a transaction and the system mechanisms that guarantee these properties.

## Core Concepts

### 1. Transaction

A **transaction** is a single logical unit of work that accesses and possibly updates the contents of a database. It is a sequence of one or more database operations (like read, write, insert, update, delete) that must be executed as a whole. It is often initiated by a user program and is terminated by either a `COMMIT` or a `ROLLBACK` statement.

*   **Example:** A simple transaction to transfer $100 from account A to account B:
    1.  `READ(A);`
    2.  `A := A - 100;`
    3.  `WRITE(A);`
    4.  `READ(B);`
    5.  `B := B + 100;`
    6.  `WRITE(B);`
    7.  `COMMIT;`

### 2. ACID Properties

For a transaction to maintain database consistency and handle failures, it must possess the ACID properties:

*   **Atomicity:** A transaction is an atomic unit; it is either performed in its entirety or not performed at all. There is no intermediate state. The system must ensure that even if a transaction fails after a few operations, the effects of those partial operations are undone. This is managed by the **Transaction Recovery** component of the DBMS.
*   **Consistency:** A transaction must transform the database from one consistent state to another. It must obey all integrity constraints (e.g., primary key, foreign key) defined on the database. This is the responsibility of both the application programmer and the DBMS.
*   **Isolation:** Even though multiple transactions may execute concurrently, the system must ensure that the execution of each transaction is isolated from others. The intermediate results of an uncommitted transaction should not be visible to any other transaction. This is achieved through **Concurrency Control** protocols.
*   **Durability:** Once a transaction has been committed, its changes must persist in the database permanently, even in the event of a system failure. This is achieved by logging the changes to a non-volatile storage (like a hard disk) before the commit is acknowledged.

### 3. System States and Operations

A transaction can be in one of the following states during its lifetime:

*   **Active:** The initial state; the transaction is currently executing.
*   **Partially Committed:** The final operation has been executed, but changes are not yet saved to disk.
*   **Committed:** The transaction has completed successfully, and its changes have been permanently recorded. It leaves the system in a consistent state.
*   **Failed:** The transaction cannot proceed due to an error, or it has been aborted.
*   **Terminated:** The transaction has either committed or been rolled back and has left the system.

The key operations to transition between these states are:

*   **COMMIT:** This statement signals the successful end of a transaction. It makes all changes made by the transaction permanent.
*   **ROLLBACK:** This statement signals that the transaction has failed and must be aborted. It undoes all the operations of the transaction, restoring the database to the state it was in before the transaction began.

### 4. System Log for Recovery

To support Atomicity and Durability, the DBMS maintains a **log**. This is a history of all actions performed by transactions. Key types of log records are:

*   **`<T_i, Start>`:** Transaction `T_i` has started.
*   **`<T_i, X, V_old, V_new>`:** Transaction `T_i` has updated data item `X`; `V_old` is the value before the update (used for undo), and `V_new` is the value after the update (used for redo).
*   **`<T_i, Commit>`:** Transaction `T_i` has committed.
*   **`<T_i, Abort>`:** Transaction `T_i` has been aborted.

In the event of a system crash, the **Recovery Manager** uses this log to ensure Atomicity (by undoing uncommitted transactions) and Durability (by redoing committed transactions whose changes were not yet written to disk).

## Key Points / Summary

| Concept | Description |
| :--- | :--- |
| **Transaction** | A logical unit of work comprising a sequence of database operations that must execute completely or not at all. |
| **ACID Properties** | The four essential properties of a transaction: **A**tomicity, **C**onsistency, **I**solation, and **D**urability. |
| **Atomicity** | Guaranteed by the **Transaction Recovery** system, ensuring all-or-nothing execution. |
| **Durability** | Guaranteed by writing log records to stable storage before acknowledging a commit. |
| **Isolation** | Managed by **Concurrency Control** protocols (e.g., locking) to control interference between concurrent transactions. |
| **System Log** | A critical component that records all transaction actions, enabling recovery from failures. |
| **Commit & Rollback** | The primary operations that terminate a transaction, making its changes permanent or undoing them, respectively. |