# Distributed Database Architecture - Summary

## Key Definitions and Concepts

- **Distributed Database System (DDBS)**: A collection of multiple, logically interrelated databases stored at different sites of a computer network, appearing as a single logical database to users.

- **Fragmentation**: Division of a relation into fragments stored at different sites—horizontal (rows) or vertical (columns).

- **Replication**: Storage of data copies at multiple sites—synchronous (strong consistency) or asynchronous (eventual consistency).

- **Transparency**: The degree to which distribution complexity is hidden from users—network, location, replication, fragmentation, and transaction transparency.

- **CAP Theorem**: States that distributed databases can guarantee only two of Consistency, Availability, and Partition Tolerance simultaneously.

## Important Formulas and Theorems

- **Fragment Reconstruction**:
  - Horizontal: R = R1 ∪ R2 ∪ ... ∪ Rn (UNION operation)
  - Vertical: R = R1 ⋈ R2 ⋈ ... ⋈ Rn (JOIN on primary key)

- **Fragmentation Completeness**: Sum of fragments must equal the original relation

- **Fragmentation Disjointness**: Horizontal fragments must not overlap (except for reconstruction key)

## Key Points

1. Distributed databases provide location independence, enabling transparent data access regardless of physical storage location.

2. Client-server architecture separates concerns with clients as front-end and servers handling data management; P2P provides equal peer responsibilities.

3. Federated database systems integrate autonomous heterogeneous databases through a mediated schema approach.

4. Horizontal fragmentation uses selection predicates to partition rows; vertical fragmentation partitions columns and requires primary key inclusion.

5. Synchronous replication ensures strong consistency but increases latency; asynchronous replication improves performance with temporary inconsistencies.

6. Two-Phase Commit (2PC) ensures atomicity in distributed transactions through prepare and commit phases but can block on coordinator failure.

7. CAP theorem forces designers to choose between consistency and availability during network partitions; modern systems offer tunable consistency.

8. Top-down database design starts with global schema planning; bottom-up approach integrates existing legacy databases.

9. Data fragmentation and replication together determine the distribution schema, affecting query performance, update costs, and consistency guarantees.

## Common Mistakes to Avoid

1. **Confusing Distributed with Parallel Databases**: Distributed databases emphasize geographically dispersed, autonomous sites; parallel databases focus on parallel processing within a single system.

2. **Vertical Fragmentation Reconstruction**: Always include primary key in all fragments—without it, join reconstruction produces incorrect results (cartesian product instead of natural join).

3. **Assuming Strong Consistency is Always Better**: Eventual consistency is appropriate for high-throughput, user-tolerant applications; strong consistency has significant latency costs.

4. **Ignoring Network Partition Scenarios**: CAP theorem assumes partitions will occur—designing for 100% availability without partitions is unrealistic.

5. **Forgetting Fragment Disjointness**: Non-disjoint horizontal fragments lead to duplicate tuples in reconstruction, causing incorrect query results.

## Revision Tips

1. Practice drawing and explaining architecture diagrams for each model (client-server, P2P, federated).

2. Write sample SQL queries for fragment reconstruction—both UNION for horizontal and JOIN for vertical fragmentation.

3. Trace through 2PC protocol with both success and failure scenarios to understand blocking behavior.

4. Use real-world examples (Cassandra as AP, HBase as CP) to remember CAP theorem trade-offs.

5. Review previous DU exam questions on this topic to understand the depth and format expected.