# CAP Theorem and Consistency Models

## Introduction
The CAP Theorem (Consistency, Availability, Partition Tolerance) is a fundamental principle governing distributed database systems. Introduced by Eric Brewer in 2000 and formally proven in 2002, it states that any networked shared-data system can guarantee only two of three properties simultaneously. This theorem has become a cornerstone for designing modern distributed systems, particularly with the rise of NoSQL databases and cloud-native architectures.

In the context of advanced database systems, understanding CAP is critical for making informed architectural decisions. For instance, financial systems prioritize consistency, while social media platforms might favor availability. The theorem's implications extend to emerging technologies like blockchain and edge computing, where network partitions are inevitable. Current research explores refinements like PACELC (extending CAP with Else Latency vs Consistency trade-offs) and probabilistic availability models.

## Key Concepts
1. **Consistency**: Linearizability - all nodes see same data at same time (strong consistency). Includes:
   - Sequential consistency
   - Causal consistency
   - Eventual consistency (weak model)

2. **Availability**: Every request receives non-error response, even during partitions. Does not guarantee response contains latest write.

3. **Partition Tolerance**: System continues operating despite arbitrary message loss/network failures.

4. **CAP Trade-offs**:
   - **CP Systems**: Sacrifice availability for consistency (e.g., Google Spanner, HBase)
   - **AP Systems**: Sacrifice consistency for availability (e.g., Cassandra, DynamoDB)
   - **CA Systems**: Theoretical ideal (rare in practice; single-node RDBMS)

5. **Consistency Models**:
   - Strong Consistency (ACID)
   - Eventual Consistency (BASE)
   - Read-Your-Writes Consistency
   - Monotonic Reads Consistency

6. **PACELC Theorem**: Extends CAP with "Else Latency vs Consistency" trade-off during normal operation.

## Examples
**Example 1: Banking System (CP)**
- Network partition occurs between Delhi and Mumbai datacenters
- System chooses consistency over availability:
  - Mumbai branch becomes unavailable for writes
  - Delhi branch processes transactions with strict quorum
  - Prevents overdrafts but causes temporary service denial

**Example 2: Social Media Feed (AP)**
- Partition between US and EU regions
- System remains available:
  - US users see cached posts
  - EU users get stale data
  - Conflict resolution via vector clocks during merge

**Example 3: Multi-Master Replication (Eventual Consistency)**
- Two nodes update same record concurrently:
  ```plaintext
  Node A: UPDATE users SET balance=150 WHERE id=1 (Version V2)
  Node B: UPDATE users SET balance=200 WHERE id=1 (Version V2)
  ```
- Conflict resolved through:
  - Last-write-wins (timestamp-based)
  - Application-specific merge (e.g., additive balances)

## Exam Tips
1. Always mention that CA systems are theoretical - real distributed systems must handle partitions
2. Differentiate between BASE (Basically Available, Soft state, Eventually consistent) vs ACID
3. For 10-mark questions, discuss PACELC extensions and real systems like CockroachDB's hybrid logical clocks
4. Remember: Availability ≠ 100% uptime - it's about non-error responses during partitions
5. Use TLA+ or formal proofs when discussing Brewer's original formulation
6. Recent DU papers emphasize CRDTs (Conflict-Free Replicated Data Types) in eventual consistency
7. Always contextualize answers - e.g., IoT systems prioritize AP, healthcare systems need CP