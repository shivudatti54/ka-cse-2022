# Static Hashing

## Introduction

In the realm of **Data Structures and Applications**, efficient data retrieval is paramount. While data structures like arrays and linked lists store data, their search time can be linear (`O(n)`), which is inefficient for large datasets. Hashing is a technique designed to overcome this by allowing for constant-time (`O(1)`) average-case complexity for search, insertion, and deletion operations. **Static Hashing** is a fundamental form of hashing where the size of the hash table is fixed at the time of creation and cannot be changed dynamically.

## Core Concepts of Static Hashing

The core idea is to map a large, possibly variable-sized, set of keys (e.g., student IDs, product codes) to a smaller, fixed set of indices in an array, called the **hash table**. This mapping is performed by a special function called a **Hash Function**.

### 1. Hash Function (`h`)

A hash function takes a search key (the element to be stored or found) as input and computes an integer value, which is then mapped to a slot/index in the hash table.

*   **Ideal Properties:** It should be easy to compute, distribute keys uniformly across the hash table, and minimize **collisions**.
*   **Example:** A simple hash function for integer keys is `h(k) = k mod m`, where `m` is the size of the hash table (preferably a prime number to ensure better distribution).

### 2. Hash Table

This is a fixed-size array (of size `m`), often denoted as `T[0..m-1]`. Each position in the array is called a **bucket** or a **slot**.

### 3. Collisions

A collision occurs when two distinct keys (`k1` and `k2`) are mapped by the hash function to the same slot in the hash table (i.e., `h(k1) = h(k2)`). Since the number of possible keys is much larger than the number of slots, collisions are inevitable.

### 4. Collision Resolution Techniques

Since the hash table is static (fixed size), we need methods to handle collisions. The two primary techniques are:

#### a) Closed Hashing (Open Addressing)

In this method, all elements are stored *within the hash table itself*. When a collision occurs, the algorithm probes (searches) the table for an empty slot according to a predefined probe sequence.

*   **Linear Probing:** The simplest method. If slot `h(k)` is occupied, check `h(k)+1`, then `h(k)+2`, and so on, modulo `m`, until an empty slot is found.
    *   **Example:** Let `m=7`, `h(k)=k mod 7`. Insert keys `[50, 700, 76, 85, 92]`.
        *   `h(50) = 50 % 7 = 1` -> Insert at index 1.
        *   `h(700) = 700 % 7 = 0` -> Insert at index 0.
        *   `h(76) = 76 % 7 = 76 - (10*7)=76-70=6` -> Insert at index 6.
        *   `h(85) = 85 % 7 = 85 - (12*7)=85-84=1` -> **Collision at index 1**. Use linear probing: check index `(1+1)%7=2` -> Free. Insert 85 at index 2.
        *   `h(92) = 92 % 7 = 92 - (13*7)=92-91=1` -> **Collision**. Check index 2 (occupied), then index 3 (free). Insert 92 at index 3.
*   **Other Methods:** Quadratic Probing, Double Hashing.

#### b) Open Hashing (Separate Chaining)

This is the most common method. Here, each slot in the hash table points to a **linked list** (chain) of all entries that hash to that slot. Collisions are handled by adding the new element to the end of the linked list at the hashed slot.

*   **Example:** Let `m=7`, `h(k)=k mod 7`. Insert the same keys `[50, 700, 76, 85, 92]`.
    *   `h(50)=1` -> Create a linked list at index 1, add 50.
    *   `h(700)=0` -> Create a list at index 0, add 700.
    *   `h(76)=6` -> Create a list at index 6, add 76.
    *   `h(85)=1` -> **Collision**. 85 is appended to the list at index 1 (now `50 -> 85`).
    *   `h(92)=1` -> **Collision**. 92 is appended to the list at index 1 (now `50 -> 85 -> 92`).

## Advantages and Disadvantages

| Advantage | Disadvantage |
| :--- | :--- |
| **Fast Access:** Provides average-case O(1) time for operations. | **Fixed Size:** The table size `m` is fixed. If underestimated, it leads to many collisions and performance degradation. If overestimated, it wastes memory. |
| **Simple to Implement:** The concept and code for separate chaining are straightforward. | **Performance Degradation:** As the hash table fills up, the number of collisions increases, leading to longer probe sequences (in open addressing) or longer chains (in separate chaining). |
| **Efficient for Lookup-Dominant Workloads:** Ideal for use cases where search operations are frequent. | **Inefficient for Dynamic Datasets:** Not suitable if the number of elements is not known in advance, as the table cannot be resized. |

## Key Points / Summary

*   **Purpose:** Static hashing enables efficient data retrieval with average-case O(1) time complexity.
*   **Components:** It consists of a **fixed-size hash table** and a **hash function**.
*   **Collisions are Inevitable:** A good hash function minimizes them but cannot eliminate them.
*   **Collision Resolution:** The two main techniques are **Open Addressing** (e.g., Linear Probing) and **Separate Chaining**.
*   **Static Nature is a Limitation:** The size of the hash table is fixed upon creation, making it unsuitable for databases where the data size grows unpredictably. This limitation leads to the concept of **Dynamic Hashing** (e.g., Extendible Hashing), which you will likely study next.
*   **Use Case:** Best used when the dataset size is known fairly accurately in advance.