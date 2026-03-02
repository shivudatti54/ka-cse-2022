# HASHING

## Introduction

Hashing is one of the most fundamental and widely used techniques in computer science for efficient data retrieval. At its core, hashing is a method that converts a large, potentially unbounded set of keys into a smaller, fixed-size range of indices, typically an array index. This transformation is accomplished using a special function called a hash function. The primary goal of hashing is to achieve constant-time O(1) average-case complexity for search, insert, and delete operations, making it indispensable for applications requiring fast data access.

The importance of hashing in modern computing cannot be overstated. It forms the backbone of database indexing, cryptographic security, compiler symbol tables, cache implementations, and distributed systems. When you use a dictionary or set in Python, or when you look up a contact in your phone, hashing is working behind the scenes to provide near-instantaneous results. In the context of the University of Delhi's Computer Science curriculum, understanding hashing is essential not only for theoretical knowledge but also for practical software development skills.

This chapter explores hashing in depth, covering hash functions, collision resolution techniques, static and dynamic hashing, and the trade-offs involved in choosing different approaches. We will examine both the mathematical foundations and practical implementations, with particular attention to how these concepts apply to real-world scenarios that you may encounter in your professional careers.

## Key Concepts

### Hash Function

A hash function is a mathematical function that maps keys (or values) to array indices. The fundamental requirement for a good hash function is that it should distribute keys uniformly across the hash table to minimize collisions. A collision occurs when two different keys hash to the same index.

The ideal hash function satisfies three properties: it must be deterministic (the same input always produces the same output), it should distribute keys uniformly, and it should be computationally efficient. Several common hash function approaches exist in practice.

The division method is perhaps the simplest approach, where the hash function is h(k) = k mod m, with m being the size of the hash table. The choice of m is critical—prime numbers not close to powers of 2 are typically preferred to avoid patterns in key distributions. For example, if storing 2000 elements, choosing m = 2003 (a prime near 2000) would be better than m = 2000.

The multiplication method uses the formula h(k) = floor(m(kA mod 1)), where A is a constant between 0 and 1. Knuth's suggested value for A is (√5 - 1)/2 ≈ 0.6180339887. This method performs well regardless of the table size and is particularly effective for keys that are strings or floating-point numbers.

For string keys, polynomial hash functions are commonly used, where characters are treated as coefficients of a polynomial. The formula might be: h(s) = (s[0]·a^(n-1) + s[1]·a^(n-2) + ... + s[n-1]) mod m, where a is a constant and n is the string length.

### Collision Resolution Techniques

When the hash table inevitably encounters collisions (due to the pigeonhole principle, which states that if n items are placed into m containers and n > m, at least one container must hold more than one item), we need strategies to handle them. There are two primary categories: separate chaining and open addressing.

Separate Chaining is the simpler approach conceptually. Each bucket in the hash table is a linked list (or other dynamic structure) that stores all keys hashing to that bucket. When inserting a key, we compute its hash value, traverse to the corresponding bucket, and append the key to the list. To search, we compute the hash and then traverse the list at that bucket. The average case complexity for operations is O(1 + α), where α = n/m is the load factor (ratio of elements to buckets). When α becomes too large (typically > 1), we resize the table to maintain efficiency.

Open Addressing is an alternative where all elements are stored directly in the table itself. When a collision occurs, we probe the table systematically until an empty slot is found. The sequence of positions probed depends on the probing strategy.

Linear probing uses the formula h(k, i) = (h'(k) + i) mod m, where i is the probe number (0, 1, 2, ...) and h' is the initial hash function. While simple, linear probing suffers from primary clustering, where large contiguous blocks of occupied slots form, causing increasingly longer searches.

Quadratic probing improves upon linear probing by using: h(k, i) = (h'(k) + c₁i + c₂i²) mod m, where c₁ and c₂ are constants. This reduces primary clustering but may not guarantee finding an empty slot even when one exists.

Double hashing uses a secondary hash function to compute the probe increment: h(k, i) = (h₁(k) + i·h₂(k)) mod m. This effectively eliminates primary clustering and provides good distribution. A common choice is h₂(k) = q - (k mod q), where q is a prime smaller than m.

### Static vs Dynamic Hashing

Static hashing uses a fixed-size hash table. Once the table is full or the load factor exceeds a threshold, the table must be resized (typically doubled), and all existing elements must be rehashed into the new table. This rehashing operation is expensive (O(n)) but occurs infrequently.

Dynamic hashing, also known as extendible hashing or linear hashing, allows the hash table to grow and shrink dynamically without requiring complete rehashing. In extendible hashing, the directory (array of bucket pointers) expands by doubling, but only buckets that overflow need to split, and this splitting can be done incrementally.

Extendible hashing uses a global depth and local depth. The global depth determines the number of bits used to index into the directory, while the local depth indicates how many bits distinguish keys within a bucket. When a bucket overflows, it splits into two buckets, and the local depth is incremented. If the local depth equals the global depth, the directory must also double in size.

Linear hashing is another dynamic approach where buckets are split in a round-robin fashion regardless of overflow. A load factor threshold triggers splits, and a pointer tracks the next bucket to split. This method provides predictable performance and eliminates the need for a directory, making it more space-efficient for certain applications.

### Load Factor and Table Sizing

The load factor (α = n/m) is a critical parameter in hash table performance. For separate chaining, α can be greater than 1, but performance degrades when α exceeds 3-5. For open addressing, α must be kept below 0.5-0.7 to maintain acceptable probe lengths; once α exceeds 0.5, performance deteriorates rapidly.

When implementing hash tables, it's standard practice to resize the table when α exceeds a threshold (commonly 0.75 for open addressing, 1.0 for separate chaining). The new table size is typically chosen as the smallest prime greater than twice the current size to maintain good distribution properties.

### Universal Hashing

To guarantee good average-case performance regardless of the input keys, universal hashing selects the hash function randomly from a family of functions. A family H of hash functions is universal if, for any two distinct keys x and y, the probability that h(x) = h(y) is at most 1/m, where h is chosen uniformly at random from H.

This randomized approach provides probabilistic guarantees that the expected performance will be good, even for adversarial inputs. The theory of universal hashing is fundamental to understanding how hash tables can provide consistent performance in theory and practice.

## Examples

### Example 1: Division Method with Linear Probing

Consider inserting the keys {23, 42, 15, 77, 89} into a hash table of size m = 11 using the hash function h(k) = k mod 11 and linear probing for collision resolution.

Initially, all buckets are empty.

Insert 23: h(23) = 23 mod 11 = 1. Bucket 1 is empty, so place 23 there.

Insert 42: h(42) = 42 mod 11 = 9. Bucket 9 is empty, so place 42 there.

Insert 15: h(15) = 15 mod 11 = 4. Bucket 4 is empty, so place 15 there.

Insert 77: h(77) = 77 mod 11 = 0. Bucket 0 is empty, so place 77 there.

Insert 89: h(89) = 89 mod 11 = 1. Bucket 1 is already occupied (by 23), so probe to bucket 2. Bucket 2 is empty, so place 89 there.

Final table (index: value): 0→77, 1→23, 2→89, 3→empty, 4→15, 5→empty, 6→empty, 7→empty, 8→empty, 9→42, 10→empty

Now, search for key 89: Compute h(89) = 1. Bucket 1 contains 23, not 89. Proceed to bucket 2, which contains 89. Found in 2 probes.

Search for key 42: Compute h(42) = 9. Bucket 9 contains 42. Found in 1 probe.

### Example 2: Separate Chaining

Using the same keys {23, 42, 15, 77, 89} with a hash table of size m = 7 and hash function h(k) = k mod 7, with separate chaining:

Insert 23: h(23) = 23 mod 7 = 2. Bucket 2: [23]
Insert 42: h(42) = 42 mod 7 = 0. Bucket 0: [42]
Insert 15: h(15) = 15 mod 7 = 1. Bucket 1: [15]
Insert 77: h(77) = 77 mod 7 = 0. Bucket 0: [42 → 77] (insert at head)
Insert 89: h(89) = 89 mod 7 = 5. Bucket 5: [89]

Final table: Bucket 0: 42→77, Bucket 1: 15, Bucket 2: 23, Bucket 3: empty, Bucket 4: empty, Bucket 5: 89, Bucket 6: empty

Load factor α = 5/7 ≈ 0.71

Search for 77: h(77) = 0. Traverse bucket 0: 42 (not 77) → 77 (found). Average chain length is 5/7 ≈ 0.71, so average search takes about 1.71 comparisons.

### Example 3: Double Hashing

Insert keys {12, 28, 35, 49, 56} into a table of size m = 13 using primary hash h₁(k) = k mod 13 and secondary hash h₂(k) = 7 - (k mod 7). The probe sequence is: h₁(k) + i·h₂(k) mod 13.

Insert 12: h₁(12) = 12, h₂(12) = 7 - 5 = 2. Probe 0: position 12. Empty, place 12.

Insert 28: h₁(28) = 2, h₂(28) = 7 - 0 = 7. Probe 0: position 2. Empty, place 28.

Insert 35: h₁(35) = 9, h₂(35) = 7 - 0 = 7. Probe 0: position 9. Empty, place 35.

Insert 49: h₁(49) = 10, h₂(49) = 7 - 0 = 7. Probe 0: position 10. Empty, place 49.

Insert 56: h₁(56) = 4, h₂(56) = 7 - 0 = 7. Probe 0: position 4. Empty, place 56.

All insertions succeed without collisions because the keys happened to hash to different primary positions. The power of double hashing becomes apparent when collisions occur, as it spreads the probes more uniformly than linear probing.

## Exam Tips

1. Remember that in open addressing, deletion is tricky—if you remove an element that lies between other elements in a probe sequence, you may break the search path for those elements. Use tombstones (marked deleted slots) instead of actually removing elements.

2. The load factor threshold for open addressing is typically 0.5; beyond this, performance degrades significantly. For separate chaining, you can allow higher load factors (up to 1.0 or more).

3. In the exam, always specify which collision resolution technique you're using when solving problems about hash table insertion or search operations.

4. Double hashing is generally preferred over linear and quadratic probing because it eliminates primary clustering and provides better distribution of probe sequences.

5. For string hashing, remember that the base (constant multiplier) should typically be a prime number, and modular arithmetic must be applied at each step to prevent integer overflow.

6. The expected number of probes for successful search in open addressing with load factor α is approximately (1/α)·ln(1/(1-α)), and for unsuccessful search it is (1/(1-α)).

7. Universal hashing guarantees O(1) expected time for any set of keys, providing protection against worst-case inputs. This is particularly relevant in competitive programming and security-sensitive applications.

8. When comparing static and dynamic hashing, remember that static hashing is simpler to implement but requires rehashing during resizing, while dynamic hashing avoids rehashing but has more complex index management.

9. The choice of table size m should generally be a prime number for the division method to avoid keys with certain patterns clustering in specific buckets.

10. In extendible hashing, remember that the directory doubles when a bucket's local depth equals the global depth, and all buckets that split will have their local depth increased by one.