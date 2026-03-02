# Transactions and ACID Properties

## Introduction

A transaction is one of the most fundamental concepts in database management systems, representing a logical unit of work that must be executed as a single, atomic operation. In real-world applications, databases frequently encounter scenarios where multiple related operations must either all succeed together or all fail together. Consider a banking system where money is transferred from one account to another—this involves debiting one account and crediting another. If only one operation succeeds while the other fails, the database would be left in an inconsistent state, leading to serious financial discrepancies.

The concept of transactions becomes even more critical when we consider the multi-user environment of modern database systems. Multiple users may simultaneously access and modify the same data, creating potential conflicts that could compromise data integrity. Without proper transaction management, scenarios like double-spending, lost updates, or reading uncommitted data could easily occur, making the database unreliable for business operations.

This topic explores the ACID properties—the gold standard for reliable transaction processing—which form the backbone of every robust database system. Understanding these properties is essential for any computer science student, as they are fundamental to building applications that handle critical data reliably. Whether you are developing e-commerce platforms, reservation systems, or financial applications, mastery of transactions and ACID properties is non-negotiable for ensuring data consistency and system reliability.

## Key Concepts

### What is a Transaction?

A transaction is a logical unit of work consisting of one or more SQL statements that are executed as a single unit of computation. A transaction transforms the database from one consistent state to another consistent state. In database terminology, a transaction has a clearly defined beginning and end, and it is marked by two special statements: BEGIN TRANSACTION (or simply BEGIN) and COMMIT or ROLLBACK.

The COMMIT statement permanently saves all changes made during the transaction to the database, while ROLLBACK undoes all changes, restoring the database to its state before the transaction began. This all-or-nothing approach is what ensures data integrity in critical applications.

### ACID Properties

The ACID model defines four crucial properties that every reliable transaction processing system must guarantee:

**Atomicity** ensures that a transaction is treated as a single indivisible unit. Either all operations within the transaction are successfully completed and their effects are permanently recorded in the database, or none of them are applied. There is no intermediate state—either the entire transaction succeeds or it fails entirely. For example, in an airline reservation system, when a passenger books a seat, the system must simultaneously update the seat availability, create a booking record, and process payment. If any of these operations fails, all changes must be rolled back to maintain consistency.

**Consistency** guarantees that a transaction, when completed, transforms the database from one valid state to another valid state. All integrity constraints, triggers, and rules defined in the database must be satisfied after the transaction completes. If a transaction violates any database constraint, it should be aborted, and changes should be rolled back. For instance, if a database has a constraint that states an employee's department number must exist in the department table, any transaction inserting an employee with an invalid department number must fail to maintain consistency.

**Isolation** ensures that concurrently executing transactions appear to execute serially—one after another without interleaving. The intermediate results of a transaction are not visible to other transactions until the transaction is committed. This prevents concurrent transactions from interfering with each other. However, strict isolation can reduce concurrency, so database systems provide different isolation levels that balance between consistency and performance.

**Durability** guarantees that once a transaction has been committed, its effects are permanent and survive any subsequent system failures, including power outages, crashes, or hardware failures. The database system must ensure that committed changes are recorded in non-volatile storage (typically disk) before acknowledging transaction completion to the user.

### Transaction States

A transaction can be in one of several states throughout its lifecycle:

- **Active**: The transaction is currently being executed, and SQL statements are being processed.
- **Partially Committed**: All statements have been executed, but the changes are still held in memory and have not been permanently written to disk.
- **Committed**: The transaction has been successfully completed, and all changes have been permanently saved to the database.
- **Failed**: The transaction could not be completed successfully due to an error or user intervention.
- **Aborted**: The transaction has been rolled back, and the database has been restored to its state before the transaction began.

### Concurrency Control

In multi-user database systems, multiple transactions often execute simultaneously. Concurrency control mechanisms ensure that concurrent transactions do not interfere with each other and that the final database state is consistent. The two primary approaches are locking and timestamp-based protocols.

**Locking protocols** use locks to control access to data items. A transaction must acquire a lock before reading or modifying data. Common lock types include shared locks (for reading) and exclusive locks (for writing). Two-phase locking (2PL) is a popular protocol where a transaction can acquire locks but cannot release any lock after it has started releasing locks.

**Timestamp-based protocols** assign unique timestamps to each transaction and use these timestamps to determine the order of execution, ensuring serializability without requiring locks.

### Serializability

Serializability is the concept that defines correct concurrent execution. A schedule (the order of operations from multiple transactions) is serializable if it produces the same result as some serial execution of the same transactions. Serializable schedules ensure that the database remains consistent even when transactions execute concurrently.

## Examples

### Example 1: Banking Fund Transfer

Consider a bank database with two tables: accounts(id, balance) and transactions(id, from_acc, to_acc, amount, timestamp). A fund transfer of ₹5000 from account A (id: 101, balance: ₹50000) to account B (id: 102, balance: ₹30000) proceeds as follows:

**Step 1: BEGIN TRANSACTION**
```sql
START TRANSACTION;
```

**Step 2: Debit from source account**
```sql
UPDATE accounts SET balance = balance - 5000 WHERE id = 101;
-- Balance of account 101 becomes ₹45000
```

**Step 3: Credit to destination account**
```sql
UPDATE accounts SET balance = balance + 5000 WHERE id = 102;
-- Balance of account 102 becomes ₹35000
```

**Step 4: Record the transaction**
```sql
INSERT INTO transactions (from_acc, to_acc, amount) VALUES (101, 102, 5000);
```

**Step 5: COMMIT**
```sql
COMMIT;
```

If step 2 succeeds but step 3 fails (perhaps due to a constraint violation or system crash), the ROLLBACK statement would undo the debit from account 101, ensuring that money is neither lost nor created out of thin air. This demonstrates **atomicity**.

### Example 2: Order Processing System

An e-commerce order processing transaction involves multiple tables:

```sql
START TRANSACTION;

-- 1. Check product availability
SELECT stock_quantity INTO @available FROM products WHERE product_id = 1001;
IF @available < @order_quantity THEN
    ROLLBACK;
    SIGNAL 'Insufficient stock';
END IF;

-- 2. Reduce inventory
UPDATE products SET stock_quantity = stock_quantity - @order_quantity 
WHERE product_id = 1001;

-- 3. Create order record
INSERT INTO orders (customer_id, product_id, quantity, total_amount) 
VALUES (@customer_id, 1001, @order_quantity, @total);

-- 4. Update customer order history
INSERT INTO customer_orders (customer_id, order_id) VALUES (@customer_id, LAST_INSERT_ID());

-- 5. Process payment (simulated)
INSERT INTO payments (order_id, amount, status) VALUES (LAST_INSERT_ID(), @total, 'COMPLETED');

COMMIT;
```

If any step fails (insufficient stock, payment failure, constraint violation), the entire transaction is rolled back. The database maintains **consistency** because all constraints are checked before commit, and the inventory, orders, and payment records remain synchronized.

### Example 3: Demonstrating Isolation Levels

```sql
-- Transaction A (READ UNCOMMITTED level)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
SELECT balance FROM accounts WHERE id = 101;  -- May see uncommitted changes
COMMIT;

-- Transaction B (SERIALIZABLE level)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
UPDATE accounts SET balance = balance + 5000 WHERE id = 101;
COMMIT;
```

At READ UNCOMMITTED level, Transaction A might read data that Transaction B has modified but not yet committed—this is called a "dirty read." At SERIALIZABLE level, such anomalies are prevented, but concurrency is reduced.

## Exam Tips

1. **Remember the full form of ACID**: Atomicity, Consistency, Isolation, Durability. In exams, always explain each property with a concrete example to score full marks.

2. **Differentiate between COMMIT and ROLLBACK**: COMMIT makes all transaction changes permanent, while ROLLBACK undoes all changes, restoring the database to its state before the transaction began.

3. **Understand transaction states**: Remember the five states (Active, Partially Committed, Committed, Failed, Aborted) and what each means for exam questions on transaction lifecycle.

4. **Isolation levels are frequently tested**: Be thorough with READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE levels, including the anomalies each prevents (dirty read, non-repeatable read, phantom read).

5. **Serializability is key for concurrency**: A serializable schedule is equivalent to some serial schedule—understand conflict serializability and view serializability concepts.

6. **Two-Phase Locking (2PL)**: Remember that the growing phase cannot release locks, and the shrinking phase cannot acquire new locks. This is a common exam topic.

7. **Real-world applications**: When explaining ACID properties, use real examples like banking transactions, airline bookings, or inventory management to demonstrate understanding beyond textbook definitions.

8. **SQL transaction commands**: Know the syntax for BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and SET TRANSACTION in SQL—practical questions often require writing SQL code.