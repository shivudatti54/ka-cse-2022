# Distributed System

## Introduction

A distributed system represents one of the most significant architectural evolutions in computing, where multiple independent computers work together as a single, unified system. In the context of operating systems, distributed systems have become increasingly important as organizations seek to leverage networked resources for enhanced performance, reliability, and scalability. The operating system plays a crucial role in managing these distributed resources, providing abstractions that mask the complexity of underlying network infrastructure from users and applications.

The study of distributed systems is fundamental to modern computing environments, from cloud computing platforms to enterprise networks. Understanding how operating systems handle distributed resources prepares students for roles in system administration, cloud architecture, and distributed application development. As DU graduates entering the technology sector, familiarity with distributed system principles is essential given that most modern applications and services operate in distributed environments.

This topic examines the fundamental characteristics of distributed systems, their architecture, the challenges they present, and how operating systems address these challenges through various mechanisms and abstractions.

## Key Concepts

### Definition and Characteristics

A distributed system is a collection of autonomous computers linked by a computer network that appear to users as a single coherent system. The key characteristic distinguishing distributed systems from simple networks is transparency—the system masks the distribution of resources and processes from users. Users interact with the system as if it were a single computer, rather than being aware of the multiple machines working together.

The essential characteristics of distributed systems include:

1. **Multiple Nodes**: The system consists of multiple independent computers (nodes) that communicate over a network
2. **No Shared Memory**: Nodes do not share physical memory; communication occurs exclusively through message passing
3. **Transparency**: The system provides various forms of transparency to hide distribution from users
4. **Scalability**: The system can grow by adding more nodes without requiring fundamental changes
5. **Fault Tolerance**: The system continues functioning despite failures of individual components
6. **Concurrency**: Multiple users can access the system simultaneously

### Advantages of Distributed Systems

Distributed systems offer several compelling advantages over centralized systems:

**Reliability and Fault Tolerance**: When one node fails, other nodes can continue operating, providing system resilience. This redundancy is crucial for mission-critical applications.

**Scalability**: Distributed systems can handle increased load by adding more machines to the network, unlike centralized systems that have finite capacity limits.

**Resource Sharing**: Expensive resources like printers, storage devices, and specialized hardware can be shared across multiple users and locations.

**Performance**: By distributing computational load across multiple machines, overall system performance can be significantly improved.

**Geographic Distribution**: Users and resources can be geographically dispersed while still functioning as a unified system.

### Challenges in Distributed Systems

Despite their advantages, distributed systems present unique challenges:

**Network Issues**: Communication depends on network reliability. Problems include latency, bandwidth limitations, and network partitions where some nodes cannot communicate with others.

**Security Concerns**: More entry points mean increased security vulnerabilities. Protecting data in transit and authenticating users across distributed nodes requires careful implementation.

**Complexity**: Designing, implementing, and maintaining distributed systems is significantly more complex than centralized systems.

**Data Consistency**: Ensuring all nodes have consistent data at any given time is challenging, especially when updates occur concurrently at multiple locations.

**Coordination**: Synchronizing processes across distributed nodes requires sophisticated algorithms to maintain correctness.

### Architecture Models

**Client-Server Model**: In this classical architecture, clients request services from servers that manage shared resources. The server handles resource management while clients provide user interfaces. This model underlies most web applications and enterprise systems.

**Three-Tier Architecture**: An extension where presentation, processing, and data management are separated into distinct tiers. The middle tier acts as an intermediary between clients and servers.

**Peer-to-Peer (P2P) Model**: All nodes in the system can act as both clients and servers, sharing resources directly with each other. This model is popular in file-sharing applications and blockchain systems.

**Middleware**: Software layer that provides common services and communication facilities between distributed applications, hiding the heterogeneity of underlying networks and operating systems.

### Distributed Operating Systems

Distributed operating systems extend traditional operating system concepts to manage resources across networked computers:

**Network Operating Systems**: Provide connectivity between independent machines but maintain separate operating systems on each node. Users must explicitly access remote resources.

**Distributed Operating Systems**: Present a unified view of distributed resources. Users perceive a single system despite physical distribution. Examples include Amoeba, Mach, and Chorus.

Key mechanisms in distributed operating systems include:

- **Remote Procedure Call (RPC)**: Allows programs to execute procedures on remote systems as if they were local
- **Distributed File Systems**: Present a unified file namespace across multiple machines
- **Process Migration**: Moving processes between nodes for load balancing
- **Clock Synchronization**: Maintaining consistent time across distributed nodes despite communication delays

## Examples

### Example 1: Distributed Database System

Consider a banking system with databases in multiple branches. When a customer withdraws money from an ATM in Delhi, the system must verify their account balance, which might be stored in a Mumbai database.

Step-by-step process:

1. ATM sends withdrawal request to the local branch server
2. Local server initiates distributed transaction across network
3. Communication with Mumbai database verifies balance
4. If sufficient funds exist, authorization travels back through the network
5. ATM dispenses cash and updates are propagated to all relevant databases
6. The system ensures all databases reflect consistent final state (ACID properties)

This example illustrates transparency (user doesn't know which database is accessed), challenges (network latency, consistency), and the role of distributed transaction managers.

### Example 2: Google Search Infrastructure

When you enter a search query on Google, the distributed system behind it performs numerous operations:

1. Load balancer distributes the request across thousands of servers
2. Query is parsed and distributed to multiple index servers simultaneously
3. Each index server searches its portion of the web index in parallel
4. Results are collected, ranked using PageRank algorithm (itself distributed)
5. Final results are assembled and returned to the user

This demonstrates horizontal scalability, fault tolerance (if one server fails, others handle the load), and the illusion of a single powerful system.

### Example 3: File Sharing with P2P Architecture

In a BitTorrent-style file distribution:

1. User requests to download a large file
2. The file is broken into small pieces distributed across many peer computers
3. The downloading client connects to multiple peers simultaneously
4. Each peer contributes bandwidth by uploading pieces it has downloaded
5. As pieces accumulate, the client assembles the complete file
6. Once complete, the node becomes a seed, contributing to network capacity

This example shows how distributed systems leverage collective resources for improved performance and resilience.

## Exam Tips

For DU semester examinations, focus on the following key areas:

1. **Definition and Characteristics**: Be prepared to define distributed systems and list at least four distinguishing characteristics. Understand transparency types: access, location, migration, replication, concurrency, and failure transparency.

2. **Advantages and Disadvantages**: Understand scalability, reliability, and resource sharing benefits versus complexity, security, and consistency challenges. These are frequently tested in short-answer questions.

3. **Client-Server vs P2P**: Know the differences between these architectures, including their respective advantages and use cases.

4. **Distributed vs Network Operating Systems**: Understand the distinction—distributed OS provides a single-system image while network OS maintains separate identities.

5. **RPC Mechanism**: Know what Remote Procedure Call is and why it is fundamental to distributed computing. Understand stub generation and marshalling concepts.

6. **CAP Theorem**: Understand the tradeoff between Consistency, Availability, and Partition tolerance—only two can be guaranteed in distributed systems.

7. **Real-World Examples**: Be prepared to explain distributed system examples like DNS, WWW, and distributed databases. Understanding how these work demonstrates practical knowledge.

8. **OS Role**: Explain how operating systems support distributed environments through process management, memory management, and file system abstractions across networked resources.

9. **Clock Synchronization**: Understand logical clocks and the challenge of maintaining time consistency in distributed environments.

10. **Consistency Models**: Know the difference between strong consistency and eventual consistency in distributed data management.