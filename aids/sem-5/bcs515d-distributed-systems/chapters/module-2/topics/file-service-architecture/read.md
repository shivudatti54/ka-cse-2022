# File Service Architecture in Distributed Systems

## Introduction to Distributed File Systems (DFS)

A **Distributed File System (DFS)** is a client/server-based application that allows clients to access and process data stored on a server as if it were on their own computer. The main goal of a DFS is to provide a transparent, location-independent interface for accessing files that may be spread across multiple physical machines in a network.

**Key Characteristics of a DFS:**
*   **Transparency:** Users should not be aware of the distribution of files.
*   **Concurrency:** Multiple clients should be able to access files simultaneously.
*   **Heterogeneity:** The system should work across different hardware and operating systems.
*   **Fault Tolerance:** The system should be resilient to failures of servers or network components.
*   **Scalability:** The system should be able to grow to accommodate more users and more data.

## The Architecture of File Services

The architecture of a file service is typically broken down into three distinct, modular components. This separation of concerns simplifies design, implementation, and maintenance. The three main components are the **Flat File Service**, the **Directory Service**, and the **Client Module**.

### 1. The Flat File Service

The Flat File Service is concerned with the **contents of files** and their **unique identifiers (UFIDs)**. It deals with the raw bytes of a file and provides a set of primitive, low-level operations.

*   **Unique File Identifier (UFID):** A unique, immutable identifier assigned to a file when it is created. It is not a human-readable pathname (e.g., `/users/alice/report.txt`); it is more like an inode number or a unique serial number (e.g., `#12345:67890`). The UFID is how the flat file service references a file.
*   **Responsibilities:**
    *   Managing file storage on disk.
    *   Performing read and write operations on file contents.
    *   Managing file attributes (e.g., owner, permissions, size, timestamps).
    *   It does *not* understand file hierarchical structures or pathnames.

**Common Operations of a Flat File Service:**
*   `Read(UFID, offset, count) -> data`
*   `Write(UFID, offset, data)`
*   `Create() -> UFID`
*   `Delete(UFID)`
*   `GetAttributes(UFID) -> attr`
*   `SetAttributes(UFID, attr)`

### 2. The Directory Service

The Directory Service provides the **mapping** between human-readable textual names (the pathnames users understand) and the machine-readable UFIDs (the identifiers the flat file service understands). It is essentially a specialized database for name-to-UFID binding.

*   **Responsibilities:**
    *   Creating and managing directories and symbolic links.
    *   Translating pathnames (e.g., `/home/user/file.txt`) into UFIDs.
    *   Maintaining the hierarchical namespace that users navigate.
    *   It does *not* handle the actual file data; it only manages the references to it.

**Common Operations of a Directory Service:**
*   `Lookup(dir UFID, name) -> UFID` (Resolves a name in a directory to a UFID)
*   `AddName(dir UFID, name, UFID)` (Adds a new name-to-UFID binding)
*   `UnLink(dir UFID, name)` (Removes a name-to-UFID binding)
*   `GetNames(dir UFID) -> list of names` (Lists the contents of a directory)

**Example of Pathname Resolution:**
```
User requests: /Users/Bob/Docs/report.txt

1. Client asks Directory Service to resolve "/" (root directory). Gets UFID for root (e.g., #1).
2. Client asks Directory Service to look up "Users" in directory #1. Gets UFID for Users dir (e.g., #101).
3. Client asks Directory Service to look up "Bob" in directory #101. Gets UFID for Bob's dir (e.g., #201).
4. Client asks Directory Service to look up "Docs" in directory #201. Gets UFID for Docs dir (e.g., #301).
5. Client asks Directory Service to look up "report.txt" in directory #301. Gets UFID for the file (e.g., #4099).
6. Client uses UFID #4099 to call the Flat File Service's `Read` operation.
```

### 3. The Client Module

The Client Module runs on each user's machine and integrates the Flat File and Directory Services to provide a seamless file system interface (e.g., POSIX-like API: `open`, `read`, `write`, `close`).

*   **Responsibilities:**
    *   Caching frequently used file blocks and attributes locally to improve performance and reduce network traffic.
    *   Implementing the user-facing API (e.g., the `open` system call).
    *   Handling pathname traversal by making multiple calls to the Directory Service.
    *   Making remote procedure calls (RPCs) to the server-based Flat and Directory services.

**How an `open()` system call is handled:**
```
+---------+      2. Lookup(path)      +-----------------+
| Client  | ------------------------> | Directory       |
| Module  |                           | Service         |
|         | <------------------------ |                 |
|         |   3. Returns File UFID    |                 |
+---------+                           +-----------------+
       |                                      ^
       | 4. Read(UFID, ...)                  |
       | -------------------------------------
       |                                      |
       v                                      |
+-----------------+                           |
| Flat File       |                           |
| Service         | --------------------------
+-----------------+
```
1.  Application calls `open("/home/file.txt")`.
2.  Client module breaks the path into components and repeatedly calls the Directory Service's `Lookup` operation to resolve each part, eventually obtaining the UFID for `file.txt`.
3.  The Client Module may now cache this name-to-UFID mapping.
4.  Subsequent `read` and `write` calls from the application use the cached UFID to communicate directly with the Flat File Service.

## Upload/Download vs. Remote Access Models

There are two primary models for designing a file service:

| Feature | Upload/Download Model | Remote Access Model |
| :--- | :--- | :--- |
| **Principle** | Entire file is transferred to client for access. | File remains on server; only requested portions are transferred. |
| **Network Use** | High bandwidth for initial transfer, then none. | Lower, more frequent network requests. |
| **Client State** | Client has a full local copy. | Client may only cache small blocks. |
| **Consistency** | Simpler, but can lead to stale data. | More complex; requires cache coherency protocols. |
| **Example** | HTTP, FTP (for reading). | NFS, AFS, CIFS/SMB. |

Most modern DFSs (like NFS and AFS) use a **Remote Access Model** with sophisticated caching to get the benefits of both models.

## Key Design Issues

### 1. Stateful vs. Stateless Servers

*   **Stateless Server:** Does not maintain any client-specific state (e.g., open file descriptors, file pointers) between requests. Each request must be complete (e.g., `Read(UFID, offset, count)`). **NFSv2** is a classic example.
    *   **Advantages:** Simple crash recovery (no state to lose), scalable.
    *   **Disadvantages:** Larger request sizes, no "session" semantics, harder for locking.

*   **Stateful Server:** Maintains client state (e.g., after an `Open`, it holds a file descriptor and a current file pointer). Subsequent `Read` requests can be simpler (e.g., just `Read(fd, count)`). **CIFS/SMB** is stateful.
    *   **Advantages:** Smaller messages, easier to implement precise locking and session guarantees.
    *   **Disadvantages:** Complex crash recovery (must manage state), less scalable.

### 2. Cache Coherence

When multiple clients cache copies of the same file block, modifications by one client must be propagated to others to prevent stale data. Common solutions include:
*   **Write-through:** Writes are immediately sent to the server. Other clients see changes quickly but performance suffers.
*   **Delayed-write (Write-back):** Writes are cached and sent to the server later. Better performance, but higher risk of data loss on crash and stale reads.
*   **Callback-based (e.g., AFS):** The server promises to notify (callback) a client if another client changes a file it has cached. This reduces the need to constantly check with the server.

### 3. Replication and Fault Tolerance

To ensure availability and durability, file data can be replicated across multiple servers.
*   **Mirroring:** Exact copies on different servers.
*   **Quorum-based protocols:** Require a majority of replicas to agree before a write is committed, ensuring consistency.

## Example: Network File System (NFS) Protocol

NFS is a widely deployed, standard DFS protocol. It exemplifies the architectural concepts above.
*   **VFS Layer:** Integrates with the OS's Virtual File System, making remote files appear local.
*   **Stateless Server:** NFS servers are designed to be stateless (especially early versions).
*   **File Handles:** The NFS equivalent of a UFID. Opaque to the client.
*   **MOUNT Protocol:** A separate protocol used by the client to first obtain the root file handle of a remote filesystem.

## Exam Tips

1.  **Memorize the Three Components:** Always be able to name and describe the role of the Flat File Service, Directory Service, and Client Module. This is a fundamental and frequent exam question.
2.  **Understand UFID vs. Pathname:** A common trick is to ask what a UFID is and why it's used instead of a pathname. The answer revolves around immutability, efficiency, and separation of concerns.
3.  **Trace a Request:** Be prepared to trace the steps of a simple file operation (like `open` followed by `read`), showing the interaction between the client, directory service, and flat file service. Use a diagram if allowed.
4.  **Compare Stateful/Stateless:** Know the advantages and disadvantages of each approach by heart. Be ready to suggest which might be better for a given scenario.
5.  **Link to Other Topics:** Be aware of how file services use **Remote Procedure Call (RPC)** from Module 1 for communication and might employ replication techniques discussed in **Coordination and Agreement** (Module 4).