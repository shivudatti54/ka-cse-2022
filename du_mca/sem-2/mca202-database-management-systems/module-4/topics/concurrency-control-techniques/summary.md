# Concurrency Control Techniques - Summary

## Key Definitions and Concepts

- **Concurrency Control**: Mechanisms ensuring correct execution of multiple simultaneous transactions while preserving database consistency
- **Serializability**: Property ensuring concurrent execution produces same results as some serial execution of the same transactions
- **Two-Phase Locking (2PL)**: Protocol with growing phase (acquire locks) and shrinking phase (release locks) ensuring conflict-serializability
- **Timestamp Ordering (TSO)**: Lockless protocol using transaction timestamps to determine serializability order
- **Optimistic Concurrency Control (OCC)**: Validation-based approach assuming rare conflicts, with three phases: read, validation, and write
- **Deadlock**: Circular waiting state where two or more transactions wait indefinitely for locks held by each other
- **MVCC**: Multiversion Concurrency Control maintaining multiple data versions for non-blocking reads

## Important Formulas and Theorems

- **Lock Compatibility**: S + S = Compatible, S + X = Incompatible, X + X = Incompatible
- **2PL Condition**: All locks acquired before any lock released
- **Timestamp Order**: TS(T_old) < TS(T_younger); older transactions have smaller timestamps
- **Thomas' Write Rule**: If TS(T) < W-timestamp(X) but TS(T) > R-timestamp(X), ignore the write

## Key Points

1. Shared locks allow concurrent reads; exclusive locks block all other access
2. Basic 2PL ensures serializability but may cause cascading rollbacks
3. Strict 2PL holds exclusive locks until commit, preventing cascading aborts
4. Timestamp protocols avoid deadlocks but may reject valid operations
5. Optimistic CC works well when conflicts are rare (low contention)
6. Wait-for graph cycle indicates deadlock; breaking cycle resolves it
7. Victim selection considers transaction age, lock count, and work done
8. MVCC provides snapshot isolation, used by PostgreSQL and Oracle

## Common Mistakes to Avoid

- Confusing growing and shrinking phases in 2PL (locks released too early breaks serializability)
- Forgetting that timestamp protocols may reject valid transactions (not just conflicting ones)
- Mixing up deadlock prevention (prevention strategies) with deadlock detection (wait-for graphs)
- Thinking strict 2PL prevents all deadlock (only prevents cascading aborts)

## Revision Tips

1. Practice drawing precedence graphs for conflict-serializability testing
2. Solve at least 3-4 timestamp protocol problems to understand rejection conditions
3. Memorize the lock compatibility matrix—it's frequently tested
4. Remember real-world DBMS examples: PostgreSQL uses MVCC, MySQL (InnoDB) uses 2PL
5. Create a comparison table of all techniques covering deadlock, cascading aborts, and performance