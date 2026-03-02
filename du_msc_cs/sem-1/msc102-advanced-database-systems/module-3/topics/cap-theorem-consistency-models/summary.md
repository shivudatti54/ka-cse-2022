# CAP Theorem and Consistency Models - Summary

## Key Definitions and Concepts

- **CAP Theorem**: States that a distributed database can provide only two of three guarantees (Consistency, Availability, Partition Tolerance) simultaneously during network partitions.

- **Consistency (C)**: Linearizability — all nodes see the same data simultaneously; every read returns the most recent write or an error.

- **Availability (A)**: Every non-failing node must respond to requests, even during partitions.

- **Partition Tolerance (P)**: System continues operating despite communication failures between nodes.

- **PACELC Theorem**: Extension of CAP addressing latency-consistency trade-offs in the absence of partitions (Partition-Availability-Consistency-Else-Latency-Consistency).

## Important Formulas and Theorems

- **CAP Trade-off**: Choose 2 of 3 (C, A, P) during partitions
- **Quorum Condition for Strong Consistency**: R + W > N, where R = read quorum, W = write quorum, N = total replicas
- **PACELC**: If Partition → (Availability OR Consistency); Else → (Latency OR Consistency)

## Key Points

- CAP theorem applies specifically during network partitions, not in normal operation
- Real distributed systems must be partition-tolerant by design
- The choice between C and A during partitions is a design decision based on application requirements
- Eventual consistency provides high availability and low latency but accepts temporary inconsistencies
- Strong consistency guarantees correctness at the cost of latency and potential unavailability
- Different data within an application may require different consistency levels
- Modern databases often provide configurable consistency (e.g., MongoDB, DynamoDB)
- CRDTs offer automatic conflict resolution for eventually consistent systems

## Common Mistakes to Avoid

- Confusing CAP "Consistency" with ACID database consistency (they're different concepts)
- Believing systems must permanently sacrifice one of C, A, or P (the choice is only during partitions)
- Assuming eventual consistency means "no consistency" (it guarantees eventual convergence)
- Overlooking latency trade-offs addressed by PACELC theorem

## Revision Tips

1. Memorize the three properties with precise definitions — consistency means linearizability, not ACID consistency
2. Practice mapping real databases (Cassandra, MongoDB, DynamoDB) to CAP categories
3. Understand quorum systems and how R + W > N ensures strong consistency
4. Review the evolution from CAP to PACELC as an exam differentiator
5. Prepare concrete examples of when to prefer each consistency model based on application needs