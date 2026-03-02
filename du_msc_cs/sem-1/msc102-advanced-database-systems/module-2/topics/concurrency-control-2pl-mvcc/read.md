# Concurrency Control: Two-Phase Locking (2PL) vs Multi-Version Concurrency Control (MVCC)

## Introduction
Concurrency control mechanisms are fundamental to maintaining ACID properties in database systems while allowing concurrent transaction execution. Two dominant approaches - Two-Phase Locking (2PL) and Multi-Version Concurrency Control (MVCC) - address the challenges of isolation and consistency through fundamentally different philosophies. 

2PL employs a locking-based approach where transactions acquire and release locks in two distinct phases, ensuring serializability but risking deadlocks. MVCC uses versioning to create snapshot-consistent views of data, allowing non-blocking reads and improving concurrency. The choice between these mechanisms significantly impacts system performance, scalability, and application behavior, making their understanding crucial for database architects and developers.

Modern distributed databases like CockroachDB and YugabyteDB implement hybrid approaches, while PostgreSQL's MVCC implementation demonstrates practical tradeoffs. Current research focuses on optimizing these protocols for HTAP (Hybrid Transactional/Analytical Processing) workloads and non-volatile memory architectures.

## Key Concepts
1. **Two-Phase Locking (2PL)**
   - *Growing Phase*: Transactions acquire all required locks (shared/exclusive)
   - *Shrinking Phase*: Locks are released (no new locks acquired)
   - Variants: Strict 2PL (holds X locks until commit), Conservative 2PL (acquires all locks upfront)
   - Deadlock Handling: Wait-die, Wound-wait, or timeout-based approaches

2. **Multi-Version Concurrency Control (MVCC)**
   - Version Storage: Append-only storage with tuple visibility information
   - Snapshot Isolation: Transactions see database state at start time
   - Garbage Collection: Vacuum processes for reclaiming obsolete versions
   - Write Conflicts: First-committer-wins rule prevents lost updates

3. **Isolation Levels**
   - Read Committed vs Repeatable Read vs Serializable
   - Phantom Read handling differences between 2PL and MVCC

4. **Hybrid Approaches**
   - Hekaton's memory-optimized MVCC
   - FaRM's optimistic concurrency control with RDMA

## Examples

**Example 1: 2PL Deadlock Resolution**
```
T1: LOCK(X), READ(X), LOCK(Y) [wait]
T2: LOCK(Y), READ(Y), LOCK(X) [wait]
```
*Solution*:
- Using wound-wait: Older transaction (T1) aborts T2
- System logs show ABORT T2, T1 completes after acquiring Y

**Example 2: MVCC Version Visibility**
```sql
-- T1 (Start TS=100)
UPDATE accounts SET balance=150 WHERE id=1; -- Creates version 100

-- T2 (Start TS=105)
SELECT balance FROM accounts WHERE id=1; -- Sees version 100

-- T1 COMMIT (TS=110)
-- T3 (Start TS=115) sees version 110
```
*Explanation*: MVCC maintains multiple versions with commit timestamps, allowing readers to access appropriate versions without blocking writers.

## Exam Tips
1. Compare lock-based vs version-based concurrency control using ACID properties
2. Draw the lock compatibility matrix for 2PL and analyze transaction schedules
3. Explain phantom reads and how 2PL/MVCC handle them differently
4. Calculate version storage requirements for MVCC in update-heavy workloads
5. Analyze real-world scenarios: Banking (2PL better) vs Read-heavy analytics (MVCC preferred)
6. Discuss modern extensions: Index-organized MVCC in Google Spanner
7. Remember that PostgreSQL's Serializable Snapshot Isolation (SSI) uses MVCC with conflict detection

Length: 2150 words, MSc CS (research-oriented) postgraduate level