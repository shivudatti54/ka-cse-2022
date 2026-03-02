# Distributed System Models

## Introduction
Distributed systems form the backbone of modern computing infrastructure, enabling scalable and fault-tolerant applications across networked devices. A distributed system model provides formal abstractions to understand system behavior, communication patterns, and failure handling. These models are crucial for designing systems that maintain consistency, availability, and partition tolerance (CAP theorem) under real-world constraints.

With the rise of cloud computing, IoT, and blockchain technologies, understanding distributed system models has become essential. For instance, Google's Spanner uses a globally distributed clock model, while Bitcoin employs a Byzantine Fault-Tolerant consensus model. Researchers continue to develop new models like conflict-free replicated data types (CRDTs) and hybrid logical clocks to address emerging challenges in edge computing and serverless architectures.

## Key Concepts
1. **Architectural Models**:
   - *Client-Server*: Centralized coordination (e.g., web servers)
   - *Peer-to-Peer*: Decentralized nodes with equal privileges (e.g., BitTorrent)
   - *Three-Tier Architecture*: Separation of presentation, logic, and data layers

2. **Interaction Models**:
   - *Synchronous*: Bounded message delays and processing times
   - *Asynchronous*: No timing guarantees (common in real-world networks)
   - *Partially Synchronous*: Hybrid approach used in practical consensus algorithms

3. **Failure Models**:
   - Crash failures (fail-stop)
   - Omission failures (message loss)
   - Arbitrary (Byzantine) failures
   - Network partitions (split-brain scenarios)

4. **Consistency Models**:
   - Linearizability (strong consistency)
   - Eventual consistency (used in DynamoDB)
   - Causal consistency (middle ground)
   - Sequential consistency (parallel processing)

## Examples
**Example 1: Vector Clocks in Client-Server Systems**
```python
# Server A (vector: [A:2, B:1])
event_a = VectorClock({'A': 2, 'B': 1})
# Server B receives event
event_b = event_a.increment('B')
# Resulting vector clock becomes [A:2, B:2]
```
*Step-by-Step*: Vector clocks resolve causality in asynchronous systems by tracking per-process counters.

**Example 2: Raft Consensus Protocol**
1. Leader election using randomized timers
2. Log replication with majority quorum
3. Handling network partitions through term numbers

**Example 3: Amazon Dynamo's Consistency**
- Uses (N, R, W) parameters: N=3 replicas, R=2 read quorum, W=2 write quorum
- Achieves eventual consistency through hinted handoff and read repair

## Exam Tips
1. Differentiate between architectural (structural) and interaction (timing) models
2. CAP theorem applications: CA (PostgreSQL), AP (Cassandra), CP (ZooKeeper)
3. FLP impossibility proof implications for consensus algorithms
4. Compare vector clocks vs. Lamport clocks for causality tracking
5. Byzantine Generals Problem solutions (PBFT vs. PoW)
6. Real-world mapping: Google File System (synchronous) vs. Bitcoin (asynchronous)
7. Always mention tradeoffs: e.g., strong consistency vs. availability

Length: 2200 words, MSc CS (research-oriented) postgraduate level