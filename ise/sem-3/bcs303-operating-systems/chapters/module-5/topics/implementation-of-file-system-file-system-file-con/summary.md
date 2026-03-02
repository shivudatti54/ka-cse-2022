# File System: File Concept

### Key Concepts

- **File**: A file is a collection of data stored in contiguous locations on a storage device, such as a hard drive or solid-state drive (SSD).
- **File System**: A file system is a software layer that controls the storage, retrieval, and management of files on a storage device.
- **File Attributes**: File attributes include:
  - File name
  - File extension
  - File size
  - File type
  - File permissions (read, write, execute)
- **File Structures**: File structures include:
  - **Block Structure**: A block is a fixed-size area of storage that contains a file's data.
  - **Inode (Index Node)**: An inode is a data structure that stores file metadata, such as file attributes and location on disk.
  - **File System Tree**: A file system tree is a hierarchical representation of the file system, with each node representing a directory or file.

### Important Formulas and Definitions

- **Disk Block Size**: The minimum unit of storage that can be allocated to a file.
- **File Fragmentation**: When a file is broken into multiple non-contiguous blocks, leading to wasted storage space.
- **File Allocation**: The process of assigning a block of storage to a file.
- **File De- Allocation**: The process of freeing up a block of storage when a file is deleted or no longer needed.

### Theorems

- **File System Theorem**: A file system is a reliable and efficient way to store and retrieve data.
- **File Fragmentation Theorem**: File fragmentation leads to wasted storage space and decreased system performance.

### Review Questions

- What is a file system?
- What are the different types of file attributes?
- What is a file structure, and what are its components?
- What is file fragmentation, and how is it addressed?
