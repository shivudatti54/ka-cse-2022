# Column-Based or Wide-Column NoSQL Systems - Summary

## Key Definitions and Concepts

- **Wide-Column Database**: A NoSQL database that stores data in columns rather than rows, optimized for read-heavy analytical workloads and large-scale data storage.
- **Column Family**: A collection of related columns stored together, serving as the basic unit of data organization in wide-column stores.
- **Row Key**: The unique identifier for each row in a column family, used for data distribution and retrieval.
- **Column Qualifier**: The specific identifier within a column family that distinguishes individual data elements.
- **Wide Row**: A single row containing many columns, enabling storage of large amounts of related data in one partition.
- **LSM Tree (Log-Structured Merge Tree)**: Storage engine architecture that optimizes write performance by appending data and periodically merging sorted files.

## Important Formulas and Concepts

- **Consistency Level**: Configurable parameter (ONE, QUORUM, ALL) that determines how many replicas must acknowledge a read or write operation
- **Replication Factor**: Number of copies of data maintained across different nodes for fault tolerance
- **Compaction**: Background process that merges multiple SSTable files to optimize storage and read performance
- **Bloom Filter**: Probabilistic data structure used to efficiently check whether a column family might contain a particular row

## Key Points

- Wide-column databases store data in column families rather than traditional tables, enabling efficient column-oriented reads and aggregations.

- Apache Cassandra, Apache HBase, and Amazon DynamoDB are the most prominent wide-column database implementations used in industry.

- The flexible schema in wide-column stores allows different rows to have different columns, accommodating sparse data efficiently.

- Horizontal scalability is achieved through partitioning (sharding) based on row keys, enabling distribution across multiple commodity servers.

- Wide-column databases typically use LSM tree storage engines optimized for high write throughput rather than B-tree structures.

- Tunable consistency allows developers to balance between strong consistency and high availability based on application requirements.

- Data modeling is query-driven, with denormalization and strategic use of composite keys to support specific access patterns.

- These systems sacrifice ACID transactions for BASE properties, embracing eventual consistency in distributed environments.

## Common Mistakes to Avoid

- **Relational thinking**: Applying normalized relational data models to wide-column databases, which leads to poor performance; always design based on query patterns.

- **Ignoring partition strategy**: Poorly designed row keys can create hot spots, degrading performance; choose keys that distribute load evenly.

- **Over-indexing**: Creating excessive secondary indexes degrades write performance; only create indexes for critical query patterns.

- **Assuming strong consistency**: Unlike relational databases, most wide-column systems provide eventual consistency by default; design applications accordingly.

## Revision Tips

1. Practice designing data models for specific query scenarios, focusing on row key and column family design.

2. Compare and contrast wide-column databases with document stores and key-value stores to understand the NoSQL landscape comprehensively.

3. Review the CAP theorem implications for wide-column systems, understanding how different consistency levels affect the consistency-availability trade-off.

4. Study CQL (Cassandra Query Language) syntax and understand its similarities and differences from SQL.

5. Memorize real-world use cases where wide-column databases excel, such as time-series data, IoT, and analytical workloads.
