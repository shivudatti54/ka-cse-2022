# HASHING

## Introduction

Hashing is one of the most fundamental and efficient techniques used in computer science for implementing associative arrays or dictionary data structures. It enables fast insertion, deletion, and lookup operations with an average time complexity of O(1), making it indispensable in scenarios where rapid data access is critical. Unlike linear search or binary search, which require scanning through data elements, hashing computes a direct address for storing or retrieving data based on a key value through a special function called the hash function.

The importance of hashing extends far beyond theoretical computer science. It forms the backbone of modern computing applications including database indexing, cache implementation, symbol tables in compilers, password storage, cryptographic security, and blockchain technology. In the context of the University of Delhi's Computer Science curriculum, hashing represents a crucial topic that bridges abstract data structure concepts with practical programming applications. Understanding hashing thoroughly prepares students for technical interviews at top companies and provides foundation knowledge for advanced topics like distributed systems and database management.

This chapter explores the fundamental concepts of hashing, including hash functions, collision resolution techniques, and the trade-offs involved in choosing different hashing strategies. We will examine both static and dynamic hashing approaches, analyze their performance characteristics, and develop the analytical skills necessary to select appropriate hashing solutions for specific problem domains.

## Key Concepts

### Hash Function

A hash function is a mathematical function that converts a given key (usually a string or integer) into a specific index within a fixed-size array called a hash table. The primary goal of a hash function is to distribute keys uniformly across all available slots in the hash table to minimize collisions. A good hash function should satisfy several critical properties: it must be deterministic (same key always produces the same hash value), efficient to compute, and should minimize the likelihood of collisions by spreading keys evenly throughout the table.

Several common methods exist for constructing hash functions. The division method computes the hash value by taking the key modulo the table size: h(k) = k mod m, where m is the size of the hash table. The multiplication method uses the formula h(k) = floor(m * (k * A mod 1)), where A is a constant between 0 and 1. The mid-square method squares the key and extracts the middle digits as the hash value. For string keys, common approaches include the ASCII value summation method and polynomial rolling hash functions.

### Collision

A collision occurs when two different keys produce the same hash value and must be stored in the same location within the hash table. Collisions are inevitable due to the pigeonhole principle—if there are more keys than available slots, some keys must share locations. The quality of a hashing system is measured by how effectively it handles collisions rather than attempting to eliminate them entirely. The load factor, denoted by α (alpha), represents the ratio of the number of elements stored to the table size: α = n/m, where n is the number of elements and m is the table size.

### Collision Resolution Techniques

Open addressing involves storing all elements within the hash table itself. When a collision occurs, the algorithm probes through alternative positions according to a predetermined sequence until an empty slot is found. Three primary probing techniques exist within open addressing: linear probing searches sequentially (h(k), h(k)+1, h(k)+2...), quadratic probing uses quadratic increments (h(k), h(k)+1², h(k)+2²...), and double hashing utilizes a secondary hash function to compute the step size (h(k), h(k)+h₂(k), h(k)+2h₂(k)...).

Chaining represents an alternative approach where each slot in the hash table contains a linked list (or more sophisticated data structure) of all elements that hash to that particular location. This method elegantly handles collisions by allowing multiple elements to occupy the same bucket without requiring additional probing. Chaining typically performs better when the load factor exceeds 0.5 or when the number of elements cannot be predicted in advance.

### Rehashing

Rehashing becomes necessary when the load factor grows too large, causing performance degradation due to increased collisions. This process involves creating a new, larger hash table (usually twice the size) and reinserting all existing elements using the new table size. Rehashing ensures that the load factor remains within acceptable bounds, maintaining the O(1) average case performance for operations. The cost of rehashing is O(n), but it is an infrequent operation that amortizes well across many operations.

### Perfect Hashing

Perfect hashing guarantees that no collisions occur, achieving O(1) worst-case lookup time. This is accomplished through a two-level scheme where a primary hash function maps keys to buckets, and each bucket uses a secondary hash function with a perfectly sized local table. While perfect hashing requires advance knowledge of all keys and additional memory, it eliminates the performance uncertainty associated with collision resolution.

## Examples

### Example 1: Division Method with Linear Probing

Consider a hash table of size 10 using the hash function h(k) = k mod 10 and linear probing for collision resolution. Insert the following sequence of keys: 23, 42, 15, 7.

**Solution:**

- Insert 23: h(23) = 23 mod 10 = 3. Slot 3 is empty. Insert 23 at index 3.
- Insert 42: h(42) = 42 mod 10 = 2. Slot 2 is empty. Insert 42 at index 2.
- Insert 15: h(15) = 15 mod 10 = 5. Slot 5 is empty. Insert 15 at index 5.
- Insert 7: h(7) = 7 mod 10 = 7. Slot 7 is empty. Insert 7 at index 7.

Final table: [_, 42, 23, _, _, 15, _, 7, _, _]

### Example 2: Handling Collisions with Linear Probing

Now insert key 33 into the table from Example 1. Since h(33) = 33 mod 10 = 3, and slot 3 already contains 23, we probe linearly:

- Try slot 3: occupied by 23
- Try slot 4: empty. Insert 33 at index 4.

Final table: [_, 42, 23, _, 33, 15, _, 7, _, _]

### Example 3: Chaining Method

Using the same keys (23, 42, 15, 7, 33) with a hash table of size 5 and hash function h(k) = k mod 5:

- h(23) = 3 → Bucket 3: [23]
- h(42) = 2 → Bucket 2: [42]
- h(15) = 0 → Bucket 0: [15]
- h(7) = 2 → Bucket 2: [42, 7]
- h(33) = 3 → Bucket 3: [23, 33]

Final table:
- Index 0: 15 → 33
- Index 1: (empty)
- Index 2: 42 → 7
- Index 3: 23 → 33
- Index 4: (empty)

The load factor α = 5/5 = 1. Average search time depends on the length of chains.

### Example 4: Double Hashing

Insert keys 12, 22, 32, 42 into a hash table of size 10 with primary hash function h₁(k) = k mod 10 and secondary hash function h₂(k) = 7 - (k mod 7).

- Insert 12: h₁(12) = 2, h₂(12) = 7 - 5 = 2. Try index 2: empty. Insert at index 2.
- Insert 22: h₁(22) = 2, h₂(22) = 7 - 1 = 6. Try index 2: occupied. Try index (2+6) mod 10 = 8: empty. Insert at index 8.
- Insert 32: h₁(32) = 2, h₂(32) = 7 - 4 = 3. Try index 2: occupied. Try index 5: empty. Insert at index 5.
- Insert 42: h₁(42) = 2, h₂(42) = 0. Since h₂(42) = 0, we use step size 1. Try index 2: occupied. Try index 3: empty. Insert at index 3.

Final table: [_, _, 12, 42, _, 32, _, _, 22, _]

## Exam Tips

For the University of Delhi end semester examinations, several key points require special attention when answering hashing-related questions. First, ALWAYS calculate and mention the load factor when analyzing hash table performance—it is fundamental to understanding time complexity. Second, remember that linear probing suffers from primary clustering, where long sequences of occupied slots form, causing performance degradation. Third, quadratic probing does not guarantee finding an empty slot even when one exists, unlike linear probing.

Fourth, double hashing is generally considered the best open addressing method because it eliminates both primary and secondary clustering through independent probe sequences. Fifth, chaining is preferred when the load factor exceeds 0.5 or when deletions are frequent, as open addressing becomes inefficient with high load factors. Sixth, when answering questions about hash function selection, always consider the table size m—it should ideally be a prime number not close to powers of 2 to minimize clustering patterns.

Seventh, remember the asymptotic complexities: average case O(1 + α) for both searching and insertion, while worst case for chaining is O(n) when all keys hash to the same bucket. Eighth, practice numerical problems involving collision resolution step-by-step, as these frequently appear in examination papers. Finally, when comparing different hashing techniques, analyze the trade-offs between memory usage, implementation complexity, and performance under various load factors.