Of course. Here is a comprehensive educational module on Dynamic Hashing and Priority Queues for  Engineering students.

# Module 5: Dynamic Hashing & Priority Queues

## 1. Introduction

As engineers, we often deal with data that grows or shrinks dynamically. Traditional static data structures like arrays have fixed sizes, leading to inefficiencies. This module introduces two fundamental concepts designed for dynamic data handling: **Dynamic Hashing**, which allows databases to scale efficiently, and **Priority Queues**, an abstract data type crucial for scheduling and greedy algorithms.

---

## 2. Dynamic Hashing

### Core Concept

Static hashing schemes (like linear probing) require knowing the maximum dataset size upfront, which is often impractical. **Dynamic Hashing** techniques allow the hash table to grow and shrink dynamically, maintaining an average constant-time complexity for search, insert, and delete operations, even as data volume changes.

The most common dynamic hashing technique is **Extendible Hashing**.

### How Extendible Hashing Works

It uses a **directory** (an array of pointers) to point to **buckets** (data blocks). The directory grows and shrinks as needed, doubling or halving in size. This process is called **directory expansion** and **contraction**.

**Key Components:**

- **Directory:** An array of pointers. The number of bits used from the hash value to index the directory is the **global depth**.
- **Bucket:** Where the actual (key, value) pairs are stored. Each bucket has a **local depth**.
- **Global Depth (_d_):** Number of bits used to index the directory. The directory has `2^d` entries.
- **Local Depth (_l_):** Number of bits used to determine the keys belonging to a specific bucket. `l <= d`.

### Example: Insertion and Bucket Overflow

Assume a system starts with a global depth `d = 1` and two buckets (local depth `l = 1`). The directory has 2 entries: `0 -> Bucket A`, `1 -> Bucket B`.

1.  **Insert key `13`** (binary `1101`). Use last `d=1` bit: `1`. It goes to Bucket B.
2.  **Insert key `5`** (binary `0101`). Last bit is `1`. It also goes to Bucket B.
3.  **Insert key `7`** (binary `0111`). Last bit is `1`. Bucket B is now full (assuming a capacity of 2).
4.  **Bucket Split:** Bucket B overflows. We increase its local depth to `l=2`. We now look at the last _2_ bits of the hash value.
    - Keys in Bucket B: `13` (`1101` -> `01`), `5` (`0101` -> `01`), `7` (`0111` -> `11`).
    - We split the bucket into two new buckets based on the last 2 bits: one for `01` and one for `11`.
    - `13` and `5` (last two bits `01`) stay in a new bucket.
    - `7` (last two bits `11`) moves to a new bucket.
5.  **Directory Expansion:** Since the local depth (`l=2`) is now greater than the global depth (`d=1`), we must double the directory size. New global depth `d = 2`. The directory now has 4 entries (`00`, `01`, `10`, `11`).
    - The `01` and `11` entries point to the two new buckets.
    - The `00` and `10` entries still point to the original Bucket A (its local depth is still 1).

This process allows the table to grow gracefully without rehashing all existing keys.

---

## 3. Priority Queues

### Core Concept

A **Priority Queue** is an Abstract Data Type (ADT) that is similar to a regular queue or stack, but where each element has a **priority**. The fundamental rule is: **the element with the highest (or lowest) priority is served (dequeued) before all elements with lower (or higher) priority.**

- **Max-Priority Queue:** Highest priority element is dequeued first.
- **Min-Priority Queue:** Lowest priority element is dequeued first.

It does not follow the strict First-In-First-Out (FIFO) behavior of a simple queue.

### Implementation

While a simple unsorted array or linked list can implement a priority queue (with O(n) time for insertion or deletion), efficient implementations use more sophisticated data structures:

1.  **Binary Heap (Most Common):**
    - A complete binary tree that satisfies the **heap property**.
    - **Max-Heap:** The key at the root is the largest. The key of any node is greater than or equal to the keys of its children.
    - **Min-Heap:** The key at the root is the smallest. The key of any node is less than or equal to the keys of its children.
    - **Operations:**
      - `insert()`: O(log n) time. Add element at the end and "heapify up".
      - `extract_max()` or `extract_min()`: O(log n) time. Remove the root, replace it with the last element, and "heapify down".

2.  **Other Implementations:** Binomial Heaps, Fibonacci Heaps (for even more efficient decrease-key operations).

### Example & Applications

**Example:** In a hospital emergency room, patients are not served in the order they arrive (FIFO) but based on the severity of their condition (priority). A patient with a critical injury (high priority) will be seen before a patient with a minor cut (low priority), even if the latter arrived first.

**Key Applications:**

- **Scheduling Algorithms:** In operating systems (e.g., shortest job first).
- **Graph Algorithms:** Dijkstra's algorithm (shortest path), Prim's algorithm (minimum spanning tree).
- **Data Compression:** Huffman coding.
- **Simulation Systems:** Where events are processed based on their simulation time.

---

## 4. Summary & Key Points

| Concept                          | Key Idea                                                                                              | Advantage                                                                                    | Common Use                                                                   |
| :------------------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Dynamic Hashing (Extendible)** | Uses a dynamic directory to point to data buckets. Directory expands (doubles) when buckets overflow. | Efficiently handles growing datasets. Avoids full-table rehashing. O(1) average access time. | Database systems, file systems.                                              |
| **Priority Queue**               | An ADT where elements are dequeued based on priority, not insertion order.                            | Enables efficient scheduling and greedy choices in algorithms.                               | Task scheduling, graph algorithms (Dijkstra, Prim), simulation.              |
| **Binary Heap**                  | An efficient (O(log n)) tree-based implementation of a priority queue.                                | Balanced tree structure ensures logarithmic time for insert and extract operations.          | The go-to implementation for priority queues when no decrease-key is needed. |

**In essence, Dynamic Hashing provides the underlying efficient storage mechanism for large, dynamic datasets, while Priority Queues provide the logical structure for processing data based on importance, a combination crucial for building scalable and intelligent systems.**
