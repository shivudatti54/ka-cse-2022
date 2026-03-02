# Storage Management

## Introduction

Storage management is a fundamental component of any operating system, responsible for controlling how data is stored, accessed, and maintained on computer systems. In the context of operating systems, storage management encompasses both main memory (RAM) and secondary storage devices such as hard disks, solid-state drives, and optical media. The operating system must efficiently allocate storage space, manage file systems, schedule disk requests, and ensure data integrity and security.

For University of Delhi students studying Computer Science, understanding storage management is crucial because it forms the backbone of modern computing systems. Every application, from simple text editors to complex database systems, relies on the operating system's ability to store and retrieve data efficiently. The principles learned in this topic directly apply to real-world scenarios like designing file systems, optimizing database performance, and implementing cloud storage solutions. Given that modern applications generate and process enormous amounts of data, efficient storage management has become more important than ever before.

This topic connects closely with other areas of operating system design, particularly memory management and process management. The operating system must coordinate between keeping frequently accessed data in fast primary memory while efficiently using slower secondary storage for long-term data retention. This hierarchical approach to storage management represents one of the most significant design challenges in computer science.

## Key Concepts

### Storage Hierarchy

Computer systems employ a hierarchy of storage devices organized by speed, cost, and capacity. At the top of this hierarchy is CPU registers, which provide the fastest access but have minimal capacity. Below registers is cache memory (L1, L2, L3), which is extremely fast but limited in size. Main memory (RAM) comes next, offering faster access than secondary storage but more expensive per byte. Finally, secondary storage devices like hard disk drives (HDD) and solid-state drives (SSD) provide the largest capacity at the lowest cost per byte, though with significantly slower access times.

The operating system manages this hierarchy through various techniques including caching, virtual memory, and demand paging. The goal is to keep frequently accessed data in faster storage levels while moving less frequently used data to slower but more economical storage. This hierarchical organization directly impacts system performance, and understanding this helps in making informed decisions about system configuration and application design.

### Disk Structure and Organization

Physical disks are organized into concentric circles called tracks, which are further divided into sectors. A sector is the smallest addressable unit on a disk, typically holding 512 bytes or 4096 bytes in modern systems. Multiple disks stacked together form cylinders, where each track at the same radius across all platters constitutes a cylinder. The operating system abstracts this physical structure into logical units that applications can easily use.

Modern disks use logical block addressing (LBA), which treats the entire disk as a linear sequence of blocks numbered from zero. This abstraction hides the physical geometry of the disk from applications and simplifies disk I/O operations. The disk controller translates LBA addresses into appropriate physical locations on the disk platters, handling the complex details of seek operations, rotation, and data transfer internally.

### File Systems

A file system provides the mechanism for storing and organizing data on secondary storage devices. Files are the fundamental abstraction that allows users and applications to interact with stored data. The operating system supports various file system types, each with different organizational strategies, performance characteristics, and reliability features.

The UNIX file system uses an inode-based structure where each file has an inode containing metadata and pointers to data blocks. Microsoft Windows supports file systems like FAT32 and NTFS, with NTFS offering advanced features like encryption, compression, and journaling. Linux supports numerous file systems including ext4, XFS, and Btrfs, each optimized for different use cases. Understanding file system design helps in selecting appropriate file systems for specific applications and troubleshooting storage-related issues.

### Disk Scheduling Algorithms

When multiple processes request disk I/O operations, the operating system must determine the order in which these requests are serviced. The choice of scheduling algorithm significantly impacts system performance, especially for systems with heavy I/O loads. Several disk scheduling algorithms have been developed to minimize seek time and improve throughput.

The FCFS (First-Come-First-Served) algorithm services requests in the order they arrive. While simple and fair, this approach often leads to poor performance due to excessive head movement. The SSTF (Shortest Seek Time First) algorithm selects the request closest to the current head position, reducing average seek time but potentially causing starvation of distant requests.

The SCAN algorithm, also known as the elevator algorithm, moves the disk head in one direction servicing all requests until reaching the end, then reverses direction. This approach ensures uniform response time across the disk. The C-SCAN (Circular SCAN) variant services requests in one direction only, returning to the beginning quickly without servicing requests during the return trip. The LOOK algorithm is similar to SCAN but only travels as far as the last request in each direction, avoiding unnecessary head movement to the disk edges.

### Storage Allocation Methods

Operating systems use several methods to allocate storage space to files. Contiguous allocation assigns consecutive blocks of storage to each file, providing excellent read performance but suffering from external fragmentation and difficulty in growing files. When a file needs to expand, sufficient contiguous space must be available, which may require moving the entire file.

Linked allocation stores each file as a linked list of disk blocks, with each block containing a pointer to the next block. This method eliminates external fragmentation and allows files to grow easily, but random access becomes inefficient since blocks must be traversed sequentially. The FAT file system uses a variation of linked allocation where pointers are stored in a central file allocation table.

Indexed allocation uses an index block containing pointers to all data blocks belonging to a file. This approach supports direct random access and eliminates external fragmentation but requires additional overhead for the index block. UNIX inodes combine contiguous allocation for small files with indexed allocation for larger files, optimizing both space efficiency and access performance.

### Free Space Management

The operating system must track which storage blocks are available for allocation to new or growing files. Several techniques exist for free space management. The bit vector (bitmap) approach uses a bit for each block, where 0 indicates free and 1 indicates allocated. This method enables fast allocation and deallocation but requires additional space for the bitmap itself.

Linked free lists maintain pointers connecting all free blocks together. While space-efficient, this approach becomes inefficient when searching for blocks of a specific size. Grouping techniques store addresses of multiple free blocks in the first free block, allowing quick acquisition of many free blocks at once. Counting methods maintain pairs of starting block addresses and count of consecutive free blocks, useful when files are frequently allocated and deallocated in groups.

## Examples

### Example 1: Disk Scheduling Calculation

Consider a disk with 200 tracks (numbered 0-199) and a disk head currently at track 50. The following requests arrive in the order given: 120, 80, 40, 100, 150. Calculate the total head movement for FCFS, SSTF, and SCAN algorithms.

**FCFS Solution:**
Head starts at 50, moves to 120: |120-50| = 70
From 120 to 80: |120-80| = 40
From 80 to 40: |80-40| = 40
From 40 to 100: |40-100| = 60
From 100 to 150: |100-150| = 50
Total head movement = 70 + 40 + 40 + 60 + 50 = 260 tracks

**SSTF Solution:**
From 50, closest request is 40: |50-40| = 10
From 40, closest is 80: |40-80| = 40
From 80, closest is 100: |80-100| = 20
From 100, closest is 120: |100-120| = 20
From 120, closest is 150: |120-150| = 30
Total head movement = 10 + 40 + 20 + 20 + 30 = 120 tracks

**SCAN Solution (assuming head moves toward higher numbered tracks first):**
From 50 to 80: |80-50| = 30
From 80 to 100: |100-80| = 20
From 100 to 120: |120-100| = 20
From 120 to 150: |150-120| = 30
From 150 to end (199), then reverse to 40: |199-150| + |199-40| = 49 + 159 = 208
Total head movement = 30 + 20 + 20 + 30 + 208 = 308 tracks

This example demonstrates that SSTF provides the best performance in this scenario, reducing head movement by more than half compared to FCFS. However, in practice, the SCAN algorithm often performs more consistently because it avoids the starvation issues inherent in SSTF.

### Example 2: File Allocation Analysis

A file system uses contiguous allocation with block size of 4 KB. A file requires 100 KB of storage.

**Calculating blocks needed:**
Block size = 4 KB = 4096 bytes
File size = 100 KB = 102400 bytes
Blocks required = 102400 / 4096 = 25 blocks (ceiling)

If the file starts at block 50, it occupies blocks 50 through 74 consecutively.

**Analyzing issues with file growth:**
If the file needs to grow by 20 KB (5 additional blocks), we need blocks 75-79 to be free. If these blocks are allocated to another file, we must either move the entire file or deny the growth request. This demonstrates the inflexibility of contiguous allocation in handling dynamic file sizes.

**Comparing with linked allocation:**
Using linked allocation, the file can span non-contiguous blocks since each block contains a pointer to the next. However, accessing block 20 of the file requires traversing 20 pointer references, resulting in 20 disk seeks in the worst case. This shows the trade-off between allocation flexibility and access performance.

### Example 3: Free Space Management with Bit Vector

Consider a disk with 16 blocks. The current allocation bit vector is: 1 1 0 1 0 0 1 1 0 0 1 1 1 0 0 1

**Converting to free block list:**
1 = allocated, 0 = free
Free blocks: 2, 4, 5, 8, 9, 12, 13, 14

**If a file needs 3 consecutive blocks:**
Scanning for 3 consecutive zeros:
Position 4-6: 0, 0, 1 (not three consecutive)
Position 8-10: 1, 0, 0 (not three consecutive)
Position 12-14: 1, 1, 0 (not three consecutive)

No three consecutive free blocks exist. The file must either use non-contiguous allocation (requiring more complex file allocation structures) or wait until sufficient consecutive space becomes available. This illustrates how bit vectors help identify fragmentation issues in storage systems.

## Exam Tips

Understanding storage management concepts is essential for DU semester examinations. The following points highlight frequently examined topics and common pitfalls to avoid.

FIRST, disk scheduling algorithms are almost always tested in exams. You should be able to calculate total head movement for FCFS, SSTF, SCAN, C-SCAN, and LOOK algorithms. Understand the advantages and disadvantages of each algorithm, particularly regarding starvation and fairness.

SECOND, remember that seek time is the dominant factor in disk access time. Rotation delay and transfer time are typically much smaller. When analyzing disk performance, focus primarily on minimizing seek operations.

THIRD, file allocation methods (contiguous, linked, indexed) are frequently compared in exam questions. Be prepared to explain how each method handles file growth, random access, and external fragmentation.

FOURTH, virtual memory concepts including paging and segmentation often appear in exam questions. Understand how logical addresses are translated to physical addresses and the role of page tables in this process.

FIFTH, free space management techniques are important. Know how bit vectors work and be able to determine free blocks from a given bitmap representation.

SIXTH, practice numerical problems involving disk scheduling calculations. These are straightforward marks and can be solved systematically by tracking head position and request positions.

SEVENTH, understand the relationship between storage hierarchy and system performance. Explain how caching and buffering improve overall system responsiveness despite the inherent speed differences between storage levels.

EIGHTH, when answering comparison questions, structure your response clearly. Present the advantages and disadvantages of each approach before drawing conclusions. Examiners appreciate balanced analysis rather than superficial coverage.