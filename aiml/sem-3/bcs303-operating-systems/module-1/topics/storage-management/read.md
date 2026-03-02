# Storage Management in Operating Systems


## Table of Contents

- [Storage Management in Operating Systems](#storage-management-in-operating-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Disk Structure and Organization](#disk-structure-and-organization)
  - [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
  - [Free Space Management](#free-space-management)
  - [Disk Organization and File Systems](#disk-organization-and-file-systems)
- [Examples](#examples)
  - [Example 1: FCFS vs. SSTF Scheduling](#example-1-fcfs-vs-sstf-scheduling)
  - [Example 2: Free Space Management with Bit Vector](#example-2-free-space-management-with-bit-vector)
  - [Example 3: Indexed File Allocation](#example-3-indexed-file-allocation)
- [Exam Tips](#exam-tips)

## Introduction

Storage management is a fundamental component of operating system design, responsible for controlling and coordinating computer storage resources. In modern computing systems, data must be persistently stored even when power is removed, making secondary storage (primarily magnetic disks) essential for long-term data retention. The operating system must efficiently manage these storage devices, providing reliable data access while optimizing performance and maximizing utilization of available storage capacity.

The storage hierarchy in computer systems comprises three main levels: primary storage (main memory/RAM), secondary storage (magnetic disks, SSDs), and tertiary storage (magnetic tapes, optical media). Each level offers different trade-offs between speed, cost, and persistence. Primary storage provides extremely fast access times but is volatile and expensive per byte, while secondary and tertiary storage offer larger capacities at lower costs but with significantly higher access latencies. The operating system's storage management layer bridges this gap, presenting a unified logical view of storage to applications while handling the physical complexities behind the scenes.

Storage management encompasses several critical functions: disk scheduling to minimize seek time, free space management to track available storage, disk organization methods to structure data effectively, and file system implementation to provide convenient named data access. This module explores these concepts in detail, examining the algorithms and data structures that operating systems employ to manage secondary storage efficiently.

## Key Concepts

### Disk Structure and Organization

Modern magnetic disks consist of one or more rotating platters coated with magnetic material, with read/write heads that move radially across the platter surfaces. The disk surface is logically divided into concentric circles called tracks, and each track is further subdivided into sectors. The collection of tracks at the same radius across all platters forms a cylinder. The operating system groups multiple sectors into blocks (or clusters) for more efficient allocation and access. Each sector typically holds 512 bytes or 4 KB of data, with modern disks using 4 KB sectors for improved efficiency.

The physical characteristics of disks significantly impact performance. The three primary delays in disk access are: seek time (time to move the read/write head to the correct track), rotational latency (time waiting for the desired sector to rotate under the head), and transfer time (time to actually read or write the data). Average seek time in modern disks ranges from 3 to 12 milliseconds, while rotational latency depends on rotational speed (7200 RPM to 15000 RPM). Understanding these parameters is crucial for designing effective disk scheduling algorithms.

### Disk Scheduling Algorithms

The operating system maintains a queue of pending disk I/O requests and determines the order in which these requests are serviced. The goal is to minimize total head movement (seek time), thereby reducing average access time and improving throughput. Several disk scheduling algorithms have been developed to address this problem.

**First-Come-First-Served (FCFS)** is the simplest algorithm, servicing requests in the order they arrive. While fair and easy to implement, FCFS performs poorly when the request queue contains requests scattered across different tracks, resulting in excessive head movement.

**Shortest Seek Time First (SSTF)** selects the request closest to the current head position, minimizing seek distance from the current location. SSTF provides significantly better performance than FCFS but may cause starvation for requests far from the current position if new nearby requests continuously arrive.

**SCAN Algorithm**, also known as the elevator algorithm, moves the head monotonically from one end of the disk to the other, servicing requests along the way. Upon reaching the end, the head reverses direction and continues. This approach ensures that all requests are serviced within a bounded time, preventing starvation, and typically performs well for systems with heavy loads.

**C-SCAN (Circular SCAN)** is a variant that services requests only in one direction (e.g., from outer to inner tracks). When reaching the end, the head jumps back to the beginning without servicing requests during the return trip. This provides more uniform wait times than SCAN but may result in slightly higher average seek distances.

**LOOK Algorithm** is similar to SCAN but does not go all the way to the end of the disk; instead, it reverses direction at the last request in each direction, reducing unnecessary head movement.

### Free Space Management

The operating system must track which storage blocks are free (unallocated) and which are in use. Several techniques exist for free space management:

**Bit Vector (Bitmap)** represents each block with one bit, where 0 indicates free and 1 indicates allocated. This approach allows quick allocation and deallocation, and the first-fit algorithm can efficiently find free blocks by scanning the bitmap. However, the bitmap requires extra storage space (one bit per block) and may not be cached effectively.

**Linked List** maintains a list of free blocks, with each free block containing a pointer to the next free block. While requiring minimal overhead, linked list traversal can be slow for large disks, especially when searching for blocks of a specific size.

**Grouping** stores addresses of n free blocks in the first free block, allowing quick acquisition of multiple free blocks. This technique combines the advantages of linked lists and bitmaps.

**Counting** maintains pairs of (first free block, count of consecutive free blocks), which is efficient when free blocks often form contiguous groups.

### Disk Organization and File Systems

The operating system organizes data on disk using file systems, which provide the abstraction of named files and hierarchical directories. Key file system components include:

**File Control Block (FCB)** is a data structure storing metadata about each file, including file name, size, creation date, permissions, and pointers to data blocks. The FCB is typically stored in a directory entry.

**Directory Structure** provides the namespace for organizing files. Common structures include single-level directories, two-level directories, tree-structured directories, and acyclic graph directories. Modern operating systems use hierarchical directory structures with support for symbolic links.

**Allocation Methods** determine how file data blocks are placed on disk:

- **Contiguous Allocation**: Files occupy consecutive blocks on disk. This provides excellent sequential access performance and simple address calculation but suffers from external fragmentation and difficulty in expanding files.

- **Linked Allocation**: Each file block contains a pointer to the next block in the file. This eliminates external fragmentation and allows easy file expansion but provides poor random access performance (must follow pointers) and reliability concerns (lost pointer means data loss).

- **Indexed Allocation**: Uses an index block containing pointers to all data blocks. This supports direct random access and eliminates external fragmentation but requires extra I/O to read the index block for each access and may have overhead for small files (index block may be partially unused).

Modern file systems like NTFS, ext4, and XFS use variations of these methods, often combining contiguous allocation for small files with more complex schemes for larger files.

## Examples

### Example 1: FCFS vs. SSTF Scheduling

Consider a disk with 200 tracks (0-199) and a request queue in FCFS order: 98, 183, 37, 122, 14, 124, 65, 67. Assume the head initially starts at track 53.

**FCFS Calculation:**

- Head moves from 53 to 98: 45 tracks
- Head moves from 98 to 183: 85 tracks
- Head moves from 183 to 37: 146 tracks
- Head moves from 37 to 122: 85 tracks
- Head moves from 122 to 14: 108 tracks
- Head moves from 14 to 124: 110 tracks
- Head moves from 124 to 67: 57 tracks
- **Total head movement: 636 tracks**

**SSTF Calculation:**
Starting at track 53:

- Nearest request is 65 (distance 12)
- Next nearest to 65 is 67 (distance 2)
- Next nearest to 67 is 37 (distance 30)
- Next nearest to 37 is 14 (distance 23)
- Next nearest to 14 is 98 (distance 84)
- Next nearest to 98 is 122 (distance 24)
- Next nearest to 122 is 183 (distance 61)
- **Total head movement: 236 tracks**

SSTF reduces head movement by approximately 63% compared to FCFS in this example.

### Example 2: Free Space Management with Bit Vector

Consider a disk with 16 blocks managed using a bit vector. If the bit vector is `0011110010011100` (blocks 0-15 from left to right):

- Bits at positions 0, 5, 6, 10, 14, 15 are 1 (allocated)
- Free blocks are at positions: 1, 2, 3, 4, 7, 8, 11, 12, 13

For first-fit allocation of a 3-block file:

- Scan from position 0: blocks 1, 2, 3 are free (3 consecutive blocks found)
- Allocate blocks 1, 2, 3
- New bit vector: `0111110010011100`

For best-fit allocation of a 2-block file:

- Find smallest gap of 2+ consecutive free blocks
- Gap at positions 7-8 (size 2) is optimal
- Allocate blocks 7 and 8
- New bit vector: `0111110010111100`

### Example 3: Indexed File Allocation

A file system uses indexed allocation with 4-byte pointers in each index block. Each index block can hold 1024 pointers (4096 bytes / 4 bytes). For a file requiring 3500 data blocks:

- The file needs one index block
- The first 1023 data blocks are directly referenced by the index block
- Data blocks 1024-2047 would require a second-level index block
- Data blocks 2048-3071 would require a third-level index block
- Our file needs 4 index blocks (1 primary + 3 second-level): one for blocks 0-1023, one for 1024-2047, one for 2048-3072, and one for 3073-3500

To access logical block 2500:

- Primary index block at offset 2 (second-level index for blocks 2048-3071)
- Follow pointer to second-level index at offset 452 (2500 - 2048)
- Access data block

This two-level scheme supports files up to approximately 1 million blocks with minimal index overhead.

## Exam Tips

1. **Understand the difference between seek time, rotational latency, and transfer time** - These are the three main components of disk I/O time. Seek time typically dominates and is the primary target of disk scheduling algorithms.

2. **Remember that SCAN and C-SCAN provide bounded response times** - This makes them suitable for real-time systems and applications requiring predictable performance, unlike SSTF which may cause starvation.

3. **Know the trade-offs of each allocation method** - Contiguous allocation offers the best sequential access but suffers from external fragmentation; linked allocation eliminates fragmentation but has poor random access; indexed allocation supports direct access but has index block overhead.

4. **Be prepared to calculate average seek distance** - Practice problems involving head movement calculations for different scheduling algorithms are common in examinations.

5. **Understand when to use each scheduling algorithm** - FCFS for simple systems with low I/O load; SSTF for moderate load where response time matters; SCAN/LOOK for high-load systems requiring fairness; C-SCAN when uniform response times are needed.

6. **Remember that modern disks use elevator algorithms internally** - Most modern hard drives incorporate built-in caching and scheduling, making OS-level scheduling less critical, though still important for understanding system behavior.

7. **Free space management affects file system performance** - Bit vectors provide fast allocation but require memory; linked lists are simple but slow for searching; grouping and counting offer middle-ground solutions.
