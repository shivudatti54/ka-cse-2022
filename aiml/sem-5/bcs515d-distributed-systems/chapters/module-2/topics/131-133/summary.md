# **Distributed Systems: 13.1-13.3 Revision Notes**

### 13.1 File Service Architecture

- **File Service Architecture**:
  - A file service is an application service that provides file-related operations (e.g., create, read, write, delete) over a network.
  - File service architecture typically consists of:
    - **Client**: requests file operations
    - **File Server**: performs file operations
    - **File System**: stores and manages files
- **File Service Protocols**:
  - NFS (Network File System)
  - SMB (Server Message Block)
  - CIFS (Common Internet File System)

### 13.2 Distributed File Systems

- **Definition**: A distributed file system is a file system that spans multiple physical machines and provides a unified view of the files.
- **Characteristics**:
  - **Scalability**: ability to handle large amounts of data and traffic
  - **Fault tolerance**: ability to continue operating even if one or more nodes fail
  - **Availability**: ability to access files from multiple locations
- **Types**:
  - **Hierarchical distributed file systems**: store files in a hierarchical structure (e.g., tape libraries)
  - **Decentralized distributed file systems**: store files in a decentralized structure (e.g., distributed hash tables)

### 13.3 File System Architecture

- **File System Architecture**:
  - Consists of:
    - **File System Manager**: manages the file system (e.g., inode, block allocation)
    - **File System Client**: interacts with the file system (e.g., file I/O operations)
  - **File System Models**:
    - **Block-based file system**: stores files in fixed-size blocks
    - **Record-based file system**: stores files in variable-size records

**Important Formulas and Definitions:**

- **Inode**: a data structure that stores information about a file (e.g., file name, permissions, ownership)
- **Block allocation**: the process of allocating fixed-size blocks to store files
- **File system hierarchy**: a hierarchical structure that organizes files and directories

**Theorems:**

- **File system consistency theorem**: ensures that the file system remains consistent even in the presence of concurrent file operations
- **File system availability theorem**: ensures that the file system remains available even in the presence of node failures
