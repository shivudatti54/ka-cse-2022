# Implementing File System

## Introduction

File system implementation is a critical component of modern operating systems that bridges the gap between user-level file operations and the physical storage of data on secondary storage devices. When a user creates, reads, writes, or deletes a file, the operating system must translate these high-level requests into low-level operations that manage disk blocks, maintain directory structures, and ensure data integrity. Understanding how file systems are implemented provides essential insights into how operating systems manage one of the most valuable resources in computing: persistent data.

The implementation of a file system involves several interrelated components working in harmony. These include the on-disk structure of files and directories, the in-memory data structures that cache frequently accessed metadata, the algorithms for allocating disk space to files, and the mechanisms for tracking free space. In the University of Delhi Computer Science curriculum, this topic builds upon the foundational concepts of file organization and access methods, preparing students to understand both the theoretical underpinnings and practical considerations in designing storage solutions.

Modern file systems must balance multiple competing objectives: maximizing throughput while minimizing seek time, ensuring data reliability through journaling or logging mechanisms, supporting concurrent access from multiple processes, and providing security through access control lists. This chapter examines the fundamental techniques that operating systems employ to achieve these goals.

## Key Concepts

### File System Structure

The file system architecture is typically organized in multiple layers, each building upon the services provided by the layer below. At the lowest level, the device driver interacts directly with the physical storage hardware, handling sector-level read and write operations. Above this, the basic file system module issues generic block-level commands without understanding file semantics. The file organization module understands files, their logical organization, and how physical blocks are mapped to logical file offsets. The directory management module handles the translation between file names and their corresponding i-nodes or file control blocks. Finally, the access control module enforces security policies determining which processes can perform which operations on which files.

The actual on-disk structure of a file system typically consists of several distinct regions. The boot control block contains information needed to bootstrap the system from this partition. The superblock contains critical metadata about the entire file system: its size, the number of free blocks, the location of the free block list or bitmap, and other fundamental parameters. The i-node structure (index node) serves as the fundamental metadata container for each file, storing attributes such as ownership, permissions, timestamps, and pointers to the actual data blocks. The data blocks contain the actual file contents.

### Directory Implementation

Directories in UNIX-like systems are implemented as special files that store mappings between file names and their associated i-nodes. Each directory entry consists of the file name (typically limited to 255 characters) and the i-node number. When a process opens a file, the operating system must search through the appropriate directory entries, comparing each file name until finding a match, then loading the corresponding i-node into memory.

In early UNIX implementations, directory entries were fixed-size structures containing a 14-character filename and two bytes for the i-node number. Modern file systems like ext4 use variable-length directory entries with longer filename support and efficient indexing structures. The directory entry structure in ext4 uses a linear list for small directories but automatically converts to a hashed B-tree (htree) structure when directory sizes grow beyond certain thresholds, ensuring efficient lookup performance even for directories containing millions of entries.

The implementation must handle several edge cases: creating files with names longer than the maximum allowed length (truncation or error), handling duplicate names within the same directory (prohibited), and managing deleted entries (typically marked with a special i-node number of zero).

### Allocation Methods

The method chosen for allocating disk space to files has profound implications for performance, storage efficiency, and reliability. Three primary allocation strategies have been widely used in operating systems.

**Contiguous Allocation** assigns each file a consecutive set of disk blocks. This approach offers excellent read performance because the disk head need not move significantly between successive blocks. File allocation tables or similar structures need only store the starting block and length. However, contiguous allocation suffers from severe external fragmentation as files are created, deleted, and resized. Compaction becomes necessary periodically, which is time-consuming and requires downtime.

**Linked Allocation** stores each file as a linked list of disk blocks. Each block contains a pointer to the next block in the chain. This method eliminates external fragmentation entirely and simplifies file growth—new blocks can be added anywhere in the free space. However, linked allocation suffers from poor random access performance because traversing to the nth block requires following n-1 pointers. The pointer overhead in each block reduces usable storage capacity. Additionally, reliability concerns arise if any pointer becomes corrupted—the entire file beyond that point becomes inaccessible.

**Indexed Allocation** addresses the limitations of linked allocation by maintaining a separate index block (or multiple index blocks) for each file. The index block contains pointers to all the data blocks belonging to that file. This structure supports direct random access, provides good performance for sequential reads, and maintains reliability through redundant copies of critical pointers in some implementations. The primary drawback is the overhead of the index block itself—particularly wasteful for small files that require only one or two data blocks.

Modern file systems like ext4 use a modified indexed allocation scheme called an i-node structure. Each i-node contains 15 block pointers: the first 12 point directly to data blocks, while the remaining three point to indirect blocks (single, double, and triple-level), creating a hierarchical structure that can address files of enormous size without proportional overhead.

### Free Space Management

Efficient tracking of available disk space is essential for file system operation. Several techniques have been developed for this purpose.

The **bit vector** (or bitmap) approach maintains a separate array of bits, one per disk block. A value of 0 indicates the block is free, while 1 indicates it is allocated. This method enables fast identification of consecutive free blocks for contiguous allocation and provides simple, efficient space allocation. However, the bit vector itself requires substantial memory for large disks, and scanning for free space may be slow unless cached in memory.

**Linked list** free space management maintains a linked list of free disk blocks. Each free block contains a pointer to the next free block. This approach requires minimal overhead—just one pointer per free block—and works well with linked allocation. However, finding a block of consecutive free blocks becomes computationally expensive, requiring traversal of the entire list.

**Grouping** combines the advantages of both approaches. Free blocks are organized into groups, where each group contains pointers to other groups. This hierarchical structure enables both quick allocation of single blocks and efficient discovery of large contiguous regions.

### File System Implementation in Memory

Operating systems maintain several in-memory data structures to optimize file system performance. The **buffer cache** caches recently accessed disk blocks in memory, avoiding repeated disk I/O for frequently used data. The **i-node cache** stores copies of recently accessed i-nodes, accelerating metadata operations. The **directory cache** maintains mappings between frequently accessed pathnames and their corresponding i-nodes, speeding up pathname resolution.

These caches must be carefully managed to maintain consistency with on-disk structures. Write-back policies determine when modified cached data is written back to disk—aggressive caching improves performance but risks data loss during system crashes, while synchronous writes ensure durability at the cost of performance. Modern journaling file systems address this trade-off by logging metadata changes before applying them, ensuring consistency while maintaining reasonable performance.

## Examples

**Example 1: Tracing File Creation**

Consider the sequence of operations when a process creates a new file named "notes.txt" in an ext4 file system:

1. The process calls `open("notes.txt", O_CREAT)` with appropriate permissions
2. The kernel must resolve the pathname "/home/student/notes.txt" by:
   - Looking up "home" in the root directory, obtaining its i-node number
   - Looking up "student" in the "home" directory, obtaining its i-node number
   - Looking up "notes.txt" in the "student" directory (which should not exist yet, so this is where creation occurs)
3. The kernel allocates a new i-node from the free i-node pool (using the bit vector)
4. The kernel allocates data blocks for the file (using the free block bit vector)
5. The kernel adds a directory entry mapping "notes.txt" to the new i-node in the "student" directory
6. The file descriptor is returned to the calling process

Each of these steps involves multiple disk I/O operations, which is why file creation is relatively expensive compared to opening an existing file.

**Example 2: Indexed Allocation for a Large File**

Suppose a file system uses the UNIX i-node structure with 12 direct pointers, one single-indirect pointer, one double-indirect pointer, and one triple-indirect pointer, where each block pointer occupies 4 bytes and each block is 4KB.

The maximum file size this structure can support can be calculated as:
- Direct blocks: 12 blocks × 4KB = 48KB
- Single indirect: 1024 pointers × 4KB = 4MB
- Double indirect: 1024 × 1024 pointers × 4KB = 4GB
- Triple indirect: 1024 × 1024 × 1024 pointers × 4KB = 4TB

Total maximum file size: approximately 4TB minus the overhead of smaller addressing, demonstrating how hierarchical indexing efficiently addresses even very large files.

**Example 3: Free Space Bit Vector Allocation**

Assume a disk with 1000 blocks managed using a bit vector. Initially all bits are 0 (free). When allocating a file requiring 5 blocks, the system scans the bit vector from the beginning:

- Block 0: free (0) → allocate
- Block 1: free (0) → allocate
- Block 2: free (0) → allocate
- Block 3: free (0) → allocate
- Block 4: free (0) → allocate

The bit vector now shows bits 0-4 set to 1 (allocated), and the free space count decreases by 5. When the file is deleted, these bits are reset to 0, making those blocks available for reallocation.

## Exam Tips

1. Understand the trade-offs between contiguous, linked, and indexed allocation—contiguous offers speed but suffers fragmentation, linked eliminates fragmentation but has poor random access, indexed provides good random access with moderate overhead.

2. Remember that the i-node structure in UNIX combines direct, single-indirect, double-indirect, and triple-indirect blocks to efficiently address files of varying sizes.

3. For free space management, know that bit vectors provide fast allocation but require memory proportional to disk size, while linked lists use minimal memory but cannot efficiently find contiguous blocks.

4. Directory implementation questions often ask about the sequence of operations during file creation—be prepared to trace through pathname resolution, i-node allocation, and directory entry creation.

5. The buffer cache and i-node cache are essential for performance—understand why they exist and how they interact with on-disk structures.

6. Journaling file systems solve the consistency problem by logging metadata changes before applying them, enabling fast recovery after crashes.

7. External fragmentation occurs in contiguous allocation when free space becomes scattered; internal fragmentation occurs when allocated blocks contain unused space—distinguish between these concepts.

8. Practice calculating maximum file sizes given different allocation structures—this is a common examination question.