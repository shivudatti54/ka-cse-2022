# **Distributed Systems: Chapter 17.1-17.6 Revision Notes**

### Introduction

- Distributed systems: a collection of interconnected computers that work together as a single system
- Advantages: increased scalability, fault tolerance, and flexibility
- Challenges: complexity, communication overhead, and consistency issues

### Flat Distributed Transactions

- A flat transaction is a sequence of operations that are executed as a single, all-or-nothing unit
- Characteristics:
  - No nested transactions
  - No compensation mechanism
- Advantages:
  - Simple implementation
  - Fast transaction completion
- Disadvantages:
  - Loss of data in case of failure
  - No guarantee of consistency

### Nested Distributed Transactions

- A nested transaction is a sequence of operations that are executed within another transaction
- Characteristics:
  - Nested within a higher-level transaction
  - Compensation mechanism to restore system consistency
- Advantages:
  - Provides strong consistency guarantees
  - Allows for data integrity
- Disadvantages:
  - Complex implementation
  - Long transaction completion time

### Distributed Transaction Protocol (DTP)

- Standard protocol for coordinating distributed transactions
- Characteristics:
  - Two-phase commit protocol
  - Atomicity, consistency, isolation, and durability (ACID) properties
- Formula:
  - `TXN = (PREPARE, COMMIT, ROLLBACK)`

### Distributed Transaction Manager (DTM)

- Component responsible for managing distributed transactions
- Characteristics:
  - Coordinates with transaction participants
  - Ensures ACID properties
- Theorem:
  - **Atomicity**: a transaction is treated as a single, indivisible unit

### Notes

- **XA Protocol**: an extension to the DTP that provides additional features for distributed transactions
- **Two-Phase Commit Protocol**: a protocol for coordinating distributed transactions

### Important Formulas and Definitions

- **ACID Properties**:
  - Atomicity: a transaction is treated as a single, indivisible unit
  - Consistency: the transaction maintains the consistency of the system
  - Isolation: the transaction is executed independently of other transactions
  - Durability: the transaction's effects are permanent
- **Two-Phase Commit Protocol**:
  - **Prepare Phase**: the transaction participants prepare for the transaction
  - **Commit Phase**: the transaction participants commit to the transaction
  - **Rollback Phase**: the transaction participants rollback the transaction if necessary
