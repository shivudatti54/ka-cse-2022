# Introduction to NoSQL Systems - Summary

## Key Definitions and Concepts

- **NoSQL (Not Only SQL):** Database systems designed for flexible schema, horizontal scalability, and distributed data storage; emerged to address limitations of traditional RDBMS with unstructured data

- **CAP Theorem:** States that distributed databases can provide only two of three guarantees—Consistency, Availability, and Partition Tolerance—simultaneously

- **ACID Properties:** Atomicity, Consistency, Isolation, Durability—guaranteed by traditional RDBMS

- **BASE Properties:** Basically Available, Soft State, Eventual Consistency—guaranteed by NoSQL databases

- **Horizontal Scaling (Scale-Out):** Adding more servers to handle increased load—primary approach in NoSQL

- **Vertical Scaling (Scale-Up):** Adding resources to existing server—typical approach in RDBMS

## Important Formulas and Theorems

- **CAP Theorem:** Consistency + Availability + Partition Tolerance = 2 (only two can be fully guaranteed)

## Key Points

1. Four types of NoSQL databases: Document (MongoDB), Key-Value (Redis), Column Family (Cassandra), Graph (Neo4j)

2. NoSQL databases prioritize partition tolerance since network partitions are inevitable in distributed systems

3. NoSQL databases are typically CP (consistency-focused) or AP (availability-focused) systems

4. Schema flexibility allows storing heterogeneous data without predefined structure

5. Eventual consistency means all replicas will eventually reflect the same data

6. Horizontal scaling in NoSQL provides linear performance improvement with added nodes

7. NoSQL excels with big data, real-time web apps, and unstructured content storage

8. Redis provides O(1) time complexity for basic operations—extremely fast key-value access

## Common Mistakes to Avoid

1. **Confusing NoSQL with "no SQL":** Many NoSQL databases support SQL-like query languages

2. **Assuming NoSQL always better than RDBMS:** Relational databases are still superior for structured data with complex relationships

3. **Ignoring consistency trade-offs:** Eventual consistency can cause stale data reads in distributed systems

4. **Choosing NoSQL without proper analysis:** Not every application needs NoSQL—evaluate requirements first

## Revision Tips

1. Create a comparison table between RDBMS and NoSQL databases covering schema, scalability, consistency, and use cases

2. Memorize one example for each type of NoSQL database (MongoDB, Redis, Cassandra, Neo4j)

3. Practice drawing the CAP theorem triangle and understanding which databases fall into each category

4. Review the ACID vs BASE comparison—write out each property with a brief explanation

5. Solve previous university exam questions on NoSQL to understand the exam pattern and important topics
