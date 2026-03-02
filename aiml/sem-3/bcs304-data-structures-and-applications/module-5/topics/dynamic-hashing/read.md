# Dynamic Hashing


## Table of Contents

- [Dynamic Hashing](#dynamic-hashing)
- [1. Introduction](#1-introduction)
- [2. Limitations of Static Hashing](#2-limitations-of-static-hashing)
- [3. Extendible Hashing](#3-extendible-hashing)
  - [3.1 Conceptual Framework](#31-conceptual-framework)
  - [3.2 Formal Hash Function Specification](#32-formal-hash-function-specification)
  - [3.3 Insertion Algorithm](#33-insertion-algorithm)
  - [3.4 Bucket Splitting: Rigorous Analysis](#34-bucket-splitting-rigorous-analysis)
  - [3.5 Comprehensive Worked Example](#35-comprehensive-worked-example)
  - [3.6 Complexity Analysis](#36-complexity-analysis)
  - [3.7 C Data Structure Implementation](#37-c-data-structure-implementation)
- [4. Linear Hashing](#4-linear-hashing)
  - [4.1 Motivation and Overview](#41-motivation-and-overview)
  - [4.2 Fundamental Principles](#42-fundamental-principles)
  - [4.3 Insertion Algorithm](#43-insertion-algorithm)
  - [4.4 Search Algorithm](#44-search-algorithm)
  - [4.5 Example Illustration](#45-example-illustration)
  - [4.6 Performance Characteristics](#46-performance-characteristics)
- [5. Comparative Analysis](#5-comparative-analysis)
- [6. Conclusion](#6-conclusion)
- [7. Assessment Questions](#7-assessment-questions)
  - [Question 1 (Application Level)](#question-1-application-level)
  - [Question 2 (Analysis Level)](#question-2-analysis-level)
  - [Question 3 (Numerical Problem)](#question-3-numerical-problem)
  - [Question 4 (Comparative Analysis)](#question-4-comparative-analysis)

## 1. Introduction

Static hashing techniques, including open addressing (linear probing, quadratic probing, double hashing) and separate chaining, employ a fixed-size hash table determined at initialization. When the number of records grows significantly beyond the initial table capacity, performance degrades substantially due to increased collision frequency. The conventional solution—rehashing all existing records into a larger table—incurs O(n) computational cost, making it impractical for large-scale database applications. **Dynamic hashing** encompasses a family of techniques that permit the hash structure to expand and contract incrementally, avoiding complete table reorganization while maintaining efficient access times.

This document examines two principal dynamic hashing methodologies: **Extendible Hashing** and **Linear Hashing**, providing formal analysis, algorithmic specifications, and comparative evaluation suitable for standard-level students.

## 2. Limitations of Static Hashing

Understanding the deficiencies of static hashing establishes the theoretical foundation for dynamic approaches:

**Definition 2.1 (Load Factor):** For a hash table with $n$ records and $m$ slots, the load factor is defined as $\alpha = n/m$.

**Theorem 2.1:** In static hashing with separate chaining, the expected search cost (average number of probes) is $\Theta(1 + \alpha)$, where $\alpha$ is the load factor.

_Proof:_ In separate chaining, the expected chain length is $\alpha = n/m$. Searching requires traversing the chain, giving expected cost $1 + \alpha$. For open addressing, the expected cost is approximately $1/(1-\alpha)$ when uniformly distributed. As $\alpha \to 1$, costs approach infinity. ∎

The limitations include:

1. **Fixed Address Space:** The table size $m$ is established during initialization. Growth beyond initial estimates causes $\alpha$ to exceed optimal thresholds (typically 0.7-0.8), degrading performance.

2. **Expensive Rehashing:** When $\alpha$ exceeds acceptable bounds, rehashing requires computing new hash values for all $n$ existing records and reinserting them into a table of size $m' > m$. This incurs $\Theta(n)$ time complexity, causing unacceptable latency spikes in production systems.

3. **Memory Inefficiency:** Pre-allocating a sufficiently large table for maximum projected data wastes memory when actual storage remains significantly below capacity.

4. **Unpredictable Data Growth:** Database applications frequently encounter variable data volumes, making optimal initial sizing impossible.

## 3. Extendible Hashing

### 3.1 Conceptual Framework

Extendible hashing, introduced by Fagin et al. (1979), combines directory-based indexing with bucket-oriented storage to achieve dynamic growth. The structure employs two levels:

**Definition 3.1 (Bucket):** A bucket is a fixed-capacity storage unit (typically one disk page) capable of holding a predetermined number of records.

**Definition 3.2 (Directory):** The directory is an array of size $2^d$, where $d$ denotes the global depth, containing pointers to buckets.

**Definition 3.3 (Global Depth):** The global depth $d$ represents the number of leading bits of the hash value employed to index into the directory.

**Definition 3.4 (Local Depth):** The local depth $d'$ of a bucket denotes the number of leading bits that uniquely identify records within that bucket.

### 3.2 Formal Hash Function Specification

**Definition 3.5 (Hash Function):** A hash function $h: K \to \{0,1\}^*$ maps keys to binary strings. For extendible hashing with global depth $d$, the index is computed as:

$$index = h(key) \bmod 2^d$$

Equivalently, using bit manipulation:
$$index = h(key) \gg (w - d)$$

where $w$ represents the word length (typically 32 bits).

### 3.3 Insertion Algorithm

**Algorithm 3.1 (Extendible Hash Insertion):**

```
procedure INSERT(key, record)
    hashValue ← HASH(key)
    index ← hashValue >> (wordLength - globalDepth)
    bucket ← directory[index]

    if bucket.count < bucket.capacity then
        INSERT_INTO_BUCKET(bucket, record)
    else
        SPLIT_BUCKET(bucket, hashValue, index)
        INSERT(key, record)  // Retry after split
    end if
end procedure
```

### 3.4 Bucket Splitting: Rigorous Analysis

When a bucket overflows, two cases arise based on the relationship between local and global depth:

**Case 1: $d' < d$ (Local depth less than global depth)**

When $d' < d$, multiple directory entries point to the overflowing bucket. Splitting proceeds as follows:

1. Create two new buckets: $B_1$ and $B_2$
2. Set local depth of both new buckets to $d' + 1$
3. Redistribute existing records based on the $(d'+1)^{th}$ bit
4. Update the $2^{d-d'}$ directory pointers that previously referenced the old bucket

The directory size remains unchanged since $d$ is unchanged.

**Theorem 3.1:** When $d' < d$, directory doubling is unnecessary during bucket split.

_Proof:_ Since $d' < d$, at least two directory indices share the first $d'$ bits but differ in bit position $d'+1$. Upon splitting, we create two buckets distinguished by bit $d'+1$. Each new bucket requires pointers from indices where this bit equals 0 and 1 respectively. The existing $2^{d-d'}$ pointers can be redistributed without increasing directory size because $2^{d-d'} = 2 \times 2^{d-(d'+1)}$. ∎

**Case 2: $d' = d$ (Local depth equals global depth)**

When $d' = d$, exactly one directory entry references the bucket (all directory entries with prefix matching the bucket's bit pattern point to this bucket). Directory doubling becomes necessary:

1. Double directory size: new size = $2^{d+1}$
2. Increment global depth: $d \leftarrow d + 1$
3. Split the bucket as in Case 1
4. Update all relevant pointers

**Theorem 3.2:** Directory doubling guarantees that no bucket is referenced by more than $2^d$ directory entries after splitting.

_Proof:_ Before doubling, the overflowing bucket has local depth $d$ and is referenced by exactly one directory entry (the index matching its hash prefix). After doubling, global depth becomes $d+1$. The bucket split creates two buckets with local depth $d+1$. Directory entries with the original prefix plus a 0-bit now point to one new bucket, while entries with prefix plus 1-bit point to the other. Thus, each new bucket is referenced by exactly $2^{d+1-d-1} = 2^0 = 1$ entry in the doubled directory. ∎

### 3.5 Comprehensive Worked Example

**Problem:** Given bucket capacity = 2, illustrate the extendible hash structure after inserting keys with the following hash values (4-bit representations):

- $h(k_1) = 0100$
- $h(k_2) = 1010$
- $h(k_3) = 0110$
- $h(k_4) = 1001$
- $h(k_5) = 0001$
- $h(k_6) = 1100$
- $h(k_7) = 0011$

**Solution:**

_Step 1: Initialization (d = 1)_

Directory has $2^1 = 2$ entries: [0] → Bucket A ($d' = 1$), [1] → Bucket B ($d' = 1$)

_Step 2: Insert $k_1$ (0100)_

First bit = 0 → Directory index 0 → Bucket A

State: A:[$k_1$], B:[]

_Step 3: Insert $k_2$ (1010)_

First bit = 1 → Directory index 1 → Bucket B

State: A:[$k_1$], B:[$k_2$]

_Step 4: Insert $k_3$ (0110)_

First bit = 0 → Bucket A. A is not full.

State: A:[$k_1$, $k_3$], B:[$k_2$]

_Step 5: Insert $k_4$ (1001)_

First bit = 1 → Bucket B. B is not full.

State: A:[$k_1$, $k_3$], B:[$k_2$, $k_4$]

_Step 6: Insert $k_5$ (0001)_

First bit = 0 → Bucket A. A is full ($d' = 1 = d$).

Action: Double directory, then split Bucket A.

- New global depth: $d = 2$
- Directory size: $2^2 = 4$ entries [00, 01, 10, 11]
- Split Bucket A using second bit:
  - $k_1$ (0100): bits "01" → Bucket A2
  - $k_3$ (0110): bits "01" → Bucket A2
  - $k_5$ (0001): bits "00" → Bucket A1

State: [00]→A1[$k_5$]($d'=2$), [01]→A2[$k_1$,$k_3$]($d'=2$), [10]→B[$k_2$,$k_4$]($d'=1$), [11]→B[$k_2$,$k_4$]($d'=1$)

_Step 7: Insert $k_6$ (1100)_

First two bits = "11" → Directory index 3 → Bucket B. B is full ($d' = 1 < d = 2$).

Action: Split Bucket B without directory doubling.

- B splits using second bit:
  - $k_2$ (1010): bits "10" → Bucket B1
  - $k_4$ (1001): bits "10" → Bucket B1
  - $k_6$ (1100): bits "11" → Bucket B2

State: [00]→A1[$k_5$]($d'=2$), [01]→A2[$k_1$,$k_3$]($d'=2$), [10]→B1[$k_2$,$k_4$]($d'=2$), [11]→B2[$k_6$]($d'=2$)

_Step 8: Insert $k_7$ (0011)_

First two bits = "00" → Directory index 0 → Bucket A1. A1 has capacity.

State: Final configuration with all 7 keys inserted successfully.

### 3.6 Complexity Analysis

**Theorem 3.3:** In extendible hashing, the expected search cost is $O(1 + \alpha/b)$ where $b$ is bucket capacity.

_Proof:_ The search operation requires accessing the directory (O(1) via array indexing) followed by accessing the bucket (sequential search within bucket). Since bucket size is bounded by capacity $b$, and the expected number of records per bucket is $\alpha/b$ when distributed uniformly, expected search cost is $O(1 + \alpha/b)$. With $\alpha$ maintained below a constant (through splitting), this simplifies to O(1). ∎

**Space Complexity:** Directory space: $O(2^d)$; Bucket space: $O(n/b)$.

### 3.7 C Data Structure Implementation

```c
#define BUCKET_CAPACITY 4
#define WORD_LENGTH 32

typedef struct Bucket {
    int local_depth;
    int count;
    int keys[BUCKET_CAPACITY];
    struct Bucket *next;  // For chaining overflow if needed
} Bucket;

typedef struct {
    int global_depth;
    int size;              // 2^global_depth
    Bucket **buckets;      // Array of bucket pointers
} Directory;

// Compute directory index using leading 'depth' bits
static inline int computeIndex(int hashValue, int depth) {
    return hashValue >> (WORD_LENGTH - depth);
}

// Initialize extendible hash directory
Directory* createDirectory(int initialDepth) {
    Directory *dir = (Directory *)malloc(sizeof(Directory));
    dir->global_depth = initialDepth;
    dir->size = 1 << initialDepth;  // 2^depth
    dir->buckets = (Bucket **)calloc(dir->size, sizeof(Bucket *));

    for (int i = 0; i < dir->size; i++) {
        dir->buckets[i] = (Bucket *)malloc(sizeof(Bucket));
        dir->buckets[i]->local_depth = initialDepth;
        dir->buckets[i]->count = 0;
    }
    return dir;
}
```

## 4. Linear Hashing

### 4.1 Motivation and Overview

While extendible hashing provides efficient directory-based access, it requires maintaining a directory structure and may experience uneven bucket distribution. **Linear hashing** (Litwin, 1980) offers an alternative approach where buckets are split sequentially based on a split pointer, without requiring a directory.

### 4.2 Fundamental Principles

**Definition 4.1 (Split Pointer):** The split pointer $p$ indicates the next bucket to be split during expansion. It ranges from 0 to $N-1$, where $N$ is the current number of buckets.

**Definition 4.2 (Level):** The level $L$ represents the number of times the splitting process has cycled through all buckets.

**Definition 4.3 (Hash Function Family):** Linear hashing employs a family of hash functions $h_0, h_1, h_2, ...$ where $h_i$ produces $i$-bit addresses (i.e., $h_i(key) = hash(key) \bmod 2^i$).

### 4.3 Insertion Algorithm

**Algorithm 4.1 (Linear Hash Insertion):**

```
procedure LINEAR_INSERT(key, record)
    level ← currentLevel
    bucketIndex ← H[level](key)  // Apply appropriate hash function

    if buckets[bucketIndex].count < capacity then
        INSERT_INTO_BUCKET(bucketIndex, record)
    else
        // Overflow: split next bucket
        SPLIT(bucketIndex)
        // Retry insertion with same key
        LINEAR_INSERT(key, record)
    end if

    // Check if expansion threshold exceeded
    if (n / N) > threshold then
        level ← level + 1
        p ← 0  // Reset split pointer
    end if
end procedure

procedure SPLIT(bucketIndex)
    newBucket ← CREATE_BUCKET()
    oldBucket ← buckets[bucketIndex]

    // Redistribute records based on h_{level+1}
    for each record in oldBucket do
        newIndex ← H[level+1](record.key)
        if newIndex == bucketIndex then
            keep in oldBucket
        else
            move to newBucket
        end if
    end for

    buckets[append] ← newBucket
    N ← N + 1
    p ← p + 1
end procedure
```

### 4.4 Search Algorithm

**Algorithm 4.2 (Linear Hash Search):**

```
procedure LINEAR_SEARCH(key)
    for level ← currentLevel downto 0 do
        index ← H[level](key)
        if buckets[index] contains key then
            return record
        end if
    end for
    return NOT_FOUND
end procedure
```

### 4.5 Example Illustration

**Problem:** Using linear hashing with initial bucket count $N = 4$ and overflow threshold 0.8, trace insertions for keys with hash values (modulo 16):

$h(k_1) = 3, h(k_2) = 7, h(k_3) = 11, h(k_4) = 15, h(k_5) = 1, h(k_6) = 5$

**Solution:**

_Initial State (Level 0, N = 4, h_0(x) = x mod 4):_

Buckets: [0]:[], [1]:[], [2]:[], [3]:[]

_Insert $k_1$ (h = 3):_ Bucket 3. State: [3]:[$k_1$]

_Insert $k_2$ (h = 7 → 7 mod 4 = 3):_ Bucket 3. State: [3]:[$k_1$, $k_2$]

_Insert $k_3$ (h = 11 → 11 mod 4 = 3):_ Bucket 3 overflows.

- Split bucket 0 using $h_1(x) = x \mod 8$:
  - $k_1$: 3 → 3 mod 8 = 3 (stays)
  - $k_2$: 7 → 7 mod 8 = 7 → bucket 7 (new)
  - $k_3$: 11 → 11 mod 8 = 3 (stays)

State: [0]:[], [1]:[], [2]:[], [3]:[$k_1$,$k_3$], [4]:[$k_2$] (N = 5)

_Continue insertions following the split pointer progression..._

### 4.6 Performance Characteristics

**Theorem 4.1:** The expected number of bucket accesses in linear hashing is $O(1 + \alpha/(b(1-L/N)))$ where $L$ is the current level and $N$ is bucket count.

_Proof Sketch:_ The search may examine buckets at multiple levels. The probability of finding a record in the primary bucket decreases as the load factor increases. The term $(1-L/N)$ represents the fraction of buckets that have been split at the current level, affecting the distribution. With proper threshold management (typically 0.7-0.8), expected access remains constant. ∎

## 5. Comparative Analysis

| Criterion               | Extendible Hashing                            | Linear Hashing                    |
| :---------------------- | :-------------------------------------------- | :-------------------------------- |
| **Directory Structure** | Required ($2^d$ pointers)                     | Not required                      |
| **Space Overhead**      | Higher (directory + potential unused buckets) | Lower                             |
| **Split Trigger**       | Bucket overflow                               | Overflow or load factor threshold |
| **Split Policy**        | Based on overflow bucket                      | Sequential (split pointer)        |
| **Search Complexity**   | O(1) directory + O(b) bucket                  | O(level + 1) bucket probes        |
| **Deletion Handling**   | Complex (bucket merging)                      | Complex (bucket merging)          |
| **Implementation**      | More complex                                  | Simpler                           |

## 6. Conclusion

Dynamic hashing techniques provide elegant solutions to the static hashing scalability problem. Extendible hashing offers O(1) search with directory-based indexing but requires additional memory for the directory structure. Linear hashing achieves similar performance without directory overhead through sequential splitting. Both techniques maintain expected constant-time operations while supporting incremental growth, making them essential knowledge for database systems and file organization courses.

---

## 7. Assessment Questions

### Question 1 (Application Level)

In an extendible hashing system with initial global depth d = 2 and bucket capacity 3, show the final state of the directory and buckets after inserting records with hash values: 0011, 0101, 0110, 1001, 1010, 1100. After each insertion that causes a split or directory doubling, clearly indicate the global depth, local depths, and which directory entries point to which buckets.

### Question 2 (Analysis Level)

Prove that in extendible hashing, when a bucket with local depth d' is split, the sum of the directory pointers referencing the two new buckets equals $2^{d-d'}$ times the number of pointers referencing the original bucket. Explain why this property ensures efficient directory management during expansion.

### Question 3 (Numerical Problem)

Consider a linear hashing scheme with initial bucket count N = 8, threshold = 0.75, and bucket capacity b = 4. If 25 records are inserted sequentially with hash values producing the following bucket indices under h₀: 0, 3, 7, 2, 5, 1, 6, 4, 0, 3, 7, 2, 5, 1, 6, 4, 0, 3, 7, 2, 5, 1, 6, 4, 0: (a) Determine the final number of buckets, (b) Calculate the final load factor, and (c) Identify how many times the split operation was performed.

### Question 4 (Comparative Analysis)

Analyze the scenario where a database system must support both point queries and range queries on a frequently growing dataset. Recommend either extendible hashing or linear hashing with justification, considering factors including directory overhead, I/O efficiency, and implementation complexity. Your answer should reference the theoretical properties of both techniques.
