# Coordination and Agreement in Group Communication - Summary

## Key Definitions and Concepts

- **Group Communication:** Communication paradigm where messages are sent to a group of processes rather than individual processes, providing abstractions for coordinated action.
- **Multicast:** Foundation of group communication enabling single message delivery to multiple recipients with various reliability guarantees.
- **Consensus:** Fundamental problem requiring all correct processes to agree on a single value despite failures.
- **View:** Snapshot of current group membership; view synchrony ensures all processes observe the same sequence of views.
- **Byzantine Failure:** Arbitrary or malicious failure where a process can behave inconsistently.

## Important Formulas and Theorems

- **FLP Impossibility:** No deterministic consensus algorithm can guarantee agreement in an asynchronous system with even one crash failure.
- **Byzantine Fault Tolerance Threshold:** n ≥ 3f + 1 (minimum processes to tolerate f Byzantine failures).
- **Majority for Consensus:** Requires (n/2 + 1) votes out of n processes for crash fault tolerance.

## Key Points

1. Group communication provides reliability, ordering, and membership management for distributed applications.

2. Total ordering (atomic broadcast) ensures all processes deliver messages in the same order; FIFO orders per-sender, causal orders by happened-before relationship.

3. Paxos achieves consensus through prepare/promise and propose/accept phases with majority agreement.

4. Raft simplifies consensus with leader election, log replication, and safety properties; more understandable than Paxos.

5. The Byzantine Generals Problem requires 3f+1 processes to tolerate f arbitrary failures.

6. View changes in group membership must be atomic to maintain consistency across all processes.

7. Practical Byzantine Fault Tolerance (PBFT) uses three phases: pre-prepare, prepare, and commit.

## Common Mistakes to Avoid

- Confusing FIFO ordering with total ordering—FIFO is per-sender while total is global.
- Forgetting that FLP proves impossibility only for deterministic algorithms in asynchronous systems with crash failures.
- Not remembering the Byzantine threshold (3f+1)—many students incorrectly use n > 2f.

## Revision Tips

1. Practice drawing state diagrams for Paxos and Raft leader election processes.

2. Memorize the Byzantine fault tolerance formula and understand its derivation.

3. Review the differences between crash failures and Byzantine failures with examples.

4. Go through previous exam questions on distributed systems consensus protocols.
