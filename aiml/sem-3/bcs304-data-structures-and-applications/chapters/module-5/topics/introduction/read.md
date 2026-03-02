# Introduction to Hashing and Priority Queues

## Introduction

Data structures form the backbone of efficient algorithm design and software development. In the realm of computer science, the ability to store, organize, and retrieve data efficiently directly impacts the performance of applications ranging from database systems to real-time computing environments. This module explores two fundamental and widely-used data structures: Hashing and Priority Queues. These structures address critical computational problems that arise in virtually every domain of computing, from operating system scheduling to network routing and database management.

Hashing provides an elegant solution to the dictionary problem—the need to insert, delete, and retrieve elements in constant average time. Unlike sequential search methods that require O(n) time complexity, hash tables leverage mathematical hash functions to compute storage locations directly, achieving remarkable efficiency for large datasets. Modern computing systems rely heavily on hash tables for tasks such as symbol table management in compilers, database indexing, caching mechanisms, and cryptographic applications.

Priority queues represent another essential abstraction in computer science, supporting the retrieval of elements based on their priority rather than their insertion order. Unlike standard queues that follow a First-In-First-Out (FIFO) discipline, priority queues ensure that the highest (or lowest) priority element is always served first. This behavior proves crucial in scenarios ranging from operating system task scheduling where time-critical processes must preempt others, to graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree, where efficient extraction of minimum-weight edges is paramount.

## Key Concepts

### Hashing Fundamentals

A hash table is a data structure that implements an associative array, allowing key-value pairs to be stored and retrieved efficiently. The core idea involves using a hash function that maps keys to array indices. When a key is inserted, the hash function computes its hash value, which determines the storage location (bucket) within the underlying array. To retrieve a value, the same hash function computes the location where the value should be stored.

The hash function must satisfy two essential properties: it should distribute keys uniformly across the available buckets to minimize collisions, and it should be computationally efficient to calculate. Common hash functions include the division method (key mod table size), multiplication method ((key × A) mod 1 mod table size), and universal hashing (selecting a function randomly from a family of functions).

A collision occurs when two different keys hash to the same bucket location. Handling collisions efficiently is central to hash table design. The two primary collision resolution techniques are chaining (maintaining a linked list of elements at each bucket) and open addressing (probing alternative locations when a collision occurs). Open addressing employs various probing strategies including linear probing, quadratic probing, and double hashing.

The load factor (α = n/m, where n is the number of elements and m is the number of buckets) critically influences hash table performance. As the load factor increases, collision probability rises, degrading performance. Dynamic hashing addresses this by allowing the hash table to grow and shrink dynamically, maintaining optimal load factor within specified bounds.

### Static vs Dynamic Hashing

Static hashing employs a fixed number of buckets that remains constant throughout the table's lifetime. While simple to implement, static hash tables suffer from performance degradation as the dataset grows beyond initial capacity, and wasted space when the dataset remains small. The hash function in static hashing typically uses the division method with a carefully chosen prime number of buckets to minimize clustering patterns.

Dynamic hashing, also known as extendible hashing, overcomes static hashing's limitations by allowing the number of buckets to grow and shrink dynamically. The most common approach uses a binary tree structure where each node corresponds to a bucket, and the tree expands or contracts based on the current load. When a bucket overflows, it splits, and entries are redistributed. This approach ensures that the hash table adapts to varying dataset sizes while maintaining efficient access times.

### Priority Queue Fundamentals

A priority queue is an abstract data type similar to a regular queue or stack, but with the additional property that each element has an associated priority. Elements with higher priority are served before elements with lower priority, regardless of their insertion order. When two elements have equal priority, they are typically served according to their insertion order (FIFO for equal priorities).

Priority queues can be implemented using various underlying structures. The simplest implementation using an unordered array or linked list supports insertion in O(1) time but requires O(n) time to find and remove the maximum (or minimum) element. Ordered implementations reverse this trade-off, achieving O(1) removal of the extreme element at the cost of O(n) insertion. The optimal implementation using a heap data structure achieves O(log n) time complexity for both insertion and extraction of the extreme element.

The heap property distinguishes heaps from other tree structures. In a max-heap, each parent node contains a value greater than or equal to both its children, ensuring that the maximum element resides at the root. Conversely, a min-heap ensures the minimum element is at the root. This hierarchical ordering enables efficient implementation of priority queue operations through heapify procedures.

### Single and Double Ended Priority Queues

A standard priority queue supports access to only one extreme element—the maximum in a max-heap or minimum in a min-heap. Single-ended priority queues (SEPQ) are the conventional form, providing operations to insert elements and extract either the maximum or minimum. Applications include task scheduling where highest-priority tasks must execute first, or event simulation where earliest-occurring events require processing.

Double-ended priority queues (DEPQ) extend this concept by supporting access to both extremes simultaneously. A DEPQ allows retrieval and removal of both the maximum and minimum elements, along with standard insertion operations. This capability proves valuable in applications such as maintaining median values in streaming data (where median equals the middle element), adaptive sorting algorithms that benefit from simultaneously accessing largest and smallest remaining elements, and real-time systems requiring awareness of both highest and lowest priority items.

Implementing a DEPQ efficiently requires careful design. Simple approaches using two separate heaps (a max-heap and a min-heap) can achieve O(log n) performance for all operations. More sophisticated implementations maintain balance between the two heaps to ensure efficient access to both extremes.

## Examples

### Example 1: Hash Table Insertion with Linear Probing

Consider inserting the elements 15, 22, 7, 31, 20 into a hash table of size 10 using hash function h(k) = k mod 10 with linear probing for collision resolution.

Solution:
- Insert 15: h(15) = 15 mod 10 = 5. Store at index 5.
- Insert 22: h(22) = 22 mod 10 = 2. Store at index 2.
- Insert 7: h(7) = 7 mod 10 = 7. Store at index 7.
- Insert 31: h(31) = 31 mod 10 = 1. Store at index 1.
- Insert 20: h(20) = 20 mod 10 = 0. Store at index 0.

Final hash table: [20, 31, 22, -, -, 15, -, 7, -, -]

### Example 2: Heap Operations

Given the array [4, 10, 3, 5, 1], perform insert(8) into a max-heap.

Solution:
First, convert the array to a max-heap by heapifying from the last non-leaf node:
- Initial array: [4, 10, 3, 5, 1]
- Heapify at index 1 (value 10): [4, 10, 3, 5, 1] (already satisfies max-heap property)
- Heapify at index 0 (value 4): Compare with children 10 and 3. Swap 4 with 10.
- Resulting heap: [10, 4, 3, 5, 1]

Now insert 8:
- Add 8 at the end: [10, 4, 3, 5, 1, 8]
- Compare 8 with parent at index 2 (value 3): 8 > 3, swap
- Heap after swap: [10, 4, 8, 5, 1, 3]
- Compare 8 with parent at index 0 (value 10): 8 < 10, stop
- Final max-heap after insertion: [10, 4, 8, 5, 1, 3]

### Example 3: Priority Queue Application in Scheduling

In an operating system, three processes arrive with priorities 3, 1, and 5 (higher number indicates higher priority) at times 0, 1, and 2 respectively. Show the order of execution using a max-heap based priority queue.

Solution:
- Time 0: Insert process with priority 3. PQ: [{priority:3}]
- Time 1: Insert process with priority 1. PQ: [{priority:3}, {priority:1}]
- Time 2: Insert process with priority 5. PQ: [{priority:5}, {priority:1}, {priority:3}]

Execution order (extract max each time):
1. Extract priority 5 (time 2): Process with priority 5 executes
2. Extract priority 3 (time 2): Process with priority 3 executes
3. Extract priority 1 (time 2): Process with priority 1 executes

## Exam Tips

Understanding hashing and priority queues is crucial for DU semester examinations. Here are essential points to remember:

1. Hash function properties: A good hash function should be deterministic, uniform, and efficient. The division method works best when the table size is a prime number not close to a power of 2.

2. Collision resolution techniques: Remember the differences between chaining (O(1 + α) average search) and open addressing (requires careful probing sequence selection). Linear probing suffers from primary clustering, while quadratic probing helps but may not find all buckets.

3. Load factor significance: Maintain load factor below 0.5 for open addressing and below 0.75 for chaining to ensure acceptable performance. When load factor exceeds threshold, rehashing becomes necessary.

4. Heap operations complexity: Insert and extract-min/max both require O(log n) time in a binary heap. Building a heap from n elements takes O(n) time using the bottom-up heapify approach.

5. Heap property visualization: In a max-heap, ancestors always have greater values than descendants. The root always contains the maximum element. This property must hold for all subtrees.

6. Priority queue implementations: For DEPQ, the two-heap approach maintains elements in both a max-heap and min-heap, typically with size difference never exceeding 1.

7. Applications recognition: Remember that Dijkstra's algorithm and Prim's algorithm both use priority queues. Operating system CPU scheduling frequently employs priority queues for process management.

8. Dynamic hashing advantage: Unlike static hashing, dynamic hashing grows the table seamlessly without requiring complete rehashing, making it suitable for databases with unpredictable growth patterns.