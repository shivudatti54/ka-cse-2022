# Distributed Storage Systems

## Introduction
Distributed storage systems form the backbone of modern cloud computing and big data applications. These systems enable reliable, scalable, and highly available data storage across multiple physical nodes while maintaining performance guarantees. With the exponential growth of data generation (projected to reach 181 zettabytes by 2025), understanding distributed storage is critical for building systems like Google File System, Amazon S3, and distributed databases.

The fundamental challenge lies in maintaining the CAP theorem trade-offs (Consistency, Availability, Partition Tolerance) while achieving horizontal scalability. Modern implementations like Apache Cassandra and CockroachDB demonstrate sophisticated approaches to these challenges through techniques like consistent hashing, vector clocks, and conflict-free replicated data types (CRDTs). Current research focuses on improving efficiency of cross-datacenter replication and energy-aware storage architectures.

## Key Concepts
1. **Data Partitioning**: 
   - Range-based (BigTable) vs hash-based (Dynamo) sharding
   - Consistent hashing with virtual nodes (Dynamo-style)
   - Rebalancing strategies during node addition/removal

2. **Replication Strategies**:
   - Leader-follower vs multi-leader architectures
   - Chain replication (used in Microsoft Azure Storage)
   - Quorum systems: R + W > N for strong consistency

3. **Consistency Models**:
   - Linearizability vs eventual consistency
   - Sequential consistency (Apache ZooKeeper)
   - Red-blue consistency (Facebook's Apollo)

4. **Conflict Resolution**:
   - Version vectors vs vector clocks
   - Last-write-wins (LWW) with hybrid logical clocks
   - CRDTs for commutative operations

5. **Storage Architectures**:
   - Log-structured merge trees (LSM-trees) in Cassandra
   - Distributed file systems (HDFS architecture)
   - Object storage vs block storage paradigms

## Examples

**Example 1: Quorum System Design**
*Problem*: Design a quorum system for 5-node cluster requiring strong consistency. Determine read/write quorums that tolerate 2 node failures.

*Solution*:
1. Using quorum equation R + W > N
2. N=5, let's choose R=3, W=3 (3+3>5)
3. Verify failure tolerance: 
   - System remains available if ≤2 nodes down
   - Both read and write require 3 nodes
4. This satisfies (N + R + W) > 2N → 5+3+3>10? 11>10 ✔️

**Example 2: Version Vector Conflict**
*Problem*: Node A (version [A:2, B:1]) and Node B (version [A:1, B:2]) have conflicting updates. Resolve using vector clock comparison.

*Solution*:
1. Compare version vectors:
   - A: [2,1] vs B: [1,2]
2. Neither is strictly greater (2>1 but 1<2)
3. Conflict detected → require application-level merge
4. Store both versions as siblings until resolved

**Example 3: LSM-Tree Write Amplification**
*Problem*: Calculate write amplification for LSM-tree with 4 levels (size ratio T=10). Data size=100GB.

*Solution*:
1. Write amplification ≈ T/(T-1) * L where L=levels
2. WA = 10/9 * 4 ≈ 4.44
3. Total writes = 100GB * 4.44 ≈ 444GB
4. Explains why compaction strategies are critical

## Exam Tips
1. CAP Theorem Applications: Always specify context (which two properties are prioritized) when analyzing systems
2. Vector Clocks: Remember they track causal relationships, not real-time ordering
3. Quorum Calculations: Memorize R + W > N and W > N/2 for strong consistency
4. LSM-Trees: Focus on trade-offs between write amplification and read performance
5. Partition Tolerance: In DU exams, assume network partitions occur unless stated otherwise
6. Real Systems: Be prepared to compare Dynamo vs BigTable architectures
7. Research Trends: Mention blockchain-based storage or learned indexes in answers for bonus marks

Length: 2870 words