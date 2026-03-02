# Characterizing Schedules Based on Recoverability - Summary

## Key Definitions and Concepts

- **Schedule:** A chronological sequence of operations from multiple concurrent transactions.
- **Recoverable Schedule (RC):** A schedule where if T_j reads data written by T_i, then T_i must commit before T_j commits.
- **Cascadeless Schedule (ACA):** A schedule where each transaction reads only committed values from other transactions; prevents cascading aborts.
- **Strict Schedule (ST):** A schedule where no transaction reads or writes a data item written by an uncommitted transaction.

## Important Formulas and Theorems

- **Hierarchy:** ST ⊂ ACA ⊂ RC (Strict is a subset of Cascadeless, which is a subset of Recoverable)
- **Recoverability Condition:** For every read operation by T_j on data written by T_i, Commit(T_i) must precede Commit(T_j)
- **Cascadeless Condition:** For every read operation by T_j on data written by T_i, Commit(T_i) must precede Read(T_j)
- **Strict Condition:** For every read/write operation by T_j on data written by T_i, Commit(T_i) must precede that operation

## Key Points

- Recoverability ensures database consistency when transactions abort during execution.
- A non-recoverable schedule can lead to committed transactions that cannot be rolled back even after the transaction they depended on aborts.
- Cascadeless schedules prevent cascading aborts where one transaction's abort forces other transactions to abort.
- Strict schedules provide the highest level of recoverability, simplifying rollback operations.
- Reading your own writes is always acceptable; the concern is reading writes from other transactions.
- All strict schedules are cascadeless, and all cascadeless schedules are recoverable (but not vice versa).

## Common Mistakes to Avoid

- Confusing "commit" with "abort" when checking conditions - always check the commit order.
- Forgetting that a transaction reading its own written values does not violate any recoverability property.
- Checking schedules in the wrong order - always verify if it is Strict first, then Cascadeless, then Recoverable.
- Missing read-write conflicts on different data items - only conflicts on the same data item matter.

## Revision Tips

- Practice identifying the type of schedule by examining the relative positions of Read, Write, Commit, and Abort operations.
- Use the quick test: look for any transaction reading uncommitted data from another transaction.
- Draw a timeline or table to visually track when each transaction reads, writes, commits, or aborts.
- Memorize the hierarchy: Strict → Cascadeless → Recoverable (most restrictive to least restrictive).
