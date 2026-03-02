# Distributed Systems

## Introduction

A **distributed system** is a collection of physically separate, possibly heterogeneous computer systems that are networked to provide users with access to the various resources the system maintains. Access to a shared resource increases computation speed, functionality, data availability, and reliability.

From an operating system perspective, distributed systems are important because the OS must manage not just a single machine but coordinate resources, communication, and processes across multiple interconnected computers.

## Why Distributed Systems?

| Motivation              | Description                                                                                |
| :---------------------- | :----------------------------------------------------------------------------------------- |
| **Resource sharing**    | Users on one site can use resources available at another (files, printers, processors)     |
| **Computation speedup** | A large computation can be partitioned and distributed among multiple sites (load sharing) |
| **Reliability**         | If one site fails, others can continue operating; redundancy improves availability         |
| **Communication**       | Users at different sites can exchange information (email, file transfer, messaging)        |

## Network Structure

A **network** is a communication path between two or more systems. Distributed systems depend on networking. Networks vary by the distances between their nodes:

### Types of Networks

| Network Type                        | Scope                                   | Example                  |
| :---------------------------------- | :-------------------------------------- | :----------------------- |
| **LAN (Local Area Network)**        | Within a room, floor, or building       | Ethernet in an office    |
| **WAN (Wide Area Network)**         | Between buildings, cities, or countries | The Internet             |
| **MAN (Metropolitan Area Network)** | Within a city                           | City-wide campus network |
| **PAN (Personal Area Network)**     | Within a few meters                     | Bluetooth devices        |

```
LAN Example:
+--------+ +--------+ +--------+
| Host A |----| Host B |----| Host C |
+--------+ +--------+ +--------+
 | | |
 +-------------+--------------+
 LAN (Ethernet)

WAN Example:
+---------+ +---------+
| Site A |---- Internet -------| Site B |
| (Delhi) | (routers, links) | (Mumbai)|
+---------+ +---------+
```

## Network Operating System

A **network operating system** provides an environment in which users can access remote resources by either logging into the appropriate remote machine (**remote login**) or transferring data from the remote machine to their own (**file transfer**).

### Features of a Network OS

1. **Remote login** — A user at site A can log into site B and use its resources (e.g., using `telnet` or `ssh`)
2. **Remote file transfer** — A user can copy files between machines (e.g., using `ftp` or `scp`)
3. **Each machine runs its own local OS** — Users are aware of the multiplicity of machines

```
Network Operating System:

 +----------+ +----------+ +----------+
 | Machine A| | Machine B| | Machine C|
 | (own OS)| | (own OS)| | (own OS)|
 +----+-----+ +----+-----+ +----+-----+
 | | |
 +------------------+------------------+
 Network
 (Users must know which machine has what)
```

**Limitation:** The user must know which machine to connect to. There is no illusion of a single system — users are aware they are working with multiple machines.

## Distributed Operating System

A **distributed operating system** provides a seamless, integrated computing environment across multiple machines. Users are **not aware** of the multiplicity of machines. The OS handles resource location, access, migration, and replication transparently.

### Features of a Distributed OS

| Feature                   | Description                                                |
| :------------------------ | :--------------------------------------------------------- |
| **Transparency**          | Users see a single system, not multiple machines           |
| **Data migration**        | Files move to where they are needed automatically          |
| **Computation migration** | Processes can be transferred to remote sites for execution |
| **Process migration**     | OS can move processes between machines for load balancing  |

```
Distributed Operating System:

 +----------+ +----------+ +----------+
 | Machine A| | Machine B| | Machine C|
 +----+-----+ +----+-----+ +----+-----+
 | | |
 +------------------+------------------+
 Distributed OS Layer
 (Users see ONE unified system)
```

### Network OS vs Distributed OS

| Aspect                 | Network OS                           | Distributed OS                            |
| :--------------------- | :----------------------------------- | :---------------------------------------- |
| **User awareness**     | Users know about multiple machines   | Users see a single system                 |
| **Resource access**    | Manual (remote login, file transfer) | Transparent and automatic                 |
| **OS on each machine** | Independent local OS                 | Single distributed OS across all machines |
| **Complexity**         | Simpler to implement                 | More complex                              |
| **Example**            | Windows network, Linux with NFS      | Amoeba, Mach                              |

## Client-Server Model

The most commonly used structure for distributed systems is the **client-server model**:

- **Server:** A system that provides a service (file server, print server, web server, database server)
- **Client:** A system that requests services from the server

```
Client-Server Architecture:

 +--------+ request +---------+
 | Client |---------------->| |
 | A |<----------------| Server |
 +--------+ response | |
 | |
 +--------+ request | |
 | Client |---------------->| |
 | B |<----------------| |
 +--------+ response +---------+

Server types:
 - Compute server: provides an interface for clients to send requests
 to perform actions (e.g., database server)
 - File server: provides an interface for clients to store and
 retrieve files (e.g., web server serving files)
```

### Types of Servers

| Server Type        | Function                                  | Example                            |
| :----------------- | :---------------------------------------- | :--------------------------------- |
| **Compute server** | Performs computation on behalf of clients | Database server processing queries |
| **File server**    | Stores and serves files to clients        | NFS server, web server             |

## Peer-to-Peer Model

In a **peer-to-peer (P2P)** system, all nodes are equal — each can act as both a client and a server. There is no central server.

```
Peer-to-Peer:

 +------+ +------+
 | Node |<------>| Node |
 | A | | B |
 +------+ +------+
 ^ ^
 | |
 v v
 +------+ +------+
 | Node |<------>| Node |
 | C | | D |
 +------+ +------+

 Every node is both client and server.
```

**Advantages:**

- No single point of failure
- Scales naturally as more nodes join
- No bottleneck at a central server

**Disadvantages:**

- Difficult to manage and secure
- Service discovery is complex (how does a node find what it needs?)

## Clustered Systems

A **clustered system** gathers together multiple CPUs (usually complete systems) to work together, providing **high availability** and **high performance**.

### Types of Clustering

| Type                      | Description                                                                                                               |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| **Asymmetric clustering** | One machine is in **hot-standby** mode, monitoring the active server. If the active server fails, the standby takes over. |
| **Symmetric clustering**  | Two or more hosts are running applications and **monitoring each other**. More efficient use of hardware.                 |

```
Asymmetric Clustering:

 +--------+ +--------+
 | Active | monitors | Standby|
 | Server |<-----------------| Server |
 +--------+ +--------+
 (runs apps) (takes over on failure)

Symmetric Clustering:

 +--------+ +--------+
 | Server | monitor each | Server |
 | A |<---------------->| B |
 +--------+ other +--------+
 (runs apps) (runs apps)
```

Clustering can be used for **high-performance computing (HPC)** where an application is parallelized across all nodes in the cluster. This requires the application to be written to take advantage of multiple nodes (parallelization).

## Summary

| Concept            | Key Point                                                      |
| :----------------- | :------------------------------------------------------------- |
| Distributed system | Collection of networked computers providing shared resources   |
| Network OS         | Users aware of multiple machines; manual remote access         |
| Distributed OS     | Users see one unified system; transparent resource management  |
| Client-server      | Server provides services, clients request them                 |
| Peer-to-peer       | All nodes are equal; each is both client and server            |
| Clustered systems  | Multiple systems coupled for high availability and performance |
| LAN vs WAN         | LAN is local (building), WAN is wide (cities/countries)        |

## Exam Tips

1. **Network OS vs Distributed OS** — This is a very common comparison question. The key difference is transparency: in a distributed OS, users don't know about multiple machines. Use a comparison table.
2. **Client-server vs peer-to-peer** — Know the architecture, advantages, and disadvantages of each model. Draw diagrams.
3. **Clustered systems** — Know asymmetric (hot standby) vs symmetric (both active, monitor each other). This is frequently asked as a short-answer question.
4. **Reasons for distributed systems** — Remember the four motivations: resource sharing, computation speedup, reliability, and communication.
5. **Data migration vs computation migration vs process migration** — Know the differences. Data migration moves files, computation migration moves the computation, process migration moves the entire process.
6. **Draw network diagrams** — exams often ask you to illustrate LAN/WAN topologies and client-server/P2P architectures.
