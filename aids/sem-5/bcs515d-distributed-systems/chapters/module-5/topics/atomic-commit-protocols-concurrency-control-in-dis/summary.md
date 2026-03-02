# **Atomic Commit Protocols, Concurrency Control in Distributed Transactions, Distributed Deadlocks, Transaction Recovery**

## **Atomic Commit Protocols**

- Definition: A set of rules that ensures the consistency of the database by ensuring that all nodes are updated simultaneously.
- Types:
  - **Two-Phase Commit (2PC)**: A widely used protocol that ensures atomicity and consistency.
  - **Piggybacking**: A protocol that combines multiple transactions into a single message.
  - **Sagas**: A protocol that allows for more complex transactions with multiple phases.

## **Concurrency Control in Distributed Transactions**

- Definition: Techniques used to manage concurrent access to a shared resource.
- Concurrency Control Protocols:
  - **Locking**: Acquiring and releasing locks to prevent concurrent access.
  - **Timestamping**: Assigning a unique timestamp to each transaction to prevent conflicts.
  - **Multiversion Concurrency Control (MVCC)**: Maintaining multiple versions of a resource to allow concurrent access.

## **Distributed Deadlocks**

- Definition: A situation where two or more transactions are blocked indefinitely, each waiting for the other to release a resource.
- Causes:
  - **Resource Incompatibility**: Resources are not compatible for concurrent access.
  - **Circular Wait**: A cycle of transactions waiting for each other to release a resource.
- Detection and Prevention Techniques:
  - **Deadlock Detection Algorithms**: Identifying deadlock situations.
  - **Deadlock Prevention Algorithms**: Preventing deadlock situations by avoiding resource incompatibility and circular waits.

## **Transaction Recovery**

- Definition: The process of restoring a system to a consistent state after a failure or error.
- Recovery Techniques:
  - **Rollback Recovery**: Rolling back the transaction to a previous consistent state.
  - **Crash Recovery**: Restoring the system to a consistent state after a crash.
  - **Recovery by Replication**: Restoring the system by replicating data from a backup.

**Important Formulas and Definitions**

- **Two-Phase Commit (2PC) Protocol**:
  - PHASE 1: Prepare
  - PHASE 2: Commit
- **Isolation Level**: The level of consistency ensured by a database system (e.g., Read Uncommitted, Repeatable Read).
- **Deadlock Detection Algorithm**: A algorithm used to detect deadlock situations (e.g., Banker's Algorithm).
- **Concurrency Control Protocol**: A protocol used to manage concurrent access to a shared resource.
