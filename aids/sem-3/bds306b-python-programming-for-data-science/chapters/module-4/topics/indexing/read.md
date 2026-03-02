# Hash Indexing

## 1. Introduction to Hash Indexing

In Database Management Systems (DBMS), an index is a data structure that improves the speed of data retrieval operations on a database table. While tree-based indexes like B+ Trees are excellent for range queries and sorted data access, **Hash Indexing** provides a fundamentally different approach optimized for **point queries** (e.g., `SELECT * FROM table WHERE primary_key = 123;`).

A hash index uses a **hash function** to map search keys (e.g., a primary key value) to a fixed-size value, which directly corresponds to the location (a "bucket" or "slot") in the index where the pointer to the actual data record is stored. This allows for, on average, **O(1) constant-time lookup**, making it one of the fastest methods for exact-match queries.

## 2. Core Concepts and Terminology

### Hash Function
A hash function `h(key)` takes a search key as input and returns an integer, which is used as an address for the storage bucket. An ideal hash function for indexing has these properties:
*   **Uniform Distribution:** It should distribute the keys uniformly across the available buckets. This minimizes collisions.
*   **Deterministic:** The same key must always produce the same hash value.
*   **Fast to Compute:** The hashing operation itself should be computationally cheap.
*   **Avalanche Effect:** A small change in the input key should produce a significantly different hash value.

### Buckets and Slots
The hash index is organized as an array of **buckets** (or slots). Each bucket can hold one or more entries. An entry is typically a pair `(key, pointer)`, where the pointer is the address of the corresponding record on disk.

### Hash Collision
A collision occurs when two distinct keys, `k1` and `k2`, hash to the same bucket, i.e., `h(k1) = h(k2)`. Since the number of possible keys is usually much larger than the number of buckets, collisions are inevitable. How a hash index handles collisions is critical to its performance.

## 3. Internal Structure and How It Works

The process of using a hash index involves two main steps: writing (insertion) and reading (lookup).

### Insertion
1.  The system takes the search key value from the new record.
2.  It applies the hash function `h(key)` to this value.
3.  The resulting hash value is used as an index to locate a bucket in the hash table array.
4.  The entry `(key, pointer_to_record)` is placed into that bucket.

### Lookup (Point Query)
1.  The system takes the search key value from the query predicate (e.g., `WHERE id = 5`).
2.  It applies the same hash function `h(key)` to this value.
3.  The resulting hash value points directly to the target bucket.
4.  The system scans the entries within that bucket to find the exact key match and retrieves the record using the pointer.

The following diagram illustrates this flow:

```
+-----------------+      +-----------------+      +-----------------+
|   Search Key    |      |   Hash Function |      |   Hash Table    |
|   (e.g., id=5)  |----->|   h(key) = 2    |----->| [0] -> ...      |
+-----------------+      +-----------------+      | [1] -> ...      |
                                                  | [2] -> (5, ptr) |---> Data Page
                                                  | [3] -> ...      |     with Record
                                                  +-----------------+
```

## 4. Handling Hash Collisions

Since multiple keys can hash to the same bucket, a method for resolving these collisions is needed. The two most common techniques are:

### 1. Separate Chaining
In this method, each bucket in the hash table is implemented as a linked list (or another data structure) of entries. When a collision occurs, the new entry is simply appended to the end of the list for that bucket.

```
Bucket i: [ Entry_A ] -> [ Entry_C ] -> [ Entry_B ] -> NULL
```
*   **Lookup:** The entire linked list for the bucket must be scanned to find the exact key.
*   **Advantage:** Simple to implement.
*   **Disadvantage:** Performance degrades if a single bucket has a very long chain.

### 2. Open Addressing
In open addressing, all entries are stored directly in the bucket array itself. When a collision occurs, the algorithm probes subsequent buckets according to a predefined sequence (e.g., linear probing: check bucket `i+1`, then `i+2`, etc.) until it finds an empty slot.
*   **Lookup:** The same probe sequence is followed until the key is found or an empty bucket is encountered.
*   **Advantage:** Avoids the overhead of storing pointers for linked lists and can have better cache performance.
*   **Disadvantage:** More complex to manage, especially when deleting entries.

## 5. Static vs. Dynamic Hashing

The choice of hashing technique depends on whether the data size is known in advance.

### Static Hashing
In static hashing, the number of buckets `M` in the hash table is fixed. This presents a major problem: if the number of records grows significantly larger than `M`, bucket overflow (long chains or probe sequences) becomes common, and performance drops dramatically. Conversely, if `M` is much larger than needed, it wastes memory.

### Dynamic Hashing
Dynamic hashing techniques allow the hash table to grow and shrink dynamically as the number of records changes. The most common scheme is **Extendible Hashing**.

#### Extendible Hashing
Extendible hashing uses a **directory** (an array of pointers to buckets) that can grow and a hash function that produces a large number of bits (e.g., 32 bits). The directory uses the first `d` bits (the **global depth**) to index into itself. Each bucket has a **local depth** `d'`.

1.  **Insertion:** When a bucket overflows, it is split into two. The local depth `d'` is incremented. If the local depth becomes greater than the global depth, the directory is doubled in size (and the global depth `d` is incremented by 1). This allows the index to grow one bucket at a time, minimizing overhead.
2.  **Lookup:** Compute the hash value. Use the first `d` bits to find the correct directory entry, which points to the correct bucket. Then search within that bucket.

This structure is highly efficient and avoids the performance degradation of static hashing.

```
Global Depth d = 2
Directory
00 -> Bucket A (d'=2) : [Entries for keys where hash starts with 00]
01 -> Bucket B (d'=2) : [Entries...]
10 -> Bucket C (d'=1) : [Entries for keys where hash starts with 0 OR 1] // This bucket has a lower local depth
11 -> Bucket C (d'=1) : [Points to the same Bucket C as above]
```

## 6. Comparison with B+ Tree Indexing

| Feature | Hash Index | B+ Tree Index |
| :--- | :--- | :--- |
| **Primary Use Case** | Exact-match queries (`=`, `IN`) | Range queries (`BETWEEN`, `>`, `<`), sorting, exact-match |
| **Lookup Time** | **O(1)** average case | **O(log n)** worst case (where n is the number of entries) |
| **Range Queries** | **Inefficient.** Requires scanning all buckets. | **Highly efficient.** Leaf nodes are linked in sorted order. |
| **Ordering** | Does not maintain any order between keys. | Maintains a sorted order of keys. |
| **Dynamic Growth** | Requires techniques like extendible hashing to be efficient. | Naturally grows and shrinks while maintaining balance. |
| **Overhead** | Low overhead for point queries. Can have overhead from collisions and directory (in extendible hashing). | Higher overhead per operation due to tree traversal and balancing. |

## 7. Practical Considerations in DBMS

*   **Limited Applicability:** Hash indexes are not a one-size-fits-all solution. They are typically chosen only for specific columns frequently used in exact-match `WHERE` clauses (e.g., a `user_id` or `email` column in a `WHERE user_id = 123` query).
*   **No Sorting:** The output of a `SELECT` query using a hash index will not be sorted. An explicit `ORDER BY` clause would require a separate sorting step, which is expensive.
*   **SQL Support:** While the SQL standard does not specify index types, many DBMS (like PostgreSQL, MySQL) allow you to choose between index types (e.g., `CREATE INDEX ... USING HASH` in PostgreSQL). However, they often use B-Trees as the default due to their versatility.
*   **In-Memory Databases:** Hash indexes are extremely popular in in-memory databases and caching systems (e.g., Redis) because of their minimal latency for lookups.

## 8. Exam Tips

1.  **Know the Strengths and Weaknesses:** Always be ready to compare and contrast hash indexes with B+ trees. The key differentiator is **point queries vs. range queries**.
2.  **Understand Collision Resolution:** Be prepared to explain separate chaining and open addressing, and discuss their pros and cons.
3.  **Explain Dynamic Hashing:** You will likely be asked why static hashing is problematic in a database context and how extendible hashing solves this problem. Be able to define **global depth** and **local depth**.
4.  **Think in Terms of Big-O:** Remember that hash indexes offer O(1) lookup *on average*, but worst-case can be O(n) if all keys collide (highly unlikely with a good hash function). B+ Trees offer a predictable O(log n) performance.
5.  **Real-World Application:** When given a scenario, choose a hash index if the query pattern is overwhelmingly exact-match on a single column. Choose a B+ tree for anything involving ranges, sorting, or being the primary key of a table (which often serves as the clustering index).