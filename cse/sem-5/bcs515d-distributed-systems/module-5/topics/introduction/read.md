# Introduction to Distributed Systems

## Introduction

A distributed system is a collection of independent computers that appear to the users as a single coherent system. These computers are connected through a network and communicate with each other by passing messages. The fundamental characteristic of a distributed system is that despite the physical separation of components, the system maintains a unified view of resources and services, presenting itself as if it were a single centralized system to the end users.

The study of distributed systems has become increasingly important in modern computing due to the proliferation of networked applications, cloud computing, and large-scale data processing. From web applications serving millions of users to enterprise databases spanning multiple data centers, distributed architectures have become the backbone of contemporary computing infrastructure. Understanding the principles of distributed systems is essential for designing, implementing, and maintaining such complex computing environments that meet the demands of scalability, reliability, and performance.

The field of distributed systems encompasses various sub-areas including distributed computing, distributed databases, distributed file systems, and distributed transaction management. This module focuses particularly on the transactional aspects of distributed systems, where multiple operations must be coordinated across different nodes to maintain data consistency and integrity.

## Key Concepts

### Characteristics of Distributed Systems

Distributed systems exhibit several defining characteristics that distinguish them from centralized systems. **Transparency** refers to the ability of the system to hide its distributed nature from users and applications, presenting a unified interface. This includes access transparency (hiding differences in data representation), location transparency (hiding where resources are located), migration transparency (allowing resources to move without user knowledge), and replication transparency (hiding the fact that multiple copies exist).

**Openness** is achieved by publishing standard interfaces and allowing components from different vendors to interoperate. Open distributed systems are constructed using well-defined, standard protocols and interfaces. **Scalability** encompasses the ability to handle increased load by adding more resources, both horizontally (adding more nodes) and vertically (adding more power to existing nodes). A scalable system should maintain performance as it grows.

### Architecture Models

The client-server model is the most common architecture in distributed systems, where clients request services and servers provide them. In this three-tier architecture, presentation, application processing, and data management are separated. The peer-to-peer (P2P) model distributes responsibilities equally among all nodes, where each node can act as both client and server. This architecture is highly resilient and scalable, commonly used in file-sharing applications and blockchain systems.

The **middleware** layer sits between the application and the operating system, providing common services and communication mechanisms. Middleware handles issues such as heterogeneity, distribution, and concurrency, allowing application developers to focus on business logic rather than low-level system details. Examples include remote procedure call (RPC) systems, message-oriented middleware, and object request brokers.

### Challenges in Distributed Systems

Distributed systems face unique challenges that do not exist in centralized systems. **Network latency** and partial failures create uncertainty about the state of the system. Messages can be delayed, lost, or duplicated, making it difficult to determine the exact state of remote components. **Heterogeneity** arises from the diversity of hardware, operating systems, and programming languages across different nodes, requiring standardized communication protocols and data representations.

**Security** in distributed systems is more complex due to the multiple points of attack and the need for distributed authentication and authorization. **Concurrency** is inherent in distributed systems, where multiple users access shared resources simultaneously, requiring proper synchronization mechanisms. The famous CAP theorem states that a distributed system can only guarantee two of three properties: Consistency, Availability, and Partition tolerance, forcing system designers to make careful trade-offs based on application requirements.

## Examples

### Example 1: Banking Transaction System

Consider a banking system where a customer transfers funds between accounts maintained at different branches. The distributed transaction must ensure that the debit from one account and credit to another account happen atomically. If the system fails after the debit but before the credit, the transaction must be rolled back to maintain consistency. This requires coordination between database systems at different branches using protocols like Two-Phase Commit (2PC), which ensures atomicity across distributed sites.

### Example 2: E-Commerce Order Processing

An e-commerce platform processing an order involves multiple services: inventory management, payment processing, shipping coordination, and notification services. Each service may run on different servers with separate databases. The order placement must be treated as a distributed transaction where either all services succeed or the entire operation is rolled back. This demonstrates the complexity of maintaining ACID (Atomicity, Consistency, Isolation, Durability) properties in a distributed environment.

### Example 3: Distributed File System

Google File System (GFS) and Hadoop Distributed File System (HDFS) are examples of distributed file systems that store data across multiple commodity servers. These systems provide transparent access to files that may be partitioned and replicated across different nodes. They handle challenges like data partitioning, replication for reliability, and consistency guarantees required for distributed operations.

## Exam Tips

1. Understand the fundamental definition of a distributed system and be able to distinguish it from centralized and parallel systems.

2. Memorize the key characteristics of distributed systems: transparency, openness, scalability, concurrency, and fault tolerance.

3. Be familiar with different architectural models (client-server, peer-to-peer, three-tier) and when each is appropriate.

4. Know the challenges in distributed systems: network issues, heterogeneity, security, concurrency, and the CAP theorem trade-offs.

5. Understand middleware and its role in simplifying distributed application development.

6. Be prepared to explain how distributed systems achieve transparency in various dimensions (access, location, migration, replication).

7. Know the difference between synchronous and asynchronous communication in distributed systems.

8. Understand the relationship between this introductory topic and subsequent topics on distributed transactions, concurrency control, and recovery.