# Characterizing Schedules Based on Serializability - Summary

## Key Definitions and Concepts

- **Schedule**: A chronological sequence of operations from multiple concurrent transactions
- **Serial Schedule**: Transactions execute one after another without interleaving
- **Conflict Serializability**: A schedule that can be transformed into a serial schedule by swapping non-conflicting operations
- **Precedence Graph**: Directed graph with nodes as transactions and edges representing conflicting operations; acyclic graph indicates serializability
- **View Serializability**: Broader concept where schedule is equivalent to some serial schedule in terms of read/write operations
- **Recoverable Schedule**: Transaction commits only after all transactions whose changes it read have committed
- **Cascadeless Schedule**: Transaction reads only values written by committed transactions

## Important Formulas and Theorems

- A schedule is conflict serializable if and only if its precedence graph is acyclic
- Every conflict serializable schedule is view-serializable ( converse is not true)
- Cascadeless ⊂ Recoverable ⊂ All schedules
- Three conflict types: Read-Write, Write-Read, Write-Write
- For n transactions in serial schedule: n! possible orderings

## Key Points

- Serializability ensures concurrent execution produces correct results equivalent to some serial execution
- Precedence graph is the standard method for testing conflict serializability
- Cycles in precedence graph indicate non-serializable schedules
- View serializability allows blind writes but is computationally expensive to test
- Recoverability ensures database can be recovered to consistent state after failures
- Cascadeless schedules prevent cascading rollbacks but have limited concurrency
- Conflict serializability is sufficient for correctness and efficiently testable
- Lock-based concurrency control protocols ensure conflict serializability

## Common Mistakes to Avoid

- Confusing conflict serializability with view serializability—they are not equivalent
- Forgetting that serial schedules are always serializable (vital exam point)
- Overlooking recoverability when analyzing schedules for practical implementation
- Incorrectly drawing precedence graph edges (direction matters!)
- Assuming acyclic graph guarantees serializability without considering all conflicts

## Revision Tips

1. Practice drawing precedence graphs from 3-4 transaction schedules regularly
2. Memorize the conflict types and identify them in example schedules
3. Remember: acyclic precedence graph = conflict serializable schedule
4. Review the hierarchy: strict → cascadeless → recoverable → all schedules
5. Solve previous university exam questions on serializability to understand pattern
6. Focus on recoverable and cascadeless schedule definitions as they are frequently asked
