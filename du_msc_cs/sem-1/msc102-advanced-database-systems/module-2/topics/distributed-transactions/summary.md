# Distributed Transactions - Summary

## Key Definitions and Concepts
- **Distributed Transaction**: ACID-compliant operation across multiple databases.  
- **2PC**: Coordinator-driven protocol with prepare/commit phases.  
- **CAP Theorem**: Consistency-Availability-Partition tolerance trade-off.  
- **BASE**: Alternative to ACID for high availability.  

## Important Formulas and Theorems
- **CAP Theorem**: A system can only satisfy 2 of {Consistency, Availability, Partition Tolerance}.  
- **2PC Message Complexity**: O(2n) for n participants.  
- **FLP Impossibility**: No deterministic consensus in asynchronous systems with faults.  

## Key Points
1. 2PC ensures atomicity but risks blocking; 3PC adds resilience.  
2. CAP dictates design choices (e.g., AP for social media, CP for banking).  
3. BASE prioritizes availability over strong consistency.  
4. Concurrency control requires global coordination (locks/timestamps).  
5. Network partitions necessitate anti-entropy mechanisms.  
6. Modern systems use hybrid models (e.g., Spanner: ACID + TrueTime).  
7. Research focuses on scalability (sharding) and low-latency consensus.  

## Common Mistakes to Avoid
1. Assuming 2PC guarantees non-blocking behavior.  
2. Misapplying CAP theorem to non-partition scenarios.  
3. Overlooking clock synchronization in timestamp ordering.  
4. Confusing eventual consistency with "no consistency."  

## Revision Tips
1. Map protocols to failure scenarios (e.g., coordinator crash in 2PC).  
2. Practice CAP theorem applications to real-world systems.  
3. Compare 2PC/3PC with Paxos/Raft consensus.  
4. Review case studies: Amazon Dynamo (AP), Google Spanner (CP).  

Length: 650 words