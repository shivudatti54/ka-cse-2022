# Module 4: Desirable Properties of Transactions (ACID Properties)

## Introduction

In a Database Management System (DBMS), a **transaction** represents a single logical unit of work that accesses and possibly modifies the contents of a database. A transaction can be a single SQL statement or a set of multiple SQL statements. For example, transferring money from one bank account to another involves two operations: debiting one account and crediting another. For the database to remain consistent and reliable, both operations must succeed or fail as a single unit. This is where the properties of transactions become critical. These properties are collectively known as the **ACID properties**, which form the fundamental cornerstone for reliable transaction processing.

## Core Concepts: The ACID Properties

The acronym ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties guarantee that database transactions are processed reliably.

### 1. Atomicity

**Concept:** Atomicity ensures that a transaction is treated as a single, indivisible unit of work. This means **either all operations of the transaction are executed completely, or none are executed at all.** There is no in-between state.

**How it works:** The DBMS achieves this using techniques like **shadow copying** or, more commonly, by maintaining a **transaction log**. Before any changes are made to the actual database (on disk), the intended changes and the old values are written to a log. If a transaction fails midway due to a system crash, power failure, or error, the DBMS uses this log to **rollback** or **undo** all the changes that the transaction made, restoring the database to its state before the transaction began.

**Example:** Consider a funds transfer transaction `T1`:
1.  `UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A1';`
2.  `UPDATE Account SET balance = balance + 500 WHERE acc_no = 'A2';`

If the system crashes after the first update (debiting A1) but before the second (crediting A2), atomicity ensures that the debit operation is rolled back. The money is not lost; it is returned to account A1, leaving the database as if `T1` never started.

### 2. Consistency

**Concept:** Consistency ensures that a transaction takes the database from one **consistent state** to another. A consistent state is one where all data integrity constraints (e.g., primary keys, foreign keys, unique constraints, `CHECK` constraints) and business rules are satisfied.

**How it works:** This property is primarily the responsibility of the user who writes the transaction. The DBMS assumes that if the database was consistent before a transaction and the transaction is executed in isolation (without interference from other transactions), it will leave the database consistent afterward. The DBMS enforces all declared integrity constraints, automatically rolling back transactions that violate them.

**Example:** In the same funds transfer, a business rule states that "an account balance must never fall below zero." A consistent transaction must ensure this rule is never broken. If debiting A1 would cause its balance to become negative, the entire transaction must be aborted to preserve consistency.

### 3. Isolation

**Concept:** Isolation ensures that the execution of multiple transactions **concurrently** happens in a way that is **separable**—as if they were executed one after the other, serially. The intermediate, uncommitted state of a transaction should not be visible to any other transactions.

**How it works:** This is achieved through **concurrency control protocols** (e.g., locking mechanisms or timestamp-based protocols). Without proper isolation, several problems can occur, such as:
*   **Dirty Read:** Reading uncommitted data from another transaction that may later be rolled back.
*   **Non-Repeatable Read:** Getting different values when reading the same row multiple times within a transaction because another transaction modified and committed it.
*   **Phantom Read:** New rows appearing or existing rows disappearing between two reads in the same transaction due to another transaction's insert/delete operations.

**Example:** If two transfer transactions `T1` (A1 to A2) and `T2` (A2 to A3) run concurrently, isolation ensures that `T2` does not see the intermediate state of `T1` where A1 has been debited but A2 has not yet been credited. This prevents `T2` from using an incorrect balance for A2.

### 4. Durability

**Concept:** Durability guarantees that **once a transaction has been committed**, its changes are permanent. These changes must persist in the database even in the event of subsequent system failures, power loss, or crashes.

**How it works:** The DBMS achieves durability by ensuring that the log records of the committed transaction are written to non-volatile storage (like a hard disk) *before* the commitment is acknowledged to the user. The actual database files might be written later, but the log is sufficient to **redo** the transaction's changes after a crash. After a crash and restart, the recovery subsystem replays the log for committed transactions that may not have had their changes written to disk.

**Example:** Once you get a "Transfer Successful" message for transaction `T1`, you can be certain that the changes are saved forever. Even if the database server fails immediately afterward, upon restart, the committed changes will be recovered and reflected in the database.

## Key Points / Summary

| Property | Description | Ensures... | Mechanism |
| :--- | :--- | :--- | :--- |
| **A**tomicity | All-or-nothing execution | Transactions are indivisible units | Transaction Log (Rollback) |
| **C**onsistency | Valid state transition | Database rules are never violated | DBMS Constraints & Application Logic |
| **I**solation | Seamless concurrency | Transactions do not interfere with each other | Concurrency Control (e.g., Locks) |
| **D**urability | Permanence of changes | Committed changes survive failures | Transaction Log (Redo) |

*   The ACID properties are fundamental to any reliable DBMS.
*   They work together to ensure data integrity, consistency, and reliability in both normal operation and failure scenarios.
*   While these properties are ideal, some may be relaxed (e.g., lower isolation levels) in certain systems to trade-off consistency for higher performance.