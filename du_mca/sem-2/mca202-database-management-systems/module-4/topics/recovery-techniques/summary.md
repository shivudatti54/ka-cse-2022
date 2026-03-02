# Recovery Techniques in DBMS - Summary

## Key Definitions and Concepts

- **Recovery**: The process of returning a database to a consistent state after a failure
- **ACID Properties**: Atomicity (all-or-nothing), Consistency (valid state transitions), Isolation (concurrent transaction independence), Durability (committed changes persist)
- **Write-Ahead Logging (WAL)**: Protocol requiring log records to be written to stable storage before data modifications are written to disk
- **Log Sequence Number (LSN)**: Unique identifier for each log record enabling efficient log navigation
- **Checkpoint**: A consistent snapshot of database state recorded in the log to limit recovery scope
- **ARIES**: Algorithm for Recovery and Isolation Exploiting Semantics—modern recovery algorithm used in commercial DBMS
- **Compensation Log Record (CLR)**: Log record generated during undo operations in ARIES to enable resumption after crashes

## Important Formulas and Theorems

- **Recovery principle**: All committed transactions must be reflected in the recovered database (redo); all uncommitted transactions must not be reflected (undo)
- **WAL constraint**: `log(Ti, X, old, new)` → stable storage BEFORE `DB[X] = new` written to disk
- **Checkpoint record contents**: Active transaction list, last LSN per active transaction, dirty page pointers

## Key Points

1. Database failures are classified into four types: transaction failures (normal aborts), system failures (memory loss), media failures (disk damage), and natural disasters (catastrophic loss)

2. Log-based recovery dominates commercial systems because it enables fine-grained recovery without requiring exclusive database access

3. The write-ahead logging protocol is fundamental—it ensures the log contains sufficient information to reconstruct database state regardless of when failure occurs

4. ARIES uses three phases: Analysis identifies what needs recovery, Redo reapplies all changes from appropriate point, Undo reverses uncommitted transactions

5. Checkpoints reduce recovery time by limiting log scan extent but introduce overhead during normal operation—frequency must be balanced

6. Shadow paging provides natural crash recovery but suffers from storage overhead and garbage collection complexity

7. CLRs in ARIES make recovery idempotent and resilient to crashes during the recovery process itself

## Common Mistakes to Avoid

- Confusing redo and undo: Redo is for committed transactions (bring their effects into the database), undo is for uncommitted transactions (remove their effects)
- Forgetting that checkpoints themselves must be logged atomically to ensure recovery correctness
- Assuming media failures can be handled by log-based recovery alone—they require backup restoration first
- Overlooking the need to force-write log records before acknowledging transaction commit (violates WAL)

## Revision Tips

1. Draw the transaction state diagram (active, partially committed, committed, aborted) and annotate with recovery implications

2. Practice tracing through simple recovery scenarios by examining log sequences and determining what redo/undo operations are needed

3. Memorize the three ARIES phases and what each accomplishes—focus on understanding the logical purpose rather than implementation details

4. Create a comparison table between log-based recovery and shadow paging covering storage overhead, recovery time, and garbage collection

5. Re-read the WAL principle until you can explain why it's necessary in your own words—it's the foundation of all recovery techniques