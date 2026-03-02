# Concurrency Control Techniques

## Introduction
Concurrency control techniques are fundamental mechanisms in database management systems (DBMS) that ensure correct results from concurrent transaction executions while maintaining data consistency. In modern applications like banking systems, e-commerce platforms, and airline reservations, multiple transactions access shared data simultaneously. Without proper control, this could lead to conflicts resulting in lost updates, dirty reads, or inconsistent analysis.

The ACID properties (Atomicity, Consistency, Isolation, Durability) mandate that transactions execute in isolation. Concurrency control protocols like locking, timestamp ordering, and multiversion concurrency control enable efficient parallel execution while preserving these properties. For DU MCA students, understanding these techniques is critical for designing high-performance database systems and troubleshooting real-world issues like deadlocks in fintech applications.

## Key Concepts
1. **Lock-Based Protocols**
   - **Shared (S) and Exclusive (X) Locks**: Shared locks allow read-only access, while exclusive locks permit write operations
   - **Two-Phase Locking (2PL)**: Growing phase (acquiring locks) and shrinking phase (releasing locks)
   - **Strict 2PL**: Holds all exclusive locks until transaction commit

2. **Timestamp Ordering**
   - Assigns unique timestamp to each transaction
   - Ensures serializability by enforcing timestamp order using:
     - **Thomas Write Rule**: Allows obsolete writes to be ignored
     - **Read/Write Timestamp Validation**

3. **Multiversion Concurrency Control (MVCC)**
   - Maintains multiple versions of data items
   - Snapshot isolation for read operations
   - Used in PostgreSQL and Oracle

4. **Deadlock Handling**
   - Prevention: Wait-Die and Wound-Wait schemes
   - Detection: Wait-for graphs with cycle detection
   - Recovery: Transaction rollback and victim selection

## Examples
**Example 1: Lock-Based Protocol**
```
Transaction T1:          Transaction T2:
1. S-Lock(A)             1. S-Lock(B)
2. Read(A)               2. Read(B)
3. X-Lock(B)             3. X-Lock(A)
4. Write(B = A+B)       4. Write(A = B+A)
```
*Solution*: Without proper locking, this could create deadlock. Using 2PL:
- T1 acquires S(A), then X(B)
- T2 acquires S(B), then blocks on X(A) request
- System detects deadlock via wait-for graph and aborts one transaction

**Example 2: Timestamp Ordering**
```
Transactions: T1(TS=100), T2(TS=150)
Data Item X: W-TS=80, R-TS=90

T1 writes X → Allowed (100 > 80)
T2 reads X → Must check:
   - T2's TS(150) > W-TS(100) → Read proceeds
   - Update R-TS(X) to max(90,150) = 150
```

**Example 3: Deadlock Prevention (Wait-Die Scheme)**
```
T1(TS=10) requests lock held by T2(TS=20)
→ T1 is older (10 < 20): Waits (Wait-Die)
If T2 requests lock held by T1:
→ T2 is younger: Aborts (Die)
```

## Exam Tips
1. Always mention ACID properties when discussing concurrency control objectives
2. For 2PL questions, clearly distinguish between growing/shrinking phases
3. In timestamp problems, compare transaction TS with data item's R-TS/W-TS
4. Deadlock handling questions often require drawing wait-for graphs
5. Real-world applications: MVCC in PostgreSQL, optimistic concurrency in e-commerce
6. Remember Strict 2PL prevents cascading rollbacks
7. Conflict vs View serializability: Use precedence graphs for analysis