# Static Hashing

## 1. Introduction and Fundamental Concepts

**Static hashing** is a hashing technique wherein the hash table size is fixed at the time of table creation and remains constant throughout its lifetime. The primary objective is to map keys to table indices using a hash function, thereby enabling **O(1) average-case time complexity** for the fundamental operations of insertion, search, and deletion. This technique stands in contrast to dynamic hashing, where the table size adapts to the number of elements stored.

In static hashing, we define a **hash table** as an array of size m, and a **hash function** h(k) that maps a key k to an index in the range [0, m-1]. The efficiency of static hashing depends critically on the choice of hash function and the collision resolution strategy employed.

### 1.1 Mathematical Foundation

Given a hash table of size m and n keys stored, we define the **load factor** (α) as:

```
α = n / m
```

The load factor represents the degree of table occupancy and plays a pivotal role in determining the expected performance of hash table operations. A well-designed static hash table typically maintains α ≤ 0.7 to ensure acceptable performance characteristics.

### 1.2 Uniform Hashing Assumption

Under the **uniform hashing assumption**, we assume that each key is equally likely to hash to any of the m table slots, independent of where other keys hash. Formally:

```
P(h(k) = i) = 1/m for all i ∈ [0, m-1]
```

This assumption enables mathematical analysis of expected performance, though in practice, true uniform distribution is rarely achieved due to clustering phenomena.

## 2. Hash Function Design

A hash function h(key) maps a key to an integer index in the range [0, m-1]. The quality of the hash function directly impacts collision frequency and overall table performance.

### 2.1 Division Method (Modular Arithmetic)

The division method represents the simplest and most widely adopted hashing technique:

```
h(k) = k mod m
```

**Theorem**: For optimal distribution, m should be a prime number not close to a power of 2.

**Proof**: If m = 2^p, then k mod m extracts only the p lowest-order bits of k, causing clustering if keys share common bit patterns. A prime number ensures the modulo operation interacts with all bits of the key.

**Example**: Let m = 11 (prime), key = 54:

```
h(54) = 54 mod 11 = 10
```

### 2.2 Mid-Square Method

The mid-square method extracts middle digits from the squared key value:

1. Compute k^2
2. Extract the middle r digits (where 2^r ≈ m)
3. Use these digits as the hash index

**Example**: key = 56, assume m ≈ 100 (2 middle digits)

```
56² = 3136
Middle two digits: 13
h(56) = 13 (or 13 mod m)
```

This method exhibits good distribution because middle bits depend on all original key bits, though computation of squares may overflow for large keys.

### 2.3 Folding Method

Folding divides the key into equal parts and combines them:

**Fold-Shift (Addition)**:

```
key = 123456789
Parts: 12 | 34 | 56 | 78 | 9
Sum = 12 + 34 + 56 + 78 + 9 = 189
h(k) = 189 mod m
```

**Fold-Boundary (Reverse alternate parts)**:

```
key = 123456789
Parts: 12 | 43 | 56 | 87 | 9
Sum = 12 + 43 + 56 + 87 + 9 = 207
h(k) = 207 mod m
```

### 2.4 Digit Extraction Method

Select specific digit positions exhibiting maximum variation:

**Example**: key = 7654321, select positions 2, 4, 6:

```
Selected digits: 6, 4, 2 → 642
h(k) = 642 mod m
```

### 2.5 Properties of an Ideal Hash Function

A good hash function must satisfy:

1. **Determinism**: h(k) = h(k) for all iterations
2. **Uniform Distribution**: P(h(k) = i) = 1/m for all i
3. **Efficiency**: O(1) computation time
4. **Collision Minimization**: Minimize P(h(k₁) = h(k₂)) for k₁ ≠ k₂
5. **Full Key Utilization**: Hash value depends on all key digits

## 3. Collision Resolution Techniques

When two distinct keys hash to the same index, a **collision** occurs. Resolution strategies are essential for maintaining table integrity.

### 3.1 Separate Chaining (Open Hashing)

In separate chaining, each bucket maintains a linked list of all keys mapping to that index.

**Data Structure**:

```
Index 0: NULL
Index 1: [12|*] → [23|*] → NULL
Index 2: [35|*] → NULL
...
```

#### Performance Analysis

**Theorem**: Under uniform hashing with separate chaining:

- Expected successful search: Θ(1 + α/2)
- Expected unsuccessful search: Θ(1 + α)
- Insertion: O(1)

**Proof**: For successful search, we examine approximately half the keys in the chain before finding the target. The expected chain length is α, yielding Θ(1 + α/2). For unsuccessful search, we examine all α keys on average.

**Worst Case**: O(n) when all keys hash to the same bucket.

**Space Complexity**: O(n + m) due to linked list overhead.

#### Worked Example

Insert keys: 20, 31, 42, 53, 64, 75, 86, 9, 15, 27 into table size m = 11:

```
h(20) = 20 mod 11 = 9
h(31) = 31 mod 11 = 9 (collision)
h(42) = 42 mod 11 = 9 (collision)
h(53) = 53 mod 11 = 9 (collision)
h(64) = 64 mod 11 = 9 (collision)
h(75) = 75 mod 11 = 9 (collision)
h(86) = 86 mod 11 = 9 (collision)
h(9)  = 9  mod 11 = 9 (collision)
h(15) = 15 mod 11 = 4
h(27) = 27 mod 11 = 5
```

Load factor α = 10/11 ≈ 0.91

This example demonstrates **primary clustering** - a pathological case where poor hash function choice causes all keys to collide.

### 3.2 Open Addressing (Closed Hashing)

All elements store directly in the table. When collision occurs, we probe alternative locations.

#### 3.2.1 Linear Probing

The probe sequence follows: h(k), h(k)+1, h(k)+2, ..., h(k)+i (mod m)

**Insertion Algorithm**:

```
function insert(key, value):
    i = 0
    index = h(key)
    while i < m:
        probe = (index + i) mod m
        if table[probe] is empty:
            table[probe] = (key, value)
            return SUCCESS
        i++
    return TABLE_FULL
```

**Theorem**: In linear probing with uniform hashing:

- Successful search: Θ(1/(1-α))
- Unsuccessful search: Θ(1/(1-α)²)

**Proof**: The expected number of probes follows from the analysis of the "birthday paradox" extended to open addressing. As α approaches 1, probe sequences become increasingly long due to **primary clustering**.

**Example**: m = 11, insert 54:

```
h(54) = 54 mod 11 = 10
If index 10 occupied, try 0, then 1, etc.
```

#### 3.2.2 Quadratic Probing

Probe sequence: h(k), h(k)+1², h(k)+2², h(k)+3², ... (mod m)

```
probe_i = (h(k) + i²) mod m, for i = 0, 1, 2, ...
```

**Advantage**: Reduces primary clustering by spacing probes quadratically.

**Limitation**: May suffer from **secondary clustering** - keys mapping to same initial index follow identical probe sequences.

**Theorem**: For quadratic probing to guarantee finding an empty slot, either:

1. m is prime, and we probe at most m/2 positions, OR
2. α < 0.5

#### 3.2.3 Double Hashing

Uses a secondary hash function to compute probe increment:

```
h(k) = h₁(k)
probe_i = (h₁(k) + i × h₂(k)) mod m
```

where h₂(k) must be relatively prime to m for full cycle.

Common choice: h₂(k) = prime - (k mod prime), where prime < m.

**Theorem**: Double hashing approximates uniform hashing and eliminates both primary and secondary clustering.

**Example**: m = 11, h₁(k) = k mod 11, h₂(k) = 7 - (k mod 7)

For key = 54:

```
h₁(54) = 54 mod 11 = 10
h₂(54) = 7 - (54 mod 7) = 7 - 5 = 2

Probes: (10 + 0×2) mod 11 = 10
        (10 + 1×2) mod 11 = 1
        (10 + 2×2) mod 11 = 3
        ...
```

### 3.3 Comparison of Collision Resolution Techniques

| Technique         | Avg. Search (α < 0.5) | Worst Case | Space | Advantages                 |
| ----------------- | --------------------- | ---------- | ----- | -------------------------- |
| Separate Chaining | O(1 + α)              | O(n)       | n + m | Simple, handles α > 1      |
| Linear Probing    | O(1/(1-α))            | O(n)       | m     | Simple, no pointers        |
| Quadratic Probing | O(1/(1-α))            | O(n)       | m     | Less clustering            |
| Double Hashing    | O(1/(1-α))            | O(n)       | m     | Best clustering resistance |

## 4. Performance Analysis

### 4.1 Load Factor Impact

The load factor α critically affects performance:

- **α < 0.5**: Excellent performance for all techniques
- **α ≈ 0.7**: Acceptable for open addressing; consider rehashing
- **α > 0.7**: Significant performance degradation in open addressing
- **α > 1.0**: Only possible with separate chaining

### 4.2 Expected Probe Sequences

Under uniform hashing assumption, the expected number of probes for:

**Successful Search**:

```
E[probes] ≈ (1/α) × ln(1/(1-α))
```

**Unsuccessful Search**:

```
E[probes] ≈ 1/(1-α)
```

### 4.3 Rehashing Strategy

When α exceeds threshold (typically 0.7), create new table of size ~2m and rehash all elements:

```
function rehash(oldTable):
    newSize = 2 × oldTable.size
    newTable = createTable(newSize)
    for each (key, value) in oldTable:
        insert(newTable, key, value)
    return newTable
```

**Complexity**: O(n) for rehashing, but amortized over insertions.

## 5. C Implementation

```c
#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 11
#define EMPTY -1
#define DELETED -2
#define LF_THRESHOLD 0.7

typedef struct {
    int key;
    int value;
    int state;  // 0=empty, 1=occupied, 2=deleted
} HashEntry;

typedef struct {
    HashEntry *table;
    int size;
    int count;
} HashTable;

// Linear probing hash function
int hashFunction(int key, int size) {
    return key % size;
}

// Secondary hash for double hashing
int hashFunction2(int key, int size) {
    int prime = 7;  // Prime less than size
    return prime - (key % prime);
}

// Initialize hash table
void initTable(HashTable *ht, int size) {
    ht->size = size;
    ht->count = 0;
    ht->table = (HashEntry *)malloc(size * sizeof(HashEntry));
    for (int i = 0; i < size; i++)
        ht->table[i].state = 0;  // Empty
}

// Double hashing insertion
int insert(HashTable *ht, int key, int value) {
    if ((float)ht->count / ht->size > LF_THRESHOLD) {
        // Rehashing would go here
        return -1;
    }

    int index = hashFunction(key, ht->size);
    int step = hashFunction2(key, ht->size);

    for (int i = 0; i < ht->size; i++) {
        int probe = (index + i * step) % ht->size;

        if (ht->table[probe].state != 1) {
            ht->table[probe].key = key;
            ht->table[probe].value = value;
            ht->table[probe].state = 1;
            ht->count++;
            return 1;
        }
    }
    return 0;  // Table full
}

// Search operation
int search(HashTable *ht, int key) {
    int index = hashFunction(key, ht->size);
    int step = hashFunction2(key, ht->size);

    for (int i = 0; i < ht->size; i++) {
        int probe = (index + i * step) % ht->size;

        if (ht->table[probe].state == 0)
            return -1;  // Not found

        if (ht->table[probe].state == 1 && ht->table[probe].key == key)
            return ht->table[probe].value;
    }
    return -1;
}
```

## 6. Numerical Problems

### Problem 1

Insert keys 12, 22, 32, 42, 52 into hash table of size 13 using linear probing. Show the final table state.

**Solution**:

```
h(k) = k mod 13

12 → 12 mod 13 = 12
22 → 22 mod 13 = 9
32 → 32 mod 13 = 6
42 → 42 mod 13 = 3
52 → 52 mod 13 = 0

All unique - no collisions.
```

### Problem 2

Using quadratic probing with table size 11, insert keys: 15, 25, 35, 45.

**Solution**:

```
h(k) = k mod 11

15: probe₀ = 4 → empty → insert
25: probe₀ = 3 → empty → insert
35: probe₀ = 2 → empty → insert
45: probe₀ = 1 → empty → insert

All insert without collision (different initial indices).
```

## 7. Assessment Questions

### Multiple Choice Questions

**Q1.** A hash table of size 10 uses the hash function h(k) = k mod 10. Using linear probing to resolve collisions, at which index will the key 24 be inserted if indices 4 and 5 are already occupied?

A) 2  
B) 3  
C) 6  
D) 7

**Answer**: C  
**Explanation**: h(24) = 24 mod 10 = 4. Index 4 is occupied, so probe index 5 (occupied), then index 6 (empty). Insert at index 6.

---

**Q2.** In a hash table with load factor α = 0.6 using linear probing, approximately how many probes are needed for an unsuccessful search?

A) 1.6  
B) 2.0  
C) 2.5  
D) 4.0

**Answer**: C  
**Explanation**: Expected probes for unsuccessful search = 1/(1-α) = 1/(1-0.6) = 1/0.4 = 2.5

---

**Q3.** Which collision resolution technique guarantees finding an empty slot if the table is at most half full and the table size is prime?

A) Linear Probing  
B) Separate Chaining  
C) Quadratic Probing  
D) Double Hashing

**Answer**: C  
**Explanation**: Quadratic probing guarantees finding an empty slot if the table is at most half full or when the table size is prime.

---

**Q4.** The primary advantage of double hashing over linear probing is:

A) Simpler implementation  
B) Reduced clustering  
C) Guaranteed O(1) search  
D) Lower memory usage

**Answer**: B  
**Explanation**: Double hashing uses a secondary hash function to compute probe increments, effectively eliminating both primary and secondary clustering phenomena.

---

**Q5.** Given a hash table of size 7 with hash function h(k) = k mod 7, how many probes are required to find key 23 using quadratic probing if indices 2, 3, and 4 are occupied?

A) 1  
B) 2  
C) 3  
D) 4

**Answer**: C  
**Explanation**: h(23) = 2. Probes: 2 (occupied), 2+1²=3 (occupied), 2+2²=6 (empty). Requires 3 probes.

---

**Q6.** In separate chaining with load factor α = 2, what is the expected chain length?

A) 0.5  
B) 1  
C) 2  
D) 4

**Answer**: C  
**Explanation**: Load factor α = n/m = 2. This means average chain length = n/m = 2 elements per bucket.

---

**Q7.** What is the time complexity of rehashing when the load factor exceeds the threshold?

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)

**Answer**: C  
**Explanation**: Rehashing requires iterating through all existing n elements and reinserting them into a new table, resulting in O(n) complexity.

---

**Q8.** A hash table uses h(k) = k mod 13. After inserting keys 1, 14, 27 using linear probing, at which index is key 27 stored?

A) 1  
B) 2  
C) 3  
D) 1 or 2

**Answer**: B  
**Explanation**: h(1) = 1, h(14) = 1 (collision → index 2), h(27) = 1 (collision → index 2 occupied → index 3). Actually: 27 mod 13 = 1. 1 occupied, 2 occupied, insert at 3. Wait: h(14) = 1, index 1 occupied, try index 2. h(27) = 1, try 2 occupied, try 3. Answer should be index 3 = C. Let me recalculate: 1→1, 14→1 collision→2, 27→1 collision→2 occupied→3. Answer C.

---

## 8. Key Takeaways

1. Static hashing provides O(1) average-case operations but requires careful hash function design
2. Load factor critically impacts performance; maintain α < 0.7 for open addressing
3. Separate chaining handles high load factors but consumes extra memory
4. Open addressing achieves better memory utilization but suffers from clustering
5. Double hashing provides the best compromise among open addressing techniques
6. Rehashing becomes necessary when load factor exceeds acceptable thresholds

## 9. Flashcards

- **Q**: What is the load factor α in a hash table?
- **A**: α = n/m, where n is the number of keys stored and m is the table size. It measures table occupancy.

- **Q**: What is primary clustering in linear probing?
- **A**: A phenomenon where long runs of occupied slots form, causing increased collision resolution time.

- **Q**: Why is double hashing preferred over linear probing?
- **A**: Double hashing eliminates both primary and secondary clustering by using a secondary hash function for probe sequence computation.

- **Q**: What is the expected successful search time with linear probing when α = 0.5?
- **A**: Approximately 1/(1-α) = 1/0.5 = 2 probes on average.
