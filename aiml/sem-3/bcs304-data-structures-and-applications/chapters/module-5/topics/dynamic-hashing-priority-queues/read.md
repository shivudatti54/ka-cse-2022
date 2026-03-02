# Dynamic Hashing & Priority Queues

## 1. Introduction

In the study of Data Structures, efficient data organization and retrieval are paramount. This module explores two fundamental concepts: **Dynamic Hashing**, a technique that allows a hash table to grow and shrink dynamically to handle varying amounts of data efficiently, and **Priority Queues**, an abstract data type where each element has a "priority" and elements are served based on this priority rather than the order of insertion. Mastering these concepts is crucial for designing high-performance systems, from database indexing to task scheduling in operating systems.

## 2. Core Concepts

### Dynamic Hashing (Extendible Hashing)

Standard hashing techniques often use a fixed-size table, which can lead to performance degradation due to collisions. Dynamic hashing solves this by allowing the hash table to grow and shrink on demand. One prominent method is **Extendible Hashing**.

It uses a **directory** (an array of pointers) and **buckets** (data blocks). The directory expands and contracts dynamically. The core components are:

*   **Directory:** An array of pointers to buckets. The directory has a **global depth (gd)**.
*   **Buckets:** Where the actual (key, value) pairs are stored. Each bucket has a **local depth (ld)**.
*   **Hash Function:** `h(k)` produces a bit string. The last `gd` bits of this string are used to find the appropriate directory index.

**How it works:**
1.  **Insertion:** Compute `h(k)` and use the last `gd` bits to find the directory index, which points to a bucket.
2.  **Bucket Overflow:** If the target bucket is full, it is split.
    *   If the bucket's `ld` is less than the `gd`, only that bucket is split. Its `ld` is incremented, and its entries are redistributed based on the new `ld`. The directory now has two pointers pointing to the two new buckets.
    *   If the bucket's `ld` equals the `gd`, the directory must be doubled in size. The `gd` is incremented by 1. The directory is rebuilt, and *then* the overflowing bucket is split.

**Example:**
Let's start with `gd=1` and a directory of size 2 (`[0, 1]`), both pointing to a single bucket with `ld=1`.
*   Insert keys `3 (binary 11)` and `5 (binary 101)`. Both end in `1`, so they go to the bucket at index `1`.
*   Now, insert `7 (binary 111)`. The bucket overflows. Since `ld (1) == gd (1)`, we double the directory. New `gd=2`. The directory is now `[00, 01, 10, 11]`.
*   The old bucket (with `ld=1`) is split. Its entries (`3, 5, 7`) are rehashed using the last 2 bits (`11` for 3 and 7, `01` for 5). The directory at indices `01` and `11` now point to two new buckets.

### Priority Queues

A Priority Queue is an Abstract Data Type (ADT) that operates like a regular queue or stack, but where each element has an associated **priority**. The fundamental rule is: **the element with the highest (or lowest) priority is always the next to be removed.**

*   **Operations:**
    *   `insert(element, priority)`: Adds an element with its priority.
    *   `getHighest()` or `getLowest()`: Returns the element with the highest/lowest priority without removing it.
    *   `deleteHighest()` or `deleteLowest()`: Removes and returns the element with the highest/lowest priority.

**Implementation:**
While a simple linked list or array can be used (with O(n) insertion or deletion time), the efficient implementation is a **Binary Heap**.

*   **Binary Heap:** A complete binary tree that satisfies the **Heap Property**.
    *   **Max-Heap:** The value of any node is **greater than or equal to** the values of its children. The largest element is at the root.
    *   **Min-Heap:** The value of any node is **less than or equal to** the values of its children. The smallest element is at the root.

**Example - Insertion into a Max-Heap:**
1.  Insert the new element at the first available leaf position (to maintain the complete tree property).
2.  **Heapify-Up:** Compare the inserted element with its parent. If it violates the heap property (i.e., it's larger than its parent), swap them.
3.  Continue this process up the tree until the heap property is restored.

**Example - Deletion (extracting the max) from a Max-Heap:**
1.  Remove the root element (the max).
2.  Move the last element in the heap to the root.
3.  **Heapify-Down:** Compare this new root with its children. If it violates the heap property (i.e., it's smaller than one of its children), swap it with the larger child.
4.  Continue this process down the tree until the heap property is restored.

The `insert` and `delete` operations in a binary heap have a time complexity of **O(log n)**, making them highly efficient.

## 3. Key Points & Summary

| Feature | Dynamic Hashing (Extendible) | Priority Queue (Heap-based) |
| :--- | :--- | :--- |
| **Primary Goal** | Dynamic data storage with efficient, predictable access (O(1) average). | Efficient access to the highest/lowest priority element. |
| **Key Advantage** | Adapts to data growth/shrinkage without massive rehashing. Performs well. | Efficient O(log n) insertion and deletion of the max/min element. |
| **Core Operations** | Insert, Search, Delete | Insert, getMax/getMin, deleteMax/deleteMin |
| **Time Complexity** | **Insert/Search/Delete:** Nearly O(1) on average. | **Insert/Delete:** O(log n), **getMax/getMin:** O(1) |
| **Common Applications** | Database systems, file systems, compiler symbol tables. | Job scheduling (OS), Dijkstra's algorithm, Huffman coding, event-driven simulation. |

**Summary:**
*   **Dynamic Hashing** provides a scalable solution for maintaining efficient access times in a hash table as the dataset size changes, crucial for large-scale database applications.
*   **Priority Queues**, especially when implemented with a Binary Heap, provide an optimal structure for scenarios where processing order is determined by priority rather than chronology, forming the backbone of many critical algorithms and systems.