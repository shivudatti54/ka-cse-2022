# Atomic Commit Protocols - Summary

## Key Definitions and Concepts

- **Atomic Commit Protocol**: A coordination protocol ensuring that a distributed transaction either commits at all participating nodes or aborts at all participating nodes.

- **Two-Phase Commit (2PC)**: A blocking atomic commit protocol with two phases - voting phase (participants vote YES/NO) and decision phase (coordinator decides commit/abort).

- **Three-Phase Commit (3PC)**: A non-blocking atomic commit protocol with three phases - can commit, pre-commit, and do commit phases.

- **Coordinator**: The node that initiates the commit protocol, collects votes, and makes the global commit/abort decision.

- **Participant (Cohort)**: Nodes that execute the transaction locally and participate in the voting process.

## Important Formulas and Theorems

- **2PC Message Complexity**: O(n) messages where n is the number of participants
- **3PC Message Complexity**: O(n) messages but with additional rounds compared to 2PC

## Key Points

- Atomic commit protocols ensure the "all-or-nothing" property of distributed transactions.

- 2PC guarantees atomicity but is blocking - participants wait indefinitely if coordinator fails after voting phase.

- 3PC adds a pre-commit phase to eliminate blocking under coordinator failure, but is more complex.

- Both protocols require a coordinator node and involve multiple message exchanges.

- Transaction logs are essential for recovery in both protocols.

- 2PC is widely used in practice (databases like PostgreSQL, MySQL use variations).

- 3PC is theoretically better but rarely implemented due to complexity and network assumptions.

## Common Mistakes to Avoid

- Confusing the phases of 2PC - remember voting phase comes before decision phase.

- Thinking 3PC is completely non-blocking - it only eliminates blocking under specific failure scenarios.

- Forgetting that participants must maintain transaction logs for recovery purposes.

- Overlooking that both protocols assume reliable communication between coordinator and participants.

## Revision Tips

1. Practice drawing the message flow diagrams for both 2PC and 3PC protocols.

2. Memorize the key difference: 2PC blocks on coordinator failure after voting; 3PC solves this with pre-commit phase.

3. Understand failure scenarios - know what happens when each type of node fails at different points.

4. Review how these protocols relate to ACID properties, particularly atomicity in distributed environments.
