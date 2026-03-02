# NoSQL Document, Key-Value, and Graph Databases - Summary

## Key Definitions and Concepts
- **Document Database**: Stores semi-structured data as self-contained documents
- **Eventual Consistency**: Guarantees all nodes will converge given no new writes
- **Index-Free Adjacency**: Graph nodes contain direct references to connected nodes
- **CRDTs**: Data structures that resolve conflicts automatically in distributed systems

## Important Formulas and Theorems
- **CAP Theorem**: A distributed system can only guarantee 2 of 3: Consistency, Availability, Partition Tolerance
- **HyperLogLog Error**: Relative error = 1.04/√m (m=2^b registers)
- **Shard Chunk Size**: MongoDB default 64MB (configurable based on workload)

## Key Points
- Document databases excel at hierarchical data with evolving schemas
- Key-value stores provide O(1) access time but limited query capabilities
- Graph databases use traversal-based queries rather than joins
- Redis Streams enable event-driven architectures with consumer groups
- Neo4j's Label Propagation Algorithm detects communities in networks
- MongoDB Atlas Search uses Lucene-based indexes for text+vector search
- Amazon QLDB challenges NoSQL norms with immutable ledger functionality

## Common Mistakes to Avoid
- Using document DBs for complex transactions spanning multiple collections
- Treating all key-value stores as simple caches (ignore RedisJSON/TimeSeries)
- Modeling many-to-many relationships in graph DBs without relationship properties
- Overlooking tombstone accumulation in LSM-tree based systems
- Assuming eventual consistency means "no consistency"

## Revision Tips
1. Practice writing Cypher queries for 3-hop network analysis
2. Compare MongoDB's $lookup vs Neo4j's native joins
3. Memorize Redis data structure time complexities
4. Study real-world architectures: Twitter's graph service, Uber's Riak use
5. Use Docker to experiment with MongoDB sharding and Neo4j clusters

Length: 650 words