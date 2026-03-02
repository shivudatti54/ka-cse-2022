# Transactions ACID Properties
## Database Management Systems - BSc Physical Science (CS), Delhi University (NEP 2024)

---

## 1. Introduction and Real-World Relevance

Imagine you transfer ₹5,000 from your savings account to your friend's account via a banking app. What happens if the system crashes after deducting ₹5,000 from your account but before adding it to your friend's account? You lose ₹5,000! This is precisely why **ACID properties** exist in database management systems.

In today's digital world, where millions of financial transactions, hotel bookings, and inventory updates occur every second, the integrity of data is paramount. Whether you're ordering food online, booking a flight, or processing an e-commerce order—every operation that modifies database state must be handled with absolute reliability.

This chapter covers the foundational ACID properties that ensure database transactions are processed reliably, which is essential for the **Delhi University BSc CS (NEP 2024)** curriculum under **GE3A: Database Management Systems**.

---

## 2. What is a Transaction?

A **transaction** is a logical unit of work that consists of one or more database operations (like INSERT, UPDATE, DELETE) treated as a single atomic unit. A transaction represents a change in the database state.

### Key Characteristics of a Transaction:
- A transaction begins when a SQL statement is executed
- It ends with either a **COMMIT** (save changes) or **ROLLBACK** (undo changes)
- Transactions transform the database from one consistent state to another

### Transaction States:
```
ACTIVE → PARTIALLY COMMITTED → COMMITTED
                     ↓
               FAILED
                     ↓
               ABORTED
```

---

## 3. ACID Properties - The Four Pillars of Reliable Transactions

### 3.1 Atomicity (The "All-or-Nothing" Principle)

**Definition:** Atomicity ensures that a transaction is treated as a single indivisible unit. Either **all** operations within the transaction are executed successfully, or **none** of them are applied to the database.

**Why it matters:** If any part of a transaction fails, the entire transaction is aborted, and the database remains unchanged—as if the transaction never happened.

**Example - Bank Transfer:**
```sql
-- Transaction T1: Transfer ₹5000 from Account A to Account B
BEGIN TRANSACTION;

-- Step 1: Deduct from Account A
UPDATE accounts 
SET balance = balance - 5000 
WHERE account_id = 'A';

-- Step 2: Add to Account B
UPDATE accounts 
SET balance = balance + 5000 
WHERE account_id = 'B';

-- If both succeed, commit
COMMIT;

-- If any step fails, rollback
-- ROLLBACK;  (executed automatically on error)
```

In this example, either both UPDATE statements succeed, or neither does. The database never shows ₹5000 deducted from A but not added to B.

**Atomicity Implementation:**
- **Write-Ahead Logging (WAL):** All changes are logged before being applied
- **Shadow Paging:** Changes are written to a temporary copy, then swapped
- DBMS automatically handles rollback using these mechanisms

---

### 3.2 Consistency (Maintaining Database Integrity)

**Definition:** Consistency ensures that a transaction transforms the database from one valid state to another, maintaining all database constraints, triggers, and rules.

**Why it matters:** The database must satisfy all integrity constraints after a transaction completes. If a transaction would violate any constraint, it is aborted.

**Examples of Constraints Preserved:**
- **Primary Key:** No duplicate values
- **Foreign Key:** Referential integrity maintained
- **Check Constraints:** Values within specified ranges
- **User-defined constraints:** Business rules

**Example - Account Balance Consistency:**
```sql
-- Constraint: Account balance cannot be negative
CREATE TABLE accounts (
    account_id VARCHAR(10) PRIMARY KEY,
    balance DECIMAL(10,2) CHECK (balance >= 0)
);

-- This transaction will FAIL if balance goes negative
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 10000 
WHERE account_id = 'A';
-- If balance was only ₹5000, constraint violation occurs
-- Transaction is rolled back automatically
COMMIT;
```

**Consistency vs. Atomicity:**
| Aspect | Atomicity | Consistency |
|--------|-----------|-------------|
| Focus | All-or-nothing execution | Valid state to valid state |
| Handles | System failures | Constraint violations |
| Role | Mechanism | Constraint enforcement |

---

### 3.3 Isolation (Concurrent Execution Transparency)

**Definition:** Isolation ensures that concurrent transactions execute as if they were sequential, preventing interference. The intermediate state of one transaction is invisible to other concurrent transactions.

**Why it matters:** Without isolation, multiple users accessing the database simultaneously could cause data anomalies.

**Example - Concurrent Ticket Booking:**
```sql
-- User 1: Book a ticket for Show A
BEGIN;
SELECT seats_available FROM shows WHERE show_id = 101;
-- Result: 5 seats available

-- User 2: Book a ticket for Show A (concurrent)
BEGIN;
SELECT seats_available FROM shows WHERE show_id = 101;
-- Result: 5 seats available (same!)

-- User 1: Book ticket
UPDATE shows SET seats_available = seats_available - 1 
WHERE show_id = 101;
COMMIT; -- Now 4 seats

-- User 2: Book ticket
UPDATE shows SET seats_available = seats_available - 1 
WHERE show_id = 101;
COMMIT; -- Now 3 seats (WRONG! Should be 3, not 4 tickets booked)
```

Without proper isolation, both users see 5 seats, book tickets, and end up with only 3 seats remaining after 2 bookings—one seat was "lost" due to concurrent modification.

**Isolation Levels (covered in detail in Section 7)** control how visible intermediate states are to other transactions.

---

### 3.4 Durability (Persistence of Committed Data)

**Definition:** Durability guarantees that once a transaction is committed, its effects are permanently saved in the database, surviving any subsequent system failures.

**Why it matters:** Even if the system crashes immediately after a COMMIT, the changes must persist.

**Durability Implementation:**
- **Write-Ahead Logging (WAL):** Transaction logs are written to stable storage before data changes
- **Checkpoints:** Periodic snapshots of database state
- **Redundant Storage:** RAID, replication across multiple systems

**Example:**
```sql
-- After successful commit, even if database server crashes:
BEGIN;
INSERT INTO transactions (tx_id, amount, timestamp) 
VALUES ('TXN001', 5000, NOW());
COMMIT;

-- System crashes 0.001 seconds later
-- When system restarts: the INSERT is still present in database
```

---

## 4. Transaction Control Commands

The DU CS syllabus emphasizes practical transaction control. These commands manage transaction boundaries:

### 4.1 COMMIT
Saves all changes made during the transaction to the database.

```sql
BEGIN;
UPDATE account SET balance = balance - 1000 WHERE id = 1;
UPDATE account SET balance = balance + 1000 WHERE id = 2;
COMMIT;  -- All changes are now permanent
```

### 4.2 ROLLBACK
Undoes all changes made during the transaction, restoring the database to its previous state.

```sql
BEGIN;
UPDATE products SET price = 50 WHERE id = 101;
-- Something went wrong
ROLLBACK;  -- Price change is undone
```

### 4.3 SAVEPOINT
Creates intermediate points within a transaction, allowing partial rollback.

```sql
BEGIN;
INSERT INTO orders (id, item) VALUES (1, 'Laptop');
SAVEPOINT sp1;

INSERT INTO orders (id, item) VALUES (2, 'Mouse');
SAVEPOINT sp2;

-- Rollback to first savepoint
ROLLBACK TO SAVEPOINT sp1;

COMMIT;  -- Only the laptop order is committed
```

---

## 5. Concurrency Problems

When multiple transactions execute simultaneously, several problems can arise. Understanding these is essential for the DU syllabus:

### 5.1 Lost Update Problem
Two transactions read and modify the same data, causing one update to be "lost."

```
Time    Transaction A        Transaction B        Account Balance
T1      READ: 1000           
T2                           READ: 1000          
T3      WRITE: 1000 + 100    
T4                           WRITE: 1000 + 200   
T5      COMMIT (1100)        
T6                           COMMIT (1200)        1200
                                                       
-- Update from A (1100) is LOST! Result should be 1300
```

### 5.2 Dirty Read
A transaction reads data written by another uncommitted transaction.

```
Time    Transaction A        Transaction B        
T1                           UPDATE: balance = 500
T2      READ: 500 (dirty!)   
T3                           ROLLBACK             
T3      -- A has read incorrect data!
```

### 5.3 Non-Repeatable Read
A transaction reads the same row twice but gets different values.

```
Time    Transaction A        Transaction B        
T1      READ: balance = 1000 
T2                           UPDATE: balance = 1500
T3      READ: balance = 1500 (different!)
```

### 5.4 Phantom Read
A transaction re-executes a query but sees new rows (phantoms).

```
Time    Transaction A        Transaction B        
T1      SELECT * FROM orders WHERE status = 'pending'
       -- Returns 5 rows
T2                           INSERT INTO orders VALUES (...)
T3      SELECT * FROM orders WHERE status = 'pending'
       -- Returns 6 rows (phantom!)
```

---

## 6. Serializability

**Serializability** is the gold standard for concurrent transaction execution. A schedule is **serializable** if it produces the same result as some serial (one-after-another) execution of the transactions.

### 6.1 Conflict Serializability
Two operations **conflict** if they access the same data item and at least one is a WRITE. There are three conflict types:

1. **Read-Write Conflict** (Unrepeatable Read)
2. **Write-Read Conflict** (Dirty Read)
3. **Write-Write Conflict** (Lost Update)

A schedule is conflict-serializable if we can reorder non-conflicting operations to form an equivalent serial schedule.

### 6.2 Testing Serializability (Precedence Graph)
```
Algorithm:
1. For each transaction Ti that reads data written by Tj (where Tj wrote first),
   create edge Ti → Tj
2. If the graph has NO cycles, schedule is conflict-serializable
```

### Example - Testing Serializability:

```
Schedule S:
T1: R(X), W(X)
T2: R(X), W(X)

Precedence Graph:
- T1 reads X written by T2? No
- T2 reads X written by T1? No
- T1 writes X, T2 writes X (conflict) → Edge T1 → T2

Graph: T1 → T2 (No cycle!)
Result: Serializable (equivalent to T1 then T2)
```

---

## 7. Isolation Levels

SQL standard defines four isolation levels, each preventing specific concurrency problems:

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|-----------------|------------|---------------------|--------------|
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Not Possible | Possible | Possible |
| REPEATABLE READ | Not Possible | Not Possible | Possible |
| SERIALIZABLE | Not Possible | Not Possible | Not Possible |

### Setting Isolation Level in SQL:
```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- Or per query:
SELECT * FROM accounts WITH (HOLDLOCK);  -- Equivalent to SERIALIZABLE
```

---

## 8. Comprehensive Examples

### Example 1: E-Commerce Order Processing
```sql
-- Transaction: Process a customer order
BEGIN TRANSACTION;

-- Step 1: Check product availability
SELECT stock_quantity INTO @available 
FROM products WHERE product_id = 1001;

IF @available < 5 THEN
    ROLLBACK;
    SELECT 'Insufficient stock' AS message;
ELSE
    -- Step 2: Reduce inventory
    UPDATE products 
    SET stock_quantity = stock_quantity - 5 
    WHERE product_id = 1001;
    
    -- Step 3: Create order record
    INSERT INTO orders (order_id, customer_id, product_id, quantity) 
    VALUES (ORD_SEQ.NEXTVAL, 5001, 1001, 5);
    
    -- Step 4: Charge customer
    UPDATE customers 
    SET account_balance = account_balance + (5 * price) 
    WHERE customer_id = 5001;
    
    COMMIT;
    SELECT 'Order processed successfully' AS message;
END IF;
```

### Example 2: University Grade Recording (with Serializability)
```sql
-- Scenario: Professor records grades for two courses
-- Transaction T1: Update Course A grades
-- Transaction T2: Update Course B grades (concurrent)

-- These are serializable (no data dependency between courses)

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;

UPDATE enrollments 
SET grade = 'A' 
WHERE course_id = 'CS101' AND student_id = 'S001';

COMMIT;

-- T2 can run serially before or after T1
```

---

## 9. Multiple Choice Questions (MCQs)

### Easy Level
1. **Which ACID property ensures that a transaction is treated as a single unit?**
   - A) Consistency
   - B) Atomicity
   - C) Isolation
   - D) Durability
   - **Answer: B**

2. **What does COMMIT do in a transaction?**
   - A) Undoes all changes
   - B) Saves all changes permanently
   - C) Pauses the transaction
   - D) Creates a savepoint
   - **Answer: B**

### Medium Level
3. **Which concurrency problem occurs when two transactions read the same data and both modify it, causing one update to be lost?**
   - A) Dirty Read
   - B) Non-Repeatable Read
   - C) Lost Update
   - D) Phantom Read
   - **Answer: C**

4. **In a precedence graph for testing serializability, what indicates a cycle?**
   - A) Schedule is serializable
   - B) Schedule is not serializable
   - C) Schedule is conflict-equivalent
   - D) None of the above
   - **Answer: B**

### Hard Level
5. **At which isolation level is it possible to have phantom reads?**
   - A) READ COMMITTED
   - B) REPEATABLE READ
   - C) SERIALIZABLE
   - D) Both A and B
   - **Answer: D**

6. **A schedule is conflict-serializable. What is true about it?**
   - A) It must be equivalent to some serial schedule
   - B) It always produces consistent results
   - C) It prevents all concurrency problems
   - D) It requires write locks on all data items
   - **Answer: A**

---

## 10. Flashcards with Context

### Flashcard 1: Atomicity
- **Term:** Atomicity
- **Simple Definition:** All-or-nothing execution of transactions
- **Context:** If a bank transfer fails mid-way (money deducted but not credited), atomicity ensures the entire transaction is rolled back—no partial updates persist
- **Mnemonic:** Think "ATOM" = indivisible

### Flashcard 2: Consistency
- **Term:** Consistency
- **Simple Definition:** Transaction transforms database from one valid state to another
- **Context:** When inserting a record with a foreign key, consistency ensures the referenced record exists; otherwise, the transaction fails
- **Mnemonic:** Think of "CONSTRAINT" = rules must be satisfied

### Flashcard 3: Isolation
- **Term:** Isolation
- **Simple Definition:** Concurrent transactions appear to execute sequentially
- **Context:** Two users booking the same flight seat simultaneously—isolation ensures only one booking succeeds, preventing overbooking
- **Mnemonic:** Think "ISO-LATE" = kept separate

### Flashcard 4: Durability
- **Term:** Durability
- **Simple Definition:** Committed data survives system failures
- **Context:** After clicking "Transfer Complete" in your banking app, even if your phone dies immediately, the transaction remains in the database
- **Mnemonic:** Think "DURA-BLE" = lasting forever

### Flashcard 5: Serializability
- **Term:** Serializability
- **Simple Definition:** A concurrent schedule producing same result as some serial execution
- **Context:** Required for critical applications like financial transactions—ensures correctness even with concurrent operations
- **Mnemonic:** Think "SERIES" = one after another

---

## 11. Key Takeaways

### Core Concepts:
1. **Transaction** is a logical unit of work that must follow ACID properties
2. **Atomicity** ensures all-or-nothing execution; implemented via logging and shadow paging
3. **Consistency** maintains database integrity constraints; transactions are aborted if constraints are violated
4. **Isolation** controls visibility of intermediate states; achieved through locking mechanisms
5. **Durability** guarantees permanence of committed changes; implemented via Write-Ahead Logging

### Transaction Control:
- **COMMIT** makes changes permanent
- **ROLLBACK** undoes all changes in the transaction
- **SAVEPOINT** allows partial rollback to intermediate points

### Concurrency Problems to Remember:
- **Lost Update:** Concurrent writes overwrite each other
- **Dirty Read:** Reading uncommitted data
- **Non-Repeatable Read:** Same row returns different values
- **Phantom Read:** New rows appear in re-executed queries

### Serializability:
- **Conflict Serializability** is tested using precedence graphs
- **No cycle** in precedence graph = serializable schedule
- **SERIALIZABLE** isolation level prevents all concurrency problems

### For Delhi University Exam:
- Understand how ACID properties work together
- Be able to identify concurrency problems from scenarios
- Know how to draw and interpret precedence graphs
- Remember the table of isolation levels and which problems they prevent

---

*Study material prepared for BSc Physical Science (CS), Delhi University NEP 2024 - GE3A: Database Management Systems*