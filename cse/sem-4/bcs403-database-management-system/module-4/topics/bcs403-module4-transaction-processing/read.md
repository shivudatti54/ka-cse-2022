# Introduction to Transaction Processing

## Table of Contents

- [Introduction to Transaction Processing](#introduction-to-transaction-processing)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What is a Transaction?](#what-is-a-transaction)
  - [ACID Properties](#acid-properties)
  - [Transaction States](#transaction-states)
  - [Concurrency Control](#concurrency-control)
  - [Schedules](#schedules)
  - [Concurrency Control Techniques](#concurrency-control-techniques)
- [Examples](#examples)
  - [Example 1: ACID Properties in a Banking Transaction](#example-1-acid-properties-in-a-banking-transaction)
  - [Example 2: Concurrency Problem - Lost Update](#example-2-concurrency-problem---lost-update)
  - [Example 3: Transaction States](#example-3-transaction-states)
- [Exam Tips](#exam-tips)

## Introduction

Transaction processing is a fundamental concept in database management systems that ensures data integrity and consistency when multiple users access the database concurrently. In real-world applications, databases are constantly accessed by many users simultaneously, and operations must be executed in a way that maintains the database in a consistent state. Transaction processing provides a mechanism to achieve this by grouping related database operations into a single logical unit of work.

The importance of transaction processing cannot be overstated in modern database systems. Banking systems, airline reservation systems, e-commerce platforms, and inventory management systems all rely heavily on robust transaction processing to ensure that financial transactions, bookings, and data modifications are handled reliably. Without proper transaction management, systems would be vulnerable to data corruption, inconsistent states, and various concurrency-related problems.

This module explores the theoretical foundations and practical implementations of transaction processing in database management systems. We will examine the ACID properties that define a valid transaction, the various states a transaction can go through, concurrency control mechanisms, and how these concepts are implemented in modern DBMS. Understanding these concepts is essential for any database professional, as they form the backbone of reliable data management.

## Key Concepts

### What is a Transaction?

A transaction is a logical unit of work that consists of one or more database operations. It represents a sequence of instructions that should be executed as a single atomic unit. A transaction transforms the database from one consistent state to another consistent state. The key characteristic of a transaction is that it either completes in its entirety or has no effect at all on the database.

Consider a simple banking example: when a customer transfers money from account A to account B, this operation involves two distinct steps - debiting account A and crediting account B. Both operations must be executed successfully for the transaction to be considered complete. If the system fails after debiting account A but before crediting account B, the database would be left in an inconsistent state. Transaction processing ensures that such scenarios do not occur by treating both operations as a single unit.

### ACID Properties

The ACID properties are the fundamental characteristics that define a valid database transaction. These properties ensure that database transactions are processed reliably.

**Atomicity** ensures that a transaction is treated as a single atomic unit - either all operations within the transaction are executed, or none of them are. The database system guarantees that partial transactions are never visible to other transactions. If any operation within a transaction fails, the entire transaction is rolled back, and the database is restored to its state before the transaction began. This property is particularly important in financial applications where partial operations could lead to significant losses.

**Consistency** ensures that a transaction transforms the database from one consistent state to another consistent state. The database must satisfy all integrity constraints after the transaction completes. If a transaction violates any integrity constraint, it should be aborted, and the database should be restored to its previous consistent state. Consistency depends on atomicity - if a transaction is atomic and starts from a consistent state, it will end in a consistent state.

**Isolation** ensures that concurrent transactions appear to execute serially - each transaction should not be affected by other transactions executing concurrently. The intermediate results of a transaction should not be visible to other transactions until the transaction is committed. This property is challenging to achieve in practice and often requires sophisticated concurrency control mechanisms.

**Durability** ensures that once a transaction has been committed, its effects are permanent and survive any subsequent system failures. The results of a committed transaction must be stored in non-volatile storage so that they can be recovered even if the system crashes immediately after commit.

### Transaction States

A transaction goes through several states during its lifecycle, reflecting its progress from initiation to completion.

The **Active** state is the initial state where the transaction is being executed. While in this state, the transaction is performing read and write operations on the database.

The **Partially Committed** state is reached when the transaction has completed its final operation but has not yet been committed. At this point, the transaction may still be rolled back if a system failure occurs.

The **Committed** state is reached after the transaction has been successfully committed. Once in this state, the transaction's effects are permanently stored in the database and cannot be rolled back.

The **Failed** state occurs when a transaction cannot proceed normally due to some error or violation. The transaction must be rolled back to undo its effects on the database.

The **Aborted** state is reached after a failed transaction has been rolled back. The database is restored to its state before the transaction began, and the transaction can be restarted if needed.

### Concurrency Control

Concurrency control is the process of managing simultaneous operations on a database without causing inconsistencies. When multiple transactions execute concurrently, various problems can arise if proper control mechanisms are not implemented.

The **Lost Update** problem occurs when two transactions read and modify the same data, and one of the updates is lost because the other transaction overwrites it. For example, if two transactions both read a value of 100, add 50 to it, and write back 150, the final value should be 200 but would incorrectly be 150.

The **Dirty Read** problem occurs when a transaction reads data that has been modified by another transaction that has not yet been committed. If the uncommitted transaction is rolled back, the reading transaction has read invalid data.

The **Non-Repeatable Read** problem occurs when a transaction reads the same data twice but gets different values because another transaction modified the data between the two reads.

The **Phantom Read** problem occurs when a transaction executes a query twice and gets different sets of rows because another transaction inserted or deleted rows.

### Schedules

A schedule is a sequence of operations from multiple transactions that indicates the order in which operations are executed. Schedules are essential for understanding how concurrent transactions interact.

A **Serial Schedule** is one where transactions are executed one after another without interleaving their operations. Serial schedules are always consistent but may not be efficient in terms of resource utilization.

A **Non-Serial Schedule** is one where operations from multiple transactions are interleaved. While non-serial schedules can improve performance, they may lead to inconsistencies if not properly controlled.

A **Recoverable Schedule** is one where a transaction never commits until all transactions from which it has read have committed. This ensures that committed transactions can be recovered correctly.

A **Cascadeless Schedule** is one where a transaction only reads data that has been committed by other transactions. This prevents dirty reads and ensures better recoverability.

### Concurrency Control Techniques

**Lock-Based Protocols** use locks to control access to database items. A **Shared Lock** allows a transaction to read an item but not modify it. Multiple transactions can hold shared locks on the same item simultaneously. An **Exclusive Lock** allows a transaction to both read and modify an item. Only one transaction can hold an exclusive lock on an item at a time.

The **Two-Phase Locking (2PL) Protocol** is a popular concurrency control method that ensures conflict-serializability. It has two phases: the **Growing Phase** where a transaction can acquire locks but cannot release any locks, and the **Shrinking Phase** where a transaction can release locks but cannot acquire any new locks.

**Timestamp-Based Protocols** use timestamps to order transactions and ensure serializability. Each transaction is assigned a unique timestamp, and operations are processed in timestamp order. The timestamp ordering protocol ensures that older transactions get priority, preventing younger transactions from reading or writing stale data.

## Examples

### Example 1: ACID Properties in a Banking Transaction

Consider a funds transfer transaction T1 that transfers Rs. 1000 from Account A (balance: Rs. 5000) to Account B (balance: Rs. 3000).

**Step 1: Read Account A balance**

```
READ(A) → 5000
```

**Step 2: Debit Account A**

```
A = 5000 - 1000 = 4000
WRITE(A) → 4000
```

**Step 3: Read Account B balance**

```
READ(B) → 3000
```

**Step 4: Credit Account B**

```
B = 3000 + 1000 = 4000
WRITE(B) → 4000
```

**Atomicity**: If the system fails after Step 2 (before writing to B), the transaction is rolled back, and Account A is restored to 5000. The customer does not lose money.

**Consistency**: The constraint that total balance = A + B is maintained. Before: 5000 + 3000 = 8000. After: 4000 + 4000 = 8000.

**Isolation**: Until the transaction commits, other transactions cannot see the intermediate values (A=4000 is not visible to others until commit).

**Durability**: Once committed, the changes persist even if the system crashes immediately after.

### Example 2: Concurrency Problem - Lost Update

Consider two transactions T1 and T2 both trying to increment a counter value:

**Initial Value**: counter = 100

**Schedule (Problematic)**:
| Time | T1 | T2 |
|------|----|----|
| t1 | READ(counter) → 100 | |
| t2 | | READ(counter) → 100 |
| t3 | counter = 100 + 50 = 150 | |
| t4 | WRITE(counter) → 150 | |
| t5 | | counter = 100 + 100 = 200 |
| t6 | | WRITE(counter) → 200 |

**Result**: Final value = 200 (T1's update of +50 is lost!)

**Corrected Schedule with Locks**:
| Time | T1 | T2 |
|------|----|----|
| t1 | LOCK-X(counter) | |
| t2 | READ(counter) → 100 | |
| t3 | counter = 100 + 50 = 150 | |
| t4 | WRITE(counter) → 150 | |
| t5 | UNLOCK(counter) | |
| t6 | | LOCK-X(counter) |
| t7 | | READ(counter) → 150 |
| t8 | | counter = 150 + 100 = 250 |
| t9 | | WRITE(counter) → 250 |
| t10 | | UNLOCK(counter) |

**Result**: Final value = 250 (correct!)

### Example 3: Transaction States

Consider transaction T that transfers money between accounts:

1. **Active State**: Transaction begins execution

- READ(savings_account) → 10000
- savings_account = 10000 - 5000 = 5000
- WRITE(savings_account) → 5000

2. **Partially Committed State**: Final operation executed

- READ(checking_account) → 2000
- checking_account = 2000 + 5000 = 7000
- WRITE(checking_account) → 7000

3. **Committed State**: All operations successful, transaction commits

- COMMIT

4. **Aborted State** (if failure occurred): All changes rolled back

- ROLLBACK → savings_account restored to 10000, checking_account to 2000

## Exam Tips

1. **Remember ACID Properties**: The acronym ACID (Atomicity, Consistency, Isolation, Durability) is frequently tested. Be prepared to explain each property with an example.

2. **Transaction States Order**: Remember the sequence: Active → Partially Committed → Committed (or Failed → Aborted).

3. **Difference between Serial and Non-Serial Schedules**: Serial schedules never interleave operations, while non-serial schedules do. Serial schedules are always correct but may be inefficient.

4. **Lock Types**: Know the difference between Shared Locks (S) and Exclusive Locks (X). Remember that S locks allow concurrent reads, while X locks block all other locks.

5. **Two-Phase Locking**: Remember the two phases - Growing Phase (can acquire locks) and Shrinking Phase (can release locks). Once you enter the shrinking phase, you cannot acquire new locks.

6. **Concurrency Problems**: Be able to identify and explain problems like Lost Update, Dirty Read, Non-Repeatable Read, and Phantom Read with examples.

7. **Recoverability**: Understand the difference between recoverable and cascadeless schedules. Cascadeless schedules are a subset of recoverable schedules.

8. **SQL Transaction Commands**: Know the basic SQL commands for transaction control: BEGIN TRANSACTION, COMMIT, ROLLBACK.

9. **Importance of Isolation**: Higher isolation levels prevent more concurrency problems but may reduce performance. Know the trade-offs.

10. **Timestamp Ordering**: Understand that timestamp-based protocols use transaction timestamps to order operations and prevent conflicts rather than using locks.
