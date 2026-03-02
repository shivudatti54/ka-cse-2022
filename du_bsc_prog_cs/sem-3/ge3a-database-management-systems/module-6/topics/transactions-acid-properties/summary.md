# Transactions ACID Properties

## Introduction
In Database Management Systems (DBMS), a transaction is a logical unit of work consisting of one or more operations (e.g., read, write). To ensure data integrity and reliability, transactions must satisfy the ACID properties—Atomicity, Consistency, Isolation, and Durability. These properties are fundamental to the Delhi University BSc Physical Science (CS) syllabus (NEP 2024) under the DBMS course, particularly in modules covering transactions and concurrency control.

## Key Concepts: ACID Properties
- **Atomicity**: 
  - Ensures a transaction is treated as a single indivisible unit.
  - All operations succeed together, or none are applied (all-or-nothing).
  - Example: In a funds transfer, both debit and credit must occur; if one fails, the transaction is rolled back.
- **Consistency**: 
  - Guarantees that a transaction transforms the database from one valid state to another.
  - All integrity constraints (e.g., unique keys, foreign keys) must be satisfied after completion.
  - If constraints are violated, the transaction aborts, leaving the database unchanged.
- **Isolation**: 
  - Ensures concurrent transactions execute independently without interfering.
  - Intermediate results are not visible to other transactions until committed.
  - Prevents issues like dirty reads, non-repeatable reads, and phantom reads; managed via locking or multiversion concurrency control (MVCC).
- **Durability**: 
  - Once a transaction commits, its effects are permanently stored in the database.
  - Survives system failures (e.g., power outage) through mechanisms like write-ahead logging or backups.

## Importance for Exam Preparation
- ACID properties are critical for maintaining data integrity in DBMS.
- Understand each property with practical examples (e.g., atomicity in bank transactions).
- Know how DBMS implements these properties via concurrency control and recovery techniques.
- Delhi University syllabus: Focus on Module 3 (Transactions) and Module 4 (Concurrency Control) as per NEP 2024.

## Conclusion
The ACID properties form the backbone of reliable transaction management in DBMS. For the Delhi University BSc Physical Science (CS) exam, master the definitions, implications, and examples of each property to ensure thorough revision.