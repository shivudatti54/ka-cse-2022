# Distributed Storage Systems - Summary

## Key Definitions and Concepts
- **Sharding**: Horizontal partitioning of data across nodes
- **Quorum**: Minimum nodes required for read/write operations
- **Vector Clock**: [Node:counter] pairs tracking causal history
- **CRDT**: Conflict-free Replicated Data Type with merge semantics
- **Write Amplification**: Extra writes caused by storage structure

## Important Formulas and Theorems
- **CAP Theorem**: Can't simultaneously guarantee C, A, P
- **Quorum Equation**: R + W > N (strong consistency)
- **LSM Write Amplification**: WA ≈ T/(T-1) * L (T=size ratio, L=levels)
- **PACELC**: Extension of CAP theorem considering latency

## Key Points
- Eventual consistency requires anti-entropy protocols
- Multi-datacenter replication needs conflict resolution layers
- LSM-trees optimize for writes but complicate reads
- Version vectors detect conflicts but don't resolve them
- Chain replication provides strong consistency at scale
- Hinted handoff preserves availability during node failures
- CRDTs enable merge operations without coordination

## Common Mistakes to Avoid
- Assuming "available" in CAP means 100% uptime
- Confusing physical vs logical clocks in versioning
- Overlooking network costs in geo-replicated systems
- Using quorums without considering fallback strategies

## Revision Tips
- Practice quorum calculations with different N values
- Map real systems (Cassandra, Spanner) to CAP categories
- Compare version vectors in Dynamo vs vector clocks in Chubby
- Study Facebook's TAO and Amazon's Dynamo papers
- Use Bloom filters to understand LSM-tree optimizations

Length: 650 words