# File Organizations and Indexes - Summary

## Key Definitions and Concepts

- **File Organization**: Physical arrangement of records on storage media—determines how efficiently data can be accessed
- **Sequential File**: Records stored in order (sorted or insertion order); efficient for range queries but poor for random access
- **Direct (Hashed) File**: Uses hash function to compute record address; O(1) average case for point queries
- **Index**: Auxiliary structure providing pointers to data records; like a book's index
- **Primary Index**: Created on primary key; data physically sorted; sparse
- **Secondary Index**: Created on non-key fields; multiple allowed; typically dense
- **Clustering Index**: Data physically ordered by non-unique field; only one per table
- **B+ Tree**: Balanced tree index structure; all leaf nodes at same level; leaf nodes linked for range queries

## Important Formulas and Theorems

- **Sequential Search Cost**: Average = b/2 block transfers (where b = total blocks)
- **B+ Tree Height**: O(logₘ n) where m = order, n = number of keys
- **B+ Tree Order**: Each node has minimum ⌈m/2⌉ children except root

## Key Points

- File organization fundamentally affects database performance for CRUD operations
- Hash files provide constant-time access for equality searches but cannot handle range queries
- B+ Trees are the industry standard for indexing due to balanced height and efficient range queries
- Primary keys automatically get primary indexes in most database systems
- Composite indexes follow left-prefix rule—only queries using leftmost columns benefit
- Dense indexes require more storage but provide faster search than sparse indexes
- Clustered indexes physically reorder data; only one per table due to physical storage constraint

## Common Mistakes to Avoid

- Confusing clustering and non-clustering indexes—only one clustering index exists because data has one physical order
- Thinking B+ Trees store data at internal nodes—they only store keys at internal nodes, data at leaf nodes
- Forgetting that secondary indexes point to primary key values, not directly to records in some systems
- Assuming hash indexes support range queries—they only support equality operations

## Revision Tips

1. Practice B+ Tree insertion with different values to understand node splitting
2. For each file organization type, note one real-world scenario where it excels
3. Memorize the difference between dense and sparse with examples
4. Review cost formulas and practice block transfer calculations
5. Understand why B+ Trees are preferred over Binary Search Trees for disk-based storage (fewer disk accesses due to higher fan-out)