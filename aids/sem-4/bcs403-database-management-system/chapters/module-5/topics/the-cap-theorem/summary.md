# The CAP Theorem - Summary

## Key Definitions and Concepts

- **CAP Theorem**: States that a distributed data store can provide only two of three guarantees—Consistency, Availability, and Partition Tolerance—simultaneously, particularly during network partitions.

- **Consistency (C)**: Linearizability where all nodes see the same data at the same time; any read returns the most recent write.

- **Availability (A)**: Every non-failing node responds to requests with data, even if that data might be stale during partitions.

- **Partition Tolerance (P)**: System continues operating despite network failures between nodes; mandatory in practical distributed systems.

## Important Formulas and Theorems

- **CAP Trade-off**: During partition → choose between Consistency OR Availability
- **PACELC Extension**: If Partition (P) → choose A or C; ELSE (no partition) → choose L or C
- System Categories: CA (single-site/traditional RDBMS), CP (BigTable, HBase, ZooKeeper), AP (Dynamo, Cassandra, CouchDB)

## Key Points

- Network partitions are inevitable in distributed systems, making partition tolerance a practical requirement.
- The choice between CP and AP is made EACH TIME a partition occurs, not just during design.
- CA systems exist only in theory or controlled environments without partitions.
- The "C" in CAP (linearizability) differs from ACID consistency (integrity constraints).
- AP systems achieve availability through eventual consistency, resolving conflicts after partitions heal.
- CP systems sacrifice availability to prevent inconsistent states during partitions.
- Modern applications often use multiple databases, selecting CP or AP based on specific use case requirements.

## Common Mistakes to Avoid

- Confusing CAP consistency with ACID consistency—these are different concepts.
- Believing CAP is a binary choice made once during design rather than a continuous trade-off.
- Assuming partitions are rare events—they are common in real-world distributed systems.
- Thinking AP systems are "inferior"—they are optimized for different use cases where availability trumps absolute consistency.

## Revision Tips

- Memorize the three properties with real-world analogies: Consistency (all see same data), Availability (always get response), Partition Tolerance (keeps working during failures).
- Associate each database with its CAP category: Dynamo/Cassandra = AP, BigTable/HBase = CP, Traditional RDBMS = CA.
- Remember the mnemonic: "DURING PARTITIONS, YOU CANNOT HAVE C AND A" (during partitions, you must choose).
- Practice identifying which CAP property to prioritize for different application scenarios (banking = C, social media = A).