# **Distributed Systems: Chapter 17.1-17.6**

## **Introduction to Distributed Transactions**

A distributed transaction is a sequence of operations that are executed as a single, all-or-nothing unit of work across multiple resources in different locations.

## **Definition of a Distributed Transaction**

A distributed transaction is a composite transaction that involves multiple autonomous database systems or other resources. It is a transaction that spans multiple sites, and its success or failure is dependent on the successful completion of all the operations.

## **Types of Distributed Transactions**

- **Flat Distributed Transaction**: A flat transaction is one in which all the resources involved in the transaction are at the same level of autonomy.
- **Nested Distributed Transaction**: A nested transaction is one in which some resources are at one level of autonomy and some are at a higher or lower level.

### Flat Distributed Transactions

#### Characteristics

- All resources involved are at the same level of autonomy
- All resources are subject to the same recovery rules
- Failure of any resource will result in failure of the entire transaction

#### Example

Suppose we have a banking system with multiple branches. We want to transfer money from branch A to branch B.

| Transaction ID | Branch A | Branch B  |
| -------------- | -------- | --------- |
| 1              | Withdrew | Deposited |

In a flat distributed transaction, both branches A and B are subject to the same recovery rules. If branch A fails to withdraw the money, the entire transaction will be rolled back.

### Nested Distributed Transactions

#### Characteristics

- Some resources are at one level of autonomy, while others are at a higher or lower level
- Each resource is subject to its own recovery rules
- Failure of any resource will result in the failure of the entire transaction, but some resources may be recovered

#### Example

Suppose we have a banking system with multiple branches. We want to transfer money from branch A to branch B, and also update the account balance of both branches.

| Transaction ID | Branch A | Branch B  |
| -------------- | -------- | --------- |
| 1              | Withdrew | Deposited |
| 2              | Updated  | Updated   |

In a nested distributed transaction, branch A and branch B have different levels of autonomy. Branch A's withdrawal may fail, but branch B's update may succeed, resulting in partial recovery.

### Characteristics of Distributed Transactions

- **Atomicity**: The transaction must be executed as a single, all-or-nothing unit of work.
- **Consistency**: The transaction must maintain the consistency of the data across all resources.
- **Isolation**: The transaction must prevent any interference with other transactions.
- **Durability**: The transaction must ensure that the effects of the transaction are permanent.

### Approaches to Implementing Distributed Transactions

- **Two-Phase Commit (2PC)**: A protocol that involves two phases: prepare and commit.
- **Pessimistic Locking**: A locking mechanism that prevents other transactions from accessing the resources until the transaction is complete.
- **Optimistic Locking**: A locking mechanism that allows multiple transactions to access the resources concurrently, but uses version numbers to detect conflicts.

### Challenges in Implementing Distributed Transactions

- **Scalability**: Distributed transactions can be difficult to scale as the number of resources increases.
- **Fault Tolerance**: Distributed transactions can be difficult to recover from failures.
- **Concurrency**: Distributed transactions can be difficult to manage concurrency.
