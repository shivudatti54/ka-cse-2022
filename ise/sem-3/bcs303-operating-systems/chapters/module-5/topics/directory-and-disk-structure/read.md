# Directory and Disk Structure

## Introduction

Directory and Disk Structure forms a fundamental component of modern operating systems, managing how files are organized, accessed, and stored on physical media. In the context of file systems, a directory serves as a logical container that maps file names to their physical locations on disk, enabling efficient file management and retrieval. The disk structure, on the other hand, defines the physical organization of data on storage devices, including how sectors, tracks, and blocks are arranged and accessed.

Understanding directory and disk structure is crucial for computer science students because it directly impacts file system performance, data integrity, and system reliability. When you save a document, create a folder, or organize your files into directories, you are interacting with these underlying structures. Operating systems like UNIX, Linux, Windows, and macOS all implement directory structures, though with different architectural approaches. The way directories are implemented affects search times, file access efficiency, and the maximum number of files a system can support.

This topic becomes particularly important when studying how operating systems manage secondary storage, allocate disk space, and provide file protection mechanisms. In DU's Computer Science curriculum, this knowledge forms the foundation for understanding more advanced topics like distributed file systems, database storage engines, and operating system design principles.

## Key Concepts

### Directory Structure

A directory is a special type of file that contains information about other files, including their names, attributes, and pointers to their data blocks. The directory structure defines how these directories are organized within the file system hierarchy.

**Single-Level Directory**: The simplest directory structure where all files are placed in a single directory. While easy to implement, this approach suffers from naming conflicts and poor organization. Users cannot have two files with the same name, and finding specific files becomes difficult as the number of files grows.

**Two-Level Directory**: Introduces a separate directory for each user, solving the naming conflict problem. Each user has their own private directory, but users cannot create subdirectories, limiting organizational flexibility.

**Hierarchical Directory Structure**: The most common structure used by modern operating systems, allowing users to create subdirectories within directories. This creates a tree-like organization where the root directory branches into multiple levels of subdirectories. UNIX uses this with "/" as the root, while Windows uses drive letters like "C:\" as starting points.

**Acyclic Graph Directory Structure**: Allows directories to share subdirectories and files through shortcuts or links, creating a directed acyclic graph rather than a strict tree. This enables file sharing without duplicating data, but requires careful handling to avoid circular references.

**General Graph Directory Structure**: Permits cycles in the directory graph, allowing more flexible sharing. However, this complexity requires algorithms to detect and handle infinite loops during directory traversals.

### Directory Implementation

**Linear List Implementation**: Stores directory entries as a simple list. Searching requires scanning the entire list, resulting in O(n) time complexity. While simple to implement, this becomes inefficient for directories containing thousands of files.

**Hash Table Implementation**: Uses a hash function to map file names to locations in the table. This provides O(1) average-case lookup time. The challenge lies in handling hash collisions and managing the fixed size of the hash table.

**File Control Block (FCB)**: Each file in a directory is represented by a File Control Block containing metadata such as file name, creation date, permissions, file size, and pointers to data blocks. The directory structure essentially maps file names to their corresponding FCBs.

### Disk Structure

**Physical Organization**: Disks are organized into concentric circles called tracks, which are further divided into sectors. The combination of track number and sector number uniquely identifies each physical location on the disk. Modern disks use zoned bit recording, where outer tracks contain more sectors than inner tracks.

**Disk Scheduling**: Operating systems use various algorithms to determine the order in which disk I/O requests are serviced. These include First-Come-First-Served (FCFS), Shortest Seek Time First (SSTF), SCAN, C-SCAN, and LOOK algorithms. The goal is to minimize disk head movement and reduce access latency.

**Sector Interleaving**: Sequential sectors are not stored consecutively on the disk. Instead, they are interleaved to allow time for the controller to process data before the next sector arrives under the head. This prevents buffer overflow during sequential reads.

### Disk Partitioning

Disks can be divided into partitions, with each partition acting as an independent logical disk. Partitions can be used to separate operating systems, user data, and system files. The partition table, stored in the master boot record (MBR) or GUID partition table (GPT), maintains information about partition boundaries and types.

### Free Space Management

**Bit Vector (Bitmap)**: Uses a bitmap where each disk block is represented by one bit. A value of 0 indicates free space, while 1 indicates allocated space. This method allows quick finding of consecutive free blocks.

**Linked List**: Maintains a linked list of free disk blocks, with each free block containing a pointer to the next free block. Simple but inefficient for finding consecutive free blocks.

**Grouping**: Stores addresses of n free blocks in the first free block. This allows quick acquisition of multiple free block addresses.

**Counting**: Keeps track of the first free block and the number of consecutive free blocks following it, useful when blocks are frequently allocated in contiguous groups.

## Examples

### Example 1: Hierarchical Directory Navigation

Consider a UNIX-like file system with the following structure:

```
/ (root)
├── home/
│   ├── student/
│   │   ├── documents/
│   │   │   ├── assignment.txt
│   │   │   └── notes.pdf
│   │   ├── pictures/
│   │   │   └── vacation.jpg
│   │   └── .bashrc
│   └── admin/
│       └── system.log
└── etc/
    └── passwd
```

When a user accesses "/home/student/documents/assignment.txt", the operating system performs the following steps:
1. Start at the root directory "/"
2. Look up "home" in root's entries - find inode number 2
3. Access inode 2 (home directory)
4. Look up "student" in home's entries - find inode number 15
5. Access inode 15 (student directory)
6. Look up "documents" in student directory - find inode number 28
7. Access inode 28 (documents directory)
8. Look up "assignment.txt" - find inode number 45
9. Access the file using its data block pointers

Each directory lookup involves reading the appropriate inode and searching its directory entries, typically using a hash table for efficiency.

### Example 2: Disk Space Allocation with Linked List

Assume a disk with 1000 blocks, where blocks 1-250 are allocated and blocks 251-1000 are free. Using linked list free space management:

The first free block (251) contains:
- Data: (typically empty for free blocks)
- Pointer: 252

Block 252 contains:
- Pointer: 253
- And so on...

When the system needs to allocate 5 consecutive blocks for a new file:
1. Start at block 251
2. Check if blocks 251-255 are consecutive (they are)
3. Allocate these blocks to the file
4. Update the free list to start at block 256

The allocation requires scanning the linked list until sufficient consecutive free blocks are found, making this method less efficient for large allocations.

### Example 3: Bit Vector Free Space Management

Consider a disk with 16 blocks represented by a bit vector:

Initial state (all free): 0000000000000000

After allocating file A (3 blocks starting at block 2): 1100000000000000

After allocating file B (4 blocks starting at block 8): 1100000011110000

To find 3 consecutive free blocks for a new file C:
1. Scan the bit vector: 1100000011110000
2. Starting at position 4, find three consecutive 0s at positions 4, 5, 6
3. Allocate blocks 4, 5, 6 to file C
4. Update bit vector: 1111000011110000

The bit vector allows O(n) scanning but can be optimized using techniques like grouping consecutive zeros to find suitable blocks faster.

## Exam Tips

1. Understand the difference between logical and physical file organization. Logical organization deals with how users perceive files, while physical organization concerns actual disk storage.

2. Memorize the time complexity of directory operations. Linear list search is O(n), while hash table lookup is O(1) on average but requires collision handling.

3. Know the advantages and disadvantages of each directory structure. Hierarchical structures offer flexibility but require more complex implementation than single-level directories.

4. Remember that directory entries contain both the file name and metadata. The File Control Block concept is essential for understanding directory implementation.

5. For disk scheduling algorithms, be able to calculate the total head movement for a given sequence of requests. SCAN and C-SCAN are particularly important for DU exams.

6. Understand why sector interleaving exists. It allows the disk controller time to process data before the next sector arrives, preventing buffer overflow.

7. Free space management methods vary in efficiency. Bit vectors provide quick searching but require extra memory, while linked lists use minimal overhead but are slower for large operations.

8. The hierarchical directory structure is the industry standard because it balances simplicity with organizational flexibility. Be prepared to explain why other structures are less practical.

9. When answering questions about directory operations (create, delete, rename), consider how each operation affects both the directory structure and the underlying file metadata.

10. In exam questions involving disk structure, pay attention to units (tracks, sectors, cylinders) and understand how these physical structures map to logical file operations.