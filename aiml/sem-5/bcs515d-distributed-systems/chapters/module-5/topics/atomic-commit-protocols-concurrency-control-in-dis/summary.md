# **Atomic Commit Protocols, Concurrency Control in Distributed Transactions, Distributed Deadlocks, and Transaction Recovery**

## **Atomic Commit Protocols**

- **Definition:** A set of rules that ensure the atomicity of a distributed commit
- **Types:**
  - **Two-Phase Commit (2PC)**: used for distributed systems with a centralized coordinator
  - **Paxos:** used for distributed systems with no centralized coordinator
  - **Raft:** used for distributed systems with a leader-based architecture
- **Formulas/Definitions:**
  - **Total Order:** a total order on a set of transactions that satisfies the 2PC protocol
  - **Local Commit:** the decision to commit a transaction locally, without affecting other transactions

## **Concurrency Control in Distributed Transactions**

- **Definition:** Mechanisms to manage multiple transactions concurrently
- **Types:**
  - **Locking:** serializes transactions by locking shared resources
  - **Timestamping:** schedules transactions based on their timestamps
  - **Multiversion Concurrency Control (MVCC):** maintains multiple versions of data, allowing concurrent transactions to read from different versions
- **Formulas/Definitions:**
  - **Lock Timeout:** a time limit for acquiring a lock
  - **Concurrency Control Protocol:** a set of rules that govern the interaction between transactions

## **Distributed Deadlocks**

- **Definition:** A situation where multiple transactions are blocked indefinitely
- **Causes:**
  - **Circular Wait:** a situation where a transaction is waiting for a resource held by another transaction in a cycle
  - **Resource Unavailability:** a situation where a transaction requests a resource that is not available
- **Prevention Techniques:**
  - **Deadlock Detection:** detecting deadlocks before they occur
  - **Deadlock Prevention:** preventing deadlocks from occurring in the first place

## **Transaction Recovery**

- **Definition:** The process of recovering from a failed transaction
- **Types:**
  - **Checkpointing:** saving the state of a transaction at a specific point
  - **Rollback Recovery:** rolling back to a previous state in case of a failure
  - **Crash Recovery:** recovering from a system crash
- **Formulas/Definitions:**
  - **Checkpoint Interval:** a time interval between checkpoints
  - **Rollback Recovery Algorithm:** an algorithm that determines the next checkpoint to recover to
