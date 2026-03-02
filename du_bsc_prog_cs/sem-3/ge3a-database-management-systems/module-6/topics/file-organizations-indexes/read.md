# File Organizations and Indexes

## Introduction

File organizations and indexes form the backbone of efficient database management systems, determining how data is physically stored, accessed, and retrieved. In real-world database applications, the difference between a well-designed file organization and a poor one can result in performance differences of several orders of magnitude. When you query a database to find a specific customer record among millions of records, the DBMS must locate that data efficiently—without scanning every single record. This is where file organizations and indexes become essential.

For University of Delhi's Computer Science students, understanding file organizations is crucial because database performance optimization is a critical skill in software development and data engineering. Modern applications from e-commerce platforms to banking systems rely heavily on proper indexing strategies. This topic covers the fundamental methods of organizing records in files, various indexing techniques including B+ Trees, and the trade-offs involved in choosing appropriate access methods. The concepts learned here directly apply to real-world scenarios like optimizing query performance in MySQL, PostgreSQL, or Oracle databases.

## Key Concepts

### File Organizations

**File organization** refers to the way records are physically arranged on storage media (typically磁盘). The choice of file organization significantly impacts database performance for different types of operations—searching, insertion, deletion, and range queries.

**Sequential File Organization**: Records are stored in a sequential order, either sorted by a primary key or in the order of insertion. This organization excels at range queries and sequential access but suffers from poor random access performance. For example, finding a record in the middle requires scanning from the beginning. Insertions at random positions require shifting records, making this expensive. However, sequential files work excellently with magnetic tapes and are ideal for batch processing where entire files need to be processed.

**Direct (Hashed) File Organization**: Records are stored at addresses calculated using a hash function applied to a key field. This provides constant-time O(1) average case access for point queries. The hash function distributes records across buckets, and collisions (multiple records mapping to the same bucket) are handled through chaining or open addressing. For instance, if we have a customer database and use customer_id % 100 as our hash function, a customer with ID 2045 would be stored in bucket 45. This method is ideal for applications performing primarily point queries on equality conditions.

**Indexed File Organization**: An index is a auxiliary data structure that provides a pointer to the actual data records. Think of it like the index at the back of a book—it doesn't contain the content but tells you exactly where to find what you're looking for. The indexed file organization maintains the data file separate from the index file, allowing multiple indexes on different fields.

### Types of Indexes

**Primary Index**: Created on a primary key field. The primary key must be unique, and records in the data file are physically ordered (sorted) by this key. A primary index provides efficient access to specific records and maintains the uniqueness constraint. Since data is physically sorted, range queries become very efficient.

**Clustering Index**: Used when records are physically ordered by a non-unique field that groups related records together. For example, if employees are stored in order of their department, a clustering index on the department field would group all employees from the same department together. A table can have only one clustering index because data can be physically stored in only one order.

**Secondary Index**: Created on non-key fields or fields that don't determine physical order. A table can have multiple secondary indexes. Since the indexed field isn't unique, the index typically stores key-pointer pairs where each key value has a list of pointers to all matching records. Secondary indexes provide flexibility in querying but require additional storage space.

**Dense vs Sparse Index**: In a dense index, an index entry exists for every record in the data file. This provides faster searching but requires more index storage. In a sparse index, index entries exist only for some records (typically every nth record), requiring less storage but potentially slower search as we may need to scan data blocks. Primary indexes are typically sparse (since data is sorted), while secondary indexes are typically dense.

### B+ Tree Index Structure

The B+ Tree is the most widely used index structure in modern database systems. It is a balanced tree structure that maintains sorted data and allows efficient insertion, deletion, and search operations.

**Properties of B+ Tree**:
- It is a tree of order m, where each node can have at most m children and at least ⌈m/2⌉ children (except the root)
- All key values in the tree are stored in sorted order
- All leaf nodes are at the same level (height-balanced)
- Leaf nodes contain all key values and pointers to actual data records (or data blocks)
- Non-leaf nodes contain only key values and child pointers (not actual data)
- Leaf nodes are linked together in a linked list for efficient range queries

**B+ Tree of Order 3** (minimum 2 keys per node, maximum 3 pointers):
```
        [20]
       /    \
   [10,15]  [30,40]
   /   |   \   |   \
->5->10->15->20->30->40-> (leaf nodes linked)
```

The height of a B+ Tree with n keys is O(logₘ n), making search very efficient even for millions of records. For a tree of order 100 with a height of 3, we can index approximately 1 million records by following just 3 pointers from root to leaf.

### Indexing in Practice

**Composite Indexes**: Indexes created on multiple columns. In database systems like MySQL, a composite index on (city, name) can efficiently support queries filtering on both fields or just the first field, but cannot efficiently support queries filtering only on the name field due to left-prefix rule.

**Unique Index**: Automatically enforces uniqueness constraint on the indexed field, preventing duplicate values.

**Bitmap Index**: Uses bit arrays (bitmaps) to index low-cardinality fields. Excellent for analytical queries on categorical data. For example, a gender field with values 'M' and 'F' would have two bitmaps—one for 'M' (1 where gender is Male, 0 otherwise) and one for 'F'.

## Examples

### Example 1: Calculating Block Transfers for Sequential Search

**Problem**: A file contains 10,000 records, and each block (page) holds 20 records. Calculate the average number of block transfers needed to find a record using sequential search, assuming the record is equally likely to be anywhere in the file.

**Solution**:

- Total records = 10,000
- Records per block = 20
- Total blocks = 10,000 / 20 = 500 blocks
- Average case: We may need to search half the file = 500 / 2 = 250 blocks
- Therefore, average block transfers = 250

**Worst case**: 500 block transfers (record is at the end)

**Best case**: 1 block transfer (record is in first block)

### Example 2: B+ Tree Insertion

**Problem**: Insert the key 25 into a B+ Tree of order 3 (minimum 2 keys per node, maximum 2 keys).

Initial tree:
```
        [20]
       /    \
   [10,15]  [30]
```

**Solution**:

1. Start at root, compare 25 > 20, go to right subtree
2. In node [30], 25 < 30, insert 25 in order: [25,30]
3. Since maximum is 2 keys, node is full
4. Split: [25] stays, 30 moves up, 25 becomes new root
5. Final tree:
```
    [25]
   /    \
[10,15]  [20,30]
```

### Example 3: Hash File Organization

**Problem**: Using simple hashing with 7 buckets (bucket = hash value % 7), show where each of these employee IDs would be stored: 10, 15, 22, 28, 35, 42.

**Solution**:

Hash function: h(employee_id) = employee_id % 7

- 10 % 7 = 3 → Bucket 3
- 15 % 7 = 1 → Bucket 1
- 22 % 7 = 1 → Bucket 1 (collision with 15)
- 28 % 7 = 0 → Bucket 0
- 35 % 7 = 0 → Bucket 0 (collision with 28)
- 42 % 7 = 0 → Bucket 0 (collision with 28, 35)

Final distribution:
- Bucket 0: 28 → 35 → 42 (chaining)
- Bucket 1: 15 → 22 (chaining)
- Bucket 2: (empty)
- Bucket 3: 10
- Bucket 4, 5, 6: (empty)

## Exam Tips

1. **Understand when to use each file organization**: Sequential is best for range queries and batch processing; Hashed is best for point queries on equality conditions; Indexed is most versatile for mixed workloads.

2. **Remember the difference between dense and sparse indexes**: Dense index has entry for every record; Sparse index has entries for some records. Primary indexes are typically sparse.

3. **B+ Trees are the most important**: Expect questions on B+ Tree insertion, deletion, and search operations. Know that all leaf nodes are at the same level and are linked.

4. **Clustered vs Non-clustered**: A table can have only one clustered index (determines physical storage order) but multiple non-clustered indexes.

5. **Index selection strategy**: For exam questions, analyze the query patterns—equality conditions benefit from hash indexes, range conditions benefit from B+ Tree indexes.

6. **Cost calculation formulas**: Remember that I/O cost (block transfers) is the primary metric. Sequential scan cost = b/2 average, where b is number of blocks.

7. **Trade-offs matter**: Every indexing strategy has pros and cons. Questions often ask you to recommend the best approach given specific access patterns—always justify your answer.