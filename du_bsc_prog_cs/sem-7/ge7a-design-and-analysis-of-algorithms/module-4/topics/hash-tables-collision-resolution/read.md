# Hash Tables: Collision Resolution Techniques

## Introduction

Hash tables are one of the most efficient data structures for implementing dictionary operations—insert, delete, and search—all of which can be performed in average-case O(1) time. The fundamental idea behind a hash table is to use a hash function that computes an index into an array of buckets or slots, from which the desired value can be found. However, when two or more keys hash to the same index, a **collision** occurs. Since perfect hash functions (those that assign unique indices to every key) are rarely practical, especially when the number of possible keys exceeds the table size, collision resolution becomes a critical aspect of hash table design.

In the University of Delhi's BSc (Hons) Computer Science program, understanding collision resolution techniques is essential not only for theoretical knowledge but also for practical implementation in database systems, compilers, caching mechanisms, and network routing tables. This module explores the two primary approaches to collision resolution—**Open Addressing** and **Chaining**—with detailed analysis of their variants, performance characteristics, and trade-offs.

## Key Concepts

### 1. Hash Table Fundamentals

A hash table consists of:
- **Hash Function (h)**: A function that maps a key 'k' to an index in the hash table. Common hash functions include:
  - Division method: h(k) = k mod m
  - Multiplication method: h(k) = ⌊m(kA mod 1)⌋ where A is a constant
  - Universal hashing: Random selection of hash function from a family

- **Table Size (m)**: The number of buckets in the hash table, typically chosen as a prime number to ensure better distribution.

- **Load Factor (α)**: Defined as α = n/m, where n is the number of elements stored and m is the table size. The load factor determines how full the table is and directly impacts collision probability.

### 2. Collision and Its Inevitability

According to the **pigeonhole principle**, if there are more keys than table slots, collisions are unavoidable. Even with a good hash function, collisions occur due to:
- Multiple keys mapping to the same hash value (primary clustering)
- Keys mapping to positions already occupied during probing (secondary clustering)

### 3. Collision Resolution Techniques

#### A. Open Addressing (Closed Hashing)

In open addressing, all elements are stored directly in the hash table itself. When a collision occurs, the algorithm probes (searches) for the next available slot using a predefined sequence.

**Linear Probing:**
The simplest form of probing where if slot h(k) is occupied, we check h(k)+1, h(k)+2, ... wrapping around the table.
- Probe sequence: h(k), h(k)+1, h(k)+2, ..., h(k)+m-1
- Index formula: (h(k) + i) mod m for i = 0, 1, 2, ...
- Suffers from **primary clustering**: long runs of occupied slots form, making insertions slower.

**Quadratic Probing:**
Uses a quadratic function to generate probe sequences, reducing clustering.
- Probe sequence: h(k), h(k)+1², h(k)+2², h(k)+3², ...
- Index formula: (h(k) + i²) mod m for i = 0, 1, 2, ...
- Condition for guaranteed insertion: Table size must be prime, and α < 0.5
- Reduces primary clustering but may suffer from **secondary clustering** (keys hashing to same initial position follow same sequence).

**Double Hashing:**
Uses a secondary hash function to determine the probe increment, eliminating both primary and secondary clustering.
- Probe sequence: h(k), h(k)+h₂(k), h(k)+2h₂(k), ...
- Primary hash: h₁(k) = k mod m
- Secondary hash: h₂(k) = prime - (k mod prime), where prime < m
- Index formula: (h₁(k) + i × h₂(k)) mod m for i = 0, 1, 2, ...

#### B. Chaining (Open Hashing)

In chaining, each bucket in the hash table contains a linked list (or another data structure) of all keys that hash to that index. This approach allows multiple elements to occupy the same bucket without probing.

- Insertion: O(1) at the head of the list (or tail for ordered insertion)
- Search: O(α) average case, where α is the load factor
- Deletion: O(1) given a pointer to the element
- Performance degrades gracefully as load factor increases

**Variants of Chaining:**
- **Simple Chaining**: Linked list implementation
- **Self-organizing Chaining**: Move-to-front, transpose method
- **Balanced BST Chaining**: When load factor is high, use AVL or Red-Black trees for O(log n) worst-case search

### 4. Performance Analysis

| Technique | Average Case | Worst Case | Space |
|-----------|--------------|------------|-------|
| Linear Probing | O(1/(1-α)) | O(n) | O(m) |
| Quadratic Probing | O(1/(1-α)) | O(n) | O(m) |
| Double Hashing | O(1/(1-α)) | O(n) | O(m) |
| Chaining | O(1+α) | O(n) | O(n+m) |

**Note**: For open addressing, best performance is achieved when α < 0.5. For chaining, acceptable performance continues until α ≈ 1, after which rehashing becomes necessary.

### 5. Rehashing

When the load factor exceeds a threshold (typically 0.7 for open addressing, 1.0 for chaining), the hash table is resized—typically doubled—and all existing elements are re-inserted into the new table using the new table size. This process is called **rehashing** or **rehashing**.

## Examples

### Example 1: Linear Probing

Consider a hash table of size 10 (m=10) using hash function h(k) = k mod 10. Insert the following sequence: 35, 25, 45, 55, 15

**Step-by-step insertion:**

- **Insert 35**: h(35) = 35 mod 10 = 5 → Index 5 is empty. Insert 35 at index 5.

- **Insert 25**: h(25) = 25 mod 10 = 5 → Index 5 is occupied (35). Probe to index 6. Index 6 is empty. Insert 25 at index 6.

- **Insert 45**: h(45) = 45 mod 10 = 5 → Index 5 is occupied (35). Probe to index 6 (occupied by 25). Probe to index 7. Index 7 is empty. Insert 45 at index 7.

- **Insert 55**: h(55) = 55 mod 10 = 5 → Index 5 occupied, 6 occupied, 7 occupied. Probe to index 8. Empty. Insert 55 at index 8.

- **Insert 15**: h(15) = 15 mod 10 = 5 → Indices 5,6,7,8 all occupied. Probe to index 9. Empty. Insert 15 at index 9.

**Final Table:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|
| Value |  |  |  |  |  | 35 | 25 | 45 | 55 | 15 |

### Example 2: Double Hashing

Using the same sequence with table size 10 and:
- h₁(k) = k mod 10
- h₂(k) = 7 - (k mod 7) [where prime = 7]

**Insert 35**: h₁(35) = 5, h₂(35) = 7 - 0 = 7. Try index 5 (empty). Insert 35.

**Insert 25**: h₁(25) = 5, h₂(25) = 7 - 4 = 3. Index 5 occupied. Try (5 + 3) mod 10 = 8. Empty. Insert 25 at index 8.

**Insert 45**: h₁(45) = 5, h₂(45) = 7 - 3 = 4. Index 5 occupied. Try (5 + 4) mod 10 = 9. Empty. Insert 45 at index 9.

**Insert 55**: h₁(55) = 5, h₂(55) = 7 - 6 = 1. Index 5 occupied. Try (5 + 1) = 6. Empty. Insert 55 at index 6.

**Insert 15**: h₁(15) = 5, h₂(15) = 7 - 1 = 6. Index 5 occupied. Try (5 + 6) = 1. Empty. Insert 15 at index 1.

**Final Table:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|
| Value |  | 15 |  |  |  | 35 | 55 |  | 25 | 45 |

Notice how double hashing distributes elements more uniformly than linear probing.

### Example 3: Chaining

Using table size 10 with h(k) = k mod 10, insert: 35, 25, 45, 55, 15, 5

**Bucket 5**: 35 → NULL
**After inserting 25**: Bucket 5: 25 → 35 → NULL
**After inserting 45**: Bucket 5: 25 → 35 → 45 → NULL
**After inserting 55**: Bucket 5: 25 → 35 → 45 → 55 → NULL
**After inserting 15**: Bucket 5: 15 → 25 → 35 → 45 → 55 → NULL
**After inserting 5**: Bucket 5: 5 → 15 → 25 → 35 → 45 → 55 → NULL

All elements ending in digit 5 are chained in bucket 5, demonstrating how chaining handles collisions gracefully.

## Exam Tips

1. **Know the formula for load factor**: α = n/m. Remember that optimal performance for open addressing requires α < 0.5.

2. **Understand why double hashing is preferred**: It eliminates both primary and secondary clustering by using a secondary hash function for probe increment.

3. **Remember the worst-case scenario for open addressing**: When α approaches 1 (table is full), search can degrade to O(n).

4. **Chaining vs Open Addressing**: Chaining is simpler to implement, handles deletions easily, and performance degrades gracefully. Open addressing has better cache performance due to sequential memory access.

5. **Quadratic probing limitation**: Not all table slots may be probed. Guarantee of finding an empty slot exists only when table size is prime and α < 0.5.

6. **Time complexity comparison**: For successful search - Linear/Quadratic/Double: O(1/(1-α)), Chaining: O(1+α). For unsuccessful search - All techniques: O(1/(1-α)) for open addressing, O(1+α) for chaining.

7. **Rehashing importance**: When resizing, choose new table size as approximately twice the old size (or prime near it) to maintain good hash distribution.