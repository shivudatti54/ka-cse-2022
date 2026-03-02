# File System

## Introduction

A file system is a fundamental component of any operating system that provides an abstraction layer for storing, organizing, and retrieving data on secondary storage devices. In the context of Operating Systems, the file system serves as the critical interface between user applications and the physical disk hardware. Without a file system, data would be stored as raw bytes without any meaningful organization, making it impossible to locate, manage, or protect information effectively.

The importance of file systems in modern computing cannot be overstated. Every operating system, from Windows and macOS to Linux and mobile platforms, relies on file systems to manage the ever-increasing volumes of digital information. File systems determine how efficiently data can be stored and accessed, how files are protected from unauthorized access, and how multiple users can share data safely. For students preparing for DU semester examinations, understanding file systems is essential because this topic appears frequently in both theoretical and practical components of the Operating Systems course.

This chapter explores the fundamental concepts of file systems, including the file abstraction, access methods, directory structures, and the various techniques used to implement efficient file systems. We will examine how operating systems organize files on disk, manage free space, allocate storage, and provide protection mechanisms to ensure data integrity and security.

## Key Concepts

### The File Concept

A file is the basic unit of data storage in a computer system. From the user's perspective, a file represents a collection of related information that can be created, modified, read, and deleted as a single entity. Operating systems abstract the physical details of storage devices and present data in the form of logical files that users and applications can manipulate using simple operations like open, read, write, and close.

Files possess several attributes that define their characteristics:

1. **Name**: A unique identifier that allows users to recognize and access the file. File names typically consist of a base name and an extension that indicates the file type.

2. **Identifier**: An internal, system-generated number (inode number in Unix-like systems) that uniquely identifies the file within the file system.

3. **Type**: Indicates the format and purpose of the file, such as text files, executable files, source code files, or binary files.

4. **Location**: A pointer to the physical position of the file on the storage device.

5. **Size**: The current size of the file in bytes, which may change as data is modified.

6. **Protection**: Access control information that determines who can read, write, or execute the file.

7. **Timestamps**: Metadata including creation time, modification time, and last access time.

8. **Owner information**: Identifies the user who created or owns the file.

### File Access Methods

Operating systems provide various methods for accessing data within files. The choice of access method significantly impacts performance and is determined by the nature of the application using the file.

**Sequential Access**: This is the simplest and most common access method, where data is read or written in a sequential manner, starting from the beginning of the file and proceeding linearly. The operating system maintains a file pointer that indicates the current position, and this pointer advances as data is read or written. Sequential access is ideal for applications that process data in order, such as reading log files or processing transaction records. The read operation moves the file pointer forward by the number of bytes read, while the write operation appends data at the end of the file.

**Direct Access (Random Access)**: This method allows any record in the file to be accessed directly without reading preceding records. Files supporting direct access are organized into fixed-length blocks or records, and each block can be accessed by specifying its block number. The operating system calculates the physical location of the requested block using the formula: block_address = starting_address + (record_number × record_size). Direct access is essential for database systems and applications requiring frequent random lookups, such as airline reservation systems.

**Indexed Access**: This sophisticated method maintains an index structure that contains pointers to various locations within the file. To access a particular record, the system first searches the index to find the appropriate pointer, then uses that pointer to directly access the desired data. This method combines the efficiency of direct access with the flexibility of sequential processing. Large files often use multi-level indexes, where a primary index points to secondary indexes, which in turn point to actual data blocks.

### File System Structure

The file system architecture consists of multiple layers that work together to provide file management services. Understanding this layered structure helps comprehend how file operations are processed and where optimizations can be applied.

**Application Programs**: The highest level where user programs interact with files through system calls like open(), read(), write(), and close().

**Logical File System**: This layer manages metadata about files, including file names, permissions, and directory structures. It translates logical file operations into requests for the next layer.

**File Organization Module**: This component handles the physical organization of files on disk, including block allocation, free space management, and optimization of storage layout.

**Basic File System**: This layer issues generic commands to the device driver and manages buffer caches for improving I/O performance.

**Device Driver**: The lowest software layer that interacts directly with the hardware controllers to perform actual data transfer operations.

**Physical I/O**: The actual hardware operations that transfer data between main memory and secondary storage devices.

### Directory Structure

Directories provide the organizational framework for files within a file system. They map logical file names to physical file locations and enable hierarchical organization of data. Several directory structures exist, each with distinct advantages and trade-offs.

**Single-Level Directory**: The simplest structure where all files reside in a single directory. While easy to implement, this approach creates naming conflicts and cannot scale beyond a limited number of files.

**Two-Level Directory**: Introduces a separate directory for each user, solving the naming conflict problem but limiting organizational flexibility. Users cannot create subdirectories to group related files.

**Tree-Structured Directory**: The most common structure where directories can contain both files and subdirectories, forming a hierarchical tree. This allows logical grouping of related files and efficient navigation using path names. Unix-like systems use this approach, with the root directory at the top and absolute or relative paths pointing to specific locations.

**Acyclic-Graph Directory**: Extends the tree structure by allowing directories to share subdirectories or files. This enables multiple paths to reference the same file, supporting efficient file sharing without duplication. However, it requires careful handling to avoid cycles and complex deletion semantics.

### File System Implementation

The implementation of a file system involves several critical components that work together to manage storage efficiently.

**File Allocation Table (FAT)**: Used in early file systems like MS-DOS, FAT maintains a table that tracks which clusters are allocated to each file. Each file entry contains a pointer to the first cluster, and subsequent clusters are linked through entries in the FAT table. While simple, FAT becomes inefficient for large disks due to the overhead of maintaining the table in memory.

**inode Structure**: Unix-like file systems use inodes (index nodes) to store file metadata. Each file is associated with an inode that contains attributes and pointers to data blocks. Inodes typically support direct pointers to a fixed number of blocks, plus single, double, or triple indirect pointers for larger files. This structure provides efficient access to file data and scales well to large file systems.

**Virtual File System (VFS)**: Modern operating systems implement VFS as an abstraction layer that allows multiple different file systems to coexist. VFS provides a standard interface for file operations, and individual file system implementations translate these requests into format-specific operations. This design enables users to mount various file system types (NTFS, ext4, FAT32, etc.) on the same system.

### Allocation Methods

The method chosen for allocating disk space to files significantly impacts storage efficiency, access speed, and file system performance.

**Contiguous Allocation**: Each file occupies a set of consecutive disk blocks. This method provides excellent sequential access performance because the head movement is minimized. However, it suffers from external fragmentation and difficulty in growing files. The operating system must perform complex allocation decisions to find suitable contiguous spaces.

**Linked Allocation**: Each file consists of scattered blocks, with each block containing a pointer to the next block in the chain. This eliminates external fragmentation and simplifies file growth but provides poor random access performance since blocks must be traversed sequentially. FAT is an optimized version of linked allocation.

**Indexed Allocation**: All pointers to file blocks are collected in a single index block. For larger files, multiple index blocks can be linked together. This method supports both sequential and direct access efficiently but requires additional I/O operations to read the index block before accessing data. Unix inode implementation is a sophisticated variation of indexed allocation.

### Free Space Management

Efficient management of free disk space is crucial for maximizing storage utilization. Several techniques are employed to track and allocate available space.

**Bit Vector (Bitmap)**: Each disk block is represented by a single bit, where 1 indicates allocated and 0 indicates free. This method enables fast allocation and deallocation but requires keeping the bitmap in memory for efficiency.

**Linked List**: Free blocks are linked together in a list, with each free block containing a pointer to the next free block. Simple to implement but inefficient for finding large contiguous free spaces.

**Grouping**: A variation of linked list where free blocks are organized into groups, with each group containing pointers to other groups. This improves efficiency when allocating multiple blocks simultaneously.

**Counting**: Maintains pairs of (starting block, count) for consecutive free blocks. Efficient for tracking large contiguous free areas but requires more complex data structures.

## Examples

### Example 1: Calculating File Access Time

Consider a disk with the following specifications: average seek time of 8ms, average rotational delay of 4ms, and a transfer rate of 4MB/s. Calculate the average time to read a 16KB file using sequential access where the file is stored in 4 blocks of 4KB each.

**Solution:**

For each block access:
- Average seek time = 8ms
- Average rotational delay = 4ms
- Transfer time for 4KB = (4KB / 4MB/s) = (4 × 1024) / (4 × 1024 × 1024) = 1/1024 second ≈ 1ms

Time per block = 8ms + 4ms + 1ms = 13ms

For 4 blocks in sequential access (assuming optimal layout with minimal seeks):
Total time = 4 × 13ms = 52ms (assuming single seek for first block)

If blocks are scattered and require separate seeks:
Total time = 4 × (8ms + 4ms + 1ms) = 52ms (same in this case)

However, with random placement requiring full seek for each block:
Total time = 4 × (8ms + 4ms + 1ms) = 52ms

In practice, contiguous allocation would yield approximately 13ms + 3×1ms = 16ms for the entire file.

### Example 2: inode-based File Access

In a Unix-like file system, an inode contains 12 direct pointers, 1 single indirect pointer, 1 double indirect pointer, and 1 triple indirect pointer. The block size is 4KB, and each block pointer requires 4 bytes. Calculate the maximum file size supported.

**Solution:**

First, calculate how many block pointers fit in one block:
Pointers per block = 4KB / 4 bytes = 1024 pointers

Direct blocks: 12 × 4KB = 48KB

Single indirect: 1024 × 4KB = 4MB

Double indirect: 1024 × 1024 × 4KB = 4GB

Triple indirect: 1024 × 1024 × 1024 × 4KB = 4TB

Maximum file size = 48KB + 4MB + 4GB + 4TB ≈ 4TB (practically limited by double and triple indirect)

The actual usable size is slightly less due to metadata overhead, but the calculation demonstrates the exponential growth of addressable space with each level of indirection.

### Example 3: Directory Entry Resolution

In a tree-structured directory, suppose the path "/home/student/documents/report.txt" is being resolved. Explain the step-by-step process the operating system follows.

**Solution:**

The operating system performs the following steps:

1. Start at the root directory "/" - the operating system reads the inode for the root directory from the superblock.

2. Locate "home" - search the root directory entries for "home", retrieve its inode number.

3. Read the "home" directory - read the inode for "home" directory, then read the directory entries.

4. Locate "student" - search within "home" directory for "student", obtain its inode number.

5. Read the "student" directory - read the inode and directory entries for "student".

6. Locate "documents" - find "documents" entry and its inode in the "student" directory.

7. Read the "documents" directory - read the inode and entries for "documents".

8. Locate "report.txt" - find the file entry and obtain its inode number.

9. Open the file - using the inode, perform permission checks and create a file descriptor for the process.

Each directory lookup involves reading the directory's inode, reading the directory data blocks, and searching for the target name. This is why path resolution is faster for short paths and directories cached in memory.

## Exam Tips

1. **Understand the difference between file and file system**: A file is a named collection of related information, while a file system is the complete software component that manages files and directories on storage devices.

2. **Memorize the three access methods**: Sequential, direct (random), and indexed access. Be prepared to explain when each is appropriate and their relative advantages.

3. **Know allocation method trade-offs**: Contiguous allocation offers fast access but suffers from fragmentation. Linked allocation eliminates fragmentation but has poor random access. Indexed allocation provides good performance for both but wastes space for index blocks.

4. **Understand inode vs FAT**: inode-based systems (Unix/Linux) use fixed-size metadata structures with direct and indirect pointers. FAT-based systems use a linked list approach with the entire allocation table kept in memory.

5. **Directory structure types**: Single-level, two-level, tree-structured, and acyclic-graph. Know the advantages and disadvantages of each, and be able to identify examples of each type in real systems.

6. **Free space management techniques**: Bit vector (bitmap), linked list, grouping, and counting. Understand how each tracks available space and their relative efficiencies.

7. **File system mounting**: When a file system is mounted, its root directory is attached to the system's directory tree at a specific mount point, making its files accessible through that path.

8. **File sharing and protection**: Understand how file permissions work, including read, write, and execute permissions for owner, group, and others in Unix-like systems.

9. **Real-world file systems**: Be familiar with common file system types like FAT32, NTFS, ext4, and their distinguishing characteristics.

10. **Buffer caching**: The file system maintains a cache of frequently accessed disk blocks in memory to improve performance by reducing physical I/O operations.