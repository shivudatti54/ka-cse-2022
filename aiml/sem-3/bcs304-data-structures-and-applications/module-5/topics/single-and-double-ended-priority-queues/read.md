# Single and Double Ended Priority Queues


## Table of Contents

- [Single and Double Ended Priority Queues](#single-and-double-ended-priority-queues)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Single-Ended Priority Queue (SEPQ)](#single-ended-priority-queue-sepq)
  - [Double-Ended Priority Queue (DEPQ)](#double-ended-priority-queue-depq)
  - [Implementation Analysis](#implementation-analysis)
- [Examples](#examples)
  - [Example 1: Binary Heap Operations](#example-1-binary-heap-operations)
  - [Example 2: Min-Max Heap Construction](#example-2-min-max-heap-construction)
  - [Example 3: Priority Queue in Dijkstra's Algorithm](#example-3-priority-queue-in-dijkstras-algorithm)
- [Exam Tips](#exam-tips)

## Introduction

A priority queue is a specialized abstract data type that maintains a set of elements, each associated with a key called a "priority," where access to the element with the highest (or lowest) priority is the primary operation. Unlike a standard queue that follows First-In-First-Out (FIFO) order, a priority queue serves elements based on their priority rather than their arrival time. Priority queues are fundamental data structures in computer science, serving as essential components in numerous algorithms including Dijkstra's shortest path algorithm, Prim's minimum spanning tree algorithm, Huffman coding, and task scheduling systems.

A **Single-Ended Priority Queue (SEPQ)**, also known as a conventional priority queue, supports the retrieval and removal of either the minimum or maximum element from the set. Depending on whether it extracts the minimum or maximum, it is classified as a Min-PQ or Max-PQ. In contrast, a **Double-Ended Priority Queue (DEPQ)** is a more sophisticated data structure that allows efficient access to both the minimum and maximum elements simultaneously. This dual-access capability makes DEPQs particularly valuable in real-time systems, load balancing applications, and scenarios requiring simultaneous tracking of extreme values, such as maintaining sliding window minimums and maximums in stream processing.

The theoretical foundations of priority queues are deeply connected to heap data structures, which provide elegant implementations achieving optimal time complexities for key operations. Understanding the mathematical properties of heaps, including the complete binary tree representation and the heap-order property, is essential for analyzing the performance characteristics of priority queue implementations. The study of priority queues also encompasses advanced amortized analysis techniques, particularly evident in Fibonacci heap implementations where the structure of the heap allows for improved asymptotic performance in certain operation sequences.

## Key Concepts

### Single-Ended Priority Queue (SEPQ)

A Single-Ended Priority Queue is formally defined as an abstract data type that supports the following fundamental operations: **insert(x)** adds an element x with an associated priority key to the priority queue; **getMin()** (or getMax() for Max-PQ) returns the element with the smallest (or largest) key without removing it; **extractMin()** (or extractMax()) removes and returns the element with the smallest (or largest) key; and **decreaseKey(x, newVal)** decreases the value of key associated with element x. The heap-ordered binary tree property states that for every node, the key of that node is less than or equal to (for Min-PQ) or greater than or equal to (for Max-PQ) the keys of its children, ensuring that the minimum (or maximum) element is always located at the root.

The binary heap implementation represents the priority queue as a complete binary tree stored sequentially in an array, where for a node at index i, its left child is at index 2i + 1, right child at 2i + 2, and parent at floor((i-1)/2). This sequential representation eliminates the need for explicit pointers, resulting in excellent cache locality. The heapify operation, comprising sift-up (bubble-up) for insertions and sift-down (bubble-down) for extractions, maintains the heap property in O(log n) time. Building a heap from an unordered array using the Floyd's heap construction algorithm achieves O(n) time complexity through bottom-up heap construction, a result derived from the summation of geometric series of work performed at different tree levels.

### Double-Ended Priority Queue (DEPQ)

A Double-Ended Priority Queue extends the conventional priority queue by supporting efficient access to both extremes simultaneously. Formally, a DEPQ must support **getMin()**, **getMax()**, **extractMin()**, and **extractMax()** operations, all in O(log n) time complexity. Additionally, operations like **insert(x)** and **delete(x)** (removing an arbitrary element) must also maintain logarithmic time performance to make the data structure practically useful.

The **Min-Max Heap** is a specialized heap structure designed explicitly for DEPQ operations, where the heap is organized in alternating min and max levels. At min-levels (root, levels 0, 2, 4, ...), each node's key is less than or equal to its children, while at max-levels (levels 1, 3, 5, ...), each node's key is greater than or equal to its children. This clever arrangement ensures that the minimum element is always found at the root, while the maximum element resides at one of the root's children. The sift-up and sift-down operations in a min-max heap require determining the current level parity and searching among grandchildren rather than children, extending the logarithmic bound by a constant factor.

The **Deap** (double-ended heap) is another DEPQ structure consisting of two parallel heaps: a min-heap and a max-heap, with a special relationship between them. Elements in the min-heap hold smaller values while corresponding "paired" elements in the max-heap hold larger values, enabling efficient access to both extremes. The **Interval Heap** represents yet another approach, where each node contains two elements forming an interval, and the intervals are organized such that consecutive nodes form a complete binary tree structure, allowing O(log n) operations for all four extreme access operations.

### Implementation Analysis

The choice of implementation depends heavily on the specific operation mix required by the application. Binary heaps provide excellent average-case performance and simple implementation, making them the default choice for most applications. Fibonacci heaps achieve amortized O(1) insertion time through lazy consolidation, though their practical performance often lags behind binary heaps due to high constant factors and cache misses. For DEPQ operations, the min-max heap provides a space-efficient solution requiring no additional storage beyond the array representation, while the deap requires approximately twice the storage of a conventional heap.

**Theorem (Heap Property Maintenance)**: For a binary heap of n elements, the height of the tree is floor(log₂ n), and therefore both sift-up and sift-down operations complete in O(log n) time.

_Proof_: A complete binary tree of height h has at most 2⁰ + 2¹ + ... + 2ʰ = 2^(h+1) - 1 nodes. Solving for h in n ≤ 2^(h+1) - 1 gives h ≥ log₂(n+1) - 1, and since h is an integer, h = floor(log₂ n). Sift-up moves an element at most h levels upward, and sift-down moves an element at most h levels downward, establishing the O(log n) bound. ∎

## Examples

### Example 1: Binary Heap Operations

Consider inserting the elements 15, 10, 20, 17, 8 into an initially empty Min-PQ using a binary heap:

After insert(15): heap = [15]
After insert(10): heap = [10, 15] (10 bubbles up past 15)
After insert(20): heap = [10, 15, 20]
After insert(17): heap = [10, 15, 20, 17]
After insert(8): heap = [8, 10, 20, 17, 15] (8 bubbles up to root)

The final heap structure (tree representation):

```
       8
     /   \
   10     20
  /
 17
```

Each insertion required O(log n) = O(1) at most for this small heap, demonstrating the heap property maintenance through the sift-up operation.

### Example 2: Min-Max Heap Construction

Construct a Min-Max Heap by inserting 5, 2, 8, 1, 9, 3, 7 into an empty structure:

After inserting all elements, the min-max heap maintains alternating min/max levels:

- Level 0 (min): 1 (minimum)
- Level 1 (max): 9 (maximum)
- Level 2 (min): 2, 5, 8
- Level 3 (max): 3, 7

getMin() returns 1 (root), getMax() returns 9 (child of root). This structure enables O(1) access to both extremes while maintaining O(log n) insertion and extraction through level-aware sift operations.

### Example 3: Priority Queue in Dijkstra's Algorithm

In Dijkstra's shortest path algorithm, a priority queue stores vertices keyed by their current distance estimates. The algorithm repeatedly extracts the vertex with minimum distance (extractMin), then relaxes edges to adjacent vertices, potentially decreasing their keys (decreaseKey operation). Using a binary heap, each operation costs O(log V), resulting in O(E log V) total time for a graph with V vertices and E edges. This demonstrates the critical role of priority queues in graph algorithms and why efficient DEPQ implementations matter in practice.

## Exam Tips

1. **Know the heap array indexing**: For a node at index i in a 0-based array representation, left child = 2i + 1, right child = 2i + 2, parent = floor((i-1)/2).

2. **Remember heap height**: The height of a heap with n nodes is always floor(log₂ n), determining the worst-case time complexity of sift operations.

3. **Understand DEPQ vs SEPQ**: DEPQ allows O(1) access to both minimum and maximum, while SEPQ provides access to only one extreme efficiently.

4. **Min-max heap levels**: Remember that min-max heaps alternate between min-levels (root, levels 0, 2, 4, ...) and max-levels (levels 1, 3, 5, ...).

5. **Floyd's heap construction**: Building a heap from an unordered array using bottom-up heapify achieves O(n) time, not O(n log n).

6. **Amortized analysis**: Fibonacci heaps achieve amortized O(1) insert but O(log n) extract-min, making them suitable when insert operations dominate.

7. **Space complexity**: Binary heaps use O(n) space with excellent cache performance; Fibonacci heaps have higher constant factors despite theoretical optimality.
