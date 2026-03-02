Of course. Here is comprehensive educational content on Static Hashing for  Engineering students, tailored for the DATA STRUCTURES AND APPLICATIONS curriculum.

# Module 5: Static Hashing

## Introduction
In data structures, efficient data retrieval is as crucial as efficient storage. While search trees offer O(log n) search time, we can do even better. Hashing is a technique that allows for optimal, **O(1)** average-case time complexity for search, insertion, and deletion operations. It achieves this by mapping keys directly to specific locations in a data structure, typically an array. **Static Hashing** refers to a hashing scheme where the size of the hash table is fixed at the time of creation and cannot be changed dynamically.

## Core Concepts of Static Hashing

### 1. The Hash Table
The central component is a fixed-size array, called a **hash table**. Each slot in this array is called a **bucket**. A bucket can hold one or more records.

### 2. The Hash Function
The magic of hashing is performed by a **hash function (h)**. This is a mathematical function that takes a search key (e.g., a student ID, a name) as input and returns an integer. This integer is then converted (usually using the modulo `%` operator) into a valid index within the range of the hash table.

**Purpose:** To uniformly distribute the keys across the hash table. A good hash function minimizes **collisions**.

**Example Hash Function:**
For a table of size `TABLE_SIZE`, a simple hash function for an integer key `k` is:
`h(k) = k % TABLE_SIZE`

If `TABLE_SIZE = 10` and `k = 25`, then `h(25) = 25 % 10 = 5`. The record with key 25 would be placed in bucket 5.

### 3. Collisions
A **collision** occurs when two or more distinct keys hash to the same bucket location. For example, if `k=25` and `k=15` both use `h(k) = k % 10`, then `h(25)=5` and `h(15)=5`—a collision occurs in bucket 5.

Collisions are inevitable (due to the pigeonhole principle) unless you have a perfect hash function for your dataset, which is rare. Therefore, we need methods to resolve them.

### 4. Collision Resolution Techniques
Since the table is static, we must handle collisions within the fixed structure. Two common methods are:

#### a) Separate Chaining (Open Hashing)
In this method, each bucket in the hash table is a pointer to the head of a linked list. All keys that hash to the same bucket are chained together in this linked list.

*   **Insertion:** Compute the hash index. Insert the new record at the head of the linked list at that index.
*   **Search:** Compute the hash index. Traverse the linked list at that index to find the key.
*   **Deletion:** Compute the hash index. Find the key in the linked list and remove that node.

**Example:** For keys 25, 15, 35 with `TABLE_SIZE=10`, all three hash to index 5. The bucket at index 5 will point to a linked list: `[35] -> [15] -> [25]` (assuming insertion in that order).

#### b) Open Addressing (Closed Hashing)
In this method, all records are stored directly *within* the hash table array itself. When a collision occurs, the algorithm systematically probes (searches) for the next empty slot in the table according to a predefined probe sequence.

The most common probe sequences are:
*   **Linear Probing:** The next slot is checked sequentially. `h(k), h(k)+1, h(k)+2, ... % TABLE_SIZE`
*   **Quadratic Probing:** The next slot is checked based on a quadratic function. `h(k), h(k)+1^2, h(k)+2^2, h(k)+3^2, ... % TABLE_SIZE`
*   **Double Hashing:** A second hash function is used to calculate the probe step size.

**Example (Linear Probing):** Insert keys 25, 15, 35 into a table of size 10.
1.  Insert 25: `h(25)=5` -> Slot 5 is empty. Place it there.
2.  Insert 15: `h(15)=5` -> Slot 5 is occupied. Check next slot, slot 6. It's empty. Place 15 there.
3.  Insert 35: `h(35)=5` -> Slot 5 is occupied. Check slot 6; occupied. Check slot 7; empty. Place 35 there.

## Key Points & Summary

| Concept | Description & Key Takeaway |
| :--- | :--- |
| **Goal** | To achieve **average-case O(1)** time complexity for search, insertion, and deletion. |
| **Static Hashing** | The hash table size is **fixed**. It does not grow or shrink dynamically. |
| **Hash Function** | Maps a key to a table index. Must be **fast** and **uniformly distribute** keys. |
| **Collision** | Inevitable event where two keys map to the same bucket. |
| **Collision Resolution** | **Separate Chaining:** Uses linked lists. Simple, efficient. <br> **Open Addressing:** Finds next open slot within the table. Saves memory but can lead to clustering. |
| **Primary Clustering** | A problem in Linear Probing where consecutive groups of occupied buckets form, slowing down operations. Quadratic and Double Hashing mitigate this. |
| **Limitation** | The fixed table size is a major drawback. If too small, collisions become frequent. If too large, memory is wasted. This leads to the need for **Dynamic Hashing** techniques (e.g., Extendible Hashing). |
| **Load Factor (α)** | A critical metric: `α = n / TABLE_SIZE` (n = number of entries). Performance degrades as α increases beyond 0.7. |