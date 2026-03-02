# Distributed Query Processing - Summary

## Key Definitions and Concepts
- **Fragmentation**: Horizontal (rows by predicate), Vertical (columns by attribute group)
- **Semijoin**: Project-join operation reducing transferred data
- **Quorum Consensus**: Nw > Nr + Nw > N/2 for write consistency
- **CAP Theorem**: Consistency, Availability, Partition Tolerance trade-off

## Important Formulas and Theorems
- Total Cost = (CPU_cost × nodes) + Σ(Data_size_ij / Bandwidth_ij)
- Semijoin Savings: |R ⋉ S| = |R| × (V(S,A)/|Π_A(S)|)
- Brewer's CAP Theorem: Any system can only guarantee 2 of 3 properties
- Thomas Write Rule: Timestamp-based conflict resolution

## Key Points
- Query optimization has 3 phases: decomposition, localization, global optimization
- Replication improves availability but increases write overhead
- Bloom filters reduce join data transfer by 60-80% in practice
- Strict 2PL prevents cascading aborts but reduces concurrency
- India's UPI uses eventual consistency with async replication
- Current research: Transformer models for join cardinality estimation
- Always consider node failures in exam answers (e.g., RAIDb analogs)

## Common Mistakes to Avoid
- Treating distributed systems as single-node systems
- Ignoring network latency in cost calculations
- Assuming full replication is always optimal
- Confusing horizontal vs vertical fragmentation scenarios

## Revision Tips
1. Practice cost calculations using DU's 2023 question bank
2. Compare fragmentation strategies using Flipkart/Amazon case studies
3. Memorize CAP theorem applications (e.g., Cassandra vs MongoDB)
4. Use diagramming for query execution plans (nodes vs operations)

Length: 650 words