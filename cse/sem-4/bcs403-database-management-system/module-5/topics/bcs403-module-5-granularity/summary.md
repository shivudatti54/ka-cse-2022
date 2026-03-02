# Granularity of Data Items and Multiple Granularity Locking - Summary

## Key Definitions and Concepts

- **Granularity**: The size of data items that can be locked in a database system. Ranges from entire database (coarse) to individual fields (fine).
- **Multiple Granularity Locking (MGL)**: A locking protocol that allows locks at multiple levels of database hierarchy simultaneously.
- **Intent Locks**: Locks (IS, IX, SIX) that indicate intention to acquire locks at lower levels of the hierarchy.

## Lock Types in MGL

| Lock Type | Full Form                    | Purpose                         |
| --------- | ---------------------------- | ------------------------------- |
| S         | Shared                       | Read-only access                |
| X         | Exclusive                    | Read and write access           |
| IS        | Intention Shared             | Intent to S-lock children       |
| IX        | Intention Exclusive          | Intent to X-lock children       |
| SIX       | Shared + Intention Exclusive | S-lock current + IX on children |

## Important Formulas and Concepts

- **Lock Compatibility**: A matrix defining which lock types can coexist
- **Lock Acquisition Order**: Root → Intermediate → Leaf (top-down)
- **Lock Release Order**: Leaf → Intermediate → Root (bottom-up)

## Key Points

1. Fine granularity (record level) provides high concurrency but high overhead and increased deadlock probability.

2. Coarse granularity (database level) provides low overhead and low deadlock probability but poor concurrency.

3. MGL protocol uses intent locks (IS, IX, SIX) to efficiently manage locks at multiple hierarchy levels.

4. To acquire S lock at level i, transaction must hold IS or S lock at level i-1.

5. To acquire X lock at level i, transaction must hold IX, SIX, or X lock at level i-1.

6. SIX lock combines S and IX, useful when reading entire granularity while updating specific child items.

7. Lock escalation automatically promotes fine-grained locks to coarse-grained when threshold is reached.

8. The compatibility matrix shows IS, IX, S, SIX, X - only IS and IX are compatible with each other.

## Common Mistakes to Avoid

1. Forgetting to acquire intent locks at intermediate levels when locking at finer levels.

2. Confusing the direction of lock acquisition (must be top-down) and release (must be bottom-up).

3. Assuming all lock types are compatible - only IS and IX are mutually compatible among intent locks.

4. Not considering the impact of lock granularity on deadlock probability in system design.

## Revision Tips

1. Practice drawing the database hierarchy and tracing lock acquisition paths for different transactions.

2. Memorize the lock compatibility matrix - it's the most frequently tested concept.

3. Work through at least 3-4 solved examples covering different scenarios (read, write, mixed operations).

4. Understand when to use SIX lock vs separate S + IX locks for efficiency.

5. Remember that higher granularity means smaller data items (more concurrency, more overhead).
