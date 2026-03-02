# Transaction Concepts (ACID)

## Introduction
In database management systems, transactions form the fundamental unit of work that ensures data consistency and reliability. A transaction represents a logical sequence of database operations that must either fully complete (commit) or fully roll back, maintaining the system's integrity even during failures. The ACID properties (Atomicity, Consistency, Isolation, Durability) provide the theoretical foundation for reliable transaction processing.

Transactions are critical in real-world applications like banking systems, airline reservations, and e-commerce platforms where multiple operations must be executed as a single logical unit. For instance, when transferring money between accounts, both debit and credit operations must succeed together or fail together to prevent financial discrepancies.

With the increasing complexity of distributed systems and high-concurrency environments, understanding transaction management has become essential for designing robust database applications. The ACID properties ensure predictable behavior even when multiple users access the database simultaneously or system failures occur.

## Key Concepts
1. **Atomicity**: 
   - Ensures "all or nothing" execution
   - Implemented using UNDO/REDO logs
   - Example: If a transaction updates 3 records, all 3 must commit or none

2. **Consistency**:
   - Maintains database invariants
   - Enforced through constraints (PK, FK, checks)
   - Transaction moves database from one valid state to another

3. **Isolation**:
   - Concurrent transactions don't interfere
   - Achieved via locking (shared/exclusive locks) or MVCC
   - Isolation levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable

4. **Durability**:
   - Committed changes survive system failures
   - Implemented using write-ahead logging (WAL)
   - Requires proper flush to persistent storage

5. **Transaction States**:
   - Active → Partially Committed → Committed
   - Failed → Aborted → Terminated

6. **Concurrency Control**:
   - Lock-based protocols (Two-Phase Locking)
   - Timestamp ordering
   - Optimistic concurrency control

7. **Recovery Techniques**:
   - Shadow paging
   - ARIES (Algorithms for Recovery and Isolation Exploiting Semantics)

## Examples

**Example 1: Bank Transfer**
```
BEGIN TRANSACTION;
UPDATE Accounts SET balance = balance - 1000 WHERE acc_no = 'A';
UPDATE Accounts SET balance = balance + 1000 WHERE acc_no = 'B';
COMMIT;
```
*Atomicity*: If either UPDATE fails, both are rolled back  
*Consistency*: Total balance remains same (A+B before = A+B after)  
*Isolation*: Other transactions see either pre-transfer or post-transfer state  
*Durability*: Once committed, survives power failure

**Example 2: Concurrent Booking System**
Two users trying to book last airline seat:
```sql
-- Transaction T1
BEGIN;
SELECT seats FROM flights WHERE id=101; -- Returns 1
UPDATE flights SET seats = 0 WHERE id=101;
COMMIT;

-- Transaction T2 (concurrent)
BEGIN;
SELECT seats FROM flights WHERE id=101; -- What isolation level allows seeing 1 or 0?
```
Solution: Use SERIALIZABLE isolation level with row-level locking to prevent lost updates

**Example 3: Crash Recovery**
1. Transaction writes "BEGIN" to log
2. Updates record X (log: <T1, X, old=5, new=10>)
3. System crashes before commit
4. On recovery: Check log, find uncommitted T1, perform UNDO using before-image (X=5)

## Exam Tips
1. Always mention all four ACID properties when asked about transactions
2. For isolation levels: Remember the anomaly matrix (dirty reads, non-repeatable reads, phantom reads)
3. In numerical problems: Use two-phase locking diagrams with growing/shrinking phases
4. Real-world scenario questions: Link ACID properties to banking/booking systems
5. Recovery questions: Focus on log-based recovery (UNDO/REDO phases)
6. Concurrency control: Compare pessimistic vs optimistic approaches
7. Always differentiate between system crash (needs durability) vs transaction abort (needs atomicity)