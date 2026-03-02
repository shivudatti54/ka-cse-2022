# NewSQL In-Memory Databases - Summary

## Key Definitions and Concepts
- **NewSQL**: Scalable RDBMS with ACID guarantees
- **HTAP**: Hybrid Transactional/Analytical Processing
- **MVCC**: Multi-Version Concurrency Control
- **WAL**: Write-Ahead Logging for persistence
- **NVM**: Non-Volatile Memory (e.g., Intel Optane)

## Important Formulas and Theorems
- **Amdahl's Law for Sharding**: Speedup ≤ 1 / (S + (1-S)/N) where S=sequential fraction
- **Latency Calculation**: Total = Network + CPU + Lock Wait
- **CAP Theorem**: NewSQL chooses CP (Consistency + Partition Tolerance)
- **PACELC Theorem**: Extension of CAP for latency considerations

## Key Points
- In-memory storage enables µs-level data access vs ms for disk
- Distributed consensus via Raft/Paxos ensures consistency
- Columnar storage optimizes OLAP; row-store for OLTP
- Hybrid log-memory architectures balance speed and durability
- RDMA (Remote Direct Memory Access) reduces network overhead
- TPC-C benchmarks show NewSQL systems achieve 10x higher TPS than MySQL
- Cloud integration requires careful data placement (EU GDPR vs US clusters)

## Common Mistakes to Avoid
- Assuming in-memory = ephemeral (persistence is still required)
- Over-sharding leading to cross-node joins
- Ignoring clock synchronization in distributed systems
- Confusing MVCC with snapshot isolation

## Revision Tips
1. Create comparison tables: NewSQL vs NoSQL vs OldSQL
2. Practice sharding diagrams for different key types (range, hash)
3. Memorize 3 real-world implementations: CockroachDB, MemSQL, VoltDB
4. Study Google Spanner's TrueTime paper (2017) for distributed systems questions

Length: 650 words