# Hashing

## Introduction

Hashing is one of the most fundamental techniques in computer science for achieving efficient data storage and retrieval. In an era where massive amounts of data are processed daily, the ability to access information in constant time has become critically important. Hashing provides a mechanism to map data of arbitrary size to fixed-size values, enabling near-instantaneous lookup operations that would otherwise require linear or logarithmic time complexity.

The concept of hashing revolves around a data structure called a hash table, which stores key-value pairs and uses a special function called a hash function to compute an index into an array of buckets or slots. When implemented correctly, hash tables can provide average-case time complexity of O(1) for insertion, deletion, and retrieval operations, making them superior to tree-based structures for many applications. This remarkable efficiency has made hashing an indispensable tool in database systems, compiler implementations, caching mechanisms, and cryptographic applications.

In the context of the University of Delhi's Computer Science curriculum, hashing represents a crucial topic that bridges theoretical concepts with practical applications. Students must understand not only the mechanics of hash tables but also the mathematical foundations that make them work, the various collision resolution strategies, and the trade-offs involved in choosing appropriate parameters for different use cases. Mastery of hashing demonstrates a student's understanding of time-space trade-offs and algorithmic optimization, skills that are essential for success in competitive examinations and professional software development.

## Key Concepts

### Hash Function

A hash function is the core component of any hashing system. It is a mathematical function that takes a key as input and produces an integer value called the hash code or simply the hash. The fundamental requirement for a hash function is that it should distribute keys uniformly across the available buckets in the hash table. A good hash function minimizes collisions by ensuring that different keys map to different positions as often as possible.

Several properties characterize a good hash function:

**Determinism**: The same key must always produce the same hash value. If the hash function returns different values for the same key at different times, the data structure becomes unreliable.

**Efficiency**: Computing the hash value should be fast, ideally constant time. The overhead of computing the hash should not negate the benefits of O(1) lookup.

**Uniform Distribution**: The hash function should spread keys evenly across all possible bucket indices. If keys cluster in certain regions, collisions increase and performance degrades.

Common hash functions include the division method, where the hash value is computed as key mod table_size; the multiplication method, which uses the fractional part of key multiplied by a constant; and string hashing methods that treat character strings as numbers in a base and compute their modulo. For integer keys, the division method with a carefully chosen table size (preferably a prime number not close to a power of two) often yields good results.

### Collision Handling

When two different keys produce the same hash value, a collision occurs. Since no perfect hash function exists that can guarantee unique mapping for all possible inputs, every practical hash table must implement collision resolution strategies. The efficiency of a hash table largely depends on how well it handles collisions.

There are two primary approaches to collision resolution:

**Open Addressing**: In open addressing, when a collision occurs, the system searches for the next available empty slot in the table using a probing sequence. The three most common probing techniques are linear probing, quadratic probing, and double hashing.

In linear probing, if a collision occurs at index h, the system checks indices h+1, h+2, h+3, and so on until an empty slot is found. While simple to implement, linear probing suffers from primary clustering, where long sequences of occupied slots form, causing increased search times.

Quadratic probing addresses primary clustering by using a quadratic function in the probe sequence. The probe sequence follows the pattern: h(key), h(key)+1², h(key)+2², h(key)+3², and so on. However, this method can still experience secondary clustering.

Double hashing uses a secondary hash function to compute the probe increment, effectively eliminating both primary and secondary clustering. The probe sequence becomes: h1(key), h1(key) + h2(key), h1(key) + 2*h2(key), where h1 and h2 are two independent hash functions.

**Separate Chaining**: In separate chaining, each bucket in the hash table is implemented as a linked list (or another dynamic data structure). All keys that hash to the same bucket are stored in this list. This approach allows the hash table to grow beyond its initial capacity, though performance degrades when chains become long. The average length of chains, called the load factor, determines the efficiency of the hash table.

### Load Factor and Rehashing

The load factor (α) of a hash table is defined as the ratio of the number of stored elements to the number of available buckets: α = n/m, where n is the number of elements and m is the table size. The load factor directly impacts performance: as α increases, collisions become more frequent, and operations slow down.

To maintain optimal performance, hash tables typically implement rehashing (also called resizing). When the load factor exceeds a threshold (commonly 0.7 or 0.75), the hash table is expanded: a new, larger array is allocated, and all existing elements are re-inserted into this new table using the hash function. This process redistributes the elements and reduces the load factor, restoring O(1) average performance. The new table size is typically chosen as approximately twice the old size, often rounded to the next prime number.

## Examples

### Example 1: Insertion with Linear Probing

Consider a hash table of size 10 using linear probing. We insert the keys 25, 73, 56, 41, and 92 in that order.

The hash function is h(key) = key mod 10.

- Insert 25: h(25) = 5. Position 5 is empty. Insert at index 5.
- Insert 73: h(73) = 3. Position 3 is empty. Insert at index 3.
- Insert 56: h(56) = 6. Position 6 is empty. Insert at index 6.
- Insert 41: h(41) = 1. Position 1 is empty. Insert at index 1.
- Insert 92: h(92) = 2. Position 2 is empty. Insert at index 2.

Final table: indices 1-6 contain 41, 73, 92, 25, 56 with indices 0, 7, 8, 9 empty.

### Example 2: Searching with Linear Probing

Now search for key 56 in the table from Example 1. Compute h(56) = 6. Check index 6: contains 56. Search successful in one probe.

Search for key 67 (not in table). Compute h(67) = 7. Index 7 is empty. The search terminates here, confirming 67 is not present.

### Example 3: Separate Chaining

Consider a hash table of size 7 using separate chaining with the hash function h(key) = key mod 7. Insert keys 14, 22, 37, 28, 42, 31, and 19.

- 14 mod 7 = 0 → Bucket 0: [14]
- 22 mod 7 = 1 → Bucket 1: [22]
- 37 mod 7 = 2 → Bucket 2: [37]
- 28 mod 7 = 0 → Bucket 0: [14, 28]
- 42 mod 7 = 0 → Bucket 0: [14, 28, 42]
- 31 mod 7 = 3 → Bucket 3: [31]
- 19 mod 7 = 5 → Bucket 5: [19]

The load factor α = 7/7 = 1. The average chain length is 1, indicating good distribution.

## Exam Tips

1. UNDERSTAND THE FUNDAMENTAL TRADE-OFF: Remember that hashing provides O(1) average case but O(n) worst case performance. Know when to choose hashing over other data structures.

2. MEMORIZE THE LOAD FACTOR FORMULA: α = n/m, where n is number of elements and m is table size. This is frequently tested in exams.

3. KNOW COLLISION RESOLUTION METHODS: Be able to explain and differentiate between linear probing, quadratic probing, double hashing, and separate chaining. Understand their advantages and disadvantages.

4. UNDERSTAND CLUSTERING PROBLEM: Linear probing suffers from primary clustering while quadratic probing suffers from secondary clustering. Double hashing eliminates both.

5. TABLE SIZE SELECTION: For division method, prefer prime numbers not close to powers of 2. This reduces patterns in the hash distribution.

6. REHASHING CONDITION: When load factor exceeds 0.7 (for open addressing) or 1.0 (for separate chaining), rehashing becomes necessary.

7. PRACTICE NUMERICAL PROBLEMS: Solve problems involving inserting elements into hash tables and computing probe sequences. This is high-weightage in DU exams.

8. COMPLEXITY ANALYSIS: Remember that with good hash function and load factor maintenance, operations are O(1) on average, but worst case remains O(n) for all methods.

9. APPLICATIONS: Know real-world applications of hashing including symbol tables in compilers, database indexing, caching, and cryptographic hash functions.

10. BE PREPARED TO COMPARE: Questions often ask to compare hashing with other structures like binary search trees. Understand when each is appropriate.