# File System Implementation

## Introduction to File System Implementation

File system implementation refers to the methods and data structures that an operating system uses to organize, store, and retrieve files on storage devices. While users interact with files through logical concepts like filenames and directories, the operating system must translate these into physical storage operations on disks or other storage media.

The implementation involves several key components:

- **File system structure**: How data is organized on the storage device
- **Allocation methods**: How disk space is assigned to files
- **Free space management**: How available space is tracked
- **Directory implementation**: How file information is organized
- **Efficiency and performance**: Techniques to optimize file operations

## File System Structure

A file system is typically organized into multiple layers:

```
+-----------------------+
| Logical File System | (File operations, directory management)
+-----------------------+
| File Organization | (Logical blocks, protection)
+-----------------------+
| Basic File System | (Block I/O, buffering)
+-----------------------+
| I/O Control | (Device drivers, interrupts)
+-----------------------+
| Physical Devices | (Disks, SSDs, storage media)
+-----------------------+
```

Most storage devices are divided into fixed-size **blocks** (typically 512 bytes to 4KB). The file system manages these blocks to store file data and metadata.

A typical disk layout includes:

- **Boot block**: Contains bootstrap code
- **Superblock**: Contains file system information (size, type, free block count)
- **Free space management**: Data structures to track available blocks
- **i-nodes or similar**: Metadata about files
- **Root directory**: Starting point of directory hierarchy
- **Data blocks**: Where file contents are stored

## File Allocation Methods

### 1. Contiguous Allocation

Each file occupies a set of contiguous blocks on the disk. The directory entry contains the starting block address and the number of blocks.

**Example:**

```
File A: blocks 3-7 (5 blocks)
File B: blocks 8-12 (5 blocks)
File C: blocks 13-17 (5 blocks)
```

**Advantages:**

- Simple to implement
- Fast sequential access
- Minimal seek time for sequential reads

**Disadvantages:**

- External fragmentation (free space becomes broken into small pieces)
- Difficult to grow files
- Need to know file size in advance

```
Disk Map with Contiguous Allocation:
+----+----+----+----+----+----+----+----+----+----+----+----+
| A | A | A | A | A | B | B | B | B | B | C | C |
+----+----+----+----+----+----+----+----+----+----+----+----+
| C | C | C | | | | | | | | | |
+----+----+----+----+----+----+----+----+----+----+----+----+
```

### 2. Linked Allocation

Each file is a linked list of disk blocks. Each block contains a pointer to the next block. The directory entry contains a pointer to the first and last blocks.

**Example:**

```
File A: block 3 → block 7 → block 12 → block 15 (end)
```

**Advantages:**

- No external fragmentation
- Files can grow easily
- Efficient for sequential access

**Disadvantages:**

- Poor random access performance
- Space overhead for pointers
- Reliability issues (broken chain if pointer is corrupted)

```
Linked Allocation Example:
+----+----+----+----+----+----+----+----+----+----+----+----+
| A | | A | | | | A | | | | A | |
|(3) | |(7) | | | |(12)| | | |(15)| |
+----+----+----+----+----+----+----+----+----+----+----+----+
| | | | | | | | | | | | |
+----+----+----+----+----+----+----+----+----+----+----+----+
Pointers: Block 3 → 7, Block 7 → 12, Block 12 → 15, Block 15 → EOF
```

### 3. Indexed Allocation

All pointers for each file are collected in a separate index block. The directory entry contains the address of the index block.

**Example:**

```
File A index block (block 5):
+---+---+---+---+
| 3 | 7 |12 |15 |
+---+---+---+---+

File data stored at blocks 3, 7, 12, 15
```

**Advantages:**

- Supports direct access
- No external fragmentation
- Files can grow easily

**Disadvantages:**

- Overhead of index block storage
- Index block size limits maximum file size

**Variations:**

- **Linked scheme**: Index blocks linked together for large files
- **Multilevel index**: Hierarchical index structure (used in UNIX i-nodes)
- **Combined scheme**: Direct, single indirect, double indirect pointers

## Free Space Management

The file system must track which blocks are free for allocation. Common methods include:

### 1. Bit Vector (Bitmask)

Each block is represented by a bit. 0 = free, 1 = allocated.

**Example:** For 16 blocks: `0010111001101011` (blocks 3,5,6,7,10,12,14,16 are allocated)

**Advantages:**

- Simple and efficient
- Easy to find contiguous free blocks

**Disadvantages:**

- The entire bit vector must be in memory for efficiency

### 2. Linked List

Free blocks are linked together via pointers. The OS maintains a pointer to the first free block.

**Advantages:**

- No wasted space for free space management
- Simple implementation

**Disadvantages:**

- Poor performance when allocating multiple blocks
- Not efficient for finding contiguous space

### 3. Grouping

Stores addresses of free blocks in free blocks. One block contains pointers to other free blocks.

**Advantages:**

- Faster than simple linked list
- Can find multiple free blocks quickly

### 4. Counting

Stores ranges of contiguous free blocks (first block, count).

**Advantages:**

- Efficient for systems with large contiguous free areas
- Compact representation

## Directory Implementation

Directories map filenames to file metadata. Implementation approaches:

### 1. Linear List

Simple list of entries with filename and pointer to file metadata.

**Advantages:**

- Simple to program
- Easy to understand

**Disadvantages:**

- Slow search time (O(n))
- Sorting required for alphabetical listing

### 2. Hash Table

Uses hash function on filename to locate directory entry quickly.

**Advantages:**

- Fast lookup (O(1) average case)
- No sorting needed

**Disadvantages:**

- Hash collisions must be handled
- Fixed size or need for rehashing

## Efficiency and Performance

### Disk Caching

The OS maintains a **buffer cache** or **page cache** in memory to store frequently accessed disk blocks.

**Replacement algorithms** (similar to page replacement):

- First-In-First-Out (FIFO)
- Least Recently Used (LRU)
- Clock algorithm

### Other Optimization Techniques

- **Read-ahead**: Prefetch blocks likely to be accessed soon
- **Delayed writes**: Write modifications to cache first, then to disk later
- **Synchronous vs asynchronous writes**: Trade-off between performance and data integrity

## Journaling File Systems

Modern file systems (ext3/4, NTFS) use journaling to improve reliability. Before making changes to the file system, the intended operations are written to a **journal** (log).

**Process:**

1. Write transaction to journal
2. Perform actual file system operations
3. Mark transaction as complete in journal

**Benefits:**

- Faster recovery after crashes
- Reduced risk of file system corruption

## Example: UNIX File System (Based on i-nodes)

UNIX systems use indexed allocation with i-nodes. Each i-node contains:

- File metadata (permissions, timestamps, size)
- Pointers to data blocks:
- 12 direct pointers
- 1 single indirect pointer (points to block of pointers)
- 1 double indirect pointer
- 1 triple indirect pointer

```
UNIX i-node Structure:
+----------------+
| Metadata |
+----------------+
| Direct ptr 0 | → Data block
| Direct ptr 1 | → Data block
| ... | → ...
| Direct ptr 11 | → Data block
+----------------+
| Single indirect| → Pointer block → Data blocks
+----------------+
| Double indirect| → Pointer block → Pointer blocks → Data blocks
+----------------+
| Triple indirect| → Pointer block → Pointer blocks → Pointer blocks → Data blocks
+----------------+
```

This structure supports very large files while minimizing overhead for small files.

## Comparison of Allocation Methods

| Method     | Sequential Access | Random Access | Fragmentation   | File Growth | Overhead |
| ---------- | ----------------- | ------------- | --------------- | ----------- | -------- |
| Contiguous | Excellent         | Good          | High (external) | Difficult   | Low      |
| Linked     | Good              | Poor          | None            | Easy        | Moderate |
| Indexed    | Good              | Excellent     | None            | Easy        | High     |

## Exam Tips

1. **Understand the trade-offs** between different allocation methods - be prepared to compare them in terms of performance, fragmentation, and implementation complexity.

2. **Know the i-node structure** in detail - this is a common exam topic, including calculating maximum file size given block size and pointer size.

3. **Free space management techniques** - be able to explain each method and when it would be most appropriate.

4. **Journaling concept** - understand why it's important and how it improves reliability compared to traditional file systems.

5. **Practice calculations** - especially for indexed allocation schemes where you need to determine maximum file size based on block size, pointer size, and levels of indirection.

6. **Relate to virtual memory** - some concepts like caching and replacement algorithms connect file systems with virtual memory topics from the same module.
