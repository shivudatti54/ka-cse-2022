# Consensus: Paxos & Raft

## Introduction
Consensus algorithms form the backbone of reliable distributed systems, ensuring agreement among nodes despite failures. In distributed computing, achieving consensus means all participating nodes agree on a single data value even when some components fail. This is critical for maintaining consistency in distributed databases, blockchain networks, and cloud infrastructure.

The Paxos algorithm, introduced by Leslie Lamport in 1989, was the first provably correct solution to the consensus problem. However, its complexity led to the development of Raft in 2014 - a more understandable alternative with equivalent fault tolerance. Today, Paxos underpins Google's Chubby lock service, while Raft is used in etcd, CockroachDB, and TiDB. Understanding these protocols is essential for designing modern distributed systems that balance safety, liveness, and operational clarity.

Recent research focuses on optimizing these algorithms for geo-distributed systems (e.g., EPaxos) and hybrid fault models. The 2023 ACM PODC conference highlighted innovations in combining consensus protocols with machine learning for adaptive leader election, demonstrating the field's evolving nature.

## Key Concepts
1. **Paxos Protocol**:
   - **Roles**: Proposers, Acceptors, Learners
   - **Phases**:
     1. Prepare Phase (Phase 1a/1b): Proposers seek promises from majority acceptors
     2. Accept Phase (Phase 2a/2b): Proposing value with highest proposal number
   - **Safety Properties**: Only one value is chosen if majority of nodes are alive
   - **Liveness Challenges**: Requires careful handling of concurrent proposals

2. **Raft Protocol**:
   - **Leader-Centric Design**: Strong leader manages log replication
   - **Key Mechanisms**:
     - Leader election using randomized timers
     - Log replication via AppendEntries RPC
     - Membership changes through joint consensus
   - **Safety via Term Numbers**: Each term acts as logical clock preventing stale leaders

3. **Byzantine vs Crash Fault Tolerance**:
   - Paxos/Raft handle crash faults (nodes stop)
   - Practical Byzantine Fault Tolerance (PBFT) addresses malicious nodes

4. **FLP Impossibility**:
   Fundamental result (Fischer, Lynch, Paterson) proving no deterministic consensus under asynchrony with single fault

## Examples
**Example 1: Paxos in Network Partition**
Scenario: 5-node cluster (A-E) with partition separating A,B from C,D,E
- Phase 1: Proposer C (partition 2) gets promises from C,D,E
- Phase 2: Proposes value V with n=5
- Partition heals: A,B learn chosen value through learners
- Key Insight: Paxos ensures safety across partitions but requires majority

**Example 2: Raft Leader Failure**
1. Initial leader (Node 1) fails
2. Nodes 2-5 start election timers (150-300ms random)
3. Node 3 times out first, becomes candidate
4. Receives votes from 3,4,5 (majority)
5. New leader 3 commits pending entries
Solution: Leader heartbeat interval must be << election timeout to prevent spurious elections

**Example 3: Multi-Paxos Optimization**
Standard Paxos: 2 rounds per value
Optimization:
- Elect stable leader (Phase 1 once)
- Subsequent proposals use Phase 2 only
- Achieves throughput comparable to Raft

## Exam Tips
1. Always distinguish between safety (nothing bad happens) and liveness (something good eventually happens)
2. For Paxos, remember: Value is locked only during Accept phase, not Prepare
3. In Raft, understand the exact conditions for log entry commitment (leader replicates to majority)
4. Compare message complexity: Paxos O(2n) vs Raft O(n) per operation
5. Be prepared to analyze scenarios with concurrent leaders (Paxos allows multiple proposers, Raft prevents via terms)
6. Know the role of quorums: Majority vs. flexible quorums in recent variants
7. Practice drawing timeline diagrams for both protocols under different failure modes