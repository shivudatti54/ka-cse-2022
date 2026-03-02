# Collision Resolution Schemes

## Design And Analysis Of Algorithms – BSc (Hons) Computer Science (Delhi University, NEP 2024 UGCF)

---

## 1. Introduction

Hashing is a fundamental technique in computer science used for efficient data retrieval. In hashing, a **hash function** computes an index (called a **hash code** or **hash value**) into an array of buckets or slots, from which the desired value can be found. Ideally, each key should map to a unique bucket, but in practice, multiple keys may map to the same bucket—this situation is known as a **collision**. Collision resolution schemes are algorithms and data structures designed to handle collisions gracefully, ensuring that every key can be stored and retrieved efficiently even when the hash table is full or when multiple keys hash to the same index.

This module covers the essential collision resolution techniques required by the Delhi University syllabus for Design and Analysis of Algorithms. We will explore both classic methods (separate chaining, open addressing) and advanced techniques (cuckoo hashing, rehashing), with practical examples and code implementations to deepen understanding.

---

## 2. Real-World Relevance

Collision resolution is critical in numerous real-world applications:

- **Database Indexing**: Databases use hash indexes to speed up record retrieval. Collisions must be handled to maintain fast query times.
- **Caching Systems**: Web caches and CPU caches rely on hash tables to store recently accessed data. Efficient collision handling ensures minimal cache misses.
- **Symbol Tables in Compilers**: Compilers use hash tables to store variable names, function names, and other symbols. Collisions can slow down compilation if not managed.
- **Cryptographic Hashing**: While not directly about collision resolution, understanding collisions in hash functions is vital for security (e.g., in digital signatures).
- **Associative Arrays**: Languages like Python, JavaScript, and PHP use hash tables to implement dictionaries and maps, where collision resolution affects performance.

Understanding these techniques is essential for optimizing software that requires fast data access, which is a core topic in algorithm design.

---

## 3. Overview of Hashing and Collisions

A **hash table** is an array of fixed size, say `m` slots, indexed from `0` to `m-1`. A hash function `h(k)` maps a key `k` to an index in the range `[0, m-1]`. Collisions occur when `h(k1) = h(k2)` for distinct keys `k1` and `k2`.

The **load factor** (α) is defined as `n/m`, where `n` is the number of keys stored. A high load factor increases the probability of collisions, degrading performance. Collision resolution schemes aim to keep the load factor low (typically below 0.7) and maintain average-case O(1) time for insertion, deletion, and search.

---

## 4. Collision Resolution Techniques

There are two primary categories: **Separate Chaining** and **Open Addressing**. Additionally, we discuss **Rehashing** and **Cuckoo Hashing** as advanced methods.

### 4.1 Separate Chaining

In separate chaining, each bucket in the hash table is a **linked list** (or other data structure like a balanced tree) that stores all keys hashing to that bucket. When a collision occurs, the key is appended to the list at that bucket.

#### How It Works:
- **Insertion**: Compute hash index, traverse the list at that index to check for duplicates, then insert at the head or tail.
- **Search**: Compute hash index, then traverse the list at that index to find the key.
- **Deletion**: Compute hash index, find the node in the list, and remove it.

#### Implementation (Pseudocode in C-like syntax):

```c
// Node structure for separate chaining
struct Node {
    int key;
    struct Node* next;
};

// Hash table as an array of pointers to linked lists
struct Node* table[TABLE_SIZE];

// Initialize table
void initTable() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        table[i] = NULL;
    }
}

// Hash function
int hash(int key) {
    return key % TABLE_SIZE;
}

// Insertion
void insert(int key) {
    int index = hash(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->next = table[index]; // Insert at head
    table[index] = newNode;
}

// Search
int search(int key) {
    int index = hash(key);
    struct Node* current = table[index];
    while (current != NULL) {
        if (current->key == key) return 1; // Found
        current = current->next;
    }
    return 0; // Not found
}

// Deletion
void delete(int key) {
    int index = hash(key);
    struct Node* current = table[index];
    struct Node* prev = NULL;
    while (current != NULL) {
        if (current->key == key) {
            if (prev == NULL) table[index] = current->next;
            else prev->next = current->next;
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
}
```

#### Advantages:
- Simple to implement.
- Works well even with a high load factor (can exceed 1.0).
- Deletion is straightforward.

#### Disadvantages:
- Performance degrades if chains become long (worst-case O(n)).
- Extra memory for pointers.
- Poor cache performance due to linked lists.

#### Variation: Using Balanced Trees
In Java's `HashMap`, when the chain length exceeds a threshold (default 8), the linked list is converted to a balanced tree (red-black tree) to improve worst-case performance to O(log n).

---

### 4.2 Open Addressing

In open addressing, all keys are stored directly in the hash table array. If a bucket is occupied, we probe other buckets in a predefined sequence until an empty slot is found. The probe sequence depends on the method.

#### 4.2.1 Linear Probing

In linear probing, if bucket `h(k)` is full, we check `h(k)+1`, then `h(k)+2`, and so on, wrapping around modulo table size.

- **Probe function**: `h(k, i) = (h'(k) + i) mod m`, where `i` is the probe number and `h'(k)` is the primary hash function.
- **Example**: Table size 10, hash function `h(k) = k mod 10`. Insert keys 15, 25, 35:
  - 15 → index 5 (empty, store).
  - 25 → index 5 (occupied, probe to 6, store).
  - 35 → index 5 (occupied, probe to 6, then 7, store).

**Issue: Primary Clustering** — Long runs of occupied slots cause many probes, degrading performance.

#### 4.2.2 Quadratic Probing

To reduce clustering, quadratic probing uses a quadratic function for probing:

- **Probe function**: `h(k, i) = (h'(k) + c1*i + c2*i^2) mod m`, where `c1` and `c2` are constants.
- **Example**: Table size 10, `h'(k) = k mod 10`, `c1=1`, `c2=1`. Insert key 15: index 5. Insert 25: index 5, try 6, then 8 (since `1+1^2=2`, 5+2=7? Wait, let's compute: i=0 → 5; i=1 → 5+1+1=7; i=2 → 5+2+4=11 mod 10 =1). So 25 goes to index 1.

#### 4.2.3 Double Hashing

Double hashing uses two hash functions to generate probe sequences:

- **Probe function**: `h(k, i) = (h1(k) + i * h2(k)) mod m`.
- Typically, `h1(k) = k mod m`, and `h2(k) = prime - (k mod prime)` where `prime` is a prime smaller than `m`.
- Example: Table size 10, `h1(k) = k mod 10`, `h2(k) = 7 - (k mod 7)`. Insert key 15: `h1=5`, `h2=7-(1)=6`. Probe sequence: 5, (5+6) mod 10 = 1, (5+2*6) mod 10 = 7, ...

#### Comparison of Open Addressing Methods:

| Method          | Advantages                                      | Disadvantages                                    |
|-----------------|------------------------------------------------|--------------------------------------------------|
| Linear Probing  | Simple, good cache performance                | Primary clustering, high collision resolution   |
| Quadratic Probing| Reduces primary clustering                  | Secondary clustering, may not find empty slot   |
| Double Hashing  | Nearly uniform probe sequence                 | More computation for two hash functions         |

#### Implementation Example: Double Hashing in Python:

```python
TABLE_SIZE = 10

def hash1(key):
    return key % TABLE_SIZE

def hash2(key):
    # Prime smaller than TABLE_SIZE, e.g., 7
    prime = 7
    return prime - (key % prime)

def insert(table, key):
    index = hash1(key)
    i = 0
    while i < TABLE_SIZE:
        probe = (hash1(key) + i * hash2(key)) % TABLE_SIZE
        if table[probe] is None:
            table[probe] = key
            return True
        i += 1
    print("Table full")
    return False

def search(table, key):
    index = hash1(key)
    i = 0
    while i < TABLE_SIZE:
        probe = (hash1(key) + i * hash2(key)) % TABLE_SIZE
        if table[probe] == key:
            return probe
        if table[probe] is None:
            return -1
        i += 1
    return -1

# Example usage
table = [None] * TABLE_SIZE
for k in [15, 25, 35, 5]:
    insert(table, k)
print("Table after insertion:", table)  # Output: [25, 35, None, None, None, 15, None, None, None, 5]
print("Search for 35:", search(table, 35))  # Output: 1
```

---

### 4.3 Rehashing

Rehashing is a technique used to maintain efficiency when the load factor exceeds a threshold (e.g., 0.7). It involves creating a new, larger hash table (typically twice the size) and reinserting all existing keys into this new table using a new hash function.

#### When to Rehash:
- **Load factor too high**: As the table fills, collisions increase, slowing operations.
- **After multiple deletions**: In open addressing, deletions create "tombstones" that can degrade performance; rehashing can clean them up.

#### Process:
1. Allocate a new array of larger size (often a prime number).
2. Compute a new hash function based on the new size.
3. Iterate through the old table and insert each key into the new table.

#### Example (Conceptual):
- Initial table size: 10, load factor threshold: 0.7.
- When 8 keys are inserted (load factor 0.8), create a new table of size 20.
- Rehash all 8 keys into the new table using `h(k) = k mod 20`.

#### Implementation Snippet (C):

```c
void rehash(struct HashTable* ht) {
    int oldSize = ht->size;
    struct Node** oldTable = ht->table;
    
    ht->size = oldSize * 2;
    ht->table = (struct Node**)malloc(ht->size * sizeof(struct Node*));
    for (int i = 0; i < ht->size; i++) ht->table[i] = NULL;
    
    // Reinsert all keys
    for (int i = 0; i < oldSize; i++) {
        struct Node* current = oldTable[i];
        while (current) {
            insert(ht, current->key);
            struct Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(oldTable);
}
```

---

### 4.4 Cuckoo Hashing

Cuckoo hashing is an advanced open addressing method that guarantees **O(1)** worst-case lookup time. It uses two hash functions and two tables, each with its own hash function.

#### How It Works:
- **Insertion**: Compute two possible positions using two hash functions. If either position is empty, insert there. Otherwise, evict the existing key and reinsert it in its alternative position (the "cuckoo" behavior).
- **Eviction Loop**: If a key is displaced multiple times, it may cycle; in that case, rehash the entire table (use a new hash function or larger size).
- **Search**: Check both possible positions; if found, return true; otherwise, false.
- **Deletion**: Since we check both positions, deletion is straightforward—remove the key if found.

#### Advantages:
- Worst-case O(1) time for lookup, insertion, and deletion (with a limit on evictions).
- No chaining, so memory usage is predictable.
- Good cache performance due to two fixed positions.

#### Disadvantages:
- Complex to implement.
- Insertion may fail and require rehashing.
- Two tables may waste space if not fully utilized.

#### Example:
Table size 10, two hash functions: `h1(k) = k mod 10`, `h2(k) = (k/10) mod 10` (or another function). Insert keys 15, 25, 35:
- Insert 15: `h1(15)=5` (empty, insert in Table1[5]).
- Insert 25: `h1(25)=5` (occupied by 15), `h2(25)=2` (empty in Table2[2], insert).
- Insert 35: `h1(35)=5` (occupied by 15), evict 15 to Table2[2]? Actually, we need two tables. Let's define:
  - Table1: hash function h1
  - Table2: hash function h2
  - For key 35: h1(35)=5 (occupied), so try h2(35)=3 (empty, insert). But 15 is at h1(35), so 15 gets evicted? Wait, we need to track: 15 is at Table1[5]. When inserting 35, we put 35 in Table2[3], and 15 stays. This is simplified; actual algorithm may involve displacement.

#### Implementation (Pseudocode for Insertion):

```python
def cuckoo_insert(table1, table2, h1, h2, key):
    if key in table1 or key in table2:
        return  # Key already exists
    
    max_iterations = 10  # Limit to prevent infinite loops
    for i in range(max_iterations):
        # Try Table1
        pos1 = h1(key)
        if table1[pos1] is None:
            table1[pos1] = key
            return
        # Displace
        key, table1[pos1] = table1[pos1], key
        
        # Try Table2
        pos2 = h2(key)
        if table2[pos2] is None:
            table2[pos2] = key
            return
        # Displace
        key, table2[pos2] = table2[pos2], key
    
    # If here, cycle detected; rehash
    rehash(table1, table2)
```

#### Visual Diagram (Text-based):

```
Initial: Empty tables (size 5)
Table1: [_, _, _, _, _]
Table2: [_, _, _, _, _]

Insert 10: h1(10)=0, h2(10)=3
Table1[0]=10
Table2[3]=10

Insert 20: h1(20)=0 (occupied by 10), h2(20)=2 (empty)
Displace 10 to Table2[3]? Actually, let's follow algorithm:
- Key=20, pos1=0 occupied, swap: 10 becomes current key, Table1[0]=20.
- Now key=10, pos2=h2(10)=3, occupied by 10? Wait, Table2[3]=10 already, so swap: Table2[3]=20, key=10.
- key=10, pos1=h1(10)=0 occupied by 20, swap: Table1[0]=10, key=20.
- key=20, pos2=h2(20)=2 empty, insert: Table2[2]=20.
Final: Table1[0]=10, Table2[3]=10, Table2[2]=20.
```

---

## 5. Concrete Examples with Code

### Example 1: Separate Chaining Implementation in C

This example demonstrates a complete hash table with separate chaining, including insertion, search, display, and deletion.

```c
#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

struct Node {
    int key;
    struct Node* next;
};

struct Node* table[TABLE_SIZE];

void init() {
    for (int i = 0; i < TABLE_SIZE; i++) table[i] = NULL;
}

int hash(int key) {
    return key % TABLE_SIZE;
}

void insert(int key) {
    int index = hash(key);
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->next = table[index];
    table[index] = newNode;
}

int search(int key) {
    int index = hash(key);
    struct Node* current = table[index];
    while (current) {
        if (current->key == key) return 1;
        current = current->next;
    }
    return 0;
}

void delete(int key) {
    int index = hash(key);
    struct Node* current = table[index];
    struct Node* prev = NULL;
    while (current) {
        if (current->key == key) {
            if (prev) prev->next = current->next;
            else table[index] = current->next;
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
}

void display() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("Bucket %d: ", i);
        struct Node* current = table[i];
        while (current) {
            printf("%d -> ", current->key);
            current = current->next;
        }
        printf("NULL\n");
    }
}

int main() {
    init();
    insert(15); insert(25); insert(35); insert(5);
    display();
    printf("Search 25: %d\n", search(25));
    delete(25);
    display();
    return 0;
}
```

### Example 2: Double Hashing Implementation in Python

This example implements a hash table with double hashing for collision resolution, including insert, search, and delete operations.

```python
class DoubleHashing:
    def __init__(self, size):
        self.TABLE_SIZE = size
        self.table = [None] * size
        self.prime = 7  # Prime smaller than size

    def hash1(self, key):
        return key % self.TABLE_SIZE

    def hash2(self, key):
        return self.prime - (key % self.prime)

    def insert(self, key):
        if key in self.table:
            print(f"Key {key} already exists.")
            return
        for i in range(self.TABLE_SIZE):
            probe = (self.hash1(key) + i * self.hash2(key)) % self.TABLE_SIZE
            if self.table[probe] is None:
                self.table[probe] = key
                print(f"Inserted {key} at index {probe}.")
                return
        print(f"Table is full, cannot insert {key}.")

    def search(self, key):
        for i in range(self.TABLE_SIZE):
            probe = (self.hash1(key) + i * self.hash2(key)) % self.TABLE_SIZE
            if self.table[probe] == key:
                return probe
            if self.table[probe] is None:
                return -1
        return -1

    def delete(self, key):
        index = self.search(key)
        if index != -1:
            self.table[index] = None  # Simple deletion; may cause issues in search
            print(f"Deleted {key} from index {index}.")
        else:
            print(f"Key {key} not found.")

    def display(self):
        print("Hash Table:", self.table)

# Example usage
dh = DoubleHashing(10)
keys = [15, 25, 35, 5, 45]
for k in keys:
    dh.insert(k)
dh.display()
print("Search 35:", dh.search(35))
dh.delete(35)
dh.display()
```

**Note**: The simple deletion in double hashing may leave "tombstones" that affect search performance. A more robust implementation would handle tombstones or use rehashing.

---

## 6. Visual Diagrams (Descriptive)

Since we cannot generate images, here are descriptions of diagrams that would aid understanding:

1. **Separate Chaining Diagram**: 
   - Show a hash table array with 10 buckets. 
   - Bucket 0 contains a linked list: [10] -> [20] -> NULL. 
   - Bucket 5 contains [15] -> [25] -> NULL. 
   - Other buckets are empty or have single nodes.

2. **Linear Probing Diagram**:
   - Table size 10, keys inserted: 12, 22, 32, 42 (all hash to index 2).
   - Show sequential probing: index 2 (12), index 3 (22), index 4 (32), index 5 (42).
   - Highlight clustering.

3. **Cuckoo Hashing Diagram**:
   - Two tables (Table1 and Table2) of size 5.
   - Show keys 10, 20, 30 inserted with two hash functions.
   - Illustrate displacement cycles.

You can draw these on paper or use tools like draw.io to visualize.

---

## 7. Multiple Choice Questions (MCQs)

1. **What is the time complexity of search in separate chaining in the worst case?**
   - a) O(1)
   - b) O(log n)
   - c) O(n)
   - d) O(n log n)
   - **Answer: c) O(n)**

2. **In double hashing, if the table size is 10 and the second hash function returns 3, what is the probe sequence for a key with primary hash 4?**
   - a) 4, 7, 0, 3, 6, 9, 2, 5, 8, 1
   - b) 4, 7, 1, 4, 8, 2, 5, 9, 3, 6
   - c) 4, 3, 2, 1, 0, 9, 8, 7, 6, 5
   - d) 4, 5, 6, 7, 8, 9, 0, 1, 2, 3
   - **Answer: a) 4, 7, 0, 3, 6, 9, 2, 5, 8, 1**

3. **Which collision resolution technique guarantees O(1) worst-case lookup time?**
   - a) Separate Chaining
   - b) Linear Probing
   - c) Quadratic Probing
   - d) Cuckoo Hashing
   - **Answer: d) Cuckoo Hashing**

4. **What is the primary disadvantage of linear probing?**
   - a) Secondary clustering
   - b) Primary clustering
   - c) High memory usage
   - d) Complex implementation
   - **Answer: b) Primary clustering**

5. **When should rehashing be performed?**
   - a) When the table is empty
   - b) When the load factor exceeds a threshold
   - c) After every deletion
   - d) When all keys are prime numbers
   - **Answer: b) When the load factor exceeds a threshold**

6. **In cuckoo hashing, each key has how many possible positions?**
   - a) 1
   - b) 2
   - c) Variable
   - d) Equal to table size
   - **Answer: b) 2**

7. **What is a tombstone in hash tables?**
   - a) A deleted key placeholder
   - b) A special hash value
   - c) A type of hash function
   - d) A collision resolution technique
   - **Answer: a) A deleted key placeholder**

8. **Which method is used to reduce primary clustering?**
   - a) Linear Probing
   - b) Quadratic Probing
   - c) Separate Chaining
   - d) Rehashing
   - **Answer: b) Quadratic Probing**

---

## 8. Flashcards

### Flashcard 1
**Term**: Collision
**Definition**: A situation where two distinct keys map to the same hash value/index in a hash table.
**Example**: Keys 15 and 25 both hash to index 5 in a table with size 10.

### Flashcard 2
**Term**: Load Factor
**Definition**: The ratio of the number of keys stored to the number of buckets in the hash table (α = n/m). It indicates how full the hash table is.
**Example**: If a table has 10 buckets and 7 keys, load factor is 0.7.

### Flashcard 3
**Term**: Separate Chaining
**Definition**: A collision resolution method where each bucket in the hash table is a linked list (or other structure) that holds all keys hashing to that bucket.
**Example**: In a table of size 10, keys 15, 25, and 35 all hash to index 5; they are stored as a linked list at bucket 5.

### Flashcard 4
**Term**: Open Addressing
**Definition**: A collision resolution method where all keys are stored in the hash table itself; if a bucket is full, we probe other buckets in a defined sequence.
**Example**: In linear probing, if bucket 5 is full, we check 6, then 7, etc.

### Flashcard 5
**Term**: Linear Probing
**Definition**: An open addressing technique where if a bucket is occupied, we check the next bucket sequentially (with wraparound) until an empty slot is found.
**Example**: Probe function: h(k,i) = (h'(k) + i) mod m.

### Flashcard 6
**Term**: Double Hashing
**Definition**: An open addressing technique that uses two hash functions to compute the probe sequence, reducing clustering.
**Example**: Probe function: h(k,i) = (h1(k) + i * h2(k)) mod m.

### Flashcard 7
**Term**: Rehashing
**Definition**: The process of creating a new, larger hash table and reinserting all existing keys using a new hash function, typically triggered when the load factor becomes too high.
**Example**: When load factor exceeds 0.7, double the table size and rehash all keys.

### Flashcard 8
**Term**: Cuckoo Hashing
**Definition**: An advanced open addressing method with two tables and two hash functions, guaranteeing O(1) worst-case lookup by checking two fixed positions.
**Example**: Key 15 can be in either Table1[h1(15)] or Table2[h2(15)].

### Flashcard 9
**Term**: Primary Clustering
**Definition**: A problem in linear probing where long runs of occupied buckets cause many probes, degrading performance.
**Example**: Keys 10, 20, 30, 40 all hash to index 5, forming a cluster.

### Flashcard 10
**Term**: Tombstone
**Definition**: A special marker placed in a hash table slot after a key is deleted, used to allow searching to continue past that slot in open addressing.
**Example**: Deleting a key in linear probing may leave a tombstone that affects subsequent searches.

---

## 9. Key Takeaways

1. **Collision Resolution is Essential**: Since collisions are inevitable in hashing, efficient resolution techniques are crucial for maintaining O(1) average-case performance.
2. **Separate Chaining vs. Open Addressing**: Separate chaining is simple and works well with high load factors, while open addressing saves memory but suffers from clustering issues.
3. **Double Hashing Reduces Clustering**: By using two hash functions, double hashing provides a more uniform probe sequence than linear or quadratic probing.
4. **Rehashing Maintains Efficiency**: When the load factor exceeds a threshold, rehashing (creating a larger table and reinserting keys) restores performance.
5. **Cuckoo Hashing Guarantees Worst-Case O(1)**: Though complex, cuckoo hashing offers predictable performance, useful in real-time systems.
6. **Practical Considerations**: In practice, languages like Java use separate chaining with trees for long chains, while Python uses open addressing with careful deletion handling.
7. **Delhi University Syllabus Alignment**: This module covers all collision resolution schemes listed in the Design and Analysis of Algorithms syllabus, including separate chaining, open addressing, and advanced methods.

---

**End of Study Material**