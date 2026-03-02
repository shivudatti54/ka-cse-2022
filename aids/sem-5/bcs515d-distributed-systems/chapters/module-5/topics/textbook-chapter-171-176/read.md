# **Distributed Systems**

### Chapter 17.1-17.6: Distributed Transactions

#### 17.1 Introduction to Distributed Transactions

A distributed transaction is a sequence of operations that are executed as a single, all-or-nothing unit of work across multiple systems or nodes in a distributed system. The characteristics of a distributed transaction include:

- **Atomicity**: The transaction is either complete or not complete, with no partial execution.
- **Consistency**: The transaction maintains the consistency of the data across all participating systems.
- **Isolation**: The transaction is executed independently of other transactions, without affecting their execution.
- **Durability**: The transaction's effects are permanent and survive even in the event of system failures.

#### 17.2 Flat Distributed Transactions

A flat distributed transaction is a single transaction that spans multiple systems, but does not involve any inter-system communication. Each system performs the required operations as a single, indivisible unit.

**Characteristics of Flat Distributed Transactions:**

- No inter-system communication
- Each system performs the required operations as a single unit
- No rollback or recovery required

**Example:**
A bank customer initiates a transaction to deposit money into their account and transfer funds to another account. Both operations are performed by separate systems (bank's accounting system and transfer system), but the transaction is considered flat since it does not involve inter-system communication.

#### 17.3 Nested Distributed Transactions

A nested distributed transaction is a transaction that involves inter-system communication and is composed of multiple, independent transactions.

**Characteristics of Nested Distributed Transactions:**

- Involves inter-system communication
- Composed of multiple, independent transactions
- May involve rollback or recovery in case of failures

**Example:**
A bank customer initiates a transaction to deposit money into their account and transfer funds to another account. The deposit operation is performed by the bank's accounting system, while the transfer operation is performed by the transfer system. The transaction is nested since it involves inter-system communication, and the customer's account is updated in two separate systems.

#### 17.4 Distributed Transaction Protocols

Distributed transaction protocols are used to manage and coordinate the execution of distributed transactions.

**Types of Distributed Transaction Protocols:**

- **Two-Phase Commit (2PC)**: A protocol used to commit a distributed transaction by sending messages to all participating systems.
- **Lectus**: A protocol used to perform distributed transactions by maintaining a read-replicas of the data.
- **Distributed Locking**: A protocol used to synchronize access to shared resources in a distributed system.

#### 17.5 Distributed Transaction Management

Distributed transaction management involves the recovery of distributed transactions in case of failures.

**Types of Distributed Transaction Recovery:**

- **Rollback Recovery**: Reverts the transaction to its previous state in case of failure.
- **Commit Recovery**: Ensures that the transaction is committed to the database in case of failure.

#### 17.6 Distributed Transaction Security

Distributed transaction security involves ensuring the integrity and confidentiality of distributed transactions.

**Types of Distributed Transaction Security:**

- **Authentication**: Verifies the identity of users and systems participating in the transaction.
- **Authorization**: Controls access to shared resources in the transaction.
- **Encryption**: Protects the data transmitted during the transaction.

By understanding the concepts and protocols outlined in this chapter, you can design and implement distributed transactions that ensure the integrity and consistency of data across multiple systems.
