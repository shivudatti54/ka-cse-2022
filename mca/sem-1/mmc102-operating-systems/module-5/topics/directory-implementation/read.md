# Directory Implementation


## Table of Contents

- [Directory Implementation](#directory-implementation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Directory Structure Overview](#directory-structure-overview)
  - [Linear List Implementation](#linear-list-implementation)
  - [Hash Table Implementation](#hash-table-implementation)
  - [File Allocation Methods and Directory Integration](#file-allocation-methods-and-directory-integration)
  - [Directory Operations](#directory-operations)
- [Examples](#examples)
  - [Example 1: Linear List Directory Search](#example-1-linear-list-directory-search)
  - [Example 2: Hash Table Directory Implementation](#example-2-hash-table-directory-implementation)
  - [Example 3: Tree-Structured Directory Navigation](#example-3-tree-structured-directory-navigation)
- [Exam Tips](#exam-tips)

## Introduction

A directory is a fundamental component of any file system, serving as the organizational backbone that enables users and programs to store, locate, and manage files efficiently. In operating systems, a directory is essentially a special type of file that maintains a collection of file descriptors or entries, each describing a file within its scope. The directory implementation determines how these file entries are stored, searched, and manipulated, directly impacting file system performance, reliability, and usability.

Directory implementation is a critical aspect of file system design that often receives less attention than file allocation methods, yet it profoundly affects the user experience and system efficiency. When you execute a command like "open /home/user/document.txt", the operating system must traverse through multiple directories to locate the file. The efficiency of this lookup operation depends entirely on how directories are internally structured and implemented. Modern operating systems support thousands of files and deep directory hierarchies, making efficient directory implementation essential for responsive system performance.

This topic explores various directory implementation techniques, from simple linear lists to sophisticated hash-based structures, analyzing their strengths, weaknesses, and appropriate use cases. Understanding these implementation details is crucial for system administrators, developers, and anyone seeking to optimize file system performance in enterprise environments.

## Key Concepts

### Directory Structure Overview

A directory entry typically contains several essential pieces of information about each file: the file name, file attributes (such as creation time, permissions, and ownership), and a pointer to the file's data blocks. The operating system maintains these entries to provide a mapping between logical file names used by users and physical locations where file data is stored on disk.

Directories can be organized in several hierarchical structures, each with distinct characteristics:

**Single-Level Directory:** The simplest structure where all files reside in one directory. While easy to implement, it suffers from name collisions—two users cannot create files with the same name. This approach is primarily of historical interest and is rarely used in modern systems.

**Two-Level Directory:** Each user gets a private directory, eliminating name conflicts between users. The system maintains a master file directory (MFD) containing entries for each user, while each user has a user file directory (UFD). This structure was used in early mainframe systems but lacks support for hierarchical organization within user spaces.

**Tree-Structured Directory:** The most common structure where directories can contain subdirectories, creating a hierarchical tree. This approach provides natural organization (documents, images, downloads) and efficient file lookup. Unix-like systems and Windows both use tree-structured directories. The full path from root to any file uniquely identifies its location.

**Acyclic Graph Directory:** Allows directories to share subdirectories and files, creating a directed acyclic graph structure. This enables file sharing without data duplication. Unix symbolic links represent one implementation of this concept. The absence of cycles simplifies traversal and prevents infinite loops during directory searches.

**General Graph Directory:** Permits cycles in the directory structure, allowing both symbolic and hard links. While flexible, this structure requires careful handling to prevent infinite loops during traversal and may complicate directory caching mechanisms.

### Linear List Implementation

The simplest directory implementation uses a linear list (array) to store directory entries sequentially. Each entry contains the file name, file attributes, and a pointer to the file's FCB (File Control Block) or i-node. When searching for a file, the system must traverse the list sequentially until finding the matching file name.

**Implementation Characteristics:**
- Simple to implement with minimal overhead
- Suitable for small directories with few files
- Search complexity: O(n) where n is the number of files
- Adding a new file involves appending to the list
- Deletion requires searching and removing the entry, potentially leaving gaps

The linear list approach works adequately for small directories but becomes inefficient as the number of files grows. Sequential scanning through hundreds or thousands of entries introduces noticeable latency, particularly on systems with slower storage devices.

### Hash Table Implementation

Hash-based directory implementation uses a hash function to compute an index into an array (hash table) based on the file name. When storing a file, the hash function generates an index, and the entry is stored at that position. When searching, the same hash function computes the expected position, allowing O(1) average-case lookup time.

**Implementation Characteristics:**
- Average-case search complexity: O(1)
- Worst-case complexity: O(n) when hash collisions occur
- Requires handling collision resolution (chaining, open addressing)
- Memory overhead for the hash table structure
- Dynamic resizing may be needed as directories grow

Hash tables significantly improve lookup performance for large directories but introduce additional complexity. Collision handling must be robust, and the hash function should distribute entries uniformly to maintain performance. Modern file systems like NTFS and ext4 use B+tree structures rather than pure hash tables for directory indexing, but the underlying principle of indexed access remains similar.

### File Allocation Methods and Directory Integration

The directory structure must coordinate with the file allocation method used to store file data on disk. Three primary allocation methods exist:

**Contiguous Allocation:** Files occupy consecutive disk blocks. The directory entry simply stores the starting block address and file length. This enables fast sequential and random access but suffers from external fragmentation and difficulty in extending files.

**Linked Allocation:** Each file's blocks are scattered across the disk, with each block containing a pointer to the next block. Directory entries store only the first block pointer. This eliminates fragmentation but only supports sequential access efficiently.

**Indexed Allocation:** Uses an index block containing pointers to all file blocks. The directory entry stores the address of the index block. This supports both sequential and direct access efficiently but requires extra I/O to read the index block.

Unix-like systems use a variation called indexed allocation with an i-node structure. Each file has an i-node containing metadata and direct/indirect block pointers. The directory entry stores only the i-node number, enabling efficient stat operations without reading file data.

### Directory Operations

Operating systems provide several fundamental operations for directory management:

**Create:** Adds a new entry to a directory, initializing file attributes and allocation structures.

**Delete:** Removes a directory entry, releasing associated file blocks (in simple systems) or updating reference counts (in systems with sharing).

**Search:** Locates a file by name within a directory, returning its attributes or handle for subsequent operations.

**List:** Returns all entries in a directory, often with filtering options for pattern matching.

**Rename:** Changes a file's name within the same directory without affecting its contents or attributes.

**Link:** Creates additional directory entries pointing to an existing file (hard links in Unix).

**Unlink:** Removes a directory entry, decrementing the link count and potentially deleting the file if no links remain.

## Examples

### Example 1: Linear List Directory Search

Consider a directory implemented as a linear list containing 1000 files. Each entry requires 64 bytes. The directory starts at disk block 500, and each block is 4096 bytes.

**Scenario:** We need to locate the file "final_report.pdf" using linear search.

**Solution:**

Step 1: Calculate the number of entries per block: 4096 / 64 = 64 entries per block

Step 2: Determine which block contains our file (worst case - file not found until the end)

Step 3: Maximum disk reads required = ceil(1000 / 64) = 16 blocks

If the file is at position 750 in the list, we need:
- Block number = 500 + floor(750/64) = 500 + 11 = 511
- Entries to read = ceil(750/64) = 12 blocks
- Disk I/O operations: approximately 12

This demonstrates why linear lists become inefficient for large directories.

### Example 2: Hash Table Directory Implementation

Using the same 1000-file directory with a hash table using chaining for collision resolution:

**Hash Function:** Sum of ASCII values of characters modulo table size (say, 256 buckets)

**Scenario:** Inserting and searching for "project_code.c"

**Solution:**

Hash calculation for "project_code.c":
- ASCII sum = 112 + 114 + 111 + 106 + 101 + 99 + 95 + 99 + 111 + 100 + 101 + 46 + 99 = 1290
- Hash bucket = 1290 mod 256 = 66

**Insertion:**
- Compute hash (66)
- Add entry to bucket 66's chain
- If bucket already has entries, append to existing chain

**Search:**
- Compute hash (66)
- Access bucket 66 directly (1 disk I/O)
- Traverse chain (average 1000/256 ≈ 4 entries) to find exact match

**Performance comparison:**
- Linear search average: 8 block reads (500 entries)
- Hash table average: 1-2 block reads
- Improvement factor: 4-8x for this directory size

### Example 3: Tree-Structured Directory Navigation

Consider the Unix-style directory structure:

```
/ (root)
├── home/
│   ├── user1/
│   │   ├── documents/
│   │   │   ├── thesis.pdf
│   │   │   └── notes.txt
│   │   ├── pictures/
│   │   │   └── vacation.jpg
│   │   └── .bashrc
│   └── user2/
│       └── projects/
│           └── main.c
└── var/
    └── log/
        └── system.log
```

**Scenario:** Process A accesses /home/user1/documents/thesis.pdf while Process B modifies /home/user1/.bashrc

**Directory Implementation Analysis:**

Each directory entry contains:
- Inode number (4 bytes)
- Name length and name (variable)
- Record length

When Process A opens thesis.pdf:
1. Read root directory (inode 2) - locate "home"
2. Read /home directory - locate "user1"
3. Read /home/user1 directory - locate "documents"
4. Read /home/user1/documents directory - locate "thesis.pdf"
5. Read file's inode - validate permissions
6. Return file descriptor

This hierarchical traversal requires multiple disk I/O operations but provides clean organization and natural access control at each level.

## Exam Tips

1. **Understand Directory vs. File Allocation:** Remember that directory implementation (how we organize file metadata) is separate from file allocation (how we store file data blocks). Both work together in a complete file system.

2. **Know Time Complexities:** Linear list search is O(n), hash table average case is O(1), but worst case is O(n). Tree traversal is O(log n) for balanced trees and O(n) for degenerate cases.

3. **Distinguish Directory Structures:** Single-level, two-level, tree-structured, acyclic graph, and general graph—understand the hierarchical relationships and trade-offs of each.

4. **Hash Table Collisions:** Be prepared to explain collision resolution techniques (chaining versus open addressing) and their impact on performance.

5. **Directory Operations:** Memorize the six fundamental directory operations: create, delete, search, list, rename, and link/unlink.

6. **Symbolic vs. Hard Links:** Understand that symbolic links create new directory entries pointing to pathnames (can cross file systems), while hard links point directly to the same inode (cannot cross file systems, cannot link to directories).

7. **Real-World Examples:** Relate concepts to familiar systems—Windows uses tree-structured directories with drive letters; Unix/Linux uses single-root tree starting from "/" with symbolic links for sharing.

8. **Performance Implications:** Consider how directory implementation affects system responsiveness. Modern systems avoid pure linear lists for large directories, using B+trees or hash tables internally.