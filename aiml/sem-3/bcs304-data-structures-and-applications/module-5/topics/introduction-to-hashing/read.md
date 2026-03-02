# Introduction to Hashing


## Table of Contents

- [Introduction to Hashing](#introduction-to-hashing)
- [1. Motivation: Why We Need Hashing](#1-motivation-why-we-need-hashing)
- [2. The Dictionary ADT / Symbol Table](#2-the-dictionary-adt--symbol-table)
- [3. Hash Function: Formal Definition](#3-hash-function-formal-definition)
  - [Properties of a Good Hash Function](#properties-of-a-good-hash-function)
  - [The Simple Uniform Hashing Assumption (SUHA)](#the-simple-uniform-hashing-assumption-suha)
- [4. Common Hash Function Methods](#4-common-hash-function-methods)
  - [4.1 Division Method](#41-division-method)
  - [4.2 Multiplication Method](#42-multiplication-method)
  - [4.3 Mid-Square Method](#43-mid-square-method)
  - [4.4 Folding Method](#44-folding-method)
  - [4.5 String Hashing](#45-string-hashing)
- [5. The Hash Table Data Structure](#5-the-hash-table-data-structure)
- [6. Collision Resolution](#6-collision-resolution)
  - [6.1 Separate Chaining](#61-separate-chaining)
  - [6.2 Open Addressing](#62-open-addressing)
  - [6.3 Complexity Analysis Under SUHA](#63-complexity-analysis-under-suha)
- [7. Load Factor and Rehashing](#7-load-factor-and-rehashing)
- [8. Key Terminology](#8-key-terminology)
- [9. Summary](#9-summary)
- [10. Assessment Questions](#10-assessment-questions)
  - [Question 1 (Hard - Numerical Analysis)](#question-1-hard---numerical-analysis)
  - [Question 2 (Hard - Application)](#question-2-hard---application)
  - [Question 3 (Hard - Analysis)](#question-3-hard---analysis)

## 1. Motivation: Why We Need Hashing

The efficiency of traditional searching algorithms is fundamentally constrained by the comparison-based paradigm. In **unsorted arrays**, linear search exhibits O(n) time complexity, requiring examination of every element in the worst case. **Sorted arrays** enable binary search with O(log n) complexity by repeatedly halving the search space, but insertion and deletion require O(n) time due to shifting elements. **Binary Search Trees (BSTs)** provide O(log n) average-case performance for search, insert, and delete operations when balanced, yet degrade to O(n) in the worst case when the tree becomes skewed.

All these methods share a critical limitation: they depend on **key comparisons** to navigate the data structure. Information-theoretic lower bounds establish that comparison-based search cannot achieve better than O(log n) time complexity in the worst case. Hashing fundamentally transcends this barrier by employing a radically different paradigm—rather than comparing keys, we **compute** the storage location directly through arithmetic operations.

| Data Structure | Search (Avg) | Search (Worst) | Insert (Avg) | Delete (Avg) |
| -------------- | ------------ | -------------- | ------------ | ------------ |
| Unsorted Array | O(n)         | O(n)           | O(1)         | O(n)         |
| Sorted Array   | O(log n)     | O(log n)       | O(n)         | O(n)         |
| Balanced BST   | O(log n)     | O(log n)       | O(log n)     | O(log n)     |
| **Hash Table** | **O(1)**     | O(n)           | **O(1)**     | **O(1)**     |

## 2. The Dictionary ADT / Symbol Table

Hashing serves as the preferred implementation for the **Dictionary** (or **Symbol Table**) Abstract Data Type. A dictionary maintains a collection of key-value pairs and supports three fundamental operations:

- **Insert(key, value)**: Adds a new key-value pair; if the key exists, updates its value
- **Search(key)**: Retrieves the value associated with a given key, or indicates absence
- **Delete(key)**: Removes the key-value pair corresponding to the specified key

Practical applications include compiler symbol tables (mapping variable identifiers to memory addresses and type information), database indexing systems, routing tables, and in-memory caches.

## 3. Hash Function: Formal Definition

A **hash function** is a deterministic mapping `h: U → [0, m-1]` from the universe of possible keys `U` to a finite set of integer indices, where `m` denotes the hash table size.

### Properties of a Good Hash Function

A well-designed hash function must satisfy three critical properties:

1. **Determinism**: For any given key `k`, the hash function must always return the same index `h(k)`. This is essential for retrievability.

2. **Uniformity**: The hash function should distribute keys uniformly across all table slots. If `P(k)` denotes the probability of key `k` being accessed, then for an ideal hash function, the expected number of keys mapping to each slot equals `n/m`, where `n` is the number of stored keys.

3. **Efficiency**: Computation of `h(k)` should be O(1) for practical applications. Hash functions involving complex cryptographic operations are unsuitable for standard data structure applications.

### The Simple Uniform Hashing Assumption (SUHA)

Theoretical analysis of hash table performance typically assumes **Simple Uniform Hashing**, which posits that any key is equally likely to hash to any of the `m` slots, independent of all other keys. While this assumption rarely holds in practice, it provides tractable analytical results that closely approximate real-world performance.

## 4. Common Hash Function Methods

### 4.1 Division Method

The division method computes the hash value as the remainder when the key is divided by the table size:

```
h(k) = k mod m
```

**Critical Selection Criterion**: The choice of `m` significantly impacts performance. Optimal choices include:

- Prime numbers not close to powers of 2
- Prime numbers that avoid systematic patterns in key generation

**Reasoning**: If `m = 2^p`, then `h(k)` depends only on the lower `p` bits of `k`, potentially creating clustering patterns. Prime numbers distribute keys more uniformly across the range.

**Example**: For `m = 13`:

- `h(25) = 25 mod 13 = 12`
- `h(100) = 100 mod 13 = 9`
- `h(273) = 273 mod 13 = 0`

### 4.2 Multiplication Method

The multiplication method leverages the fractional part of key multiplication:

```
h(k) = ⌊m × (kA mod 1)⌋
```

where `A` is a constant in `(0,1)`. Knuth's research established that `A ≈ 0.6180339887` (the golden ratio conjugate, φ⁻¹ = (√5 - 1)/2) provides optimal distribution.

**Example**: For `k = 123456`, `m = 10000`, `A = 0.6180339887`:

- `kA = 123456 × 0.6180339887 = 76300.0041...`
- Fractional part: `0.0041...`
- `h(k) = ⌊10000 × 0.0041⌋ = 41`

### 4.3 Mid-Square Method

The mid-square method squares the key and extracts middle digits:

1. Compute `k²`
2. Extract middle `r` digits
3. Apply modulo `m`

**Example**: `k = 4321`

- `k² = 18671041`
- Middle 2 digits: `71`
- `h(k) = 71 mod m`

### 4.4 Folding Method

Folding partitions the key into equal parts and sums them:

**Example**: Key `9876543210` with 3-digit parts:

- Parts: `987`, `654`, `321`, `0`
- Sum: `987 + 654 + 321 + 0 = 1962`
- `h(k) = 1962 mod m`

### 4.5 String Hashing

For string keys, a polynomial accumulation function provides excellent distribution:

```c
int hashString(const char *key, int m) {
    int hash = 0;
    int prime = 31;  // Common prime multiplier
    while (*key) {
        hash = (hash * prime + *key) % m;
        key++;
    }
    return hash;
}
```

The prime multiplier (typically 31 or 37) ensures that character positions contribute differently, avoiding collisions from character permutation.

## 5. The Hash Table Data Structure

A **hash table** is a fixed-size array of `m` buckets, where each bucket can store one or more key-value pairs. The index for any key is computed via the hash function.

```
Hash Table (m = 7):
Index:    [0]    [1]    [2]    [3]    [4]    [5]    [6]
Bucket:   |  |   |  |   |  |   |  |   |  |   |  |   |  |
          +----+-------+----+-------+----+-------+----+

Insert(15, "Alice"): h(15) = 15 mod 7 = 1 → Store at index 1
Insert(23, "Bob"):   h(23) = 23 mod 7 = 2 → Store at index 2
Insert(8, "Carol"):  h(8)  =  8 mod 7 = 1 → Collision with 15!
```

## 6. Collision Resolution

A **collision** occurs when distinct keys `k₁ ≠ k₂` produce identical hash values: `h(k₁) = h(k₂)`. Since the domain of keys typically exceeds the table size, collisions are inevitable—this is formalized in the **pigeonhole principle**. Effective collision resolution is crucial for maintaining O(1) average-case performance.

### 6.1 Separate Chaining

Separate chaining maintains a linked list (or dynamic array) at each bucket to store all keys mapping to that index.

**Data Structure**:

```c
typedef struct Node {
    int key;
    int value;
    struct Node *next;
} Node;

typedef struct {
    Node *buckets[TABLE_SIZE];
    int size;
} ChainedHashTable;
```

**Operations Complexity** (under SUHA):

- Search (successful): θ(1 + α) ≈ θ(α)
- Search (unsuccessful): θ(1 + α) ≈ θ(α)
- Insert: O(1)
- Delete: θ(1 + α)

where **load factor** α = n/m denotes the average number of elements per bucket.

### 6.2 Open Addressing

Open addressing stores all elements directly within the table array. When a collision occurs, we probe alternative positions until an empty slot is found.

**Probe Sequence**: For a key `k`, we generate a sequence of probe positions `h(k, 0), h(k, 1), h(k, 2), ...` where `h(k, i)` denotes the i-th probe for key `k`.

#### Linear Probing

```
h(k, i) = (h'(k) + i) mod m
```

The probe sequence examines consecutive slots. While cache-friendly, linear probing suffers from **primary clustering**—long runs of occupied slots tend to grow longer, degrading performance.

**Example**: Table size m = 13, inserting keys 18, 41, 22, 44, 59, 32:

- `h(18) = 5`, insert at [5]
- `h(41) = 2`, insert at [2]
- `h(22) = 9`, insert at [9]
- `h(44) = 5` → collision with 18, probe [6], insert at [6]
- `h(59) = 7`, insert at [7]
- `h(32) = 6` → collision with 44, probe [7] → collision with 59, probe [8], insert at [8]

#### Quadratic Probing

```
h(k, i) = (h'(k) + c₁i + c₂i²) mod m
```

Common choices: `c₁ = c₂ = 1/2`, yielding:

```
h(k, i) = (h'(k) + i/2 + i²/2) mod m
```

Quadratic probing mitigates primary clustering but introduces **secondary clustering**—keys mapping to the same initial slot follow identical probe sequences.

#### Double Hashing

Double hashing uses a secondary hash function to compute the probe increment:

```
h(k, i) = (h₁(k) + i × h₂(k)) mod m
```

where `h₁(k) = k mod m` and `h₂(k) = prime - (k mod prime)` with `prime < m`.

**Critical Requirement**: `h₂(k)` must be relatively prime to `m` for the probe sequence to visit all slots. Choosing `m` as prime and `prime = m-1` guarantees this property.

### 6.3 Complexity Analysis Under SUHA

**Theorem**: Under Simple Uniform Hashing, the expected number of probes for successful search in open addressing with load factor α = n/m is:

```
θ(1/(1-α))
```

**Proof Sketch**: Consider the probability that the i-th probe finds an occupied slot. After i-1 unsuccessful probes, the table has (n-i+1) occupied slots among (m-i+1) remaining slots. The probability of the i-th probe succeeding is (n-i+1)/(m-i+1). Summing the expected probe count yields the harmonic series approximation:

```
E[probes] ≈ 1/(1-α) for α < 1
```

**Asymptotic Behavior**:

- α = 0.5: Expected probes ≈ 2
- α = 0.9: Expected probes ≈ 10
- α → 1: Probes → ∞ (table saturation)

**Recommendation**: Maintain α ≤ 0.5 for linear probing, α ≤ 0.75 for general open addressing.

## 7. Load Factor and Rehashing

The **load factor** α = n/m critically determines hash table performance. As α approaches 1, collision frequency increases dramatically.

**Rehashing**: When α exceeds a threshold (typically 0.7-0.75), we allocate a new, larger table (typically 2× the size) and reinsert all elements using a new hash function.

```c
void rehash(HashTable *ht) {
    int oldSize = ht->size;
    Entry *oldTable = ht->table;

    ht->size = oldSize * 2;
    ht->table = calloc(ht->size, sizeof(Entry));
    ht->count = 0;

    for (int i = 0; i < oldSize; i++) {
        if (oldTable[i].key != EMPTY) {
            insert(ht, oldTable[i].key, oldTable[i].value);
        }
    }
    free(oldTable);
}
```

## 8. Key Terminology

| Term                      | Definition                                                     |
| ------------------------- | -------------------------------------------------------------- |
| **Hash value**            | Integer index returned by hash function for a given key        |
| **Hash table**            | Array storing key-value pairs indexed by hash values           |
| **Bucket/Slot**           | Individual position in the hash table array                    |
| **Collision**             | When distinct keys produce identical hash values               |
| **Probe**                 | Attempted access to a bucket during collision resolution       |
| **Load factor (α)**       | Ratio n/m of stored elements to table capacity                 |
| **Rehashing**             | Rebuilding table with larger capacity when α exceeds threshold |
| **Perfect hash function** | Injective mapping for a specific, static key set               |
| **Universal hashing**     | Random selection from family of hash functions                 |

## 9. Summary

Hashing achieves O(1) average-case performance for dictionary operations by computing storage locations directly through hash functions, bypassing the comparison-based search barrier. Key insights include:

1. The **simple uniform hashing assumption** enables tractable average-case analysis
2. **Collision resolution strategies** (separate chaining vs. open addressing) trade memory overhead for cache performance
3. **Load factor management** through rehashing maintains acceptable collision rates
4. **Good hash function design** requires uniformity, determinism, and O(1) computation

---

## 10. Assessment Questions

### Question 1 (Hard - Numerical Analysis)

A hash table of size m = 13 uses linear probing. Keys are inserted in the order: 18, 31, 52, 77, 23, 41. After each insertion, what is the average number of probes required? If the table is 75% full and uses quadratic probing with h(k,i) = (k mod 13 + i²) mod 13, what is the expected number of probes for an unsuccessful search?

### Question 2 (Hard - Application)

Given h₁(k) = k mod 17 and h₂(k) = 13 - (k mod 13) for double hashing in a table of size 17, compute the probe sequence for key k = 45. Show all probe positions until insertion succeeds or failure is determined.

### Question 3 (Hard - Analysis)

Prove that under Simple Uniform Hashing, the expected number of probes for unsuccessful search with linear probing is approximately 1/(2)(1 - α)² when load factor α < 1. Explain why this is worse than the general bound of 1/(1-α).
