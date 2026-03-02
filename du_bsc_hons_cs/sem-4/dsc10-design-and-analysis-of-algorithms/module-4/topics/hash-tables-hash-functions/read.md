# Hash Tables and Hash Functions

## Introduction

Hash tables are one of the most important data structures in computer science, providing efficient average-case time complexity of O(1) for basic operations like insertion, deletion, and lookup. In an era where data volumes are massive and performance is critical, hash tables serve as the backbone of many real-world applications including database indexing, caching mechanisms, symbol tables in compilers, and associative arrays in programming languages.

In this topic, we explore the fundamental concepts of hash tables, the mathematics behind hash functions, and various collision resolution techniques. Understanding these concepts is essential for the Design and Analysis of Algorithms course at DU, as hash tables represent a classic example of the time-space tradeoff in algorithm design. The average-case O(1) performance makes hash tables superior to binary search trees and balanced trees for primary memory operations, though they require additional memory overhead.

This module will cover the theoretical foundations of hashing, practical hash function design, and the analysis of different collision resolution strategies. These concepts frequently appear in DU examinations, with questions testing both conceptual understanding and problem-solving abilities.

## Key Concepts

### 1. Hash Table Fundamentals

A hash table is a data structure that implements an associative array, allowing key-value pairs to be stored and retrieved efficiently. The core idea is to use a hash function that computes an index into an array of buckets or slots, from which the desired value can be found.

**Basic Structure:**
- **Array (Table):** A fixed-size array of size m, where each position is called a slot or bucket
- **Hash Function:** A function h(k) that maps keys to indices in the range [0, m-1]
- **Key Space (U):** The universe of all possible keys
- **Actual Keys (K):** The set of keys actually stored in the hash table

The hash table implements the dictionary abstract data type with operations:
- INSERT(key, value)
- DELETE(key)
- SEARCH(key)

### 2. Properties of Good Hash Functions

A well-designed hash function must satisfy several important properties:

**Uniform Distribution:** The hash function should distribute keys uniformly across all bucket indices. If m is the table size, each bucket should have approximately n/m keys (where n is the number of keys).

**Determinism:** For the same key, the hash function must always return the same index.

**Efficiency:** The hash function should be computationally efficient, ideally O(1).

**Minimize Collisions:** Different keys should map to different indices as much as possible.

### 3. Common Hash Function Methods

**Division Method:**
The hash function is h(k) = k mod m, where m is the table size. The choice of m is crucial—prime numbers not close to powers of 2 are typically better. For example, if m = 12 and k = 100, then h(k) = 4.

**Multiplication Method:**
The hash function is h(k) = ⌊m(kA mod 1)⌋, where A is a constant between 0 and 1. Knuth suggested A = (√5 - 1)/2 ≈ 0.618. This method works well regardless of m.

**Mid-Square Method:**
Square the key and extract the middle digits as the index. For k = 45, k² = 2025; if we extract middle two digits (02), then h(k) = 2.

**Folding Method:**
Split the key into parts and combine them:
- Shift folding: Add the parts (1234 → 12 + 34 = 46)
- Boundary folding: Reverse every part except the first (1234 → 12 + 43 = 55)

**Universal Hashing:**
Select the hash function randomly from a carefully designed family of hash functions. This provides probabilistic guarantees against worst-case behavior.

### 4. Collision Resolution Techniques

When two different keys hash to the same index, a collision occurs. Since the key space is typically larger than the table size, collisions are inevitable (by the pigeonhole principle). Several techniques exist to handle collisions:

#### A. Chaining (Separate Chaining)

In chaining, each bucket is a linked list (or other data structure) that stores all keys hashing to that index. The hash table is an array of pointers to these lists.

**Structure:**
```
Index 0: → [key1] → [key5] → NULL
Index 1: → [key2] → NULL
Index 2: → [key3] → [key7] → [key9] → NULL
Index 3: → [key4] → NULL
...
```

**Performance Analysis:**
- INSERT: O(1) at head or O(1) at tail
- DELETE: O(1) if at head, O(n) otherwise
- SEARCH: O(1 + α) where α = n/m is the load factor

The average case assumes simple uniform hashing: every key is equally likely to hash to any bucket.

#### B. Open Addressing

In open addressing, all elements are stored directly in the hash table itself. When a collision occurs, we probe other positions according to a probe sequence until an empty slot is found.

**Probe Sequences:**
- **Linear Probing:** h(k, i) = (h'(k) + i) mod m
- **Quadratic Probing:** h(k, i) = (h'(k) + c₁i + c₂i²) mod m
- **Double Hashing:** h(k, i) = (h₁(k) + i·h₂(k)) mod m

**Operations in Open Addressing:**
- **INSERT:** Probe until an empty slot is found
- **SEARCH:** Probe until we find the key or reach an empty slot
- **DELETE:** Cannot directly delete (creates gaps); use lazy deletion or rehashing

### 5. Load Factor and Table Resizing

The load factor (α) is a critical parameter: α = n/m, where n is the number of elements and m is the table size.

**Chaining:**
- α can be > 1 (elements can exceed buckets)
- Good performance: α ≈ 1
- As α grows, search time increases

**Open Addressing:**
- α must be < 1 (table must have empty slots)
- Recommended: α ≤ 0.5 for good performance
- When α exceeds threshold, resize and rehash

**Table Resizing:**
When the load factor becomes too high, create a new, larger table (typically 2× size) and rehash all existing elements into the new table. This is an O(n) operation but happens infrequently, maintaining average O(1) operations.

### 6. Perfect Hashing

Perfect hashing guarantees O(1) worst-case lookup time. It uses two levels of hashing:
- First level: Hash to bucket with multiple slots
- Second level: Hash within bucket using a perfect hash function

For static sets, perfect hashing can achieve zero collisions.

## Examples

### Example 1: Division Method with Chaining

**Problem:** Insert keys 15, 25, 35, 45, 55 into a hash table of size 7 using the division method h(k) = k mod 7 and chaining.

**Solution:**
- h(15) = 15 mod 7 = 1 → Bucket 1: [15]
- h(25) = 25 mod 7 = 4 → Bucket 4: [25]
- h(35) = 35 mod 7 = 0 → Bucket 0: [35]
- h(45) = 45 mod 7 = 3 → Bucket 3: [45]
- h(55) = 55 mod 7 = 6 → Bucket 6: [55]

All keys map to different buckets. No collisions occurred in this case.

### Example 2: Linear Probing

**Problem:** Insert keys 10, 22, 31, 4, 15 into a hash table of size 11 using linear probing with h(k) = k mod 11.

**Solution:**
- Insert 10: h(10) = 10 mod 11 = 10 → Index 10
- Insert 22: h(22) = 22 mod 11 = 0 → Index 0
- Insert 31: h(31) = 31 mod 11 = 9 → Index 9
- Insert 4: h(4) = 4 mod 11 = 4 → Index 4
- Insert 15: h(15) = 15 mod 11 = 4 → Collision at index 4!
  - Probe to index 5 → Index 5 is empty → Insert 15 at index 5

Final table:
```
Index:  0   1   2   3   4   5   6   7   8   9   10
Value: 22  --   --   --   4   15  --   --   --   31  10
```

### Example 3: Double Hashing

**Problem:** Using double hashing with table size 13, insert keys 6, 16, 26, 36, 46. Use h₁(k) = k mod 13 and h₂(k) = 7 - (k mod 7).

**Solution:**
- h₁(6) = 6 mod 13 = 6, h₂(6) = 7 - 6 = 1 → Insert 6 at index 6
- h₁(16) = 16 mod 13 = 3, h₂(16) = 7 - 2 = 5 → Insert 16 at index 3
- h₁(26) = 26 mod 13 = 0, h₂(26) = 7 - 5 = 2 → Insert 26 at index 0
- h₁(36) = 36 mod 13 = 10, h₂(36) = 7 - 1 = 6 → Insert 36 at index 10
- h₁(46) = 46 mod 13 = 7, h₂(46) = 7 - 4 = 3
  - Index 7 is empty → Insert 46 at index 7

No collisions required probing for this insertion sequence.

### Example 4: Analyzing Successful Search in Linear Probing

**Problem:** For a hash table with load factor α = 0.5 using linear probing, what is the average successful search time?

**Solution:**
For linear probing with load factor α:
- Average successful search: (1/α) · ln(1/(1-α))
- Average unsuccessful search: (1/α) · (1 + 1/(1-α))

For α = 0.5:
- Successful: (1/0.5) · ln(1/(1-0.5)) = 2 · ln(2) ≈ 2 × 0.693 = 1.386

This demonstrates why maintaining α below 0.5 is important for open addressing.

## Exam Tips

1. **Know the formula for load factor:** α = n/m, where n is the number of elements and m is table size. This is frequently tested in numerical problems.

2. **Time complexities to remember:**
   - Chaining average: O(1 + α)
   - Open addressing average: O(1/(1-α)) for unsuccessful search
   - Worst case for all: O(n)

3. **Linear probing vs. double hashing:** Remember that linear probing suffers from primary clustering, while double hashing eliminates this problem by using a second hash function.

4. **Open addressing load factor:** Unlike chaining, open addressing requires α < 1. If α approaches 1, the table becomes nearly full and operations degrade significantly.

5. **When to use each method:**
   - Chaining: Better when deletions are frequent
   - Open Addressing: Better when load factor is low and deletions are rare
   - Universal Hashing: When worst-case guarantees are needed

6. **Table size selection:** For division method, choose a prime number not close to powers of 2. For multiplication, any m works but powers of 2 are convenient.

7. **Hash function properties:** Be able to identify whether a given hash function satisfies uniformity, determinism, and efficiency.

8. **Remember the birthday paradox:** With n items and m slots, collisions become likely when n ≈ √m. This is important for understanding hash table performance with large datasets.

9. **Rehashing:** When α exceeds threshold (typically 0.5-0.75), double the table size and rehash all elements. This maintains O(1) average operations.

10. **DU Exam Pattern:** Expect numerical problems on insertion sequence, calculating probe positions, and computing average case time complexities.