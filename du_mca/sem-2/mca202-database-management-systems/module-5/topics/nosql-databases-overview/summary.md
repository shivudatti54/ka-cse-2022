# NoSQL Databases Overview - Summary

## Key Definitions and Concepts
- **NoSQL**: Non-relational databases designed for scalability and flexible data models
- **BASE**: Basically Available, Soft state, Eventually consistent (vs ACID)
- **Sharding**: Horizontal partitioning of data across servers
- **Denormalization**: Optimizing read performance by duplicating data

## Important Formulas and Theorems
- **CAP Theorem**: Consistency + Availability + Partition Tolerance (Choose 2)
- **Quorum Consistency**: (W + R > N) where W=write nodes, R=read nodes, N=replicas
- **Brewer's Conjecture**: Formal proof of CAP theorem (2002)
- **PACELC**: Extension of CAP addressing latency trade-offs

## Key Points
- Document DBs excel at hierarchical data storage
- Key-value stores provide fastest read/write operations
- Column-family DBs optimize for write-heavy workloads
- Graph DBs minimize complex joins via relationship indexing
- Eventual consistency ≠ "inconsistent" – system converges over time
- Horizontal scaling is cheaper than vertical scaling for big data
- NoSQL doesn't replace RDBMS – used for complementary scenarios

## Common Mistakes to Avoid
- Using NoSQL for complex transactions requiring ACID compliance
- Ignoring consistency requirements in AP systems
- Over-denormalizing leading to update anomalies
- Treating all NoSQL systems as schema-less (some require schema-on-write)

## Revision Tips
1. Create comparison tables: SQL vs NoSQL features
2. Practice writing queries for all 4 NoSQL types
3. Memorize CAP theorem trade-offs with real examples
4. Use flashcards for database-type-to-use-case matching
5. Solve DU previous years' questions on sharding strategies

Length: 650 words