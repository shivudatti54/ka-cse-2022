# NoSQL Key-Value Stores - Summary

## Key Definitions and Concepts

- **Key-Value Store**: A NoSQL database that stores data as unique key-value pairs, where each key serves as an identifier for retrieving its corresponding value
- **NoSQL**: databases that provide flexible schemas and scale horizontally, unlike traditional relational databases
- **CAP Theorem**: States that distributed databases can only guarantee two of three properties: Consistency, Availability, and Partition Tolerance
- **Eventual Consistency**: Guarantees that if no new updates are made, all replicas will eventually return the same value
- **Sharding/Partitioning**: Distributing data across multiple nodes for horizontal scalability
- **TTL (Time-to-Live)**: Mechanism to automatically expire keys after a specified duration

## Important Formulas and Characteristics

- **Replication Factor**: Number of copies of data maintained across nodes
- **Quorum**: Minimum number of nodes that must respond for read/write operations to succeed
- **Hash Function**: Maps keys to specific partitions; consistent hashing minimizes data movement during node changes

## Key Points

1. Key-value stores are the simplest form of NoSQL databases, storing data as unique key-value pairs
2. They prioritize scalability and availability over strong consistency (AP systems per CAP theorem)
3. Redis offers in-memory storage with optional persistence and supports complex data structures
4. Amazon DynamoDB provides fully managed key-value/document storage with single-digit millisecond latency
5. Apache Cassandra is designed for high write throughput with linear scalability
6. Horizontal scaling is achieved through partitioning (sharding) data across multiple nodes
7. Key-value stores excel in caching, session management, real-time analytics, and distributed locking scenarios
8. TTL functionality makes them ideal for implementing caches and temporary data storage

## Common Mistakes to Avoid

- Confusing key-value stores with document databases (MongoDB stores JSON-like documents, not simple key-value)
- Assuming all key-value stores sacrifice consistency (some like etcd provide strong consistency)
- Overlooking the importance of choosing appropriate partition strategies based on access patterns

## Revision Tips

1. Focus on understanding why key-value stores are preferred for specific use cases (high-speed caching, session storage)
2. Remember the trade-offs between consistency, availability, and partition tolerance
3. Practice distinguishing between different key-value store implementations and their strengths
4. Review the GET/SET/DELETE basic operations and understand TTL implementation
