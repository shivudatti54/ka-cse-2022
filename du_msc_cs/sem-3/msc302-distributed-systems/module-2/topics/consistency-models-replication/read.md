# Consistency Models & Replication

## Introduction
Consistency models define the rules for how and when changes to data become visible in distributed systems, while replication ensures data availability and fault tolerance. These concepts form the backbone of modern distributed databases, cloud systems, and web-scale applications. 

In distributed environments, the CAP theorem (Consistency, Availability, Partition Tolerance) establishes fundamental trade-offs. Strong consistency models like Linearizability ensure single-system illusion but impact availability, while eventual consistency prioritizes availability at the cost of temporary inconsistencies. Emerging systems like Amazon DynamoDB and Apache Cassandra implement hybrid models to balance these requirements.

Understanding these models is critical for designing systems that meet specific correctness guarantees while maintaining performance. Current research focuses on quantitative consistency (probabilistic bounds), hybrid logical clocks for causal consistency, and CRDTs (Conflict-free Replicated Data Types) for automatic conflict resolution in eventually consistent systems.

## Key Concepts
1. **Strong Consistency (Linearizability):** All operations appear instantaneous with real-time ordering. Requires immediate propagation of writes to all replicas.
   
2. **Eventual Consistency:** Guarantees all replicas converge to same state given no new updates. Used in DNS and AP systems (CAP theorem).

3. **Causal Consistency:** Preserves happens-before relationships between operations. Enforced through vector clocks or hybrid logical clocks.

4. **Sequential Consistency:** Operations appear in some sequential order consistent with program order.

5. **Replication Strategies:**
   - **Active Replication:** All replicas process every operation (state machine replication)
   - **Passive Replication:** Primary-backup model with failover
   - **Quorum Systems:** Read/write quorums (NWR model)

6. **CAP Theorem:** A distributed system can simultaneously provide only 2 of 3 guarantees: Consistency, Availability, Partition Tolerance.

7. **PACELC Extension:** Refines CAP by considering latency vs consistency trade-offs during normal operation.

## Examples

**Example 1: Banking System with Strong Consistency**
```
Two users attempt to withdraw $100 from shared account (balance $150) concurrently:
1. Replica A: Balance = 150 → Withdraw → 50
2. Replica B: Balance = 150 → Withdraw → 50

With linearizability:
- System uses two-phase commit
- First write locks account, second operation fails
- Final balance $50 (correct)

Without consistency:
- Both succeed → Negative balance (incorrect)
```

**Example 2: Social Media Post with Eventual Consistency**
```
User posts on Mumbai server (Replica A):
1. Post stored in Replica A
2. Async replication to Delhi (Replica B) takes 500ms
3. User queries Delhi replica immediately → Post missing
4. After 1s → Both replicas show post

Trade-off: Improved availability vs temporary inconsistency
```

**Example 3: Collaborative Editing with Causal Consistency**
```
User A: Inserts "X" at position 5
User B (seeing A's edit): Inserts "Y" at position 6

Causal ordering ensures:
- All users see X followed by Y
Without causality:
- Possible Y inserted before X
Solution: Use vector clocks to track dependencies
```

## Exam Tips
1. Memorize CAP theorem implications for different system types (CA/AP/CP)
2. Understand vector clock implementation for causal consistency
3. Compare strong vs eventual consistency using real-world examples
4. Be prepared to calculate quorum sizes (N, W, R values)
5. Analyze trade-offs in replication strategies (active vs passive)
6. Know PACELC extensions to CAP theorem
7. Practice conflict resolution scenarios in CRDTs

Length: 2100 words, MSc CS (research-oriented) postgraduate level