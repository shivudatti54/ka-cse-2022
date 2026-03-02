# Introduction to NoSQL Systems

## Table of Contents

- [Introduction to NoSQL Systems](#introduction-to-nosql-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Types of NoSQL Databases](#1-types-of-nosql-databases)
  - [2. CAP Theorem](#2-cap-theorem)
  - [3. ACID vs BASE Properties](#3-acid-vs-base-properties)
  - [4. Scalability](#4-scalability)
  - [5. Schema Flexibility](#5-schema-flexibility)
- [Examples](#examples)
  - [Example 1: Document Database Query (MongoDB)](#example-1-document-database-query-mongodb)
  - [Example 2: Key-Value Store with Redis](#example-2-key-value-store-with-redis)
- [Store session data](#store-session-data)
- [Retrieve session data](#retrieve-session-data)
- [Set expiration (session valid for 30 minutes)](#set-expiration-session-valid-for-30-minutes)
  - [Example 3: CAP Theorem Application](#example-3-cap-theorem-application)
- [Exam Tips](#exam-tips)

## Introduction

NoSQL (Not Only SQL) systems represent a fundamental shift in database management that emerged in the late 2000s to address the limitations of traditional relational database management systems (RDBMS). As web applications grew to handle massive volumes of unstructured and semi-structured data, the rigid schema of relational databases became a bottleneck. NoSQL databases were designed to provide flexible schema, horizontal scalability, and high performance for distributed data storage requirements.

The term "NoSQL" does not mean "no SQL" but rather "Not Only SQL," acknowledging that these systems often support query languages that resemble SQL in functionality. NoSQL databases have become the backbone of modern web applications, powering companies like Facebook, Google, Amazon, and Netflix to handle billions of user interactions daily. For CSE students, understanding NoSQL systems is essential as industry demand for professionals skilled in these technologies continues to grow exponentially.

## Key Concepts

### 1. Types of NoSQL Databases

**Document Databases:** Store data in document format, typically using JSON or BSON (Binary JSON). Each document contains key-value pairs and can have varying structures. Examples include MongoDB, CouchDB, and Amazon DocumentDB. Documents are grouped into collections, providing flexibility without predefined schemas.

**Key-Value Stores:** The simplest form of NoSQL databases, storing data as pairs of keys and values. They provide extremely fast read/write operations. Examples include Redis, Amazon DynamoDB, and Apache Cassandra (when used in simple mode). Ideal for caching, session management, and real-time bidding systems.

**Column Family Stores:** Also known as wide-column stores, these databases store data in columns rather than rows. They are optimized for queries over large datasets and provide excellent compression. Examples include Apache Cassandra, HBase, and Amazon Redshift. These are particularly useful for time-series data and analytical workloads.

**Graph Databases:** Designed specifically for handling interconnected data with many relationships. They use nodes to represent entities and edges to represent relationships. Examples include Neo4j, Amazon Neptune, and ArangoDB. Perfect for social networks, recommendation engines, and fraud detection.

### 2. CAP Theorem

The CAP theorem (Brewer's theorem) states that a distributed database system can provide only two of the following three guarantees simultaneously:

- **Consistency (C):** Every read receives the most recent write or an error
- **Availability (A):** Every request receives a non-error response, without guarantee of the most recent write
- **Partition Tolerance (P):** The system continues to operate despite network failures between nodes

Since network partitions are inevitable in distributed systems, designers must choose between consistency and availability. NoSQL databases are often categorized as CP (consistency + partition tolerance) or AP (availability + partition tolerance) systems.

### 3. ACID vs BASE Properties

Traditional relational databases follow ACID properties:

- **Atomicity:** Transactions are all-or-nothing
- **Consistency:** Database moves from one valid state to another
- **Isolation:** Concurrent transactions appear serial
- **Durability:** Committed data survives system failures

NoSQL databases typically follow BASE properties:

- **Basically Available:** The system guarantees availability
- **Soft State:** State may change over time without input
- **Eventual Consistency:** System will become consistent over time

### 4. Scalability

**Horizontal Scaling (Scale Out):** Adding more servers to the database cluster. NoSQL databases are designed for horizontal scaling, making them ideal for handling massive datasets.

**Vertical Scaling (Scale Up):** Adding more resources (CPU, RAM, storage) to a single server. Traditional RDBMS typically rely on vertical scaling, which has practical limits.

### 5. Schema Flexibility

NoSQL databases offer flexible or schema-less data models, allowing:

- Dynamic schema changes without database downtime
- Storage of heterogeneous data in the same collection
- Rapid iteration in application development

## Examples

### Example 1: Document Database Query (MongoDB)

**Problem:** Insert and query student documents with varying structures.

**Solution:**

```javascript
// Insert documents with different structures
db.students.insertMany([
  { name: 'Rahul', marks: { math: 85, physics: 78 } },
  { name: 'Priya', marks: { math: 92, chemistry: 88 }, sports: ' cricket' },
  { name: 'Amit', marks: { math: 70, physics: 65, chemistry: 72 } },
]);

// Query all students
db.students.find();

// Query with condition
db.students.find({ 'marks.math': { $gt: 80 } });

// Update with $set (add new field dynamically)
db.students.updateOne({ name: 'Rahul' }, { $set: { attendance: 95 } });
```

This demonstrates schema flexibility—each document can have different fields.

### Example 2: Key-Value Store with Redis

**Problem:** Implement a simple session cache for a web application.

**Solution:**

```python
import redis

r = redis.Redis(host='localhost', port=6379)

# Store session data
session_id = "user:12345"
r.hset(session_id, mapping={
 'username': 'john_doe',
 'login_time': '2024-01-15 10:30:00',
 'cart_items': '3'
})

# Retrieve session data
session_data = r.hgetall(session_id)
print(session_data)

# Set expiration (session valid for 30 minutes)
r.expire(session_id, 1800)
```

Key-value stores provide O(1) time complexity for read/write operations, making them extremely fast.

### Example 3: CAP Theorem Application

**Problem:** Choose appropriate database for an e-commerce inventory system where consistency is critical.

**Analysis:**

- For inventory management, consistency is paramount—you cannot sell more items than available
- Availability can be temporarily sacrificed during network partitions
- **Recommendation:** Use CP system like Apache Cassandra with strong consistency settings or MongoDB with appropriate write concerns
- **Avoid:** Systems optimized for eventual consistency (like DynamoDB in default mode) for critical inventory data

## Exam Tips

1. **Remember the four types of NoSQL databases** (Document, Key-Value, Column Family, Graph) with at least one example for each.

2. **Understand CAP theorem thoroughly**: Be able to explain what each property means and why all three cannot be guaranteed simultaneously in distributed systems.

3. **Differentiate ACID and BASE**: Know that ACID is for traditional RDBMS while BASE is for NoSQL systems, and understand each property.

4. **Horizontal vs Vertical scaling**: NoSQL databases primarily use horizontal scaling (scale-out), while RDBMS typically uses vertical scaling (scale-up).

5. **Schema flexibility advantage**: Remember that NoSQL allows dynamic schema, enabling storage of unstructured data and rapid application development.

6. **Real-world applications**: Know common use cases—MongoDB for content management, Redis for caching, Cassandra for time-series data, Neo4j for social networks.

7. **Eventual consistency concept**: Understand that NoSQL databases often sacrifice immediate consistency for better availability and partition tolerance, with consistency achieved over time.
