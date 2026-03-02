# File Service Architecture - Summary

## Key Definitions and Concepts

- **File Service Architecture**: The design of systems that provide file-based storage and access capabilities, either locally or across networks.
- **Local File System**: A file system operating on a single machine, managing disk space, file metadata, and access control.
- **Client-Server File Service**: Centralized file management where a server provides file access to multiple clients over a network.
- **Distributed File System**: A file system that spans multiple servers, providing location transparency and horizontal scalability.
- **NFS (Network File System)**: A protocol for file sharing in Unix/Linux environments, with NFSv4 being the current standard.
- **CIFS/SMB**: Protocol for file sharing in Windows environments with built-in printer sharing and Windows integration.
- **File Locking**: Mechanisms to manage concurrent access to files, preventing data corruption from simultaneous modifications.

## Important Formulas and Theorems

- **File Access Time**: Total time = Seek time + Rotational delay + Transfer time
- **Cache Hit Ratio**: (Cache hits / Total cache accesses) × 100%
- **Replication Factor**: Number of copies stored = Desired reliability level

## Key Points

- Local file systems use File Control Blocks (FCB) to store file metadata and directory structures for hierarchical organization.
- Client-server architecture provides centralized management, improved security, and easier backup compared to local file systems.
- NFS uses a stateless design (v3) or stateful design (v4), while CIFS/SMB provides more built-in features for Windows environments.
- Distributed file systems like HDFS use NameNode for metadata and DataNodes for actual data storage.
- File caching can be write-through (synchronous) or write-back (asynchronous), each with different consistency guarantees.
- File locking includes shared locks (multiple readers) and exclusive locks (single writer).
- Mount operations in NFS involve server validation, file handle generation, and client-side registration.
- Security in modern file services uses Kerberos authentication with NFSv4.

## Common Mistakes to Avoid

- Confusing NFS and CIFS protocols—one is primarily Unix-based while the other is Windows-based.
- Misunderstanding the difference between advisory and mandatory locking.
- Believing distributed file systems always provide stronger consistency guarantees than they actually do.
- Overlooking the performance implications of different caching strategies.

## Revision Tips

- Create comparison tables for NFS vs CIFS, write-through vs write-back caching, and different locking types.
- Draw the architecture diagrams for client-server and distributed file systems.
- Practice explaining the sequence of events in NFS mount operations.
- Review the roles of NameNode and DataNode in HDFS thoroughly.
