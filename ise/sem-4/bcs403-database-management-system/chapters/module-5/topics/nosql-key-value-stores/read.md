# Redis (Key-Value Store)

## Introduction to Redis

Redis, which stands for **Remote Dictionary Server**, is an open-source, in-memory key-value data store. It is often categorized as a NoSQL database and is renowned for its exceptional performance, versatility, and wide range of data structures. Unlike traditional databases that persist data primarily on disk, Redis stores its entire dataset in memory, which allows for extremely fast read and write operations. It is a critical component in the modern big data ecosystem, primarily used for caching, session storage, real-time analytics, and as a message broker.

### Key Characteristics of Redis

- **In-Memory Data Store:** The primary reason for Redis's speed. Data is accessed from RAM, not disk.
- **Data Persistence:** Despite being in-memory, Redis offers options to persist data to disk (RDB snapshots and AOF logs) to prevent data loss.
- **Rich Data Structures:** It is more than a simple key-string store. It supports strings, hashes, lists, sets, sorted sets, bitmaps, and more.
- **Atomic Operations:** All Redis operations are atomic, ensuring data integrity when multiple clients access the server simultaneously.
- **Replication and High Availability:** Redis supports master-replica replication for data redundancy and failover.
- **Pub/Sub Messaging:** Built-in Publish/Subscribe messaging paradigm for building real-time features.

## Core Data Structures in Redis

Redis's power comes from its support for various data structures. A key can point to different types of values.

| Data Structure        | Description                                                                         | Example Use Case                                                       |
| :-------------------- | :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **String**            | The most basic type. Can hold text, binary data, or integers.                       | Caching HTML fragments, counter values.                                |
| **Hash**              | A map between string fields and string values. Perfect for representing objects.    | Storing user profiles (e.g., `user:1000` with fields `name`, `email`). |
| **List**              | A collection of ordered string elements. Elements can be added to the head or tail. | Implementing queues (e.g., a task queue for background jobs).          |
| **Set**               | An unordered collection of unique strings.                                          | Tracking unique visitors to a website, tags for a blog post.           |
| **Sorted Set (ZSet)** | Like a Set, but every member has a score, used for ordering.                        | Leaderboards, priority queues.                                         |

**Example Commands:**

```bash
# String
SET user:1000:name "Alice"
GET user:1000:name

# Hash
HSET user:1000 name "Alice" email "alice@example.com"
HGETALL user:1000

# List
LPUSH tasks "send_email"
RPOP tasks

# Set
SADD article:123:tags "tech" "nosql" "database"
SMEMBERS article:123:tags

# Sorted Set
ZADD leaderboard 100 "player1" 85 "player2"
ZREVRANGE leaderboard 0 2 WITHSCORES # Get top 3 players
```

## Redis Architecture and Persistence

### In-Memory Architecture

```
+-----------------------+
|   Redis Client        |     GET key
| (Application Code)    | ------------+
+-----------------------+             |
                                      |
                                +------------+
                                | Redis Server|
                                | +---------+ |
                                | | In-Memory | |  # Data lives here
                                | | Dataset   | |
                                | +---------+ |
                                +------------+
                                      |
                                      | (Optional Persistence to Disk)
                                +------------+
                                |   Disk     |
                                | (RDB/AOF)  |
                                +------------+
```

The diagram illustrates the core principle: clients interact directly with the in-memory dataset for blazing-fast performance. Persistence to disk is an asynchronous operation.

### Persistence Mechanisms

To ensure durability, Redis provides two main persistence options:

1.  **RDB (Redis Database Backup):**
    - Takes point-in-time **snapshots** of the dataset at specified intervals.
    - **Pros:** Compact, single file. Perfect for backups and disaster recovery. Faster restart times.
    - **Cons:** Can lose data from the last snapshot if the system crashes.

2.  **AOF (Append-Only File):**
    - Logs every **write operation** received by the server. This log can be replayed on restart to rebuild the state.
    - **Pros:** Greater durability. Configurable sync policies (e.g., sync every second, sync every write).
    - **Cons:** Larger file size than RDB. Can be slower than RDB on restarts if the log is large.

In practice, both can be used together for a balance of performance and durability.

## Primary Use Cases in Big Data Architecture

### 1. Caching

This is the most common use case. Redis sits in front of a slower primary database (like MySQL or PostgreSQL) to store frequently accessed data.

```
+-------------+  Cache Miss  +----------+  Query  +---------------+
| Application |------------->|  Redis   |-------->| Primary DB    |
|   Server    |              | (Cache)  |         | (e.g., MySQL) |
+-------------+              +----------+         +---------------+
       ^                          |                    |
       |       Cache Hit          |        Store Result|
       +--------------------------+<-------------------+
```

**How it works:**

1.  The app requests data from Redis first.
2.  If the data is found (**cache hit**), it is returned immediately.
3.  If not found (**cache miss**), the app queries the primary database.
4.  The result is stored in Redis for future requests and returned to the app.

This drastically reduces latency and load on the primary database.

### 2. Pub/Sub (Publish/Subscribe) Messaging

Redis provides a Pub/Sub system where senders (publishers) are not programmed to send messages to specific receivers (subscribers). Instead, messages are published to "channels," and subscribers receive all messages published to the channels they are interested in.

```
+------------+      PUBLISH news.tech "Redis 7 released!"      +-----------------+
| Publisher  | ----------------------------------------------> | Redis Broker   |
+------------+                                                 +-----------------+
                                                                       |
                                                                       | (Message routed to
                                                                       | subscribed channels)
+-------------+     Message Delivered     +-------------+      +-------------+
| Subscriber  | <-----------------------  |   Channel   |      | Subscriber  |
|(Topic: tech)|                           |  news.tech  |      |(Topic: all) |
+-------------+                           +-------------+      +-------------+
```

This is fundamental for building real-time features like live chat, notification systems, and live score updates.

### 3. Session Store

Web applications often use Redis to store user session data (e.g., user preferences, shopping cart items). This is especially useful in distributed systems where user requests might be handled by different application servers. Storing sessions in Redis provides a single, shared source of truth.

### 4. Real-Time Analytics

Using commands like `INCR` (for counters) and HyperLogLog (for efficient unique counting), Redis can track metrics like page views, unique visitors, and user actions in real-time with minimal performance overhead.

## Redis vs. Other NoSQL Databases

| Feature                | Redis (Key-Value)                                                           | MongoDB (Document)                                               | Cassandra (Wide-Column)                             |
| :--------------------- | :-------------------------------------------------------------------------- | :--------------------------------------------------------------- | :-------------------------------------------------- |
| **Primary Data Model** | Key-Value with rich data types                                              | Document (JSON-like BSON)                                        | Wide-Column (Rows & Column Families)                |
| **Storage**            | **In-Memory** (with disk persistence)                                       | Disk-Based                                                       | Disk-Based                                          |
| **Performance**        | **Extremely Low Latency** (μs)                                              | Low Latency (ms)                                                 | High Throughput (ms)                                |
| **Query Flexibility**  | Simple key-based access. Complex queries require processing on client side. | **Rich Query Language** (e.g., range, text search, aggregations) | Queryable by primary key; limited secondary indexes |
| **Primary Use Case**   | Caching, Queues, Pub/Sub, Session Storage                                   | Content Management, User Profiles, Catalogs                      | Time-Series Data, Write-Heavy Applications          |

## Exam Tips

1.  **Focus on Use Cases:** Be prepared to explain _why_ you would use Redis. The answer will almost always involve **caching for performance** or **Pub/Sub for real-time messaging**.
2.  **Understand Persistence:** Know the difference between RDB and AOF. RDB is for snapshots/backups, AOF is for durability. You should be able to list a pro and con for each.
3.  **Data Structures are Key:** Remember that Redis is more than simple strings. Be able to match a data structure (Hash, Sorted Set, List) to a problem (e.g., "How would you implement a leaderboard?" -> **Sorted Set**).
4.  **CAP Theorem Context:** Redis is often configured as a **CP** (Consistent and Partition-Tolerant) system in its primary mode. In a network partition, it prioritizes consistency by rejecting requests if it can't guarantee them, potentially sacrificing availability. This is different from AP systems like Cassandra.
5.  **Vocabulary:** Ensure you know terms like **cache hit/miss**, **replication**, **atomicity**, and **in-memory**.
