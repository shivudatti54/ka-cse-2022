# NoSQL Databases Types

## Introduction
NoSQL databases have become fundamental in modern cloud computing and big data ecosystems due to their ability to handle unstructured data, scale horizontally, and provide high availability. Unlike traditional relational databases, NoSQL systems sacrifice strict ACID properties for flexibility and scalability, making them ideal for applications like real-time analytics, content management, and IoT data processing.

The rise of web-scale applications and distributed systems has driven adoption of NoSQL databases. Major types include Document, Key-Value, Column-Family, and Graph databases, each optimized for specific data models and access patterns. Understanding these types is critical for designing efficient cloud-native applications and big data solutions.

## Key Concepts
1. **Document Databases**:
   - Store data as JSON/BSON documents with dynamic schemas
   - Ideal for hierarchical data and nested structures
   - Examples: MongoDB, Couchbase
   - Use cases: Content management, user profiles

2. **Key-Value Stores**:
   - Simplest NoSQL model with unique keys and values
   - High performance for simple queries
   - Examples: Redis, DynamoDB
   - Use cases: Session storage, caching

3. **Column-Family Stores**:
   - Organize data into columns rather than rows
   - Optimized for querying large datasets
   - Examples: Cassandra, HBase
   - Use cases: Time-series data, event logging

4. **Graph Databases**:
   - Use nodes, edges, and properties to represent data
   - Efficient for complex relationships
   - Examples: Neo4j, Amazon Neptune
   - Use cases: Social networks, fraud detection

5. **CAP Theorem**:
   - Consistency, Availability, Partition Tolerance
   - NoSQL databases prioritize either AP or CP
   - Example: Cassandra (AP) vs MongoDB (CP)

## Examples

**Example 1: Social Network Relationships**
- *Problem*: Efficiently store and query user connections
- *Solution*: Use Neo4j graph database
```cypher
CREATE (Alice:User {name: 'Alice'})
CREATE (Bob:User {name: 'Bob'})
CREATE (Alice)-[:FRIEND]->(Bob)
```
- *Analysis*: Graph databases enable efficient traversal of relationships without complex joins.

**Example 2: E-Commerce Shopping Cart**
- *Problem*: Handle high-speed session data
- *Solution*: Redis key-value store
```redis
SET cart:user123 '{items: [{"id":5,"qty":2}], total: 100}'
EXPIRE cart:user123 3600
```
- *Analysis*: Sub-millisecond response times suit volatile data.

**Example 3: IoT Time-Series Data**
- *Problem*: Store sensor readings from 10M devices
- *Solution*: Cassandra column-family database
```cql
CREATE TABLE sensor_data (
   sensor_id uuid,
   timestamp timestamp,
   value float,
   PRIMARY KEY (sensor_id, timestamp)
);
```
- *Analysis*: Columnar storage enables efficient time-range queries.

## Exam Tips
1. Always contrast NoSQL types with relational databases in answers
2. Memorize CAP theorem implications for each database type
3. Use real-world examples (e.g., "Netflix uses Cassandra for...")
4. Highlight schema flexibility as key differentiator
5. Discuss trade-offs: Consistency vs latency, scalability vs complexity
6. Prepare to draw architecture diagrams for column-family stores
7. Understand BASE (Basically Available, Soft state, Eventual consistency) properties

Length: 1500-3000 words, MCA (Master of Computer Applications) PG level