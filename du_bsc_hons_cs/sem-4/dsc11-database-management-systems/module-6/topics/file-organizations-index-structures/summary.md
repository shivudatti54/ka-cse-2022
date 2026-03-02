# File Organizations and Index Structures - Summary

## Key Definitions and Concepts

- **File Organization**: The way records are physically arranged on storage media (disk)
- **Record Blocking**: Packing records into fixed-size blocks for efficient disk I/O
- **Sequential File**: Records stored in sorted order on a search key; efficient for range queries
- **Heap File**: Unordered file organization; fastest for insertions but slow for searches
- **Hash File**: Uses hash function to compute bucket address; efficient for equality searches
- **Clustered File**: Records of different relations stored together based on clustering key
- **Index**: Auxiliary data structure providing fast access paths to records
- **Primary Index**: Built on primary key, sparse, data file is physically ordered
- **Secondary Index**: Built on non-primary attributes, always dense
- **B+ Tree**: Height-balanced tree index with all data at leaf level
- **Bitmap Index**: Uses bit vectors for low-cardinality attributes

## Important Formulas and Theorems

- **B+ Tree Capacity**: Maximum keys at height h = m^h - 1 (approximately)
- **Minimum keys**: ⌈m/2⌉ - 1 keys per non-root node
- **Block accesses for primary index point query**: log₂(b) + 1 (where b = number of index blocks)
- **Sequential scan**: b block accesses (b = number of data blocks)
- **Hash index point query**: 1 bucket access (average case)
- **Sparse vs Dense**: Sparse = 1 index entry per block; Dense = 1 index entry per record

## Key Points

- Sequential organization suits range queries but has high insertion/deletion costs
- Heap files are optimal when insertions are frequent and searches are rare
- Hash organization provides O(1) average access for point queries but cannot handle range queries efficiently
- Primary indexes are sparse and require sorted data files; secondary indexes are always dense
- B+ Trees are preferred over B-Trees because all data is at leaf level and leaf nodes are linked
- Multi-level indexing (like B+ Trees) keeps top levels in memory for faster access
- Bitmap indexes excel for low-cardinality attributes and complex boolean queries using bitwise operations
- Clustering determines how related data is physically stored; affects JOIN performance significantly

## Common Mistakes to Avoid

- Confusing primary and secondary indexes—secondary indexes are always dense, not sparse
- Thinking B-Trees and B+ Trees are the same—B+ Trees have all data at leaf level
- Using hash indexes for range queries—they perform poorly
- Forgetting that index maintenance (updates) has overhead
- Underestimating the space cost of secondary indexes
- Confusing clustered indexes with clustering file organization—these are different concepts
- Assuming bitmap indexes work well for high-cardinality attributes

## Revision Tips

1. Practice drawing and analyzing B+ Trees with different orders and operations
2. Memorize the formulas for calculating B+ Tree capacity and block accesses
3. Create a comparison table of all file organizations and their use cases
4. Work through numerical problems from previous year DU question papers
5. Understand the relationship between index type (sparse/dense, primary/secondary) and query performance
6. Review how different index structures behave with insertions and deletions
7. Focus on understanding when to use each type—exams often ask you to recommend an organization for a given scenario