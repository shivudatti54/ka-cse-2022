# NoSQL Key-Value Stores

## Table of Contents

- [NoSQL Key-Value Stores](#nosql-key-value-stores)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Architecture and Data Model](#architecture-and-data-model)
  - [Consistency Models](#consistency-models)
  - [Partitioning and Sharding](#partitioning-and-sharding)
  - [Replication and Fault Tolerance](#replication-and-fault-tolerance)
  - [Caching and In-Memory Storage](#caching-and-in-memory-storage)
  - [Data Expiration and TTL](#data-expiration-and-ttl)
- [Examples](#examples)
  - [Redis](#redis)
- [Storing user session data](#storing-user-session-data)
- [Store session data with 30-minute expiry](#store-session-data-with-30-minute-expiry)
- [Store as JSON string](#store-as-json-string)
- [Retrieve session](#retrieve-session)
  - [Amazon DynamoDB](#amazon-dynamodb)
  - [Cassandra](#cassandra)
- [Exam Tips](#exam-tips)

## Introduction

NoSQL (Not Only SQL) databases have emerged as a powerful alternative to traditional relational database management systems (RDBMS) in the era of big data and cloud computing. Among the various NoSQL database models, Key-Value stores represent the simplest and most fundamental form of NoSQL databases. A key-value store is a data storage paradigm designed for storing, retrieving, and managing associative arrays, also known as dictionaries or hash tables. In this model, data is stored as a collection of key-value pairs where each key is unique and serves as an identifier for retrieving its corresponding value.

The significance of key-value stores in modern computing cannot be overstated. They form the backbone of many high-performance, distributed systems that handle massive amounts of data across multiple servers. Companies like Amazon (DynamoDB), Google (Cloud Datastore), and Redis Labs (Redis) have developed robust key-value store solutions that power some of the world's largest applications. These databases are particularly well-suited for scenarios requiring extreme scalability, low latency, and the ability to handle unstructured or semi-structured data. For students studying Database Management Systems, understanding key-value stores is essential as they represent a fundamental shift from traditional relational database thinking and prepare students for modern data engineering challenges.

## Key Concepts

### Architecture and Data Model

The architecture of a key-value store is remarkably simple yet powerful. At its core, the database consists of a global collection of key-value pairs stored across one or more nodes. Each key acts as a unique identifier, and the associated value can be any type of data - a string, number, JSON document, binary data (BLOB), or even more complex structures serialized into a single value. This simplicity is both the strength and the defining characteristic of key-value stores.

The data model follows a GET/SET paradigm where applications issue commands to store values associated with keys and retrieve values using those keys. Typical operations include SET (to store a value), GET (to retrieve a value), DELETE (to remove a key-value pair), and UPDATE (to modify an existing value). Some key-value stores support additional operations like INCREMENT, EXISTS, and EXPIRE (for setting time-to-live on keys).

### Consistency Models

Key-value stores typically offer tunable consistency models, allowing developers to balance between strong consistency and high availability based on application requirements. **Strong consistency** ensures that all reads see the most recent write, while **eventual consistency** guarantees that if no new updates are made, all replicas will eventually return the same value. The CAP theorem states that a distributed database can only guarantee two of three properties: Consistency, Availability, and Partition tolerance. Most key-value stores prioritize availability and partition tolerance (AP) while offering eventual consistency, though some like etcd offer strong consistency (CP).

### Partitioning and Sharding

To achieve horizontal scalability, key-value stores employ partitioning strategies to distribute data across multiple nodes. **Hash partitioning** maps keys to nodes using a hash function, ensuring even distribution but making range queries inefficient. **Range partitioning** divides the key space into ordered ranges, enabling efficient range queries but potentially causing hot spots. Consistent hashing is a popular technique that minimizes data movement when nodes are added or removed from the cluster.

### Replication and Fault Tolerance

Key-value stores typically replicate data across multiple nodes to ensure high availability and fault tolerance. Replication can be synchronous (waiting for confirmation from all replicas before acknowledging a write) or asynchronous (acknowledging writes immediately while replicating in the background). The **replication factor** determines how many copies of each data item are maintained. Some systems like Amazon Dynamo use quorum-based approaches where reads and writes must succeed across a majority of replicas.

### Caching and In-Memory Storage

Many key-value stores are designed to operate primarily in memory, providing extremely low latency access to data. Redis, for example, offers both in-memory storage with optional persistence and pure memory-based caching modes. This makes key-value stores ideal for session management, caching frequently accessed data, and real-time analytics where response time is critical.

### Data Expiration and TTL

Key-value stores often support time-to-live (TTL) functionality, allowing values to automatically expire after a specified duration. This feature is particularly useful for implementing caching systems, session stores, rate limiting, and temporary data storage scenarios where data becomes stale after a certain period.

## Examples

### Redis

Redis (Remote Dictionary Server) is an open-source, in-memory key-value store that supports various data structures beyond simple strings, including lists, sets, sorted sets, hashes, bitmaps, and hyperloglogs. Redis is widely used for caching, session management, real-time analytics, and message queuing. Its persistence options include RDB snapshots and AOF (Append-Only File) logging, allowing users to balance between performance and durability.

**Example: Session Management in Redis**

```python
# Storing user session data
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Store session data with 30-minute expiry
session_data = {
 'user_id': '12345',
 'username': 'john_doe',
 'role': 'student',
 'login_time': '2024-01-15 10:30:00'
}

# Store as JSON string
import json
r.setex('session:abc123', 1800, json.dumps(session_data))

# Retrieve session
session = json.loads(r.get('session:abc123'))
print(session['username']) # Output: john_doe
```

### Amazon DynamoDB

DynamoDB is a fully managed NoSQL database service by AWS that offers single-digit millisecond latency at any scale. It supports both key-value and document data models, making it flexible for various use cases. DynamoDB automatically partitions data based on throughput requirements and provides features like global tables for multi-region replication.

### Cassandra

Apache Cassandra is a distributed key-value store designed for high write throughput and linear scalability. Originally developed at Facebook, it uses a peer-to-peer architecture with no single point of failure. Cassandra's data model is optimized for time-series data and write-heavy workloads, making it popular for IoT applications and logging systems.

## Exam Tips

1. **Remember the fundamental difference**: Key-value stores store data as simple key-value pairs, unlike relational databases which use tables with rows and columns.

2. **Understand CAP theorem implications**: Know that key-value stores typically sacrifice strong consistency for availability and partition tolerance (AP systems).

3. **Hash partitioning vs Range partitioning**: Hash partitioning distributes keys evenly but prevents range queries; range partitioning allows efficient range queries but may cause hot spots.

4. **Redis is not just a key-value store**: Remember that Redis supports complex data structures (lists, sets, hashes, sorted sets) beyond simple strings.

5. **Consistency levels**: Be familiar with terms like strong consistency, eventual consistency, and causal consistency in the context of distributed key-value stores.

6. **Use cases matter**: Key-value stores excel at caching, session management, real-time analytics, and storing user preferences.

7. **Replication factor**: Understand how data replication across multiple nodes provides fault tolerance and high availability.

8. **TTL functionality**: Remember that time-to-live allows automatic expiration of keys, useful for caching and temporary data.

9. **Horizontal scalability**: Key-value stores scale by adding more nodes rather than upgrading server capacity (vertical scaling).

10. **Persistence options**: Know that in-memory key-value stores like Redis offer various persistence strategies (RDB, AOF) for data durability.
