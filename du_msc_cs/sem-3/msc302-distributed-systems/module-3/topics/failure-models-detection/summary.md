# Failure Models and Detection in Distributed Systems - Summary

## Key Definitions and Concepts

- **Crash Failure**: Process stops permanently without producing incorrect outputs
- **Omission Failure**: Failure to send or receive messages (send, receive, or channel omissions)
- **Timing Failure**: Response times exceed expected bounds in synchronous systems
- **Byzantine Failure**: Arbitrary or malicious behavior producing contradictory outputs
- **Failure Detector**: Mechanism to determine which processes have crashed in a distributed system
- **Heartbeat**: Periodic message indicating process liveness
- **Quorum**: Minimum number of nodes required to agree for an operation to succeed

## Important Formulas and Theorems

- **CAP Theorem**: A distributed system can provide only 2 of 3 guarantees (Consistency, Availability, Partition tolerance)
- **FLP Impossibility**: No deterministic async consensus algorithm guarantees termination with even one crash failure
- **Byzantine Fault Tolerance**: n ≥ 3f + 1 required to tolerate f Byzantine failures
- **Heartbeat Timeout**: timeout ≥ mean + (z × std_dev) where z is the confidence level multiplier
- **Write Quorum**: n - f nodes required for safe writes in Byzantine tolerant systems

## Key Points

- Failure models define what behaviors systems must handle; stronger fault tolerance requires more replicas and communication overhead
- Eventually consistent systems prioritize availability and partition tolerance during network failures
- Adaptive failure detectors using φ accrual approach compute suspicion levels rather than binary decisions
- Paxos provides safe consensus but with complex implementation; Raft simplifies through leader-centric design
- Gossip protocols provide probabilistic failure detection with good scalability properties
- The FLP impossibility drives practical systems to use timeouts and partially synchronous models
- Real-world Byzantine systems use economic incentives (Proof of Work) or reduced participant sets (DPoS)

## Common Mistakes to Avoid

- Confusing crash failures with network partitions; they require different handling strategies
- Misunderstanding CAP theorem as a binary choice; most systems offer tunable consistency
- Using fixed timeouts without considering network characteristics; adaptive approaches are superior
- Assuming Byzantine failures only mean malicious behavior; arbitrary behavior covers more cases

## Revision Tips

- Practice drawing the failure taxonomy tree and associating real systems with each failure type
- Review the derivation of the 3f+1 Byzantine bound to understand its logical basis
- Compare Raft and Paxos side-by-side focusing on how they handle leader failures
- Study how Kubernetes, Cassandra, and etcd implement failure detection in production
- Remember that the CAP theorem applies specifically during network partitions, not during normal operation