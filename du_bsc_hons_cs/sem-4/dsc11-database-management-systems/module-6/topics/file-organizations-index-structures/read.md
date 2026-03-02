# File Organizations and Index Structures

## Introduction

File organization is a critical aspect of database management systems that determines how data is physically stored on disk and accessed efficiently. In the context of the University of Delhi's BSc (Hons) Computer Science program, understanding file organizations and index structures is essential for designing efficient database systems and optimizing query performance. When we interact with a database—whether performing a simple SELECT query or a complex JOIN operation—the underlying file organization determines how quickly the system can locate and retrieve the required data.

The choice of file organization and indexing technique directly impacts database performance in terms of storage space utilization, data retrieval speed, and update efficiency. A well-designed file organization can reduce disk I/O operations from thousands to just a few, resulting in significant performance improvements for database applications. In real-world scenarios, organizations like Amazon, Netflix, and banking systems rely heavily on sophisticated index structures to handle millions of transactions per second.

This module explores various file organization techniques including sequential, hash-based, and indexed organizations, along with advanced index structures such as B+ Trees—the most widely used index structure in modern database systems. We will also examine bitmap indexes, which are particularly useful in data warehousing environments, and understand how different organizations suit different access patterns.

## Key Concepts

### 1. Files and Records

A **file** is a collection of related records stored on secondary storage (typically magnetic disks). Each **record** represents a collection of related fields (attributes) corresponding to a tuple in a relation. Records are organized into **blocks**, which are the fundamental units of data transfer between disk and memory. The block size is typically a multiple of the sector size (usually 4KB-8KB in modern systems).

**Record blocking** refers to how records are packed into blocks. There are three main approaches:
- **Fixed-length records**: All records have the same size, making it easy to calculate record addresses using the formula: `block_address = (record_number - 1) / records_per_block`
- **Variable-length records**: Records have different sizes, requiring additional overhead to store record lengths and potentially using spanning across multiple blocks
- **Spanned records**: Records that do not fit entirely within one block can span multiple blocks

### 2. Types of File Organizations

#### Sequential File Organization

In **sequential file organization**, records are stored in a particular order (sorted by a primary key or any search key). This organization is ideal for applications that require processing records in order or performing range queries.

**Advantages:**
- Efficient for queries involving range searches (e.g., "find all students with CGPA between 7 and 9")
- Simple to implement and understand
- Low overhead for storage

**Disadvantages:**
- Expensive insertions and deletions (may require reorganization)
- Binary search can be used for point queries, giving O(log n) access time

#### Heap File Organization

In **heap (unordered) file organization**, records are inserted at the end of the file without any particular order. This is the simplest form of file organization.

**Advantages:**
- Fastest insertion (O(1) - simply append to end)
- No maintenance overhead

**Disadvantages:**
- Sequential scan required for searches (O(n))
- Not suitable for queries with selection conditions

#### Hash File Organization

**Hash file organization** uses a hash function to compute the address of a record based on the value of a search key. The hash function maps search key values to bucket addresses, distributing records across buckets.

**Static Hashing**: A fixed number of buckets are allocated. The hash function is: `h(key) = key mod n`, where n is the number of buckets. Problems arise when the file grows or shrinks significantly.

**Dynamic Hashing**: The number of buckets grows and shrinks with the file size. Techniques include:
- **Linear Hashing**: Buckets are added in a linear sequence
- **Extendible Hashing**: Uses a directory of bucket pointers, allowing dynamic expansion

**Hashing is ideal for point queries** (equality searches) but **inefficient for range queries** because related records may be scattered across different buckets.

#### Clustered File Organization

In **clustered file organization**, records of different relations are stored together based on a clustering key. Records with the same clustering key value are stored in the same block or nearby blocks. This is particularly useful for JOIN operations where records from two tables are frequently joined on a common attribute.

For example, if students and enrollments are frequently joined on student_id, storing them together based on student_id can significantly reduce disk I/O for JOIN operations.

### 3. Index Structures

An **index** is a data structure that provides fast access to records based on the values of one or more attributes (index key). Think of an index like the index at the back of a textbook—it helps you find information quickly without reading the entire book.

#### Primary Index

A **primary index** is built on the primary key of a relation. The index key must be unique, and the data file is physically ordered (sorted) on the primary key. Since the data file is sorted, we can use sparse indexing—storing one index entry per block rather than per record.

**Characteristics:**
- Unique key values
- Data file is sequentially ordered on the key
- Sparse index (one entry per block)
- Provides O(log n) + b access time for point queries, where b is the number of blocks

#### Secondary Index

A **secondary index** can be built on any attribute (including non-unique attributes) and does not require the data file to be physically ordered on the index key. Secondary indexes are always dense—every record has an index entry.

**Characteristics:**
- Can be built on non-unique keys
- Data file need not be ordered on the key
- Always dense
- Provides O(log n) + r access time, where r is the number of qualifying records

#### B+ Tree Index

The **B+ Tree** is the most widely used index structure in modern database systems. It is a balanced tree data structure that maintains sorted data and allows efficient insertion, deletion, and search operations.

**Structure of a B+ Tree:**
- **Root**: The top node, has at least 2 children if not a leaf
- **Internal Nodes**: Guide search, contain key values and child pointers, have between ⌈m/2⌉ and m children (where m is the order)
- **Leaf Nodes**: Contain actual data pointers (or data records) and sibling pointers for sequential access, have between ⌈m/2⌉ and m values

**Properties:**
- All leaf nodes are at the same level (height-balanced)
- Internal nodes guide the search
- Leaf nodes are linked for efficient range queries
- Supports point queries, range queries, and sequential access efficiently

**Example B+ Tree of order 3:**
```
        [15]
       /    \
   [5,10]  [15,20]
   / | \    / |  \
 1  5 10  15  20  25
```

For a B+ Tree of order m:
- Maximum pointers per node: m
- Maximum keys per node: m-1
- Minimum keys per node (for non-root): ⌈m/2⌉ - 1

#### Bitmap Index

A **bitmap index** is a special type of index designed for attributes with a small number of distinct values (low cardinality). It uses bit vectors (sequences of 0s and 1s) to represent the presence or absence of a value.

For an attribute with n distinct values and a table with t tuples, we create n bit vectors, each of length t.

**Example**: For a "Gender" attribute with values {Male, Female}:
- Male: 101010... (1 if Male, 0 otherwise)
- Female: 010101... (1 if Female, 0 otherwise)

Bitmap indexes are highly efficient for:
- Low-cardinality attributes
- Complex queries using AND, OR operations (bitwise operations are extremely fast)
- Data warehousing applications

### 4. Multi-level Indexing

When an index grows too large to fit in memory, we need multi-level indexing. The first-level index is dense (one entry per record), and we build a sparse index on top of it. This creates a hierarchical structure similar to how books have chapters, sections, and pages.

The B+ Tree is essentially a multi-level index that dynamically adjusts its height as data grows or shrinks.

## Examples

### Example 1: Calculating B+ Tree Properties

**Question**: A B+ Tree of order 3 is used to index a file with 1000 records. Each node can hold at most 2 keys. Calculate:
(a) Maximum number of keys in the tree
(b) Minimum number of keys in the tree (assuming root is not a leaf)
(c) Height of the tree

**Solution**:

Given: Order m = 3

(a) Maximum keys: For a tree of height h, maximum keys = m^h - 1
- Height 1 (root only): 2 keys
- Height 2: 3 × 2 = 6 keys  
- Height 3: 3² × 2 = 18 keys
- Height 4: 3³ × 2 = 54 keys
- Height 5: 3⁴ × 2 = 162 keys
- Height 6: 3⁵ × 2 = 486 keys
- Height 7: 3⁶ × 2 = 1458 keys (exceeds 1000)

Therefore, height = 7

(b) Minimum keys: For minimum, assume root has minimum children (2), and all other nodes have minimum keys (⌈3/2⌉ - 1 = 1 key, so 2 children):
- Level 0 (root): 1 key
- Level 1: 2 nodes × 1 key = 2 keys
- Level 2: 2 × 2 = 4 keys
- Level 3: 4 × 2 = 8 keys
- Level 4: 8 × 2 = 16 keys
- Level 5: 16 × 2 = 32 keys
- Level 6: 32 × 2 = 64 keys
Total = 1 + 2 + 4 + 8 + 16 + 32 + 64 = 127 keys (minimum)

(c) Height = 7 levels

### Example 2: Comparing Access Methods

**Question**: Consider a database with 10,000 records stored in 100 blocks (100 records per block). Compare the number of block accesses for the following operations:

(a) Search for a record with key = 500 using:
   - Sequential scan
   - Primary index (sparse)
   - Hash indexing (assuming 10 buckets, uniform distribution)

(b) Search for all records with key BETWEEN 100 and 500

**Solution**:

(a) Point query for key = 500:

1. **Sequential scan**: In worst case, we might need to read all blocks = 100 block accesses

2. **Primary index (sparse)**: Since it's sparse (1 index entry per block):
   - Binary search on index: log₂(100) ≈ 7 block accesses
   - Then access the data block: 1 block access
   - Total: 7 + 1 = 8 block accesses

3. **Hash indexing** (10 buckets):
   - Hash function: h(500) = 500 mod 10 = 0
   - Access bucket 0: Approximately 1000/10 = 100 records per bucket = 1 block
   - Total: 1 block access (in best case)

(b) Range query (key BETWEEN 100 and 500):

1. **Sequential scan**: Must scan entire file = 100 block accesses (or fewer if we stop early)

2. **Primary index**: 
   - Locate first record (key = 100): 7 + 1 = 8 accesses
   - Then traverse sequentially through leaf nodes: approximately (500-100)/100 = 4 data blocks
   - Total: approximately 8 + 4 = 12 block accesses

3. **Hash indexing**: Cannot perform range queries efficiently—would need to scan entire file = 100 block accesses

### Example 3: Bitmap Index Construction

**Question**: A table has 8 records with a "Department" attribute having values: {CS, IT, CS, EE, CS, IT, ME, CS}. Construct the bitmap index for this attribute.

**Solution**:

Distinct values: {CS, IT, EE, ME} — 4 bitmaps needed, each of length 8 bits

**CS bitmap**: For each row, mark 1 if Department = 'CS'
- Row 1: CS → 1
- Row 2: IT → 0
- Row 3: CS → 1
- Row 4: EE → 0
- Row 5: CS → 1
- Row 6: IT → 0
- Row 7: ME → 0
- Row 8: CS → 1
- CS bitmap: 10101001

**IT bitmap**:
- IT bitmap: 01000101 (rows 2, 6, 8 have IT)

**EE bitmap**:
- EE bitmap: 00010000

**ME bitmap**:
- ME bitmap: 00000010

Query: "Find all CS and IT employees"
- CS OR IT = 10101001 OR 01000110 = 11101111
- Result: Rows 1, 2, 3, 5, 6, 8 (6 employees)

This demonstrates how bitmap operations can quickly answer complex queries using simple bitwise OR operations.

## Exam Tips

1. **Understand the difference between dense and sparse indexes**: Dense indexes have an entry for every record, while sparse indexes have one entry per block. Remember that primary indexes are sparse, secondary indexes are always dense.

2. **B+ Tree is the most important topic**: Be thorough with B+ Tree properties, insertion algorithms, and calculating capacity. Remember: minimum children = ⌈m/2⌉, maximum children = m.

3. **Know when to use each file organization**: Heap for frequent insertions, sequential for range queries, hashing for point queries. This is a common exam question.

4. **Remember that clustered vs. non-clustered is about data ordering**: Clustered indexes mean the actual data is physically ordered; non-clustered indexes have a separate structure pointing to data.

5. **Calculate I/O costs accurately**: For exams, always show your calculation method for block accesses. The standard formula is crucial.

6. **Bitmap indexes are for low-cardinality attributes**: Understand when bitmap indexes provide advantages and their space requirements.

7. **Multi-level indexing solves the "index too large" problem**: Understand how creating an index on an index solves the problem of keeping the index in memory.

8. **Practice numerical problems**: Questions involving B+ Tree capacity, block access calculations, and index selection are frequently asked in DU exams.