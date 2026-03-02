# CAP Theorem

## Introduction

The **CAP Theorem** (also known as Brewer's Theorem) is a fundamental principle in distributed systems that states it is impossible for a distributed system to simultaneously provide all three of the following guarantees:

- **C**onsistency
- **A**vailability
- **P**artition Tolerance

## The Three Properties

### Consistency (C)
Every read receives the most recent write or an error.

**Characteristics:**
- All nodes see the same data at the same time
- After a write completes, all subsequent reads return that value
- Linearizability - operations appear instantaneous

**Example:** A banking system where balance must be accurate across all ATMs immediately after a transaction.

### Availability (A)
Every request receives a response (not an error).

**Characteristics:**
- System always responds to requests
- No timeouts or errors due to system issues
- May return stale data

**Example:** A website that always loads, even if showing slightly outdated content.

### Partition Tolerance (P)
System continues to operate despite network partitions.

**Characteristics:**
- Network can lose messages between nodes
- System handles arbitrary message loss
- Must function even when split into disconnected groups

**Example:** Nodes in different data centers continue operating when the connection between them fails.

## The CAP Trade-off

During a network partition, a distributed system must choose between:

| Choice | Trade-off | Behavior |
|--------|-----------|----------|
| CP | Sacrifice Availability | Return error or timeout when partition occurs |
| AP | Sacrifice Consistency | Return potentially stale data during partition |
| CA | Sacrifice Partition Tolerance | Not possible in distributed systems |

### Why CA is Not Possible

In any distributed system, network partitions WILL occur. Therefore:
- You must choose either C or A when partition happens
- CA only exists in single-node systems (not distributed)

## System Classifications

### CP Systems (Consistency + Partition Tolerance)
Prioritize correctness over availability.

**Examples:**
- MongoDB (in certain configurations)
- HBase
- Redis Cluster
- Zookeeper

**Use Cases:**
- Financial transactions
- Inventory management
- Any system where incorrect data is worse than no data

### AP Systems (Availability + Partition Tolerance)
Prioritize responsiveness over consistency.

**Examples:**
- Cassandra
- DynamoDB
- CouchDB
- DNS

**Use Cases:**
- Social media feeds
- Shopping carts
- Caching systems
- Any system where stale data is acceptable temporarily

## PACELC Theorem

An extension of CAP that also considers latency:

**P**artition: Choose **A**vailability or **C**onsistency
**E**lse (no partition): Choose **L**atency or **C**onsistency

| System | During Partition | Normal Operation |
|--------|------------------|------------------|
| DynamoDB | A (available) | L (low latency) |
| BigTable | C (consistent) | C (consistent) |
| MongoDB | C (consistent) | L (low latency) |

## Practical Implications

### 1. Design Decisions
- Understand your data's consistency requirements
- Accept that trade-offs are necessary
- Different data may have different requirements

### 2. Consistency Models
When choosing availability, consider:
- **Eventual Consistency:** Data converges over time
- **Causal Consistency:** Related operations ordered correctly
- **Read-your-writes:** User sees their own writes

### 3. Handling Partitions
- Detect partitions quickly
- Define behavior during partition
- Resolve conflicts after partition heals

## Real-World Examples

### Amazon DynamoDB
- AP system with eventual consistency by default
- Offers strongly consistent reads as option
- Sacrifices consistency for high availability

### Google Spanner
- CP system with strong consistency
- Uses TrueTime API for global synchronization
- Provides external consistency (linearizability)

### Apache Cassandra
- AP system, tunable consistency
- Consistency level configurable per operation
- QUORUM reads/writes provide stronger guarantees

## CAP in Practice

### E-Commerce Example

**Shopping Cart (AP):**
- Better to show cart than show error
- Conflicts resolved at checkout
- Last-write-wins or merge strategy

**Payment Processing (CP):**
- Cannot allow incorrect charges
- Better to fail than process wrong amount
- Strong consistency required

### Social Media Example

**News Feed (AP):**
- Slightly stale content acceptable
- User experience prioritized
- Eventual consistency is fine

**Account Settings (CP):**
- Password changes must be immediate
- Security requires consistency
- Can tolerate brief unavailability

## Common Misconceptions

### Misconception 1: Must Choose One Forever
Reality: Different parts of system can make different choices.

### Misconception 2: It's All or Nothing
Reality: Consistency and availability are spectrums, not binary.

### Misconception 3: Partition Tolerance is Optional
Reality: Network partitions are inevitable; you must handle them.

## Summary

- CAP theorem states you can only have 2 of 3 properties
- Network partitions are inevitable in distributed systems
- Must choose between CP (consistency) and AP (availability)
- PACELC extends CAP to include latency considerations
- Different use cases require different trade-offs
- Modern systems often provide tunable consistency
