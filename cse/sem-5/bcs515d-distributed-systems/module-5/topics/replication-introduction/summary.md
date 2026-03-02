# Database Replication - Summary

## Key Definitions and Concepts

- **Database Replication**: The process of copying and maintaining database objects across multiple database servers to ensure high availability, fault tolerance, and improved performance
- **Synchronous Replication**: Write operation waits for confirmation from all replicas before committing, ensuring strong consistency
- **Asynchronous Replication**: Primary confirms commit immediately, changes propagated to replicas in background; better performance but potential temporary inconsistency
- **Primary-Replica (Master-Slave)**: One primary handles all writes, multiple replicas handle reads; simpler architecture
- **Primary-Primary (Multi-Master)**: Multiple databases accept writes; complex but provides better write scalability
- **Conflict Resolution**: Strategies to handle concurrent updates in multi-master environments (Last-Writer-Wins, First-Writer-Wins, Application-defined)

## Important Formulas and Theorems

- **CAP Theorem**: A distributed system can only guarantee two of three properties - Consistency, Availability, and Partition Tolerance simultaneously
- **Replication Lag**: Time difference between primary and replica (async replication). Calculated as: `Lag = Current_Time - Last_Applied_Transaction_Timestamp`
- **Read/Write Distribution**: In primary-replica with N replicas, reads can be distributed as: `Reads_per_Replica = Total_Reads / N`

## Key Points

1. Replication provides high availability by maintaining multiple data copies across servers
2. Synchronous replication ensures strong consistency but increases transaction latency
3. Asynchronous replication offers better performance but may result in eventual consistency
4. Primary-Replica architecture is ideal for read-heavy workloads with infrequent writes
5. Primary-Primary architecture enables write scalability but introduces conflict resolution complexity
6. Conflict resolution strategies must be chosen based on business requirements
7. Vector clocks and CRDTs are advanced mechanisms for conflict-free concurrent updates
8. Replication introduces overhead in network bandwidth, storage, and processing requirements

## Common Mistakes to Avoid

1. Assuming synchronous replication is always better - it adds significant latency
2. Ignoring conflict resolution in multi-master setups - conflicts are inevitable
3. Not considering replication lag in asynchronous systems when designing queries
4. Confusing replication with partitioning - replication copies data, partitioning divides data

## Revision Tips

1. Practice drawing and explaining replication architecture diagrams
2. Memorize key differences between synchronous and asynchronous replication
3. Remember CAP theorem trade-offs for different consistency models
4. Review conflict resolution examples to understand practical implications
5. Focus on real-world scenarios where each replication type is appropriate
