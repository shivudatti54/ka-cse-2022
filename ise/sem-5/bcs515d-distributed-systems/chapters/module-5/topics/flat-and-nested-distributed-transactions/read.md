# Flat and Nested Distributed Transactions

## Introduction

In distributed systems, a transaction is a fundamental unit of work that must be executed atomically—it either **completes entirely (commits)** or has **no effect at all (aborts)**. This Atomicity, along with Consistency, Isolation, and Durability (ACID properties), is challenging to maintain when data is spread across multiple machines. To manage complexity and improve performance, transactions can be structured in different ways. This module explores two primary structures: **Flat Transactions** and the more advanced **Nested Transactions**.

## Core Concepts

### 1. Flat Distributed Transactions

A flat transaction is the simplest transaction model. It is a single, indivisible unit of work that accesses multiple distributed resources (e.g., databases on different servers). It has a single begin point and a single end point (either commit or abort).

- **Structure:** It consists of a series of operations (`read`, `write`, `compute`) that are executed sequentially. There is no concept of sub-transactions.
- **Coordination:** A single coordinator (often using the **Two-Phase Commit protocol - 2PC**) is responsible for ensuring atomicity across all participating servers.
- **Semantics:** The entire transaction is atomic. If any participant fails or votes to abort, the entire transaction is rolled back at all participants.

**Example: A Simple Bank Transfer**
Imagine transferring $100 from an account in Server A to an account in Server B.

1.  `Begin Transaction`
2.  `Debit $100 from Account_X (on Server A)`
3.  `Credit $100 to Account_Y (on Server B)`
4.  `Commit Transaction`

This is a flat transaction. Both operations (debit and credit) are part of one atomic unit. If the credit operation fails after the debit has already occurred, the entire transaction is aborted and the debit is rolled back.

**Limitation:** The primary limitation of flat transactions is their lack of modularity. A failure in any single operation causes the entire, potentially long-lived, transaction to fail and restart from the beginning.

### 2. Nested Distributed Transactions

A nested transaction (or transaction with sub-transactions) introduces a hierarchical structure. A top-level transaction can spawn several **sub-transactions**, which can themselves spawn further sub-transactions, creating a tree-like structure.

- **Structure:** The transaction is broken down into smaller, modular sub-units. Each sub-transaction is a transaction in its own right, with its own begin and end points.
- **Coordination:** Commit and abort are managed hierarchically. A sub-transaction can commit or abort independently, but its results are only made permanent when its parent (and ultimately the top-level transaction) commits.
- **Semantics:**
  - **Atomicity:** The entire nested transaction is atomic. A commit at the top-level makes the effects of all committed sub-transactions permanent. An abort at the top-level rolls back everything.
  - **Failure Isolation:** A failure of a sub-transaction does _not_ automatically force the entire transaction to abort. The parent transaction can handle the failure, for example, by starting an alternative sub-transaction (e.g., using a different service replica). This provides finer-grained control and greater robustness.
  - **Visibility:** The effects of a committed sub-transaction are visible to other sub-transactions within the _same_ top-level transaction. However, they are **not** visible to transactions outside the hierarchy until the top-level transaction commits. This preserves isolation.

**Example: An Online Travel Booking**
Booking a trip involves reserving a flight, a hotel, and a car.

1.  `Begin Top-Level Transaction T`
2.  `Begin Sub-Transaction T1 (Book Flight)`
    - ...flight booking operations...
    - `Commit T1` (This commit is provisional, held within T)
3.  `Begin Sub-Transaction T2 (Book Hotel)`
    - ...hotel booking operations...
    - `Commit T2` (provisional)
4.  `Begin Sub-Transaction T3 (Book Car)`
    - ...car rental operations... **-> Fails (No cars available)**
    - `Abort T3`
5.  Top-level transaction `T` now handles the failure of `T3`. It can:
    - **Abort:** Abort the entire trip, rolling back `T1` and `T2` (the flight and hotel).
    - **Retry:** Try booking a car from a different rental company (`Begin Sub-Transaction T4`).
    - **Proceed:** Decide to commit anyway, confirming just the flight and hotel.

This modularity and ability to handle partial failures is the key advantage of nested transactions over flat ones.

## Key Points & Summary

| Feature              | Flat Transaction                                         | Nested Transaction                                         |
| :------------------- | :------------------------------------------------------- | :--------------------------------------------------------- |
| **Structure**        | Single, indivisible unit                                 | Hierarchical tree of sub-transactions                      |
| **Modularity**       | Low                                                      | High                                                       |
| **Failure Handling** | All-or-nothing; any failure aborts the whole transaction | Fine-grained; parents can handle sub-transaction failures  |
| **Concurrency**      | Limited                                                  | Higher; sub-transactions can execute concurrently          |
| **Complexity**       | Simple to implement and understand                       | More complex coordination is required                      |
| **Performance**      | Can be poor for long transactions due to locking         | Potentially better due to concurrency and modular recovery |

- **Flat Transactions** are simple but inflexible. They are suitable for short, straightforward operations where the all-or-nothing requirement is clear-cut.
- **Nested Transactions** provide a more powerful and flexible model for building complex distributed applications. They enable modularity, better error recovery, and increased concurrency, which are essential for scalability and robustness in modern systems like microservices architectures.
- The concept of **provisional commit** is crucial for nested transactions. Sub-transactions commit their results temporarily, making them visible within the transaction family but not to the outside world until the top-level commit.
