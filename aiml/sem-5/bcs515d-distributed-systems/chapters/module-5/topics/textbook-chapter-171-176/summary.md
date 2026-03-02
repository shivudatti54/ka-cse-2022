# Distributed Systems: Chapter 17.1-17.6 Revision Notes

==============================================

### Introduction to Distributed Systems (17.1)

- A distributed system is a collection of interconnected nodes that work together to achieve a common goal.
- Distributed systems can be classified into two categories:
  - Homogeneous systems: all nodes have the same type and capabilities.
  - Heterogeneous systems: nodes have different types and capabilities.
- Characteristics of distributed systems:
  - Decentralization
  - Autonomy
  - Distribution
  - Cooperation

### Flat Distributed Transactions (17.2)

- A flat distributed transaction is a single, atomic unit of work that spans multiple nodes.
- A flat transaction is characterized by:
  - Atomicity: either all or none of the operations are committed.
  - Consistency: the transaction maintains the consistency of the system.
  - Isolation: multiple transactions can execute concurrently without interference.
  - Durability: once committed, the transaction is permanent.
- Flat transaction protocols:
  - Two-Phase Commit (2PC)
  - Local Commit (LC)

### Nested Distributed Transactions (17.3)

- A nested distributed transaction is a transaction that contains another transaction.
- Characteristics of nested transactions:
  - Inner transaction: executed within the outer transaction.
  - Outer transaction: coordinates the execution of the inner transaction.
- Types of nested transactions:
  - Innermost nesting: innermost transaction is executed within another transaction.
  - Outermost nesting: outermost transaction is executed within another transaction.

### Types of Distributed Transactions (17.4)

- **Atomicity**: a single, indivisible unit of work.
- **Consistency**: the transaction maintains the consistency of the system.
- **Isolation**: multiple transactions can execute concurrently without interference.
- **Durability**: once committed, the transaction is permanent.

### Distributed Transaction Models (17.5)

- **Retransmission model**: each node retransmits its vote to the coordinator.
- **Superfluous model**: a node sends its vote to the coordinator only if it is necessary.
- **Hybrid model**: combines elements of retransmission and superfluous models.

### Distributed Transaction Protocols (17.6)

- **Two-Phase Commit (2PC)**: a protocol for coordinating distributed transactions.
- **Local Commit (LC)**: a protocol for coordinating distributed transactions with a local commit.
- **XA (Extends Atomicity)**: a protocol for coordinating distributed transactions.

Formulas, Definitions, and Theorems:

- **2PC protocol**:
  - Phase 1: Prepare
  - Phase 2: Commit
- **LC protocol**:
  - Commit
  - Rollback
- **XA protocol**:
  - Atomicity
  - Consistency
  - Isolation
  - Durability
