# Static Hashing

## Introduction

In the realm of computer science, efficiently storing and retrieving data is a fundamental challenge. Hashing is a powerful technique that maps large amounts of data, typically represented by keys, into a smaller, fixed-size table called a **hash table**. **Static Hashing** refers to a hashing scheme where the size of the hash table is fixed at the time of creation. This means that the number of buckets (slots in the hash table) cannot be changed dynamically. It's a crucial concept for  Engineering students to understand, as it forms the basis for database indexing, symbol tables in compilers, and various caching mechanisms.

## Core Concepts

### 1. Hash Table and Hash Function

A **hash table** is an array of `M` elements, often called **buckets**. Each bucket can hold one or more records.
A **hash function** (`h`) is a mathematical function that takes a search key (e.g., a student ID, a word) as input and returns an integer. This integer is then converted into a valid array index (between `0` and `M-1`) using the modulo operation (`% M`).

`index = h(key) % M`

The primary goal of a good hash function is to uniformly distribute the keys across the available buckets, minimizing collisions.

### 2. Collisions

A **collision** occurs when two or more distinct keys hash to the same bucket index. For example, if `h("John") % 10 = 3` and `h("Jane") % 10 = 3`, a collision occurs at bucket 3. Since the number of possible keys is much larger than the number of buckets (`M`), collisions are inevitable.

### 3. Overflow Handling

An **overflow** occurs when a bucket has no more space to store a new record that hashes to it. In static hashing, the table size is fixed, so handling overflows is a critical design aspect. The two most common methods are:

*   **Chaining (Open Hashing):** Each bucket contains a pointer to a linked list (chain) of records that share the same hash value. New records are simply inserted at the head of the list. This is simple and effective.

    **Example:** Inserting keys 5, 28, 19, 15, 20 into a table of size 10 with hash function `h(key) = key % 10`.
    *   5 % 10 -> bucket 5
    *   28 % 10 -> bucket 8
    *   19 % 10 -> bucket 9
    *   15 % 10 -> bucket 5 -> **Collision with key 5**. A chain is created at bucket 5.
    *   20 % 10 -> bucket 0

*   **Open Addressing (Closed Hashing):** All records are stored directly in the hash table itself. When a collision occurs, the algorithm probes (searches) the table for the next empty slot according to a predefined sequence. Common probe sequences include:
    *   **Linear Probing:** Check the next bucket sequentially. `(h(key) + i) % M` for `i = 0, 1, 2, ...`
    *   **Quadratic Probing:** Check buckets using a quadratic function. `(h(key) + c₁*i + c₂*i²) % M`

### 4. Performance and Limitations

The average-case time complexity for search, insertion, and deletion in a static hash table is **O(1)**, assuming a good hash function and low load factor.

The **load factor** (`α`) is defined as `α = n / (M * bucket_size)`, where `n` is the number of records.
*   As `α` increases, the probability of collisions increases, leading to performance degradation.
*   The major limitation of static hashing is its inflexibility. If the dataset grows significantly larger than the pre-allocated table size (`M`), performance can become very poor (closer to O(n)). Conversely, if the table is too large for the dataset, it wastes memory.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Definition** | A hashing technique with a fixed-size hash table. |
| **Main Components** | Hash Table (array of buckets), Hash Function. |
| **Inevitable Problem** | Collisions (multiple keys mapping to the same bucket). |
| **Collision Resolution** | **Chaining** (using linked lists) and **Open Addressing** (probing for empty slots). |
| **Performance Metric** | Load Factor (`α = n / (M * bucket_size)`). Aim for `α < 0.7` for good performance. |
| **Advantage** | Very fast data access (O(1)) on average. Simple to implement. |
| **Major Disadvantage** | **Fixed table size** leads to performance issues if data grows too much (overflow problems) or memory waste if the table is too large. |
| **Application** | Ideal for situations where the maximum dataset size is known in advance, such as fixed-size lookup tables or caches. |

Static hashing provides excellent performance for known, fixed-size datasets. However, its inability to adapt to growing data led to the development of more flexible techniques like **Dynamic Hashing** and **Extendible Hashing**, which you will likely explore next.