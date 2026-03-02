# Distributed Systems

## Introduction

A distributed system is a collection of independent computers that appear to the users as a single coherent system. In the context of operating systems, distributed systems represent an advanced architectural paradigm where computation and data are spread across multiple interconnected machines, yet users perceive the entire system as a single entity. This concept has become increasingly important in modern computing environments, from cloud services to enterprise networks, and forms a crucial part of the operating system curriculum at Delhi University.

The study of distributed systems in operating systems examines how traditional OS concepts evolve when computers are networked together. Unlike standalone systems, distributed operating systems must manage resources spread across multiple physical locations, handle communication between processes on different machines, and maintain consistency and reliability despite potential failures. Understanding distributed systems prepares students for modern computing environments where virtually all significant computational workloads involve multiple interconnected machines.

## Key Concepts

### Definition and Characteristics

A distributed system is defined as a collection of autonomous computers linked by a computer network that appears to its users as a single coherent system. The key characteristics that distinguish distributed systems from simple networks include:

**Transparency**: The system masks the distribution of resources and processes from users. There are several types of transparency:
- Access transparency: Hides differences in data representation and access mechanisms
- Location transparency: Hides where resources are physically located
- Migration transparency: Allows resources to move without user knowledge
- Replication transparency: Hides the fact that multiple copies of resources exist
- Concurrency transparency: Hides that multiple users may be sharing resources
- Failure transparency: Hides failures and recovery mechanisms

**Openness**: Distributed systems should be open, meaning they offer services according to standard rules that describe the syntax and semantics of these services.

**Scalability**: The system should function effectively at different scales, from a few computers to millions of nodes. This includes size scalability (adding more users and resources), geographical scalability (users spread across vast distances), and administrative scalability (managing systems across organizations).

### Types of Distributed Systems

**Distributed Computing Systems**: These focus on high-performance computing where computation is divided among multiple machines. Examples include cluster computing (homogeneous machines in a local area network) and grid computing (heterogeneous machines across geographic locations).

**Distributed Information Systems**: These integrate data and information across organizational boundaries. Enterprise resource planning (ERP) systems and transaction processing systems fall under this category.

**Distributed Pervasive Systems**: These are embedded in our environment, such as ubiquitous computing devices, sensor networks, and mobile ad hoc networks.

### Distributed Operating Systems vs Network Operating Systems

It is essential to distinguish between distributed operating systems and network operating systems:

**Network Operating Systems**: Each machine maintains its own local operating system. Users are aware of multiple machines and must explicitly log into remote machines. Examples include Windows NT, Unix with NFS (Network File System), and early versions of LAN Manager. Resources are shared but not seamlessly integrated.

**Distributed Operating Systems**: There is a single operating system image that spans all machines. Users perceive the system as a single computer regardless of how many machines are involved. Processes can execute on any machine, and the system handles load balancing transparently. Examples include Amoeba, Mach, and Chorus.

### Communication in Distributed Systems

Communication is fundamental to distributed systems. The primary models include:

**Message Passing**: Processes communicate by sending and receiving messages through a communication channel. This can be synchronous (blocking send/receive) or asynchronous (non-blocking operations).

**Remote Procedure Call (RPC)**: A procedure call paradigm that allows a program to execute code on a remote machine as if it were a local call. The stub compiler generates client and server stubs that handle parameter marshalling, transmission, and unmarshalling.

**Distributed Shared Memory (DSM)**: Provides an abstraction where each process sees a shared memory address space, even though physical memory is distributed across machines. This simplifies application development but introduces complexity in maintaining consistency.

### Middleware

Middleware is software that provides services above the operating system but below the application layer. It implements common abstractions and services needed by distributed applications, including communication support, information services, transaction management, and security. Examples include CORBA (Common Object Request Broker Architecture), DCOM (Distributed Component Object Model), and Java RMI (Remote Method Invocation).

## Examples

### Example 1: Distributed File System (NFS)

Consider a scenario where a user on workstation A wants to access a file located on server B. Using Network File System (NFS), the process involves:

1. The user issues a file open command for /home/user/data.txt
2. The client-side NFS client translates this to an RPC call
3. The RPC is sent over the network to the NFS server on machine B
4. The server checks permissions, locates the file, and returns a file handle
5. Subsequent read/write operations are translated to NFS calls
6. The server performs actual I/O operations on its local disk
7. Results are returned to the client, which presents them to the user

The user perceives this as a local file operation, demonstrating location transparency. If the server moves, only the mount point configuration changes, not the application code.

### Example 2: Distributed Transaction Processing

A banking transaction transferring Rs. 10,000 from account A to account B, located on different servers, demonstrates distributed atomicity:

1. The transaction manager initiates a two-phase commit protocol
2. Phase 1 (Prepare): Both servers are asked to prepare for commit; they ensure they can complete the transaction and lock the necessary resources
3. Phase 2 (Commit): If both respond positively, the commit is sent; otherwise, rollback commands are sent
4. Both accounts are updated atomically—the transaction either completes entirely or rolls back entirely

This ensures the ACID (Atomicity, Consistency, Isolation, Durability) properties even in a distributed environment.

### Example 3: Load Balancing in Web Servers

In a distributed web hosting scenario, multiple web servers serve the same website:

1. A user enters www.example.com in their browser
2. The DNS server returns one of several IP addresses (using round-robin or more sophisticated routing)
3. The request goes to the selected web server
4. If that server is overloaded, it can forward the request to another server
5. Session state might be maintained through distributed shared memory or a separate session server

This provides scalability and fault tolerance—if one server fails, others continue serving requests.

## Exam Tips

For Delhi University semester examinations, keep the following points in mind:

1. **Definition is crucial**: Be able to define a distributed system precisely. The definition should mention independent computers appearing as a single system.

2. **Transparency types**: Remember all seven types of transparency—access, location, migration, replication, concurrency, performance, and failure.

3. **Distinguish OS types**: Know the difference between distributed and network operating systems. Network OS has separate OS images per machine; distributed OS has a single system image.

4. **Advantages and disadvantages**: Be prepared to list benefits (resource sharing, reliability, scalability, flexibility) and drawbacks (complexity, security issues, network dependency, debugging difficulties).

5. **Middleware role**: Understand middleware as the enabling technology between OS and applications in distributed environments.

6. **Communication models**: Know RPC and message passing as primary communication paradigms in distributed systems.

7. **ACID properties**: In the context of distributed transactions, remember how two-phase commit ensures atomicity and durability.

8. **Real-world examples**: Be familiar with examples like NFS, DNS, World Wide Web, and cloud services to illustrate distributed system concepts.

9. **Classification**: Know the three main types—distributed computing systems, distributed information systems, and distributed pervasive systems.

10. **Scalability dimensions**: Remember the three dimensions—size, geographical, and administrative scalability.