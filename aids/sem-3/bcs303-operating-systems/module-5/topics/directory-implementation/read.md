# Directory Implementation


## Table of Contents

- [Directory Implementation](#directory-implementation)
- [Introduction](#introduction)
- [Linear List Implementation](#linear-list-implementation)
  - [Operations](#operations)
  - [Advantages](#advantages)
  - [Disadvantages](#disadvantages)
  - [Improvements](#improvements)
- [Hash Table Implementation](#hash-table-implementation)
  - [How It Works](#how-it-works)
  - [Operations](#operations)
  - [Advantages](#advantages)
  - [Disadvantages](#disadvantages)
  - [Handling the Fixed-Size Problem](#handling-the-fixed-size-problem)
- [Comparison: Linear List vs Hash Table](#comparison-linear-list-vs-hash-table)
- [Real-World Directory Implementations](#real-world-directory-implementations)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

A directory is a special file that contains information about other files — primarily a mapping from **file names** to **file metadata** (or pointers to metadata). The OS must implement this mapping efficiently because directory operations (searching for a file, creating a file, listing files) are performed very frequently.

The two main data structures used to implement directories are **linear lists** and **hash tables**. This topic corresponds to **Section 12.4** of Silberschatz (Operating System Concepts).

## Linear List Implementation

The simplest method: store the directory as a **linear list** of file names with pointers to their data blocks (or inodes/FCBs).

```
Directory as Linear List:

+------------------+------------------+
| File Name | Pointer to FCB |
+------------------+------------------+
| report.txt | → inode 42 |
| main.c | → inode 17 |
| data.csv | → inode 88 |
| image.png | → inode 53 |
| notes.md | → inode 29 |
+------------------+------------------+
```

### Operations

| Operation  | How It Works                                                   | Time Complexity |
| :--------- | :------------------------------------------------------------- | :-------------- |
| **Search** | Scan the list sequentially until file name is found            | O(n)            |
| **Create** | Search list to ensure no duplicate name, then add entry at end | O(n) for search |
| **Delete** | Search for the entry, then remove it (or mark as unused)       | O(n)            |
| **List**   | Read all entries sequentially                                  | O(n)            |

### Advantages

- Simple to program and implement
- No complex data structures needed

### Disadvantages

- **Slow search** — must perform linear search for every file operation
- For directories with many files (thousands), this becomes very slow
- Deleting a file can leave gaps in the list (either compact the list or mark entries as unused and reuse later)

### Improvements

- **Sorted list** — Allows binary search, reducing search time to O(log n). But insertion and deletion become more expensive because entries must be kept in sorted order.
- **B-tree** — Balanced tree structure for faster search, insert, and delete. Used by some modern file systems.

## Hash Table Implementation

A **hash table** provides much faster search than a linear list. The directory is implemented as a hash table where the file name is hashed to produce an index into the table.

```
Hash Table Directory:

File name → hash function → index

hash("report.txt") = 3
hash("main.c") = 7
hash("data.csv") = 3 (collision with report.txt!)

Hash Table:
+-------+-------------------+
| Index | Entry |
+-------+-------------------+
| 0 | (empty) |
| 1 | (empty) |
| 2 | (empty) |
| 3 | report.txt → 42 --+--> data.csv → 88 → NULL
| 4 | (empty) |
| 5 | (empty) |
| 6 | (empty) |
| 7 | main.c → 17 |
+-------+-------------------+
```

### How It Works

1. To find a file: compute `hash(filename)` → get index → search the linked list at that index
2. Collisions (two names hashing to the same index) are handled by **chaining** (linked lists at each slot)

### Operations

| Operation  | Average Time | Worst Case                          |
| :--------- | :----------- | :---------------------------------- |
| **Search** | O(1)         | O(n) if all names hash to same slot |
| **Create** | O(1)         | O(n) for collision chain            |
| **Delete** | O(1)         | O(n) for collision chain            |

### Advantages

- **Much faster search** — O(1) average case instead of O(n)
- Greatly improves file system performance for directories with many files

### Disadvantages

- **Fixed size** — The hash table has a fixed number of slots determined at creation time. If the directory grows beyond expectations, the hash function may need to change (rehashing), which is expensive.
- **Collisions** — Poor hash functions or unlucky data can cause many collisions, degrading performance
- More complex to implement than a linear list

### Handling the Fixed-Size Problem

Solutions to the fixed-size limitation:

- **Chained overflow** — Each hash slot points to a linked list of entries (most common approach)
- **Extendible hashing** — The hash table can grow dynamically by splitting buckets when they overflow
- **Rehashing** — Create a larger table and reinsert all entries with a new hash function (expensive but rare)

## Comparison: Linear List vs Hash Table

| Aspect             | Linear List                       | Hash Table                              |
| :----------------- | :-------------------------------- | :-------------------------------------- |
| **Search time**    | O(n) — slow for large directories | O(1) average — fast                     |
| **Implementation** | Simple                            | More complex                            |
| **Space overhead** | Minimal                           | Hash table structure + collision chains |
| **Insert**         | O(n) for duplicate check          | O(1) average                            |
| **Delete**         | O(n) for search                   | O(1) average                            |
| **Best for**       | Small directories                 | Large directories with many files       |
| **Used by**        | Simple file systems               | Most modern file systems                |

## Real-World Directory Implementations

| File System           | Directory Structure                                    |
| :-------------------- | :----------------------------------------------------- |
| **FAT (MS-DOS)**      | Linear list of 32-byte directory entries               |
| **ext2/ext3 (Linux)** | Linked list of variable-length directory entries       |
| **ext4 (Linux)**      | Hash tree (HTree) — B-tree indexed by hash of filename |
| **NTFS (Windows)**    | B+ tree (within the MFT)                               |
| **HFS+ (macOS)**      | B-tree catalog file                                    |

Most modern file systems use **tree-based** structures (B-trees or hash trees) that combine the simplicity of sorted lists with the speed of hash tables.

## Summary

| Concept        | Key Point                                                           |
| :------------- | :------------------------------------------------------------------ |
| Linear list    | Simple but slow — O(n) search                                       |
| Hash table     | Fast — O(1) average search, but fixed size and collision issues     |
| Collisions     | Handled by chaining (linked lists at each slot)                     |
| Best approach  | Hash table for large directories, linear list for simple/small ones |
| Modern systems | Use B-trees or hash trees for best performance                      |

## Exam Tips

1. **Linear list vs hash table** — This is the core exam question for this topic (5-10 marks). Use a comparison table and mention time complexity for each operation.
2. **Hash table collision handling** — Explain chaining with a diagram. Show what happens when two file names hash to the same index.
3. **Time complexities** — Know that linear list is O(n) for all operations, hash table is O(1) average but O(n) worst case.
4. **Fixed-size problem** — Mention that hash tables have a fixed size and explain solutions (chained overflow, extendible hashing).
5. **Real-world examples** — Mentioning that ext4 uses HTree and NTFS uses B+ trees shows depth of understanding.
6. **Sorted list optimization** — If asked about improving linear list, mention sorting + binary search as an intermediate solution.
