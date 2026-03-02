# Multiversion Concurrency Control Techniques - Summary

## Key Definitions and Concepts

- **MVCC (Multiversion Concurrency Control)**: A concurrency control method that maintains multiple versions of data items, allowing read operations to access consistent snapshots without blocking writes.
- **Snapshot Isolation**: An isolation level where each transaction sees a database snapshot as of the transaction start time.
- **Serializable Snapshot Isolation (SSI)**: An enhancement to Snapshot Isolation that detects and prevents serialization anomalies.
- **Timestamp Ordering (TSO)**: Concurrency control using transaction timestamps to determine serialization order.
- **Thomas's Write Rule**: Optimization that allows ignoring obsolete writes in timestamp-based systems.

## Important Formulas and Concepts

- **Read Rule (TSO)**: Transaction T can read item Q if T's timestamp > last write timestamp on Q
- **Write Rule (TSO)**: Transaction T can write item Q if T's timestamp > both last read and last write timestamps on Q
- **First-Committer-Wins**: In Snapshot Isolation, the transaction that commits first succeeds; others are aborted on write-write conflicts

## Key Points

- MVCC allows readers and writers to operate concurrently without blocking each other
- Each data version contains metadata including transaction ID and validity interval
- Snapshot Isolation provides consistent reads but may allow Write Skew anomalies
- SSI extends Snapshot Isolation to achieve true serializability by detecting dangerous structures
- Major databases (PostgreSQL, MySQL, Oracle) use MVCC for high concurrency
- Storage overhead increases due to maintaining multiple versions
- Old versions must be cleaned up through garbage collection
- Read operations in MVCC never block and never abort
- Write-write conflicts are resolved using First-Committer-Wins policy

## Common Mistakes to Confuse

- **Snapshot Isolation vs Serializable**: Snapshot Isolation is NOT serializable (allows Write Skew); SSI provides true serializability
- **Blocking vs Aborting**: MVCC eliminates blocking but may cause transaction aborts under certain conditions
- **Version Selection**: Transactions read the appropriate version based on timestamp, not necessarily the latest committed version

## Revision Tips

1. Draw timeline diagrams showing version creation and selection for different transactions
2. Memorize the difference between blocking (2PL) and non-blocking (MVCC) approaches
3. Practice identifying write-write conflicts in Snapshot Isolation scenarios
4. Remember that MVCC trades blocking for increased storage and potential aborts
5. Know which database systems implement which MVCC variant (PostgreSQL-SSI, Oracle-rollback segments, MySQL-InnoDB)
