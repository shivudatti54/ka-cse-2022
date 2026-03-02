# CAP Theorem

## Overview

The CAP Theorem, formulated by Eric Brewer, states that distributed systems can only provide two of three guarantees simultaneously: Consistency, Availability, and Partition Tolerance. This fundamental principle shapes blockchain architecture by forcing trade-offs between data correctness, system responsiveness, and network resilience.

## Key Points

- **Consistency**: All nodes see the same data at the same time; every read receives most recent write
- **Availability**: Every request receives response without error, though may return stale data
- **Partition Tolerance**: System continues operating despite network message loss or node isolation
- **The Trade-off**: During network partition, must choose between consistency (CP) and availability (AP)
- **CA Systems Not Possible**: Network partitions inevitable in distributed systems, making partition tolerance non-negotiable
- **CP Systems**: Sacrifice availability for correctness (MongoDB, HBase, Zookeeper)
- **AP Systems**: Sacrifice consistency for responsiveness (Cassandra, DynamoDB, DNS)
- **PACELC Extension**: Also considers Latency vs Consistency trade-off during normal operation

## Important Concepts

- Consistency and availability are spectrums, not binary choices
- Different system components can make different CAP choices
- Eventual consistency allows AP systems to converge over time
- Tunable consistency lets systems adjust guarantees per operation
- Real systems combine approaches based on data criticality

## Notes

- Remember that network partitions WILL occur, making partition tolerance essential
- Understand use case examples: financial transactions need CP, social feeds can use AP
- Know system classifications and examples for each category
- Be able to explain PACELC theorem as extension of CAP including latency
