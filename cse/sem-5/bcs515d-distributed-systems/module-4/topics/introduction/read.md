# Introduction to Distributed Systems

## Introduction

A distributed system is a collection of independent computers that appear to users as a single coherent system. The fundamental characteristic that distinguishes distributed systems from centralized systems is the absence of shared memory or a global clock. Instead, these systems rely on message passing over a computer network to achieve coordination among independent nodes. This architectural paradigm has become the backbone of modern computing infrastructure, powering everything from web applications and cloud services to blockchain networks and Internet of Things (IoT) platforms.

The development of distributed systems emerged from the need to achieve goals that centralized systems could not accomplish efficiently. These goals include resource sharing, where expensive peripherals or specialized hardware can be accessed by multiple users across the network; openness, which allows the system to be extended and improved through the addition of new services; concurrency, enabling multiple users to access shared resources simultaneously; and scalability, permitting the system to grow by adding more nodes without disrupting existing services. The transparency requirement ensures that the complexity of distribution is hidden from users, presenting the system as if it were a single, unified entity.

Distributed systems present unique challenges that do not exist in centralized systems. The fundamental issues include the uncertainty of message delivery in asynchronous systems where network delays are unpredictable, the possibility of partial failures where some nodes or network links fail while others continue operating, and the inherent complexity of maintaining consistency across geographically dispersed data. Furthermore, designing secure systems that are resilient to both external attacks and internal malicious behavior adds another layer of difficulty. Understanding these challenges and the techniques to address them forms the foundation for studying advanced topics such as consensus, mutual exclusion, and election algorithms.

## Key Concepts

### Characteristics of Distributed Systems

Distributed systems exhibit several defining characteristics that differentiate them from other computing paradigms. **Heterogeneity** refers to the diversity of hardware, operating systems, programming languages, and software components that must work together seamlessly. Modern distributed systems often integrate devices ranging from high-performance servers to mobile phones, each with different capabilities and constraints. The **openness** property determines whether the system can be extended and implemented in various ways, typically achieved through well-defined standard interfaces and protocols.

**Scalability** is perhaps the most critical characteristic, measuring the system's ability to handle growing amounts of work or its capacity to be enlarged to accommodate that growth. A scalable system should maintain performance as the number of users, data volume, or geographic distribution increases. This requires careful design decisions regarding the placement of data, the routing of requests, and the distribution of processing load. **Transparency** encompasses multiple dimensions: access transparency hides differences in data representation, location transparency hides where resources are physically located, migration transparency allows resources to move without user knowledge, and replication transparency makes multiple copies of resources appear as single entities.

### System Models and Architecture

Distributed systems are typically characterized by three architectural models. The **client-server model** is the simplest, where clients request services and servers provide them. This model, while straightforward, can become a bottleneck when demand is high. The **three-tier model** introduces an intermediate layer between clients and servers, often for business logic or data transformation. The **peer-to-peer model** eliminates the distinction between clients and servers, with each node acting as both client and server, sharing resources and responsibilities equally.

The **network architecture** fundamentally affects system behavior. In synchronous systems, there are known bounds on processing speed, message transmission delays, and clock drift, making it easier to detect failures. Asynchronous systems, more common in practice, make no such assumptions, presenting significant challenges for algorithm design. Understanding whether a system is synchronous or asynchronous is crucial because many distributed algorithms work correctly only under specific timing assumptions.

### Fundamental Challenges

The **CAP theorem** (Brewer's theorem) states that a distributed system can provide only two of three guarantees simultaneously: Consistency, Availability, and Partition tolerance. Since network partitions are inevitable in distributed systems, designers must choose between strong consistency with potential unavailability during partitions, or availability with eventual consistency. This trade-off is fundamental to system design and influences technologies ranging from traditional databases to modern NoSQL systems.

**Failure handling** presents unique challenges in distributed environments. Failures can be classified as crash failures (a node stops functioning), omission failures (messages are lost), timing failures (responses arrive outside expected windows), and Byzantine failures (nodes behave arbitrarily or maliciously). Designing systems that detect, mask, or recover from these failures requires sophisticated techniques including redundancy, replication, and checkpointing.

## Examples

**Example 1: DNS (Domain Name System)**

The DNS system is a classic example of a distributed system that provides name resolution services globally. When a user types "example.com" in a browser, hundreds of DNS servers cooperate to translate this human-readable name into an IP address. The system uses a hierarchical structure with root servers, top-level domain servers, and authoritative name servers. Each server maintains only a portion of the total namespace, and queries propagate through the hierarchy until the appropriate authoritative server is found. This design ensures scalability, fault tolerance, and resilience to high query volumes, demonstrating how distribution enables global-scale services.

**Example 2: Distributed Database Systems**

Modern distributed databases like Cassandra, DynamoDB, or Google's Spanner partition data across multiple nodes, either by row (horizontal partitioning) or by function. When a write operation occurs, the system must coordinate updates across multiple replicas to maintain consistency guarantees. The choice of consistency level (strong, eventual, or somewhere in between) directly impacts performance and availability. For instance, a financial application might require strong consistency for balance transfers, while a social media application might accept eventual consistency for likes and comments to maximize responsiveness.

**Example 3: Blockchain and Cryptocurrency Networks**

Bitcoin and Ethereum represent highly distributed systems where consensus among potentially untrustworthy participants determines the state of a shared ledger. These systems must solve the Byzantine Generals Problem, ensuring agreement despite the presence of malicious nodes. The consensus mechanism (Proof of Work in Bitcoin, Proof of Stake in Ethereum) determines how new blocks are added and how conflicts are resolved, demonstrating how distributed systems achieve coordination without central authority.

## Exam Tips

1. **Understand the CAP theorem thoroughly**: Be prepared to explain the trade-offs between consistency, availability, and partition tolerance with concrete examples.

2. **Differentiate between transparency types**: Know all eight types of transparency (access, location, migration, relocation, replication, failure, concurrency, and persistence) and provide examples of each.

3. **Classify failure types correctly**: Be able to distinguish between crash, omission, timing, and Byzantine failures and explain why Byzantine failures are most difficult to handle.

4. **Relate introduction to advanced topics**: Understand how the challenges introduced here (coordination, agreement, mutual exclusion) connect to the sibling topics of consensus, group communication, and elections.

5. **Compare system models**: Be prepared to contrast client-server, three-tier, and peer-to-peer architectures with their advantages and disadvantages.

6. **Address scalability in designs**: When discussing any distributed system, consider how it scales and what limitations exist.

7. **Synchronous vs. asynchronous**: Know the fundamental differences and how they impact algorithm design and failure detection capabilities.