# Distributed System Models - Summary

## Key Definitions and Concepts
- **Logical Clock**: Mechanism to order events without physical synchronization
- **Quorum System**: Majority voting for distributed consistency
- **Byzantine Fault**: Arbitrary node failures that threaten system integrity
- **CRDTs**: Conflict-free data structures for eventual consistency

## Important Formulas and Theorems
- **CAP Theorem**: Any system can achieve at most 2 of {Consistency, Availability, Partition Tolerance}
- **FLP Impossibility**: No deterministic consensus in async systems with crash failures
- **Vector Clock Ordering**: Event e1 → e2 iff VC(e1) < VC(e2) component-wise
- **Raft Safety**: Leader completeness property: log entries from prior terms are committed

## Key Points
- Synchronous models simplify algorithms but are unrealistic in WANs
- Eventual consistency enables high availability at cost of temporary inconsistencies
- Three-tier architecture separates concerns for scalable web applications
- Byzantine Fault Tolerance requires 3f+1 nodes to tolerate f malicious nodes
- Hybrid logical clocks combine physical and logical time for global ordering
- Gossip protocols enable eventual consistency through epidemic dissemination
- ZooKeeper uses Zab protocol (CP system) for coordination services

## Common Mistakes to Avoid
- Confusing network delays (async model) with node crashes (failure model)
- Assuming consensus algorithms work identically in sync vs async environments
- Overlooking clock skew in physical time-based systems
- Misapplying CAP theorem to non-partition scenarios

## Revision Tips
- Create comparison tables: Sync vs Async, Crash vs Byzantine failures
- Practice drawing timeline diagrams for vector clock operations
- Study real systems: Google Chubby (CP), Cassandra (AP), Ethereum (BFT)
- Focus on model implications for system design tradeoffs
- Solve past DU papers on consensus protocols and failure handling

Length: 650 words