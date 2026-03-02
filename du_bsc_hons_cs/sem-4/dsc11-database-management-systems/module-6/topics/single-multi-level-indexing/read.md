# Single and Multi-Level Indexing in Database Management Systems

## Introduction

Indexing is a fundamental concept in database management systems that significantly improves the speed of data retrieval operations. In real-world applications, databases can contain millions of records, and without proper indexing, searching for specific records would require scanning the entire database—a process known as full table scan that is computationally expensive and time-consuming. Indexing provides a solution by creating auxiliary data structures that allow the database engine to locate desired records quickly, much like the index at the back of a book helps you find specific topics without reading every page.

In the context of University of Delhi's Computer Science curriculum, understanding indexing is crucial because it bridges the gap between theoretical database concepts and practical database optimization skills. This topic covers both single-level indexing (including primary, secondary, and clustering indexes) and multi-level indexing (with a focus on B-trees and B+ trees). These concepts are essential for database administrators and software developers who need to design efficient database schemas and write optimized queries.

The importance of indexing extends beyond academic requirements—major technology companies like Google, Amazon, and Oracle heavily invest in indexing research to optimize their massive databases. Understanding how indexes work internally will help you make informed decisions about database design, which is a valuable skill in today's data-driven world.

## Key Concepts

### 1. Need for Indexing

In a database table without indexes, when you execute a SELECT query with a WHERE clause, the database管理系统 must perform a linear search, examining every row until it finds the matching records. For a table with 1 million records, this could mean reading all 1 million rows, resulting in poor performance. Indexes solve this problem by creating a sorted data structure that allows for binary search, reducing the search complexity from O(n) to O(log n).

Consider a university database containing student records. If you frequently search students by their roll number, creating an index on the roll number column would dramatically speed up these queries. The index acts as a pointer to the actual data rows, allowing quick access without scanning the entire table.

### 2. Single-Level Indexing

Single-level indexing refers to the creation of indexes at one level of the data structure. There are three main types:

**Primary Index**: Created on a primary key column. The primary key must have unique values, and the data file is physically ordered (sorted) on this key. In primary indexing, the index entries follow the format (key value, pointer to record), and since the data is sequentially stored, the index is dense—every record has an entry in the index. Primary indexes provide the fastest possible access but require the data file to be sorted on the indexed attribute.

**Clustering Index**: Created on a non-key column that has a logical ordering or where records with similar values are physically grouped together. Unlike primary indexes, clustering indexes allow duplicate values. The data file is sorted based on the clustering key, and all records with the same clustering value are stored together. For example, in a student database, if you frequently query students by their course, creating a clustering index on the 'course' column would group all students of the same course together on disk.

**Secondary Index**: Created on any non-key attribute, allowing multiple indexes per table. The data file is not required to be sorted on the secondary index key, making it more flexible than primary or clustering indexes. Secondary indexes are always dense and can be created on columns with duplicate values. They provide excellent query optimization but require additional storage space.

### 3. Index File Organization

An index file consists of index entries organized in a specific order. Each index entry contains a search key value and a pointer to the actual data record. The search key is the attribute or combination of attributes on which the index is built. Index files are typically much smaller than the data files because they only contain key-pointer pairs, making them faster to search.

For single-level indexes, we commonly use sequential file organization where index entries are stored in sorted order. The height of the index (number of levels) determines the search time. A single-level index with 'b' blocks can be searched in O(log₂b) time using binary search, making it highly efficient compared to linear search.

### 4. Multi-Level Indexing

As databases grow larger, even single-level indexes can become too large to search efficiently. Multi-level indexing solves this problem by creating a hierarchy of indexes, similar to how a book's index might have main topics with subtopics.

**Tree-Based Indexing**: The most common multi-level indexing structure uses B-trees and B+ trees. These are balanced tree data structures that maintain sorted data and allow searches, sequential access, insertions, and deletions in logarithmic time.

**B-Tree**: A self-balancing tree data structure that maintains sorted data and allows searches and sequential access in logarithmic time. In a B-tree of order m:
- Each node can have at most m children
- Each internal node (except root) has at least ⌈m/2⌉ children
- The root has at least 2 children if it's not a leaf
- All leaves appear at the same level
- A non-leaf node with k children contains k-1 keys

B-trees keep data sorted and allow searches, insertions, and deletions in O(log n) time. Both leaf nodes and internal nodes can store data values, making B-trees efficient for both point queries and range queries.

**B+ Tree**: An enhanced version of B-tree specifically optimized for disk-based storage systems. In a B+ tree of order m:
- All data records are stored in leaf nodes only
- Internal nodes only contain key values (no data)
- Leaf nodes are linked together in a linked list for efficient range queries
- Each leaf node contains between ⌈m/2⌉ and m records
- Internal nodes follow the same splitting rules as B-trees

B+ trees are the most widely used indexing structure in modern database systems (MySQL, PostgreSQL, Oracle) because they provide better performance for range queries and have a more compact structure.

### 5. Comparison: Single vs Multi-Level Indexing

| Aspect | Single-Level Index | Multi-Level Index (B+/B-Tree) |
|--------|-------------------|-------------------------------|
| Height | 1 level | Multiple levels (typically 2-4) |
| Search Complexity | O(log₂b) | O(logₘn) where m is order |
| Storage | Smaller datasets | Larger datasets |
| Insertion/Deletion | Complex (file reorganization) | Automatic (tree balancing) |
| Disk I/O | May require more blocks | Optimized for disk pages |

## Examples

### Example 1: Understanding Single-Level Primary Index

Consider a student database table 'Students' with the following structure:
- StudentID (Primary Key): 1 to 1000
- Name: String
- Course: String
- Marks: Integer

The data file is sorted by StudentID, and we create a primary index on StudentID.

**Problem**: Find the record with StudentID = 750.

**Solution using Primary Index**:
1. The primary index is sorted on StudentID
2. Using binary search on the index, we locate the entry for StudentID = 750
3. The index entry contains a pointer to the exact disk block where the record is stored
4. We directly access that block and retrieve the record
5. Instead of potentially scanning 1000 records, we only examined approximately log₂(number of index blocks) entries

**Calculation**: If we have 1000 students and each index block holds 100 entries, we need to search only 10 index blocks using binary search, then access just 1 data block—a significant improvement over scanning all 1000 records.

### Example 2: B+ Tree Index Construction

Construct a B+ tree of order 3 for the following key values inserted in sequence: 10, 20, 5, 6, 12, 30, 7, 17

**Step-by-step construction**:

**Insert 10**: Create root with [10]

**Insert 20**: Root becomes [10, 20] (still has room for 3 keys)

**Insert 5**: Root becomes [5, 10, 20] (now full)

**Insert 6**: Root exceeds capacity (3 keys). Split into:
- Left node: [5, 6]
- Right node: [10, 20]
- New root: [10]
(Pointer from 10 in root points to right node containing [10, 20])

**Insert 12**: Traverse to appropriate leaf, insert in order: [5, 6, 10, 12, 20]
- Leaf exceeds capacity (max 3), split:
  - Left leaf: [5, 6]
  - Right leaf: [10, 12, 20]
- Middle key 10 moves to root

**Insert 30**: Add to right leaf: [10, 12, 20, 30] - split required
- Left leaf: [10, 12]
- Right leaf: [20, 30]
- Key 20 moves to root: [10, 20]

**Insert 7**: Add to left leaf: [5, 6, 7] - full but doesn't split (at minimum threshold)

**Insert 17**: Add to right leaf: [10, 12, 17] - full, split needed
- Left leaf: [10, 12]
- Right leaf: [17, 20, 30]
- Key 17 moves to root: [10, 17, 20]

Final B+ Tree structure:
- Root: [10, 17, 20]
- Level 1 leaves (internal nodes point to data blocks)
- Leaf level: [5, 6, 7] → [10, 12] → [17, 20, 30]

### Example 3: Analyzing Query Performance

Given a table 'Orders' with 1,000,000 records and a B+ tree index on 'order_date':
- Tree order (m) = 100
- Each index entry = 12 bytes
- Each disk block = 4 KB

**Calculate the number of levels in the B+ tree**:

**Level 0 (Root)**: Can hold up to 99 keys (m-1), so can point to 99 children
- Each child pointer block can hold: 4096 / 8 = 512 pointers

**Level 1**: 512 × 99 = 50,688 index entries
- Each entry ~12 bytes: 50,688 × 12 = 608,256 bytes ≈ 149 blocks

**Level 2**: 149 × 99 = 14,751 entries → ~4 blocks

**Level 3 (Leaf)**: Points to actual data records

For a query searching for a specific date:
- Disk I/O required = Height of tree = 3-4 I/O operations
- Without index: 1,000,000 I/O operations (full table scan)
- **Improvement: 250,000 to 333,333 times faster!**

## Exam Tips

1. **Understand the difference between dense and sparse indexes**: Dense indexes have an entry for every record in the data file, while sparse indexes have entries only for some records. Primary indexes are sparse (data is sorted), while secondary indexes are always dense.

2. **Remember the B+ tree properties**: All data is in leaf nodes, leaf nodes are linked, internal nodes only store keys (not data). This is why B+ trees are preferred in databases.

3. **Know when to use each index type**: Primary index for unique keys with sorted data, clustering index for frequently queried non-unique attributes with logical grouping, secondary index for other frequently queried attributes.

4. **Understand the trade-offs**: Indexes speed up read operations but slow down write operations (INSERT, UPDATE, DELETE) because the index must be updated. Too many indexes waste storage and increase maintenance overhead.

5. **Remember the formula for B-tree search complexity**: O(logₘn) where m is the order (maximum children) and n is the number of keys. This is crucial for comparing index performance.

6. **For exam problems, always calculate I/O costs**: When comparing query execution plans, count the number of disk blocks accessed. This is the primary metric for database performance.

7. **Multi-level indexing solves the "index too large" problem**: If a single-level index doesn't fit in memory, you need multi-level indexing. Remember that each level adds one disk access to the search.