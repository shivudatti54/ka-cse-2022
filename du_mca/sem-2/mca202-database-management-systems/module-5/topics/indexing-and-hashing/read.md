# Indexing and Hashing

## Introduction
Indexing and hashing form the backbone of efficient data retrieval in modern database systems. As databases grow to terabyte-scale, the ability to quickly locate records without full-table scans becomes critical. Indexing provides an organized pathway to data through tree-based structures, while hashing offers direct access via mathematical mapping functions.

These techniques directly impact query performance in OLTP systems and analytical processing in data warehouses. For instance, e-commerce platforms like Amazon use B+ tree indexes for fast product searches, while distributed systems like Apache Cassandra employ consistent hashing for data partitioning. Understanding these mechanisms is essential for database tuning and optimizing CRUD operations.

The choice between indexing and hashing involves trade-offs between query flexibility and access speed. Index structures support range queries efficiently, while hash-based methods excel at exact-match lookups. Modern DBMS like PostgreSQL implement both strategies, using indexes for complex queries and hash joins for equi-joins.

## Key Concepts

**1. B+ Trees**
- Balanced search trees with all data in leaf nodes
- Order 'm' defines maximum children per node (min ⌈m/2⌉)
- Supports range queries through linked leaf nodes
- Insertion involves node splitting; deletion uses redistribution/merging

**2. Static vs Dynamic Hashing**
- Static hashing (bucket hashing) uses fixed table size
- Dynamic hashing (extendible/linear hashing) adapts to data growth
- Load factor α = n/(k*b) determines hash table efficiency

**3. Hash Functions**
- Ideal properties: uniform distribution, minimal collisions
- Common methods: division, multiplication, universal hashing
- Cryptographic vs non-cryptographic hash functions

**4. Collision Resolution**
- Open addressing: linear probing, quadratic probing
- Closed hashing: separate chaining with linked lists
- Double hashing: h(k,i) = (h1(k) + i*h2(k)) mod m

**5. Multi-level Indexing**
- Secondary indexes (non-clustered indexes)
- Covering indexes that include all query fields
- Bitmap indexes for low-cardinality columns

## Examples

**Example 1: B+ Tree Insertion**
Construct B+ Tree of order 3 with sequence: 5, 15, 25, 35, 45

Step 1: Insert 5,15
        [5,15] (leaf)
        
Step 2: Insert 25 → Split
        [15] (internal)
       /    \
[5,15] [15,25] (leaves)

Step 3: Insert 35 → Add to right leaf
        [15]    
       /    \
[5,15] [15,25,35]

Step 4: Insert 45 → Split leaf and update internal nodes
        [15,35]
       /   |   \
[5,15] [15,25] [35,45]

**Example 2: Linear Probing**
Hash table size=7, h(k)=k mod 7
Insert: 12, 19, 5, 14

Insert 12 → index 5
Insert 19 → 5 (collision) → 6
Insert 5 → 5 (collision) → 0
Insert 14 → 0 (collision) → 1

Final table:
0:5,1:14,5:12,6:19

**Example 3: Index-based Query Optimization**
SELECT * FROM orders WHERE customer_id=123 AND order_date > '2023-01-01'

Without index: Full table scan O(n)
With composite index on (customer_id, order_date): Index range scan O(log n + k)

## Exam Tips
1. Always draw B+ Trees with clear distinction between internal nodes (keys only) and leaf nodes (data pointers)
2. For hashing questions, explicitly state your hash function and collision resolution method
3. Remember that B+ Tree leaf nodes form a linked list - crucial for range query explanations
4. When comparing techniques, consider factors: insertion cost, query types supported, space overhead
5. For collision resolution, calculate probe sequences step-by-step
6. In index selection questions, consider cardinality and query patterns (OLTP vs OLAP)
7. Use proper notation: B+ Tree order (maximum children), hash load factor α < 0.75 for optimal performance