# Two-Phase Locking Techniques for Concurrency Control - Summary

## Key Definitions and Concepts

- **Two-Phase Locking (2PL)**: A concurrency control protocol where a transaction must acquire all locks during a growing phase before releasing any lock in the shrinking phase.
- **Growing Phase**: Initial phase where a transaction can acquire new locks but cannot release any lock.
- **Shrinking Phase**: Second phase where a transaction can only release locks but cannot acquire new locks.
- **Lock Point**: The point in a transaction where it acquires its final lock.
- **Shared Lock (S Lock)**: Lock for read operations; compatible with other shared locks.
- **Exclusive Lock (X Lock)**: Lock for write operations; incompatible with all other locks.

## Important Formulas and Theorems

- **2PL Serializability Theorem**: Any schedule that follows the Two-Phase Locking protocol is conflict serializable.
- **Lock Compatibility**: S-S = Compatible, S-X = Incompatible, X-X = Incompatible

## Key Points

1. Basic 2PL ensures serializability but allows cascading rollbacks due to early lock release.

2. Strict 2PL retains exclusive (write) locks until transaction commit, preventing cascading aborts.

3. Rigorous 2PL retains all locks until commit, completely eliminating cascading rollbacks.

4. Deadlock occurs when transactions wait circularly for locks held by each other.

5. Deadlock prevention uses wait-die and wound-wait schemes; detection uses wait-for graphs.

6. Timestamp-based protocols avoid deadlocks but may cause starvation.

7. Thomas's Write Rule improves timestamp ordering by allowing certain write operations to proceed as blind writes.

8. Most commercial databases implement Rigorous 2PL or variations for simpler recovery.

## Common Mistakes to Avoid

- Confusing the growing and shrinking phases - remember locks are acquired first, then released
- Thinking that 2PL eliminates deadlocks - it only guarantees serializability
- Believing that all 2PL schedules are recoverable - only Strict and Rigorous 2PL ensure recoverability
- Forgetting that shared locks can coexist but exclusive locks cannot share

## Revision Tips

1. Draw a timeline for transactions showing lock acquisition and release points to identify phases.

2. Practice identifying whether a schedule follows Basic, Strict, or Rigorous 2PL.

3. Memorize the lock compatibility matrix - this is frequently tested in exams.

4. For deadlock questions, always draw the wait-for graph to visualize the cycle.
