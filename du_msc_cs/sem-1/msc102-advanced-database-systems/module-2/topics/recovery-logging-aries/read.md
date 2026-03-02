# Recovery & Logging (ARIES)

## Introduction
Database recovery mechanisms are critical for ensuring ACID properties in transaction processing systems. The ARIES (Algorithms for Recovery and Isolation Exploiting Semantics) algorithm revolutionized crash recovery by introducing write-ahead logging with sophisticated analysis, redo, and undo phases. Developed by IBM researchers in 1992, ARIES remains foundational in modern DBMS like Oracle and SQL Server.

This topic gains significance in distributed databases and cloud-native systems where fault tolerance is paramount. Current research extends ARIES concepts to NewSQL databases and blockchain systems, making it essential for advanced database architects. For DU students, understanding ARIES provides critical insights into both theoretical underpinnings and industrial implementations of recovery systems.

## Key Concepts
1. **Write-Ahead Logging (WAL)**: All modifications recorded in log before actual data page updates
2. **Log Sequence Number (LSN)**: Unique identifier for log records enabling temporal ordering
3. **Checkpoints**:
   - Fuzzy Checkpoints: Allow concurrent transactions during checkpointing
   - Sharp Checkpoints: Block transactions momentarily
4. **ARIES Three-Phase Recovery**:
   - Analysis Phase: Identify dirty pages and active transactions at crash
   - Redo Phase: Reconstruct database state using log history
   - Undo Phase: Rollback uncommitted transactions
5. **CLR (Compensation Log Records)**: Special log entries for undo operations
6. **Dirty Page Table**: Tracks modified pages not yet written to disk

## Examples

**Example 1: Transaction Failure Recovery**
```
T1: BEGIN
T1: UPDATE Accounts SET balance = balance - 100 WHERE accno = 101
T1: UPDATE Accounts SET balance = balance + 100 WHERE accno = 202
SYSTEM CRASH AFTER FIRST UPDATE BUT BEFORE COMMIT

Recovery Steps:
1. Analysis: T1 was active at crash
2. Redo: Replay log record for first update
3. Undo: Compensate both updates using CLRs
4. Final State: Both accounts revert to original balances
```

**Example 2: Checkpoint Handling**
```
Log Sequence:
LSN100: BEGIN T1
LSN101: UPDATE T1 (Page P5)
LSN102: CHECKPOINT (Active Txns: T1)
LSN103: UPDATE T1 (Page P7)
CRASH OCCURS

Recovery Process:
- Last checkpoint at LSN102
- Redo from LSN100 (oldest active txn LSN)
- Undo uncommitted T1 operations up to LSN103
```

## Exam Tips
1. Always mention WAL principle before discussing ARIES specifics
2. Differentiate between physiological and physical logging
3. Remember that ARIES redoes from oldest dirty page, undoes from newest log record
4. Prepare to draw log sequence diagrams with LSN pointers
5. Contrast ARIES with shadow paging techniques
6. Understand the role of Transaction Table and Dirty Page Table in analysis phase
7. Practice calculating LSN chains for rollback operations

Length: 2500 words