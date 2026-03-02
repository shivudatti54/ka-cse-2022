# Directory and Disk Structure


## Table of Contents

- [Directory and Disk Structure](#directory-and-disk-structure)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Directory Overview](#directory-overview)
  - [Single-Level Directory](#single-level-directory)
  - [Two-Level Directory](#two-level-directory)
  - [Hierarchical Directory Structure](#hierarchical-directory-structure)
  - [Acyclic Graph Directory Structure](#acyclic-graph-directory-structure)
  - [Disk Structure Fundamentals](#disk-structure-fundamentals)
  - [Disk Partitioning](#disk-partitioning)
  - [File Allocation Methods](#file-allocation-methods)
  - [Free Space Management](#free-space-management)
  - [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
- [Examples](#examples)
  - [Example 1: Directory Path Resolution](#example-1-directory-path-resolution)
  - [Example 2: Indexed File Allocation](#example-2-indexed-file-allocation)
  - [Example 3: SCAN Disk Scheduling](#example-3-scan-disk-scheduling)
- [Exam Tips](#exam-tips)

## Introduction

A file system is the most visible aspect of any operating system—it provides the interface through which users and applications interact with stored data. At the core of every file system lies the directory structure, which organizes files logically, and the disk structure, which manages physical storage efficiently. Understanding directory and disk structure is fundamental to comprehending how operating systems handle persistent data, manage storage space, and provide reliable data access to users and processes.

In modern computing environments, directories (also called folders) serve as the hierarchical organizational framework for millions of files across enterprise systems, cloud storage platforms, and personal computing devices. The operating system must maintain directory entries that map symbolic file names to physical disk locations, while simultaneously managing free space, ensuring data integrity, and optimizing access performance. For Computer Science students preparing for industry roles in system administration, database management, or software development, a thorough understanding of these concepts is essential for designing efficient storage solutions and troubleshooting performance issues.

This chapter examines the various directory organization techniques employed by modern operating systems, ranging from simple single-level structures to complex hierarchical and graph-based implementations. Additionally, we explore disk structure fundamentals, including physical geometry, partitioning, and the critical algorithms that govern disk I/O operations.

## Key Concepts

### Directory Overview

A directory is a special file that contains information about other files. Each directory entry stores metadata including the file name, file attributes (size, creation time, permissions), and a pointer to the file's control block or i-node. The directory structure fundamentally defines how users perceive and organize their data, while the underlying disk structure determines how that data is physically stored and retrieved.

### Single-Level Directory

The simplest directory structure consists of a single directory containing all files. Also known as the flat directory, this approach assigns unique names to every file since all entries reside in one namespace. While extremely simple to implement—with minimal overhead for file creation, deletion, and lookup—it becomes unmanageable as the number of files grows. Users cannot create files with the same name, and there is no mechanism for grouping related files. This structure is suitable only for extremely simple embedded systems with limited storage requirements.

### Two-Level Directory

The two-level directory structure addresses the naming conflict problem by creating separate directories for each user. A master directory (also called the user file directory or UFD) contains entries for individual user directories, while each user directory (known as the user working directory or UWD) holds that user's files. This approach, used by early versions of the IBM OS/360 and MS-DOS, provides user isolation and prevents naming conflicts between users. However, it still lacks the ability to group related files within a user's directory, forcing users to manage large collections of unrelated files.

### Hierarchical Directory Structure

The hierarchical or tree-structured directory represents the most common organizational paradigm in modern computing. Starting from a root directory, the system creates a branching structure of subdirectories, allowing infinite depth in file organization. Users can create logical groupings of files, navigate between directories using relative or absolute paths, and establish clear organizational hierarchies. Each directory entry points to either a file or another directory, forming a tree data structure. The UNIX/Linux file system and Windows NTFS are prominent examples of hierarchical implementations.

Key operations in hierarchical directories include path navigation, directory creation and deletion, and file lookup. The system maintains a current working directory for each process, enabling relative path resolution without specifying full absolute paths. When a directory is deleted, the system must decide how to handle its contents—either restricting deletion to empty directories or implementing recursive deletion of all contained files and subdirectories.

### Acyclic Graph Directory Structure

Acyclic graphs extend the tree structure by allowing directories to share subtrees through symbolic links or shortcuts. In this model, multiple directory entries can reference the same file or directory without creating cycles in the directory graph. UNIX systems implement this through symbolic links (soft links) and hard links. A hard link creates an additional directory entry pointing directly to the same file's i-node, while a symbolic link stores the path to the target file.

The acyclic property ensures that algorithms traversing the directory structure will eventually terminate. However, file deletion becomes complex: when a hard-linked file is deleted, the file's data persists until all links are removed. Symbolic links can point to non-existent targets (dangling links), requiring appropriate error handling during traversal.

### Disk Structure Fundamentals

Physical disks consist of concentric tracks divided into sectors, with multiple platters stacked on a common spindle forming cylinders. Modern disks use logical block addressing (LBA), presenting a linear array of addressable sectors to the operating system, abstracting away the physical geometry. The disk structure encompasses the entire storage hierarchy: physical sectors, partitions, file system structures, and individual files.

### Disk Partitioning

Before a disk can store files, it must be partitioned into logical divisions. A partition is a contiguous range of disk blocks treated as an independent storage device. The partition table, stored in the master boot record (MBR) or GUID partition table (GPT), defines partition boundaries and types. Common partition types include primary partitions, extended partitions (containing logical partitions), and swap partitions. Each partition can host an independent file system, enabling multi-boot configurations and separation of system and user data.

### File Allocation Methods

The operating system must decide how to allocate disk space for files. Three primary methods exist, each with distinct performance characteristics.

**Contiguous Allocation** assigns each file a single continuous range of disk blocks. This method offers excellent sequential access performance since the disk head need not move extensively between blocks. However, it suffers from external fragmentation as files are created and deleted, and determining optimal file size at creation time is challenging. Compaction strategies can reclaim free space but require significant I/O overhead.

**Linked Allocation** stores each file as a linked list of disk blocks, with each block containing a pointer to the next block. This eliminates external fragmentation and simplifies file growth—new blocks can be appended anywhere on the disk. However, random access becomes inefficient since blocks must be traversed sequentially from the beginning. The File Allocation Table (FAT) file system exemplifies this approach, storing pointers in a central table rather than within blocks themselves.

**Indexed Allocation** uses an index block containing pointers to all file blocks. A single disk read of the index block enables direct access to any file block, supporting both sequential and random access efficiently. The UNIX file system implements this through i-nodes, where each file has a fixed-size structure containing both metadata and direct/indirect block pointers. Index blocks do introduce overhead, particularly for small files that could fit contiguously.

### Free Space Management

The operating system must track unallocated disk blocks to satisfy new file creation and file growth requests. Several techniques manage free space effectively.

The **bit vector** (or bitmap) maintains one bit per disk block, indicating whether each block is free or allocated. Bit vectors enable fast allocation and deallocation, with algorithms that efficiently locate contiguous free regions. However, the bitmap itself requires storage proportional to disk size, making it less suitable for very large disks without additional structures.

The **linked list** approach maintains a list of free blocks by storing pointers to the next free block within each free block itself. While requiring minimal overhead, finding contiguous free space becomes inefficient as the list grows scattered.

**Grouping** improves upon linked lists by storing addresses of multiple free blocks in the first free block, enabling quick acquisition of multiple blocks during allocation.

**Counting** maintains pairs of (first free block, count of consecutive free blocks), efficient for managing large contiguous free regions created by file deletion.

### Disk Scheduling Algorithms

When multiple processes request disk I/O, the operating system must order these requests to minimize mechanical motion and improve throughput. Several algorithms address this challenge.

**First-Come-First-Served (FCFS)** processes requests in arrival order. While fair and simple, it provides no optimization for seek distance.

**Shortest Seek Time First (SSTF)** selects the request closest to the current head position, minimizing seek time. This approach resembles SJF scheduling and can significantly improve performance, but may cause starvation for requests at disk extremities.

**SCAN** (elevator algorithm) moves the disk head in one direction, servicing all requests until reaching the end, then reversing direction. This approach ensures uniform response times and reduces starvation, though requests just ahead of the head experience longer waits than those behind it.

**C-SCAN** (Circular SCAN) services requests in one direction only, returning to the beginning without servicing requests during the return trip. This provides more uniform wait times than SCAN.

**LOOK** optimizes SCAN by reversing direction when no further requests exist in the current direction, avoiding unnecessary travel to disk edges.

## Examples

### Example 1: Directory Path Resolution

Consider a UNIX-style hierarchical directory with the following structure:

```
/
├── home/
│   ├── student/
│   │   ├── documents/
│   │   │   ├── report.txt
│   │   │   └── notes.txt
│   │   └── downloads/
│   │       └── image.png
│   └── admin/
└── var/
    └── log/
        └── system.log
```

When a process with current working directory "/home/student/documents" attempts to open "../../admin/config.cfg", the operating system performs path resolution as follows:

1. The ".." entry refers to the parent directory (home/student)
2. Another ".." refers to the parent again (home)
3. "admin" refers to the "admin" subdirectory within home
4. "config.cfg" refers to the file within admin

The final resolved path is "/home/admin/config.cfg", which the operating system then attempts to access, checking permissions at each directory level.

### Example 2: Indexed File Allocation

Assume a UNIX-style i-node with the following structure: 12 direct pointers, 1 single indirect pointer, 1 double indirect pointer, and 1 triple indirect pointer. Disk block size is 4 KB, and each block pointer is 4 bytes.

For a file containing exactly 50 KB of data:

- Blocks 1-12: Direct blocks (12 × 4 KB = 48 KB)
- Block 13: Single indirect block points to additional data blocks

The i-node contains: 12 direct pointers pointing to the first 12 data blocks, 1 single indirect pointer pointing to an index block containing pointers to remaining blocks. The single indirect block can address 4 KB / 4 bytes = 1024 pointers, each pointing to a 4 KB data block, providing support for files up to 4 TB using triple indirect pointers.

### Example 3: SCAN Disk Scheduling

Given a disk with 200 tracks (0-199) and the following request queue in order of arrival: [55, 58, 39, 18, 90, 160, 150, 38, 184]. Assume the initial head position is 50, moving toward increasing track numbers.

**FCFS Sequence:** 55 → 58 → 39 → 18 → 90 → 160 → 150 → 38 → 184
Total head movement: |55-50| + |58-55| + |39-58| + |18-39| + |90-18| + |160-90| + |150-160| + |38-150| + |184-38| = 5 + 3 + 19 + 21 + 72 + 70 + 10 + 112 + 146 = 558 tracks

**SCAN Sequence:** Starting at 50, moving upward: 55 → 58 → 90 → 150 → 160 → 184 → 199 (end) → 39 → 38 → 18
Total head movement: |55-50| + |58-55| + |90-58| + |150-90| + |160-150| + |184-160| + |199-184| + |199-39| + |39-38| + |38-18| = 5 + 3 + 32 + 60 + 10 + 24 + 15 + 160 + 1 + 20 = 330 tracks

The SCAN algorithm reduces total head movement by 40.8% compared to FCFS in this scenario, demonstrating significant performance improvement for sequential-like access patterns.

## Exam Tips

1. **Directory vs. Disk Structure**: Remember that directory structure refers to the logical organization of files (hierarchical, tree, graph), while disk structure refers to physical storage organization (tracks, sectors, partitions).

2. **File Allocation Trade-offs**: Understand that contiguous allocation excels in sequential access but suffers from external fragmentation; linked allocation eliminates fragmentation but performs poorly in random access; indexed allocation provides good random access but requires additional I/O for index blocks.

3. **Hard Links vs. Symbolic Links**: Hard links cannot span partitions (same i-node required) and cannot link to directories, while symbolic links can reference non-existent targets (dangling links) and can span partitions.

4. **Directory Deletion in Acyclic Graphs**: When deleting directories with shared subtrees, understand that hard links maintain file existence until all links are removed, while symbolic link deletion affects only the link itself.

5. **Disk Scheduling Performance**: Remember that FCFS is fair but slow, SSTF is faster but can cause starvation, SCAN and C-SCAN provide better average performance with reduced starvation, and LOOK optimizes SCAN by not traveling to disk edges unnecessarily.

6. **Free Space Management Selection**: Bit vectors provide fast allocation but require significant memory for large disks; linked lists waste space for pointers; grouping and counting offer compromises for specific access patterns.

7. **i-node Structure**: For UNIX-style indexed allocation, understand how direct, single indirect, double indirect, and triple indirect pointers work together to address files of various sizes efficiently.