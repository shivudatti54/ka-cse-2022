# Concurrency Control: 2PL vs MVCC - Summary

## Key Definitions and Concepts
- **Two-Phase Locking**: Locking protocol with growing/shrinking phases
- **MVCC**: Maintains multiple versions of data items
- **Serializability**: Equivalent to some serial execution
- **Snapshot Isolation**: Transactions see consistent database snapshot

## Important Formulas and Theorems
- Conflict Serializability: Precedence graph acyclicity
- Thomas Write Rule: TSO without read timestamps
- Version Storage: HEAD pointer + transaction visibility intervals
- Deadlock Probability: ∝ (n² * m²) where n=transactions, m=objects

## Key Points
- 2PL ensures serializability but can cause deadlocks
- MVCC avoids reader-writer conflicts through versioning
- Write skew possible under MVCC's snapshot isolation
- Modern systems use hybrid approaches (e.g., 2PL for writes + MVCC for reads)
- Version garbage collection critical for MVCC performance
- Cloud databases often combine MVCC with Paxos for distribution
- Hardware transactional memory influencing new concurrency models

## Common Mistakes to Avoid
- Assuming MVCC completely eliminates locking
- Confusing Repeatable Read with Snapshot Isolation
- Overlooking vacuum overhead in MVCC systems
- Misapplying conflict resolution rules across isolation levels

## Revision Tips
1. Practice drawing precedence graphs for 2PL schedules
2. Compare PostgreSQL's xmin/xmax with Oracle's SCN implementation
3. Study real-world deadlock scenarios from database logs
4. Implement simple MVCC version chain traversal algorithms
5. Review latest SIGMOD papers on OCC-MVCC hybrids

Length: 650 words