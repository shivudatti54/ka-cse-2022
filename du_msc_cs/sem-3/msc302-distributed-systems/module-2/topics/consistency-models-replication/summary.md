# Consistency Models & Replication - Summary

## Key Definitions and Concepts
- **Linearizability:** Strongest model where operations appear instantaneous
- **Vector Clock:** [s1, s2, ... sn] tracking causal dependencies across n nodes
- **NWR Quorum:** N=replicas, W=write quorum, R=read quorum (W + R > N)
- **CRDTs:** Data structures that guarantee convergence without coordination

## Important Formulas and Theorems
- **CAP Theorem:** Consistency ∧ Availability ∧ Partition Tolerance → Impossible
- **Quorum Calculation:** W + R > N (for strong consistency)
- **Vector Clock Comparison:** VC1 ≤ VC2 iff ∀i: VC1[i] ≤ VC2[i]
- **PACELC:** Partition (A/ELse C) ↔ (Else L/atency vs C/onsistency)

## Key Points
- Strong consistency requires global coordination (high latency)
- Eventual consistency enables high availability but needs conflict resolution
- Causal consistency prevents paradoxes in ordered operations
- Active replication uses state machines; passive uses primary-backup
- Modern systems often implement tunable consistency levels
- CRDTs enable automatic conflict resolution through mathematical properties
- Hybrid logical clocks combine physical and logical time for scalability

## Common Mistakes to Avoid
- Confusing eventual consistency with "no consistency"
- Assuming causal consistency implies total order
- Overlooking clock synchronization issues in implementations
- Using quorum sizes that violate W + R > N condition

## Revision Tips
1. Create comparison tables: Consistency vs Availability vs Latency
2. Practice vector clock scenarios for causal dependencies
3. Memorize CAP/PACELC trade-offs using real system examples
4. Study DynamoDB's consistency modes and Cassandra's tunable consistency

Length: 650 words