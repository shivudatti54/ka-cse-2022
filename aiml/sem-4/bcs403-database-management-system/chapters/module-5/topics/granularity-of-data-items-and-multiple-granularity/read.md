Of course. Here is a comprehensive educational note on the topic for  engineering students.

# Module 5: Concurrency Control - Granularity & Multiple Granularity Locking

## Introduction

In a Database Management System (DBMS), concurrency control protocols like Two-Phase Locking (2PL) ensure transaction isolation. However, a fundamental question arises: **what exactly is a transaction locking?** Is it an entire table, a single row, or even a whole database? The size of the data object chosen as the unit for locking is called its **granularity**. This module explores the concept of granularity and introduces **Multiple Granularity Locking (MGL)**, a sophisticated protocol that allows transactions to lock data items at different levels of granularity efficiently.

## Core Concepts

### 1. Granularity of Data Items

**Granularity** refers to the size of a data item that can be locked. It defines the level of detail at which database objects are considered for locking purposes.

**Levels of Granularity (from finest to coarsest):**
*   **Attribute (Field) Level:** Locking a single cell in a table. (Finest Granularity)
*   **Tuple (Record) Level:** Locking a single row in a table.
*   **Page (Block) Level:** Locking a fixed-size data block (e.g., 4KB), which may contain multiple rows.
*   **Table (Relation) Level:** Locking an entire database table.
*   **Database Level:** Locking the entire database. (Coarsest Granularity)

**The Granularity Trade-off:**
The choice of granularity presents a crucial trade-off:
*   **Fine Granularity (e.g., row-level locks):**
    *   **Advantage:** Higher concurrency. Many transactions can access different rows of the same table simultaneously.
    *   **Disadvantage:** Higher overhead. The system must manage a large number of locks, consuming more memory and CPU cycles.
*   **Coarse Granularity (e.g., table-level locks):**
    *   **Advantage:** Lower overhead. The system manages very few locks.
    *   **Disadvantage:** Lower concurrency. Locking an entire table for one transaction blocks all others trying to access any part of that table.

### 2. Multiple Granularity Locking (MGL)

MGL is a protocol designed to resolve the granularity trade-off. It allows a transaction to lock data items at an appropriate level of granularity, dynamically choosing between fine and coarse locks based on its needs. This provides the high concurrency of fine-grained locks and the low overhead of coarse-grained locks.

#### How MGL Works: Intention Locks

MGL operates using a hierarchy of data items (e.g., Database -> Table -> Page -> Row) and a new type of lock called **Intention Locks**.

An intention lock signals that a transaction *intends* to acquire a finer-granularity lock on a descendant (lower-level) node in the hierarchy. This prevents other transactions from placing a coarse-grained lock on a higher-level node that would conflict with the finer-grained locks already held.

There are two main types of intention locks:
*   **Intention-Shared (IS):** Indicates that the transaction intends to place **S-locks (shared locks)** on some descendant nodes.
*   **Intention-Exclusive (IX):** Indicates that the transaction intends to place **X-locks (exclusive locks)** on some descendant nodes.
*   **Shared+Intention-Exclusive (SIX):** A combination lock where the node itself is locked in **shared mode**, but the transaction *intends* to set **exclusive locks** on its descendants. This is useful for transactions that need to read an entire table and then update a few rows within it.

#### The MGL Protocol Rules:
1.  Before a transaction can lock any node, it must lock all its ancestors.
2.  A transaction can lock a node in:
    *   **S or IS** mode only if it has locked the parent node in **IS or IX** mode.
    *   **X, IX, or SIX** mode only if it has locked the parent node in **IX or SIX** mode.
3.  Locking must follow the Two-Phase Locking (2PL) protocol.

## Example

Consider a hierarchy: `Database (DB)` -> `Table (T1)` -> `Page (P1)` -> `Record (R1)`.

**Transaction Txn_A** wants to update a specific record `R1` in table `T1`.
1.  Txn_A must first acquire an **IX lock** on the entire `Database`. This announces its intent to set an exclusive lock somewhere down the hierarchy.
2.  Next, it acquires an **IX lock** on `Table T1`. This announces its intent to set an exclusive lock on a part of this specific table.
3.  Finally, it acquires an **X lock** on the target `Record R1`.

**Transaction Txn_B** wants to read all records in `Table T1`.
1.  Txn_B requests an **S lock** on `T1`.
2.  The lock manager checks the ancestors of `T1` (the Database). It finds that Txn_A holds an **IX lock** on the Database.
3.  Since **S** (requested by Txn_B) and **IX** (held by Txn_A) are compatible (see compatibility matrix), the lock is granted.
Txn_B can now read all records in `T1` (except the one locked by Txn_A, which it will wait for).

This demonstrates high concurrency: Txn_B can read most of the table while Txn_A is updating a single row within it.

## Key Points & Summary

*   **Granularity** is the size of a data item chosen as the unit for locking (e.g., row, table, database).
*   The **Granularity Trade-off** is between **concurrency** (favors fine-grained locks) and **overhead** (favors coarse-grained locks).
*   **Multiple Granularity Locking (MGL)** is a protocol that allows transactions to efficiently lock items at different levels of granularity within a hierarchy.
*   **Intention Locks (IS, IX, SIX)** are the core mechanism of MGL. They signal a transaction's intent to lock finer-grained items, preventing conflicting coarse-grained locks.
*   MGL provides a practical balance, enabling high concurrency for typical transactions (that access few items) while keeping the number of managed locks low. It is widely implemented in modern DBMS like Oracle, SQL Server, and MySQL (InnoDB).