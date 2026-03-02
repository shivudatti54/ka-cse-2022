# Introduction to Distributed File Systems

## What is a Distributed File System?

A **Distributed File System (DFS)** is a file system that allows clients to access and store files on multiple computers across a network as if they were on their local machine. It provides a unified view of files and directories spread across various servers, enabling transparent access and efficient resource sharing in a distributed environment.

The primary goal of a DFS is to provide:
*   **Location Transparency:** Clients access files using a uniform namespace without needing to know their physical location.
*   **Concurrency Transparency:** Multiple clients can access files simultaneously with consistency maintained.
*   **Failure Transparency:** The system continues to operate, perhaps with degraded performance, even if some components fail.

## Key Characteristics and Challenges

Distributed File Systems are characterized by their ability to manage files across networked hosts. Key features include:

*   **Network Transparency:** The file system appears local to the user.
*   **Heterogeneity:** Can operate across different hardware and operating systems.
*   **Scalability:** Can grow to accommodate more users and data.
*   **High Availability:** Files remain accessible despite server or network failures.
*   **Efficiency:** Performance should be comparable to local file systems.

However, building such systems presents significant challenges:

*   **Concurrency Control:** Managing simultaneous read/write operations from multiple clients to prevent data corruption.
*   **Consistency:** Ensuring all clients see a consistent view of the file system, especially after updates.
*   **Fault Tolerance:** Handling server crashes, network partitions, and client failures gracefully.
*   **Security:** Authenticating users and authorizing access to files across the network.
*   **Performance:** Minimizing latency and network bandwidth usage for remote file operations.

## File Service Architecture

A typical DFS architecture is composed of three main abstract components, often implemented as separate services:

### 1. Flat File Service
This is the core service responsible for the actual file operations on the contents of files. It deals with **Unique File Identifiers (UFIDs)** rather than human-readable names. Its main operations include:
*   `Read(UFID, position, size) -> data`
*   `Write(UFID, position, data)`
*   `Create() -> UFID`
*   `Delete(UFID)`

```
+----------------+    Request: Read(UFID:123, offset:0, size:1024)    +---------------------+
|    Client      | -------------------------------------------------> |  Flat File Service |
|                | <------------------------------------------------- |   (File Server)    |
+----------------+    Response: Data (1024 bytes of file content)     +---------------------+
```

### 2. Directory Service
This service maps human-readable text names (e.g., `/home/user/report.txt`) to the UFIDs used by the Flat File Service. It provides operations for managing the directory hierarchy.
*   `Lookup(dir, name) -> UFID`
*   `AddName(dir, name, UFID)`
*   `UnName(dir, name)`
*   `GetNames(dir) -> name-list`

```
+----------------+    Request: Lookup(DirID:456, "report.txt")        +-----------------------+
|    Client      | -------------------------------------------------> |   Directory Service   |
|                | <------------------------------------------------- |   (Name Server)      |
+----------------+    Response: UFID:123                              +-----------------------+
```

### 3. Client Module
This software runs on each client machine. It integrates the DFS with the client's local operating system, often by providing a API or a virtual file system (VFS) layer. It caches frequently used file blocks to improve performance and is responsible for making the entire system appear local and transparent to the user and their applications.

```
+-----------------------------------------------+
|                 Application                   |
| (uses local OS file calls: open, read, write) |
+-----------------------------------------------+
|              Client's Local OS                |
+-----------------------------------------------+
|             DFS Client Module                 |  <-- Caches data, talks to remote services
|  (Implements transparency, handles UFIDs)     |
+-----------------------------------------------+
         |                  |
         V                  V
+----------------+    +-----------------------+
| Flat File      |    | Directory Service     |
| Service        |    |                       |
+----------------+    +-----------------------+
```

## Access Models and Semantics

Different DFS designs adopt different semantics for handling concurrent file access.

### Unix File Semantics (Strong Consistency)
*   Every read operation sees the effects of all previous writes.
*   Suitable for a single-server system or a tightly coupled cluster.
*   **Challenge:** Difficult to maintain in a wide-area distributed system with high latency.

### Session Semantics
*   Changes made to an open file are visible only to the client that has it open.
*   Changes are propagated to the server (and thus to other clients) only when the file is closed.
*   **Advantage:** Good performance and works well for mobile or disconnected clients.
*   **Disadvantage:** Can lead to conflicts if multiple clients modify the same file concurrently.

### Immutable Files
*   Files cannot be changed once created. To "update" a file, a new version is created with a new name.
*   **Advantage:** Simplifies caching and replication dramatically.
*   **Disadvantage:** Not intuitive for all use cases; can waste storage.

## Case Study: Sun Network File System (NFS)

NFS, developed by Sun Microsystems, is a widely deployed DFS that provides a good example of the architecture in practice.

*   **Stateless Design:** NFS servers are stateless; they do not maintain open file state for clients. Each request (read, write) is self-contained, containing a file handle, offset, and count. This simplifies crash recovery.
*   **VFS Layer:** The NFS Client Module integrates into the UNIX VFS, making remote files indistinguishable from local ones.
*   **Caching:** Clients cache recently used file blocks. The server does not participate in consistency management beyond a simple timestamp-based check (`cache_validity` attribute).
*   **Idempotent Operations:** Most operations are designed to be idempotent (can be repeated without ill effects), which allows for simple retransmission on failure.

```
NFS Client-Server Interaction:

Client         Server
  | -- LOOKUP("dir", "file") -> |
  | <-- file_handle (UFID) ---- |
  |                              |
  | -- READ(file_handle, offset, size) -> |
  | <-- DATA ------------------- |
```

## Comparison of Concepts

| Feature | Single-Machine FS | Distributed FS |
| :--- | :--- | :--- |
| **Data Location** | Local disk | Remote servers (network) |
| **Failure Mode** | Total failure if OS/hardware fails | Partial failure; some files may remain accessible |
| **Consistency** | Easy to enforce strong consistency | Complex; often uses weaker models (e.g., session semantics) |
| **Performance** | Limited by local disk speed | Limited by network latency and bandwidth |
| **Transparency** | N/A | A primary design goal (location, access, failure) |

## Exam Tips

1.  **Focus on Transparency:** Be ready to define and give examples of the different types of transparency (location, access, concurrency, failure, replication) in the context of a DFS.
2.  **Understand the Architecture:** Clearly explain the roles of the three core components: Flat File Service, Directory Service, and Client Module. You will likely be asked to describe their interactions for an operation like `open()` or `read()`.
3.  **Compare Semantics:** Be prepared to contrast strong consistency (Unix semantics) with weaker models like session semantics. Discuss the trade-offs between consistency, availability, and performance (hint: this relates to the CAP theorem).
4.  **Know NFS:** Understand the significance of NFS's stateless design and how it aids failure recovery. Be able to explain the concept of idempotent operations.
5.  **Use Diagrams:** In longer answers, a simple ASCII diagram showing the flow of requests between client modules and services can earn significant marks for clarity.