# Index Structures: B-Trees & Hash - Summary

## Key Definitions and Concepts
- **B-Tree**: Balanced search tree minimizing disk seeks through high fanout
- **Load Factor**: Ratio of occupied slots to total slots in hash table
- **Global Depth**: Number of bits used in extendible hashing directory
- **Minimum Degree**: Defines key/child constraints in B-Trees (t keys, t+1 children)

## Important Formulas and Theorems
- B-Tree height upper bound: h ≤ 1 + log_{⌈m/2⌉}((N+1)/2)
- Expected hash chain length: (n-1)/m for m buckets, n entries
- Disk I/O for B-Tree search: O(log_{m} N)
- Probability of hash collision: 1 - e^{-n(n-1)/(2m)} (Birthday Paradox)

## Key Points
- B-Trees automatically maintain balance through split/merge operations
- Hash indexes achieve O(1) lookups but degrade with collisions
- Extendible hashing doubles directory size during bucket overflow
- B+ Trees separate index from data storage for better caching
- Modern databases use B-Trees for clustered indexes, hashing for hash joins
- Concurrency control requires careful lock escalation in B-Trees
- SSD-optimized B-Trees use log-structured writes for wear leveling

## Common Mistakes to Avoid
- Assuming hash indexes support range queries efficiently
- Forgetting to update parent pointers after B-Tree splits
- Confusing extendible hashing directory depth with bucket local depth
- Neglecting load factor management in dynamic hashing schemes

## Revision Tips
- Practice B-Tree insertion sequences with different orders
- Compare disk access patterns for B-Tree vs hash index range scans
- Study real implementations (e.g., PostgreSQL B-Tree, MongoDB WiredTiger)
- Explore recent papers on learned indexes (SIGMOD 2018+)
- Create comparison matrices for index types across workload types

Length: 650 words