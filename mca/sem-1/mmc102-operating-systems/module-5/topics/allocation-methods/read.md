# Allocation Methods


## Table of Contents

- [Allocation Methods](#allocation-methods)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Contiguous Allocation](#contiguous-allocation)
  - [Linked Allocation](#linked-allocation)
  - [Indexed Allocation](#indexed-allocation)
- [Examples](#examples)
  - [Example 1: Contiguous Allocation Scenario](#example-1-contiguous-allocation-scenario)
  - [Example 2: Linked Allocation Access](#example-2-linked-allocation-access)
  - [Example 3: Indexed Allocation Performance](#example-3-indexed-allocation-performance)
- [Exam Tips](#exam-tips)

## Introduction

File allocation methods determine how disk space is organized and managed for storing files. When a user creates a file, the operating system must decide where to store the file's data on the physical disk. The choice of allocation method significantly impacts file access speed, disk utilization, and overall system performance. In modern operating systems, three primary allocation methods dominate: contiguous allocation, linked allocation, and indexed allocation. Each method presents unique trade-offs between access speed, storage efficiency, and implementation complexity.

Understanding these allocation methods is crucial for system administrators and software developers alike. The method chosen affects how quickly files can be accessed, how much disk space is wasted due to fragmentation, and how the file system handles file growth and deletion. As operating systems evolve, hybrid approaches combining the best aspects of these fundamental methods have emerged, demonstrating the enduring importance of these foundational concepts in modern computing.

## Key Concepts

### Contiguous Allocation

Contiguous allocation assigns each file a single continuous block of disk sectors. The file allocation table (FAT) or directory entry simply stores the starting block number and the length of the file. When a process requests file creation, the operating system searches for a contiguous free space large enough to accommodate the file.

The directory entry for a file using contiguous allocation contains:
- File name
- Starting block address
- Length (in blocks)
- Other metadata (permissions, timestamps)

Contiguous allocation offers several advantages. Sequential access is extremely efficient since the read head moves linearly across the disk. Random access also performs well because the block location can be calculated directly from the starting address and offset. The simplicity of implementation reduces overhead and improves reliability.

However, this method suffers from significant limitations. External fragmentation occurs when free disk space becomes divided into small, non-contiguous chunks, making it impossible to allocate large files even when total free space exceeds the file size. File growth poses another challenge: if a file needs to extend beyond its allocated space, the entire file may need to be moved to a new location. The degree of fragmentation can be quantified using the formula:

EXTERNAL FRAGMENTATION = (Total Free Space) - (Largest Contiguous Free Block)

Three strategies exist for allocating contiguous space. First-fit allocates the first free block large enough to hold the file, offering speed but potentially creating fragmentation. Best-fit searches for the smallest free block that can accommodate the file, minimizing wasted space but requiring more search time. Worst-fit always uses the largest available free block, promoting larger remaining free spaces but often resulting in poor performance.

### Linked Allocation

Linked allocation solves the fragmentation problem by storing each file as a linked list of disk blocks. Each block contains a pointer to the next block in the sequence, and the directory entry stores only the pointer to the first block. This approach eliminates external fragmentation entirely, as any free block can be used for file extension.

The directory entry for linked allocation contains:
- File name
- Pointer to first block
- Pointer to last block (optional, for efficient append operations)
- File size

Linked allocation provides several benefits. Any free block can be used for file extension, eliminating the need for complex allocation algorithms. The file system can grow dynamically without requiring contiguous space. Storage utilization approaches 100% since all free blocks can be allocated.

However, linked allocation introduces significant performance overhead. Random access becomes inefficient because the system must traverse the linked list from the beginning to reach any specific block. The n-th block access requires reading n-1 pointer blocks first, resulting in O(n) time complexity. This is particularly problematic for large files.

Reliability concerns also arise. If any pointer becomes corrupted due to disk errors or software bugs, the entire file may become inaccessible. The pointer overhead reduces usable storage capacity, with each block requiring space for the next-pointer (typically 4 bytes in modern systems). Additionally, local access patterns become poor since blocks may be scattered throughout the disk.

The File Allocation Table (FAT) system represents a refinement of linked allocation. FAT maintains a separate table indexed by block numbers, where each entry contains the block number of the next block in the file. The directory stores only the starting block number. This centralized structure improves reliability and allows the FAT to be cached in memory for faster access. MS-DOS and early Windows systems extensively used FAT file systems.

### Indexed Allocation

Indexed allocation addresses the random access limitation of linked allocation by using an index block. Each file has a dedicated index block that stores the addresses of all data blocks belonging to the file. The directory entry points to the index block, and block access occurs by reading the index block first to find the desired data block address.

The directory entry for indexed allocation contains:
- File name
- Pointer to index block
- File size

Indexed allocation provides efficient random access. Any block can be accessed directly by reading the index block and retrieving the corresponding pointer, achieving O(1) access time after the index block is in memory. Sequential access also performs well since all block addresses are available in the index.

The main disadvantage is the overhead of the index block. For small files, the index block represents significant wasted space. For instance, with 4KB blocks and 4-byte block pointers, an index block can address 1024 data blocks (4MB of data), but a 1KB file still requires a full 4KB index block.

Several variations optimize indexed allocation for different use cases. Single-level indexed allocation uses one index block per file, suitable for small to medium files but limiting maximum file size. Multi-level indexed allocation uses a hierarchy of index blocks (similar to page tables), where first-level index blocks point to second-level index blocks that point to data blocks. This approach supports larger files but increases access time for deeply nested blocks. UNIX inode structure implements a hybrid approach combining direct pointers (for small files), single indirect pointers, double indirect pointers, and triple indirect pointers.

The combined scheme, used by UNIX-like systems, provides excellent performance for small files (direct pointers avoid indirection) while supporting very large files through multi-level indirection. An inode typically contains 12 direct pointers, one single indirect pointer, one double indirect pointer, and one triple indirect pointer, supporting files up to several terabytes depending on block size.

## Examples

### Example 1: Contiguous Allocation Scenario

Consider a disk with 100 blocks numbered 0-99. The following sequence of operations occurs:

1. Process A creates a 10-block file (requires blocks 10-19)
2. Process B creates a 15-block file (requires blocks 20-34)
3. Process A's file is deleted (frees blocks 10-19)
4. Process C creates an 8-block file

Using first-fit allocation, Process C receives blocks 10-17 (the first available contiguous space). The disk now has a 2-block hole at blocks 18-19, which may remain unused or cause fragmentation for future allocations.

If worst-fit were used, the largest free space would be identified. After deletion of Process A's file, free spaces are blocks 10-19 (10 blocks) and blocks 35-99 (65 blocks). Worst-fit would allocate from block 35, leaving even larger fragmented spaces.

### Example 2: Linked Allocation Access

A file "data.txt" stored using linked allocation has blocks at positions: 50 → 25 → 12 → 78 → 60. The directory stores only the first block number (50).

To read the 4th block (content at position 60), the system must:
1. Read block 50, extract pointer to block 25
2. Read block 25, extract pointer to block 12
3. Read block 12, extract pointer to block 78
4. Read block 78, extract pointer to block 60
5. Read block 60 to get the actual data

This requires 5 disk I/O operations compared to 1-2 operations with contiguous or indexed allocation, demonstrating why linked allocation performs poorly for random access.

### Example 3: Indexed Allocation Performance

Using single-level indexed allocation with 4KB blocks and 4-byte pointers:
- Each index block can address 1024 data blocks
- Maximum file size: 1024 × 4KB = 4MB
- To access any block: 1 I/O for index block + 1 I/O for data block = 2 I/O operations

Using two-level indexed allocation:
- First-level index: 1024 pointers to second-level index blocks
- Second-level index: 1024 pointers to data blocks each
- Maximum file size: 1024 × 1024 × 4KB = 4GB
- To access a block requiring both index levels: 3 I/O operations (first-level + second-level + data)

## Exam Tips

Contiguous allocation provides THE FASTEST SEQUENTIAL AND RANDOM ACCESS but suffers from external fragmentation and difficulty in file extension.

Linked allocation ELIMINATES EXTERNAL FRAGMENTATION but has slow random access (must follow pointers sequentially) and reliability issues if pointers are corrupted.

Indexed allocation OFFERS FAST RANDOM ACCESS but wastes space for small files and has overhead of accessing index blocks.

FAT file systems use LINKED ALLOCATION with a centralized table, allowing the FAT to be cached in memory for improved performance.

UNIX inodes use a HYBRID APPROACH with direct, single indirect, double indirect, and triple indirect pointers to optimize for both small and large files.

The main disadvantage of indexed allocation for small files is INDEX BLOCK OVERHEAD consuming significant space relative to file size.

Contiguous allocation requires EXTERNAL FRAGMENTATION MANAGEMENT through compaction, which is time-consuming and requires downtime.

Best-fit allocation MINIMIZES WASTED SPACE but takes longer to search, while first-fit is faster but may create small unusable fragments.

Key formula for external fragmentation in contiguous allocation: fragmentation occurs when no single free block is large enough despite total free space being adequate.

Memory cache consideration: keeping the FAT or index blocks in memory dramatically improves performance for all allocation methods.