# Transaction Concepts (ACID) - Summary

## Key Definitions and Concepts
- **Transaction**: Logical unit of work with ACID properties
- **Atomicity**: All-or-nothing execution
- **Consistency**: Valid state transitions
- **Isolation**: Concurrent execution appears serialized
- **Durability**: Surviving system failures
- **Schedule**: Execution sequence of transaction operations
- **Serializability**: Equivalent to some serial schedule

## Important Formulas and Theorems
- **Two-Phase Locking Protocol**: 
  Growing Phase (acquire locks) → Shrinking Phase (release locks)
- **Conflict Serializability**: 
  Swap non-conflicting operations to achieve serial schedule
- **ACR (Atomicity, Consistency, Recovery) Theorem**: 
  Atomicity + Consistency + Recovery logs ⇒ Durability
- **Log-Based Recovery**:
  WAL Rule: Log record must be written before database update

## Key Points
- ACID properties are interdependent - e.g., Atomicity enables Consistency
- Higher isolation levels reduce concurrency but prevent anomalies
- Write-ahead logging is fundamental for crash recovery
- Two-phase locking prevents lost updates but can cause deadlocks
- Optimistic concurrency control works best with low conflict rates
- Distributed transactions require protocols like Two-Phase Commit (2PC)
- BASE (Basically Available, Soft state, Eventually consistent) relaxes ACID for scalability

## Common Mistakes to Avoid
- Confusing transaction abort (atomicity) with system failure (dubility)
- Assuming all databases implement full ACID by default (e.g., NoSQL systems)
- Overlooking phantom reads when using row-level locks
- Forgetting to set proper isolation levels in application code
- Missing the shrinking phase in two-phase locking diagrams

## Revision Tips
1. Create ACID property matrix with implementation techniques
2. Practice drawing state diagrams for transactions
3. Compare isolation levels using anomaly charts
4. Solve past papers on conflict serializability testing
5. Use mnemonics: ACID (Atomic, Consistent, Isolated, Durable)
6. Study real DBMS implementations: PostgreSQL's MVCC vs MySQL's locking