# Index Structures: B-Trees & Hash

## Introduction
Modern database systems rely heavily on efficient index structures to accelerate data retrieval operations. B-Trees and Hash-based indexes form the backbone of most contemporary storage engines, enabling O(log n) and O(1) access times respectively. With the exponential growth of data in applications ranging from financial transaction systems to genomic databases, understanding these fundamental structures is critical for database architects and system developers.

The B-Tree family (including B+ Trees and B* Trees) remains the gold standard for disk-based storage systems due to their ability to minimize I/O operations through careful node sizing that matches disk block sizes. Hash indexes, particularly extendible and linear hashing variants, dominate in memory-resident databases and equality search scenarios. Recent research directions like learned indexes and hybrid structures (e.g., LSM-trees with B-Tree components) build upon these classical foundations.

## Key Concepts
1. **B-Tree Properties**:
   - Balanced m-way search tree (typically order 100-1000)
   - All leaves at same depth
   - Minimum occupancy guarantee (⌈m/2⌉ - 1 keys except root)
   - Node structure: [n, K₁, P₁, K₂, P₂,..., Kₙ, Pₙ₊₁]

2. **B+ Tree Variants**:
   - Data only in leaf nodes
   - Linked leaves for range queries
   - Higher fanout compared to classic B-Trees

3. **Dynamic Hashing Techniques**:
   - Extendible Hashing: Directory-based approach with bucket splitting
   - Linear Hashing: Progressive bucket splitting without directory
   - Collision resolution: Separate chaining vs open addressing

4. **Cost Analysis**:
   - B-Tree height: h ≈ log_{m/2}(N) for N records
   - Hash index probe cost: 1 disk access (ideal), 2-3 with overflows
   - Insertion cost for B-Trees: O(h) read + O(h) write

5. **Modern Adaptations**:
   - Flash-optimized B+-Trees (log-structured leaf nodes)
   - Concurrent access patterns (B-link trees)
   - Learned indexes using ML models for position prediction

## Examples

**Example 1: B-Tree Insertion**
Problem: Insert sequence [20, 40, 60, 80, 70] into empty B-Tree (order m=3)

Solution:
1. Insert 20,40 → Root: [20,40]
2. Insert 60 → Split root:
   New root: [40]
   Children: [20], [60]
3. Insert 80 → Right child becomes [60,80]
4. Insert 70 → Split right child:
   Root: [40,70]
   Children: [20], [60], [80]
   (Final tree height 2)

**Example 2: Extendible Hashing**
Problem: Store keys {5,7,15,18} using extendible hashing (hash function: key mod 8)

Solution:
1. Initial directory depth=1:
   - Bucket 0-7: [5,7] (local depth=1)
2. Insert 15 (15 mod 8=7):
   - Split bucket 7, increase directory depth=2
   - New buckets: 7 (local depth=1) and 15 (local depth=2)
3. Directory now has 2 entries pointing to each split bucket

## Exam Tips
1. Always mention the disk I/O implications when comparing B-Trees vs Hashing
2. For insertion algorithms, track node splits and height changes systematically
3. Remember B+ Trees require leaf node traversal for range queries
4. Hash indexes cannot efficiently support range queries - this is a favorite exam question
5. When calculating B-Tree height, use ⌈log_{⌈m/2⌉}(N)⌉ rather than base 2
6. Recent question trends include hybrid indexes (e.g., LSM-Trees with B-Tree components)
7. Always specify whether discussing static or dynamic hashing variants

Length: 2500 words, MSc CS (research-oriented) postgraduate level