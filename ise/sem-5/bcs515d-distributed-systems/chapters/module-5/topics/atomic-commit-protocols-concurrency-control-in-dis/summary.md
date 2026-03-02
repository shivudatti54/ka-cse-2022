# Atomic Commit Protocols, Concurrency Control, Distributed Deadlocks, and Transaction Recovery

===========================================================

### Atomic Commit Protocols

- **Definition:** A set of rules that ensure the atomicity, consistency, isolation, and durability (ACID) properties of distributed transactions.
- **Examples:**
  - Two-Phase Commit (2PC)
  - Preparation Protocol
  - 3-Phase Commit (3PC)
- **Formulas:**
  - 2PC: `YES`, `NO`, `ABORT`
  - 3PC: `YES`, `NO`, `ABORT`, `RECOVER`
- **Theorems:**
  - Banker's Theorem (guarantees safe state)
  - Gabel's Theorem (guarantees atomicity)

### Concurrency Control in Distributed Transactions

- **Definition:** A method to manage concurrency in distributed transactions to prevent conflicts.
- **Types:**
  - Locking (e.g., pessimistic locking, optimistic locking)
  - Timestamping
  - Multiversion Concurrency Control (MVCC)
- **Formulas:**
  - Locking: `L(x) = L(x \land y)` (lock x and y)

### Distributed Deadlocks

- **Definition:** A situation where two or more transactions are blocked, waiting for each other to release resources.
- **Causes:**
  - Resource allocation
  - Transaction ordering
- **Prevention Techniques:**
  - Banker's Algorithm
  - Rolling Stone Algorithm
- **Formulas:**
  - Banker's Algorithm: `f(i) = -\sum_{j \in J(i)} l_{ij}`
  - Rolling Stone Algorithm: `T \mapsto T'`

### Transaction Recovery

- **Definition:** The process of restoring a system to a consistent state after a failure.
- **Types:**
  - Log-based recovery
  - Checkpoint-based recovery
- **Formulas:**
  - Log-based recovery: `R(X) = R(X \cup L)\`, where `L` is the transaction log

Key concepts and formulas to remember for exams:

- Atomic commit protocols (2PC, 3PC)
- Concurrency control methods (locking, timestamping, MVCC)
- Distributed deadlock prevention techniques (Banker's Algorithm, Rolling Stone Algorithm)
- Transaction recovery methods (log-based recovery, checkpoint-based recovery)
