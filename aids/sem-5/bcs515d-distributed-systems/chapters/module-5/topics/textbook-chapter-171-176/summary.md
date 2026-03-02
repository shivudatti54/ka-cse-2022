# **Distributed Systems: Chapters 17.1-17.6 Quick Revision Notes**

### Introduction to Distributed Transactions

- Definition: A distributed transaction is a sequence of operations that are executed as a single, all-or-nothing unit of work.
- Characteristics:
  - Span multiple sites or nodes
  - Involves multiple databases or resources
  - Requires atomicity, consistency, isolation, and durability (ACID) properties

### Types of Distributed Transactions

- **Flat Distributed Transactions**: A single transaction that spans multiple sites or nodes, with no nesting.
- **Nested Distributed Transactions**: A transaction that is nested inside another transaction, allowing for more complex business logic.

### Distributed Transaction Protocols

- **Two-Phase Commit (2PC)**: A protocol for achieving atomicity in distributed transactions.
  - **Prepare Phase**: Each node prepares to commit or abort the transaction.
  - **Commit Phase**: If all nodes prepare to commit, the transaction is committed; otherwise, it is rolled back.
- **Pessimistic Concurrency Control (PCC)**: A protocol that uses locking to prevent concurrent transactions from accessing shared resources.

### Notions of Progress

- **Progress**: The degree to which a transaction has made progress towards completion.
- **Notion of Progress**: A way to define the progress of a transaction, such as the percentage of committed operations.

### Distributed Transaction Concurrency Control

- **Conflict Resolution**: A mechanism for resolving conflicts between concurrent transactions.
- **Ordering**: The order in which transactions are executed, to prevent conflicts.

### Key Formulas and Definitions

- **2PC Protocol**:
  - `Prep(Req)`: Prepare request for a transaction
  - `Commit(Req)`: Commit request for a transaction
  - `Abort(Req)`: Abort request for a transaction
- **Notion of Progress**:
  - `P(progress)`: Progress of a transaction
  - `C(progress)`: Committed operations of a transaction

### Important Theorems

- **2PC Theorem**: If a distributed transaction is executed using the 2PC protocol, then the transaction is either committed or rolled back, and all nodes agree on the outcome.
- **PCC Theorem**: If a distributed transaction is executed using PCC, then the transaction is either committed or rolled back, and all nodes agree on the outcome.
