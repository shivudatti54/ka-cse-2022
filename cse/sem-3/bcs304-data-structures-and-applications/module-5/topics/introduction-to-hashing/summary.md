# Introduction to Hashing

## Overview

Hashing is a data structure technique that maps keys to specific indices of a backing array using a hash function, achieving O(1) average-case performance for search, insert, and delete operations. It breaks the O(log n) barrier of comparison-based search methods like binary search trees. Hashing is used in various applications, including symbol tables, database indexing, caches, and deduplication.

## Key Points

- Hashing achieves O(1) average-case performance for search, insert, and delete operations.
- The hash function maps a key to an integer index in a fixed range [0, m-1], where m is the hash table size.
- Common hash function methods include division, multiplication, mid-square, and folding.
- Collisions occur when two different keys map to the same hash table index.
- Collision resolution techniques include separate chaining (open hashing) and open addressing (closed hashing).
- The load factor (alpha = n/m) affects hash table performance, and it's essential to keep it below a certain threshold.
- Hash tables do not support ordered operations like finding minimum, maximum, or range queries.

## Important Definitions

- **Hash value**: The integer index returned by the hash function for a given key.
- **Hash table**: The array that stores key-value pairs, indexed by hash values.
- **Bucket/Slot**: A single position in the hash table array.
- **Collision**: When two different keys produce the same hash value.
- **Load factor (alpha)**: Ratio of number of stored elements to table size (alpha = n/m).
- **Probe**: An attempt to access a bucket during collision resolution (in open addressing).

## Key Formulas / Syntax

- Division method: `h(key) = key % m`
- Multiplication method: `h(key) = floor(m * (key * A mod 1))`
- Mid-square method: `h(key) = (key^2) % m`
- Folding method: `h(key) = (sum of parts of key) % m`

## Comparisons

| Data Structure | Search       | Insert       | Delete       | Space  |
| -------------- | ------------ | ------------ | ------------ | ------ |
| Unsorted Array | O(n)         | O(1)         | O(n)         | O(n)   |
| Sorted Array   | O(log n)     | O(n)         | O(n)         | O(n)   |
| Linked List    | O(n)         | O(1)         | O(n)         | O(n)   |
| Balanced BST   | O(log n)     | O(log n)     | O(log n)     | O(n)   |
| Hash Table     | **O(1) avg** | **O(1) avg** | **O(1) avg** | O(m+n) |

## Exam Tips

- State that hashing achieves O(1) average-case performance but O(n) worst-case.
- Know the division method thoroughly and mention that m should be a prime number.
- Understand and define key terms like hash value, bucket, collision, load factor, and probe.
- Be ready to write a C implementation of a hash table with insert and search operations.
- Know at least two hash function methods with worked examples.
- Distinguish between hash functions used in data structures and cryptographic hash functions.
