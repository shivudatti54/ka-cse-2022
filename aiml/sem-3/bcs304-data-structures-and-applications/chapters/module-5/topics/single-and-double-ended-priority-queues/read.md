# Single and Double Ended Priority Queues

## Introduction

A Priority Queue is an abstract data type that extends the concept of a regular queue by assigning a priority to each element. Unlike a standard FIFO (First-In-First-Out) queue where elements are removed in the order they were inserted, a priority queue removes elements based on their priority level. Elements with higher priority are served before elements with lower priority, regardless of their insertion order.

In the context of data structures, priority queues play a fundamental role in algorithm design, particularly in scheduling algorithms, graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree, and event-driven simulations. The study of priority queues is essential for any computer science student as they form the backbone of numerous real-world applications.

This chapter explores two important variants of priority queues: Single-Ended Priority Queues (SEPQ) and Double-Ended Priority Queues (DEPQ). While a single-ended priority queue supports operations at only one end (either finding minimum or maximum), a double-ended priority queue allows operations at both ends, enabling efficient access to both the smallest and largest elements simultaneously.

## Key Concepts

### Single-Ended Priority Queue (SEPQ)

A Single-Ended Priority Queue, also known as a conventional priority queue, is designed to support operations primarily at one end. Depending on the implementation, it can function as either a Min-Priority Queue or a Max-Priority Queue.

In a Min-Priority Queue, the element with the smallest key value has the highest priority and is removed first during deletion operations. Conversely, in a Max-Priority Queue, the element with the largest key value receives the highest priority. The choice between min and max depends entirely on the application requirements.

**Operations supported by SEPQ:**

- **INSERT(Q, x)**: Inserts element x into priority queue Q. The time complexity for a binary heap implementation is O(log n) on average and worst case.

- **MIN(Q) / MAX(Q)**: Returns the element with minimum or maximum priority respectively without removing it. This operation has O(1) time complexity.

- **DELETE-MIN(Q) / DELETE-MAX(Q)**: Removes and returns the element with minimum or maximum priority. This operation requires O(log n) time in binary heap implementations.

- **IS-EMPTY(Q)**: Returns true if the priority queue contains no elements, otherwise returns false.

### Double-Ended Priority Queue (DEPQ)

A Double-Ended Priority Queue is an extension of the conventional priority queue that allows access and removal of both the minimum and maximum elements efficiently. This makes DEPQ particularly useful in scenarios where both extremes need to be processed, such as in median maintenance, load balancing, and certain scheduling problems.

The DEPQ supports all the operations of a single-ended priority queue plus symmetric operations at the opposite end:

- **INSERT(Q, x)**: Inserts element x into the DEPQ.

- **GET-MIN(Q)**: Returns the minimum element without removal.

- **GET-MAX(Q)**: Returns the maximum element without removal.

- **DELETE-MIN(Q)**: Removes and returns the minimum element.

- **DELETE-MAX(Q)**: Removes and returns the maximum element.

- **SIZE(Q)**: Returns the number of elements in the DEPQ.

- **IS-EMPTY(Q)**: Checks whether the DEPQ is empty.

### Implementation Approaches

**Binary Heap Implementation:**

The most common implementation for priority queues is using a binary heap, which is a complete binary tree that satisfies the heap property. For a min-heap, each parent node has a value less than or equal to its children (min-heap property). For a max-heap, each parent node has a value greater than or equal to its children (max-heap property).

For a single-ended priority queue, a binary heap provides efficient O(log n) insert and delete operations. However, implementing a DEPQ using a single binary heap becomes inefficient because maintaining both min and max properties simultaneously is challenging.

**Dual Heap Implementation:**

One efficient approach for DEPQ uses two heaps working in tandem: a min-heap and a max-heap. Each element is stored in both heaps, with additional pointers or indices to maintain correspondence between the two heap representations. This approach achieves O(log n) time complexity for all operations, but requires twice the storage space.

**Balanced BST Implementation:**

A balanced binary search tree (such as AVL tree or Red-Black tree) can efficiently implement both SEPQ and DEPQ. In a BST, the minimum element is found at the leftmost node while the maximum is at the rightmost node. All operations (insert, delete, find min, find max) can be performed in O(log n) time. The main advantage over heaps is that BSTs support efficient traversal in sorted order, which heaps cannot provide directly.

**Interval Heap:**

An interval heap is a specialized data structure specifically designed for DEPQ operations. In an interval heap, each node contains two elements representing an interval [min, max]. For odd-numbered elements, the structure behaves like a min-heap for the lower half and a max-heap for the upper half. This elegant design allows all DEPQ operations to be performed in O(log n) time with efficient space utilization.

### Heapify and Heap Sort

The process of converting an arbitrary array into a heap structure is called heapify. Two approaches exist: bottom-up heapify (sift-down) for building a heap from an array, and top-down heapify (sift-up) for inserting elements one by one. Building a heap using the bottom-up approach takes O(n) time, which is more efficient than inserting n elements individually at O(n log n).

Heap Sort utilizes the heap property to sort elements in ascending or descending order. By building a max-heap and repeatedly extracting the maximum element, we can sort an array in O(n log n) time with O(1) auxiliary space, making it an efficient comparison-based sorting algorithm.

## Examples

**Example 1: Operations on a Min-Priority Queue**

Consider inserting the following elements into a Min-Priority Queue in the given order: 15, 10, 20, 8, 25, 5.

Step 1: Insert 15
Heap: [15]

Step 2: Insert 10 (sift-up: 10 < 15, swap)
Heap: [10, 15]

Step 3: Insert 20
Heap: [10, 15, 20]

Step 4: Insert 8 (sift-up: 8 < 10, swap; 8 < 15, swap)
Heap: [8, 10, 20, 15]

Step 5: Insert 25
Heap: [8, 10, 20, 15, 25]

Step 6: Insert 5 (sift-up: 5 < 8, swap; 5 < 10, swap; 5 < 15, swap)
Heap: [5, 8, 20, 15, 10, 25]

Now, perform DELETE-MIN three times:
- First DELETE-MIN: Remove 5, replace with 25, sift-down: [8, 10, 20, 15, 25]
- Second DELETE-MIN: Remove 8, replace with 25, sift-down: [10, 15, 20, 25]
- Third DELETE-MIN: Remove 10, replace with 25, sift-down: [15, 25, 20]

**Example 2: DEPQ Operation Sequence**

Consider performing the following operations on a Double-Ended Priority Queue:

1. INSERT(10)
2. INSERT(5)
3. INSERT(20)
4. INSERT(15)
5. GET-MIN() → returns 5
6. GET-MAX() → returns 20
7. DELETE-MIN() → removes 5, returns 5
8. DELETE-MAX() → removes 20, returns 20

After operations 1-4, the DEPQ contains elements {10, 5, 20, 15}. The minimum is 5 and maximum is 20. After deleting both extremes, the remaining elements are {10, 15}.

**Example 3: Application in Job Scheduling**

In a print queue system where print jobs have priority levels (lower number = higher priority), a Min-Priority Queue efficiently handles job scheduling. When a new print job arrives with priority 2, it is inserted into the queue. The print scheduler always selects the job with minimum priority value (highest priority) to process next. If two jobs have the same priority, FIFO order is typically used as a tiebreaker, which can be implemented by storing a timestamp along with each element.

## Exam Tips

1. **Understand the fundamental difference**: Remember that SEPQ supports either min or max operations, while DEPQ supports both. This distinction is frequently tested in DU examinations.

2. **Time Complexities**: For binary heap implementations, remember that INSERT and DELETE-MIN/MAX take O(log n) time, while GET-MIN/MAX takes O(1) time. Building a heap from n elements takes O(n) time.

3. **Heap Property**: In a min-heap, the parent is always smaller than or equal to its children. In a max-heap, the parent is always greater than or equal to its children. Know how to identify violations and how to fix them through sift-up and sift-down operations.

4. **Complete Binary Tree Property**: Since heaps are implemented using arrays, understand how to calculate parent, left child, and right child indices using formulas: parent = floor(i/2), left = 2i, right = 2i + 1.

5. **DEPQ Implementation**: For exams, the dual heap approach and interval heap are the two most commonly discussed implementations. Know the trade-offs between them in terms of space and time complexity.

6. **Applications**: Be prepared to explain real-world applications of priority queues such as CPU scheduling, Dijkstra's algorithm, Prim's algorithm, and event simulation.

7. **Heap Sort**: Remember that heap sort works by building a max-heap and repeatedly extracting the maximum element. The time complexity is O(n log n) in all cases.

8. **Space Complexity**: Binary heap requires O(n) space, while dual heap for DEPQ requires O(2n) space. Interval heap requires O(2n) space but is more space-efficient in practice for certain scenarios.