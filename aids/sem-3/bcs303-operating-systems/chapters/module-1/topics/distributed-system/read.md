# What are Distributed Systems?

## Definition

A **distributed system** is a collection of independent computers that appears to its users as a single coherent system. These computers communicate and coordinate their actions by passing messages over a network, working together to achieve a common goal.

## Key Characteristics

### 1. Multiple Components

- System consists of multiple autonomous computers (nodes)
- Each node has its own local memory and processor
- Nodes may be heterogeneous (different hardware/OS)

### 2. Message Passing

- Components communicate through network messages
- No shared memory between nodes
- Communication introduces latency and potential failures

### 3. Common Goal

- All components work toward a unified objective
- Users perceive the system as a single entity
- Coordination ensures consistent behavior

## Why Distributed Systems?

| Motivation           | Description                                         |
| -------------------- | --------------------------------------------------- |
| **Scalability**      | Handle growing workload by adding more nodes        |
| **Reliability**      | Continue operating despite individual failures      |
| **Performance**      | Parallel processing and geographic distribution     |
| **Resource Sharing** | Share hardware, software, and data across locations |
| **Cost Efficiency**  | Use commodity hardware instead of supercomputers    |

## Centralized vs Distributed Systems

| Aspect                  | Centralized     | Distributed |
| ----------------------- | --------------- | ----------- |
| Single Point of Failure | Yes             | No          |
| Scalability             | Limited         | High        |
| Complexity              | Lower           | Higher      |
| Latency                 | Lower           | Variable    |
| Cost                    | Higher per unit | Lower total |

## Examples of Distributed Systems

### 1. World Wide Web

- Millions of web servers worldwide
- Clients access resources transparently
- DNS provides name resolution

### 2. Cloud Computing Platforms

- AWS, Google Cloud, Microsoft Azure
- Resources distributed across data centers
- Elastic scaling based on demand

### 3. Distributed Databases

- Apache Cassandra, MongoDB, CockroachDB
- Data partitioned across multiple nodes
- Replication for fault tolerance

### 4. Peer-to-Peer Networks

- BitTorrent, Blockchain networks
- No central server
- Nodes share resources directly

### 5. Content Delivery Networks (CDNs)

- Cloudflare, Akamai, AWS CloudFront
- Content cached at edge locations
- Reduces latency for end users

## Challenges in Distributed Systems

### 1. Network Unreliability

- Messages can be lost, duplicated, or delayed
- Network partitions can isolate nodes
- Bandwidth limitations

### 2. Partial Failures

- Individual nodes can fail independently
- Difficult to determine if a node is slow or dead
- Must handle failures gracefully

### 3. Concurrency

- Multiple operations happening simultaneously
- Race conditions and deadlocks
- Need for synchronization

### 4. No Global Clock

- Each node has its own clock
- Clocks can drift
- Ordering events is challenging

### 5. Heterogeneity

- Different hardware, OS, networks
- Different programming languages
- Need for interoperability

## Transparency in Distributed Systems

Distributed systems aim to hide the complexity of distribution from users:

| Type            | Description                             |
| --------------- | --------------------------------------- |
| **Access**      | Hide differences in data representation |
| **Location**    | Hide where resources are located        |
| **Migration**   | Hide that resources may move            |
| **Replication** | Hide that resources are replicated      |
| **Concurrency** | Hide that resources may be shared       |
| **Failure**     | Hide failure and recovery               |

## Lamport's Definition

Leslie Lamport famously defined a distributed system as:

> "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable."

This highlights the complexity and interdependencies in distributed systems.

## Summary

- Distributed systems are collections of networked computers working as one
- They provide scalability, reliability, and resource sharing
- Key challenges include network failures, concurrency, and clock synchronization
- Transparency hides distribution complexity from users
- Understanding distributed systems is essential for cloud computing
