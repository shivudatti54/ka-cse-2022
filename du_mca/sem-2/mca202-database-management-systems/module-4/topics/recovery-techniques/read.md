# Recovery Techniques in Database Management Systems

## Introduction

Database recovery techniques constitute a critical component of modern Database Management Systems (DBMS), ensuring that databases can return to a consistent state after experiencing various types of failures. In enterprise environments where data integrity is paramount, the ability to recover from failures without losing data or compromising consistency is not just desirable—it's absolutely essential. The University of Delhi's MCA program emphasizes recovery techniques because real-world database systems face constant threats from hardware failures, software bugs, human errors, and environmental disasters.

The importance of recovery mechanisms has grown exponentially with the increasing reliance of organizations on database-driven applications. Consider a banking transaction where money is being transferred between accounts—if the system crashes midway through the transaction, the database could be left in an inconsistent state where money is deducted from one account but not credited to another. Without robust recovery techniques, such scenarios could lead to significant financial losses and regulatory complications. This topic explores the theoretical foundations and practical implementations of recovery mechanisms that DBMS architects employ to maintain data integrity under adverse conditions.

Modern recovery techniques build upon fundamental concepts from transaction management, particularly the ACID properties (Atomicity, Consistency, Isolation, Durability). When a transaction fails to complete successfully, recovery mechanisms ensure that either all its effects are applied (commit) or none at all (abort). This chapter examines the classification of failures, the role of logging in recovery, checkpointing strategies, and advanced algorithms like ARIES that form the backbone of commercial database systems.

## Key Concepts

### Classification of Database Failures

Understanding the various types of failures is essential for designing appropriate recovery strategies. Database systems typically encounter four major categories of failures:

**Transaction Failures** occur when a transaction cannot complete due to logical errors or user requests. These include deadlocks (where transactions wait indefinitely for each other to release locks), validation failures (when a transaction cannot satisfy integrity constraints), and user-initiated aborts. Transaction failures are considered normal operational scenarios that the DBMS must handle gracefully.

**System Failures** encompass hardware malfunctions, operating system crashes, or software bugs that cause the entire DBMS to stop unexpectedly. The key characteristic of system failures is that the contents of main memory (including database buffers) are lost, while secondary storage typically remains intact. Examples include power outages, kernel panics, and application software crashes.

**Media Failures** involve physical damage to secondary storage devices holding the database. This category includes head crashes, controller failures, and file system corruption. Media failures are the most severe because they may result in permanent loss of data stored on the affected media.

**Natural Disasters** represent catastrophic events including fires, floods, earthquakes, and other environmental catastrophes that can destroy entire data centers. Recovery from such events requires off-site backup strategies and potentially geographic distribution of data.

### The Log-Based Recovery Approach

Log-based recovery is the most widely adopted technique in commercial database systems. The fundamental principle involves recording all modifications made by transactions to a separate log file before writing the actual data to disk. This approach enables the system to reconstruct database state even after catastrophic failures.

**Write-Ahead Logging (WAL)** is the cornerstone principle of log-based recovery. It mandates that the log record for a modification must be written to stable storage before the modified data is written to disk. This ensures that if a crash occurs, the log contains sufficient information to either redo committed transactions or undo uncommitted ones. The WAL protocol prevents the database from reaching an inconsistent state where data modifications exist without corresponding log records.

**Log Records** contain several critical fields: transaction identifier (identifies which transaction performed the operation), data item identifier (specifies which database object was modified), old value (the value before modification, needed for undo), and new value (the value after modification, needed for redo). Additionally, log records include a unique log sequence number (LSN) that enables efficient navigation through the log.

**Transaction Commit** in log-based systems follows a specific sequence: first, all log records for the transaction are force-written to stable storage (ensuring WAL); second, the commit record is written to the log; third, the actual data modifications are written to disk. This ordering ensures that committed transactions can be redone even if the data pages haven't been written to disk.

### Checkpointing Techniques

Checkpointing addresses the problem of potentially infinite recovery time by periodically creating consistent snapshots of the database state. A checkpoint record in the log indicates that all modifications before this point have been successfully written to disk.

**Types of Checkpoints**: Fuzzy checkpoints allow ongoing transactions to continue modifying the database during the checkpoint process, improving system performance. Consistent checkpoints require all active transactions to pause, ensuring the database is in a known good state. Most modern systems implement variations of fuzzy checkpointing to minimize disruption to normal processing.

The checkpoint record typically includes: the list of all active transactions at checkpoint time, the location of the last log record written by each active transaction, and pointers to dirty pages in the buffer pool. This information enables efficient recovery by limiting the scan to the portion of log created after the checkpoint.

### The ARIES Recovery Algorithm

ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), developed at IBM, represents the state-of-the-art in recovery techniques and influences virtually all modern database systems including IBM DB2, Microsoft SQL Server, and Oracle.

ARIES employs three main phases:

**Analysis Phase**: Upon recovery initiation, ARIES scans the log backward from the last checkpoint to identify all transactions that were active at the time of failure (loser transactions) and all dirty pages in the buffer pool. This phase determines the starting point for the redo phase and the set of transactions requiring undo.

**Redo Phase**: ARIES re-applies all updates from the log, starting from the appropriate point determined during analysis, to ensure all committed transactions' effects are reflected in the database. The redo phase is idempotent—it can be safely executed multiple times without adverse effects.

**Undo Phase**: ARIES rolls back all uncommitted transactions by processing their log records in reverse order (last-to-first), restoring affected data items to their pre-transaction values. The undo phase generates compensation log records (CLRs) that enable resumption of undo operations if another failure occurs during recovery.

### Shadow Paging

Shadow paging offers an alternative to log-based recovery by maintaining two versions of the database: a current master and a shadow copy. When a transaction modifies data, changes are written to new pages rather than overwriting existing pages. Upon transaction commit, the pointer to the current master is atomically switched to point to the new version, making the changes visible.

This technique provides natural recovery semantics—if a failure occurs, the system simply continues using the previous (shadow) copy. However, shadow paging faces challenges with storage overhead and the complexity of managing multiple versions, limiting its adoption in most commercial systems.

## Examples

### Example 1: Transaction Recovery with Immediate Update

Consider a simple banking database where transaction T1 transfers Rs. 1000 from account A (balance: Rs. 5000) to account B (balance: Rs. 3000). The DBMS uses immediate update with write-ahead logging.

**Transaction T1 operations:**
1. Read A (5000), subtract 1000 → write A (4000)
2. Read B (3000), add 1000 → write B (4000)
3. Commit

**Log sequence:**
- Log 1: `<T1, A, 5000, 4000>`
- Log 2: `<T1, B, 3000, 4000>`
- Log 3: `<T1, COMMIT>`

**Scenario: Crash occurs after writing new A value but before writing new B value**

During recovery, the system examines the log. Since T1 has a COMMIT record, the transaction was committed. However, only the update to A appears on disk. The recovery process performs **redo**: it re-applies the logged changes, updating B from 3000 to 4000. The final database state shows A=4000, B=4000—consistent and correct.

**Scenario: Crash occurs before commit (T1 never reached COMMIT)**

During recovery, T1 appears in the log but has no COMMIT record. The system performs **undo**: it restores A to its old value (5000). The database returns to its original state, as T1 never completed.

### Example 2: Checkpoint Recovery Analysis

Consider a system with three transactions (T1, T2, T3) where a checkpoint occurs at time C. The log shows:

```
CKPT (active: T2, T3)
<T1, COMMIT>
<T2, A, 100, 200>
<T3, B, 500, 600>
[CRASH]
```

**Analysis Phase**: The checkpoint indicates T2 and T3 were active. T1 has a COMMIT record, so it completed successfully before the crash. T2 and T3 were active at crash time—they are losers requiring undo.

**Redo Phase**: Starting from the checkpoint, we redo all operations. Both T2's update to A and T3's update to B are reapplied since they appear after the checkpoint. After redo: A=200, B=600.

**Undo Phase**: T2 and T3 are uncommitted, so we undo their changes. T3's change to B is undone first (600→500), then T2's change to A is undone (200→100). The final database state reflects only T1's committed changes.

### Example 3: ARIES CLR Handling

In ARIES, when undoing a transaction operation during recovery, the system writes a Compensation Log Record (CLR) instead of simply reversing the change. Suppose during undo of transaction T5, we need to undo an update: `<T5, X, 50, 75>`.

**CLR generated**: `<T5, X, 75, 50, undoNextLSN>`

The CLR records that T5 performed an update that changed X from 75 to 50. This is not a normal log record—it's an "undo" of a previous action. The CLR itself must be logged (following WAL) because if another crash occurs during recovery, the system must know that this undo operation was performed to avoid repeating it.

CLRs enable **recovery resilience**: if the system crashes during the undo phase, the next recovery can read the CLR and know that this portion of T5 has already been undone. The undo can resume from the undoNextLSN pointer rather than starting over.

## Exam Tips

1. **Understand the ACID properties and their relationship to recovery**: Atomicity ensures all-or-nothing transaction execution; Durability ensures committed changes survive failures. These properties directly drive recovery mechanism design.

2. **Memorize the Write-Ahead Logging rule**: The log must be written to stable storage BEFORE the data is modified on disk. This is the fundamental principle underlying virtually all commercial recovery systems.

3. **Distinguish between Redo and Undo operations**: Redo applies logged changes to bring committed transactions' effects to the database. Undo reverses uncommitted transactions' effects to restore the pre-transaction state.

4. **Know the three phases of ARIES recovery**: Analysis (identifies transactions to undo and dirty pages), Redo (reapplies all changes from appropriate point), and Undo (reverses uncommitted transactions).

5. **Checkpoint purposes and limitations**: Checkpoints limit recovery time by bounding how far back in the log recovery must scan. However, they don't eliminate the need for log files—they're performance optimizations, not complete solutions.

6. **Media failure vs. system failure handling**: System failures lose main memory contents but disk data typically survives—recovery uses the log. Media failures require restoring from backups and reapplying logged changes since the database itself is damaged.

7. **Transaction states and recovery implications**: Active transactions at crash time must be undone (they didn't commit). Committed transactions before crash must have their effects reflected (redo). Committed transactions after crash never happened from the database's perspective.

8. **Fuzzy checkpoint advantages**: Unlike consistent checkpoints that require all transactions to pause, fuzzy checkpoints allow concurrent transaction processing, making them essential for high-performance systems.