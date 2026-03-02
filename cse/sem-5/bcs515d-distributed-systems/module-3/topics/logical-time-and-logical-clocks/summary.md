# Logical Time and Logical Clocks - Summary

## Key Definitions and Concepts

- **Happened-Before Relation (→)**: A partial ordering defining causal dependence between events in distributed systems based on: same-process order, message send→receive, and transitivity.

- **Logical Clock**: A counter-based mechanism that assigns timestamps to events based on causal ordering rather than physical time.

- **Lamport Clock**: A scalar logical clock providing total ordering; increments locally, syncs on message receipt using: C = max(local, received) + 1.

- **Vector Clock**: An array of counters capturing complete causal history; each process maintains knowledge of all processes' logical times.

- **Concurrent Events**: Events where neither a → b nor b → a; detected when vector clocks are incomparable.

## Important Formulas and Theorems

- **Lamport Clock Update (local event)**: C = C + 1
- **Lamport Clock Update (message receive)**: C = max(C, T) + 1
- **Vector Clock Update (receive)**: V[i] = max(V[i], Vm[i]) for all i; then V[self]++
- **Causal Ordering (Vector)**: VC(a) < VC(b) if ∀k: VC(a)[k] ≤ VC(b)[k] and ∃k: VC(a)[k] < VC(b)[k]
- **Key Property**: If a → b, then L(a) < L(b) and VC(a) < VC(b)

## Key Points

1. Logical clocks solve the impossibility of perfect physical clock synchronization in distributed systems.

2. Happened-before relation captures causality but is a partial order—some events are incomparable (concurrent).

3. Lamport clocks give total ordering but cannot distinguish concurrent events from causally ordered ones.

4. Vector clocks can exactly determine causal relationships and detect concurrency between events.

5. Vector clock size grows linearly with the number of processes (O(n) space complexity).

6. Logical time is essential for distributed mutual exclusion, deadlock detection, and checkpointing algorithms.

7. Version vectors (practical vector clocks) are used in Amazon Dynamo and Cassandra for conflict detection.

8. Total ordering via Lamport clocks extends happened-before but may order events that are actually concurrent.

## Common Mistakes to Assume

- **Confusing total and partial ordering**: Lamport gives total, happened-before is partial.
- **Forgetting to increment after receive**: Both local events AND message receives require incrementing the clock.
- **Wrong max() application**: On message receive, use max of local and received, not min.
- **Vector clock comparison error**: Both vectors must be compared element-wise; partial dominance indicates causality.
- **Assuming logical clocks replace physical clocks**: They are complementary; logical for ordering, physical for real-time.

## Revision Tips

1. Practice tracing Lamport and vector clock values through multi-process message-passing scenarios.

2. Draw event diagrams with arrows showing happened-before relations before applying clock algorithms.

3. Remember: "Send happens-before Receive" is the fundamental rule for message-based systems.

4. For vector clocks, always initialize all elements to zero and update the "self" element last.

5. In exams, first identify the happened-before relationships, then apply clock update rules systematically.
