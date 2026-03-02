# The CAP Theorem - Summary

## Key Definitions and Concepts

- **CAP Theorem**: States that a distributed database system can provide only two of three guarantees (Consistency, Availability, Partition Tolerance) simultaneously during a network partition.

- **Consistency (C)**: All nodes see the same data at the same time; every read returns the most recent write or an error.

- **Availability (A)**: Every request receives a response, even if some nodes are down; guaranteed response but not necessarily the latest data.

- **Partition Tolerance (P)**: System continues operating despite network partitions between nodes.

- **Eventual Consistency**: Weaker consistency model where all replicas eventually become consistent if no new updates occur.

## Important Formulas and Theorems

- **CAP Theorem**: C + A + P = 2 (only two guarantees can be fully provided)
- **PACELC Extension**: If Partition (P) occurs → choose Availability (A) or Consistency (C); Else (E) → choose Latency (L) or Consistency (C)
- **Consistency Factor**: w = number of nodes that must acknowledge writes; r = number of nodes required for read operations

## Key Points

1. Network partitions are inevitable in distributed systems - partition tolerance is mandatory in practice.

2. During a partition, you must choose between consistency and availability - you cannot have both.

3. CA systems don't truly exist in distributed environments as they become unavailable during partitions.

4. CP systems sacrifice availability to maintain consistency (e.g., HBase, MongoDB with strong consistency).

5. AP systems sacrifice consistency to maintain availability (e.g., Cassandra, DynamoDB, CouchDB).

6. Traditional RDBMS are typically CA systems in single-node configurations.

7. Eventual consistency is acceptable for many web applications but not for financial transactions.

8. The CAP choice should be driven by application business requirements, not technology preferences.

## Common Mistakes to Avoid

- Believing CA systems are practical in distributed environments - they are not.
- Confusing availability with durability - availability means responding to requests, not data persistence.
- Thinking eventual consistency means no consistency - it's a weaker but valid consistency model.
- Ignoring partition tolerance - it's not optional in real-world distributed systems.

## Revision Tips

1. Memorize the CAP acronym and remember the trade-off triangle.

2. Know real-world database examples: Cassandra (AP), MongoDB (CP), DynamoDB (AP), HBase (CP).

3. Practice drawing the CAP theorem diagram showing the three system categories.

4. Understand that the choice between CP and AP depends on application requirements.

5. Review PACELC as an extension that considers latency even without partitions.
