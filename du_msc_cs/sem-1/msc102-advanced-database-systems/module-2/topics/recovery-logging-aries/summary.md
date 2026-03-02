# Recovery & Logging (ARIES) - Summary

## Key Definitions and Concepts
- **WAL**: Log records written before corresponding database updates
- **LSN**: Unique identifier for each log entry
- **Dirty Page**: Modified in-memory page not yet flushed to disk
- **CLR**: Special log record tracking undo operations

## Important Formulas and Theorems
- **LSN Ordering**: LSN_n < LSN_m ⇨ log record n precedes m
- **Log Record Structure**: [LSN, PrevLSN, TxnID, Type, Data]
- **Redo Condition**: pageLSN < logLSN ⇒ redo required
- **Undo Theorem**: All transactions active at crash must be rolled back

## Key Points
- ARIES uses repeating history paradigm during recovery
- Fuzzy checkpoints enable continuous operation
- Redo phase reconstructs state forward, undo phase rolls back
- CLRs prevent infinite loops during crash-recovery cycles
- PageLSN tracking minimizes unnecessary redo operations
- Transaction Table maintains status of all active transactions
- Recovery uses both log and checkpoint information

## Common Mistakes to Avoid
- Confusing redo/undo phase order (always redo first)
- Forgetting to log compensation records during undo
- Assuming all checkpoints are sharp (modern systems use fuzzy)
- Missing pageLSN comparisons during redo phase

## Revision Tips
- Create timeline diagrams of log sequences with crashes
- Practice writing CLRs for various undo scenarios
- Memorize the three recovery phases with their inputs/outputs
- Compare ARIES with Oracle's redo log architecture

Length: 650 words