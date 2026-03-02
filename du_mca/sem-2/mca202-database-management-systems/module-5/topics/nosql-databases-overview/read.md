# NoSQL Databases Overview

## Introduction
NoSQL databases have emerged as a critical solution for handling modern data challenges that traditional relational databases struggle with. With the exponential growth of unstructured data, real-time web applications, and distributed systems, NoSQL offers flexible schemas, horizontal scalability, and superior performance for specific use cases. Unlike relational databases that enforce ACID properties, NoSQL systems often follow BASE (Basically Available, Soft state, Eventually consistent) principles, making them ideal for big data, social networks, and IoT applications.

The importance of NoSQL lies in its ability to handle:
- High-velocity data streams (e.g., sensor data)
- Semi-structured data (JSON/XML documents)
- Distributed architectures (cloud-native applications)
- Rapid iteration cycles (schema-less designs)

Major tech companies like Amazon (DynamoDB), Google (Bigtable), and Meta (Cassandra) rely on NoSQL systems to manage petabytes of data. For DU MCA students, understanding NoSQL is essential for designing modern web-scale applications.

## Key Concepts
1. **Data Models**:
   - **Document Stores**: MongoDB, CouchDB (JSON-like documents)
   - **Key-Value Stores**: Redis, DynamoDB (simple data pairs)
   - **Column-Family Stores**: Cassandra, HBase (tabular data with column groups)
   - **Graph Databases**: Neo4j (nodes + relationships)

2. **CAP Theorem**:
   - A distributed system can only guarantee two of three properties:
     - **Consistency**: All nodes see same data
     - **Availability**: Every request receives response
     - **Partition Tolerance**: System operates despite network failures

3. **Horizontal Scaling**:
   - Sharding: Distributing data across multiple servers
   - Replication: Maintaining copies for fault tolerance

4. **Query Mechanisms**:
   - MapReduce (Hadoop)
   - Gremlin (graph queries)
   - CQL (Cassandra Query Language)

## Examples
**Example 1: Social Media Post Storage (Document DB)**
- Problem: Store user posts with nested comments and reactions
- Solution:
  ```javascript
  // MongoDB document
  {
    _id: "post123",
    user: "john_doe",
    content: "DU MCA insights!",
    comments: [
      {user: "alice", text: "Great post!"},
      {user: "bob", text: "Needs more examples"}
    ],
    reactions: {likes: 45, shares: 12}
  }
  ```
- Benefits: Schema flexibility, easy nested data handling

**Example 2: E-commerce Product Catalog (Key-Value Store)**
- Problem: Fast retrieval of product details
- Solution (Redis):
  ```bash
  SET product:789 '{"name":"Wireless Mouse","price":19.99,"stock":100}'
  GET product:789
  ```
- Latency: ~1ms for read/write operations

**Example 3: Fraud Detection (Graph DB)**
- Problem: Identify suspicious transaction patterns
- Neo4j Cypher Query:
  ```cypher
  MATCH (a:Account)-[t:TRANSACTION]->(b:Account)
  WHERE t.amount > 10000 AND a.risk_score > 8
  RETURN a, t, b
  ```
- Identifies high-risk transactions in real-time

## Exam Tips
1. **CAP Theorem Applications**: Always analyze trade-offs (e.g., AP vs CP systems)
2. **Use Case Matching**: Link database types to scenarios (e.g., graph DBs for social networks)
3. **Sharding Strategies**: Understand range-based vs hash-based sharding
4. **Consistency Models**: Compare strong vs eventual consistency
5. **Syntax Differences**: Note query language variations (SQL vs CQL vs Cypher)
6. **ACID vs BASE**: Highlight transaction model differences
7. **Exam Trends**: Recent DU papers emphasize real-world NoSQL implementation challenges

Length: 2500 words, MCA PG level