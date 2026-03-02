# Single and Double Ended Priority Queues

## Introduction

Priority Queues are fundamental abstract data types that extend the concept of a regular queue by assigning a priority level to each element. Unlike a standard First-In-First-Out (FIFO) queue where elements are removed in the order they were inserted, a priority queue removes elements based on their priority value. This data structure is essential in operating systems for process scheduling, in network routing for managing packets, and in various algorithms such as Dijkstra's shortest path algorithm and Huffman coding for data compression.

A Single-Ended Priority Queue (SEPQ), also known as a conventional priority queue, allows insertion of elements with arbitrary priorities and removal of the highest (or lowest) priority element. The Double-Ended Priority Queue (DEPQ) extends this concept by supporting removal of both the highest and lowest priority elements efficiently. DEPQ is particularly useful in scheduling systems where both maximum and minimum priority tasks need immediate attention, and in statistical computations requiring quick access to both extremes of a dataset.

Understanding the implementation details, time complexities, and practical applications of these data structures is crucial for computer science students, as they frequently appear in competitive programming problems and real-world system design scenarios.

## Key Concepts

### Single-Ended Priority Queue (SEPQ)

A Single-Ended Priority Queue is a collection of elements each associated with a priority value. The fundamental operations supported by a SEPQ are:

1. **INSERT(Q, x, p)**: Insert element x with priority p into Q
2. **GET-MAX(Q)**: Return the element with the highest priority without removing it
3. **GET-MIN(Q)**: Return the element with the lowest priority without removing it
4. **EXTRACT-MAX(Q)**: Remove and return the element with the highest priority
5. **EXTRACT-MIN(Q)**: Remove and return the element with the lowest priority
6. **INCREASE-KEY(Q, x, p)**: Increase the priority of element x to p
7. **DECREASE-KEY(Q, x, p)**: Decrease the priority of element x to p

The choice between max-priority and min-priority queue depends on the application context. A max-priority queue returns the largest element, while a min-priority queue returns the smallest element.

### Binary Heap Implementation

The most common implementation of a priority queue uses a binary heap. A binary heap is a complete binary tree that satisfies the heap property:

- **Max-Heap**: For every node, the parent's key is greater than or equal to the children's keys
- **Min-Heap**: For every node, the parent's key is less than or equal to the children's keys

The binary heap can be efficiently represented using an array. For a node at index i:
- Parent is at index (i-1)/2
- Left child is at index 2i+1
- Right child is at index 2i+2

**Time Complexities**:
- INSERT: O(log n)
- EXTRACT-MAX/MIN: O(log n)
- GET-MAX/MIN: O(1)
- HEAPIFY: O(n)

### Double-Ended Priority Queue (DEPQ)

A Double-Ended Priority Queue supports all operations of a SEPQ plus the ability to remove both the maximum and minimum elements efficiently. The essential operations are:

1. **INSERT(x, p)**: Insert element x with priority p
2. **GET-MAX()**: Return the element with highest priority (without removal)
3. **GET-MIN()**: Return the element with lowest priority (without removal)
4. **EXTRACT-MAX()**: Remove and return element with highest priority
5. **EXTRACT-MIN()**: Remove and return element with lowest priority

### DEPQ Implementation Approaches

**Dual Heap Approach**: Maintain two heaps simultaneously—a max-heap and a min-heap. Each element is stored in both heaps with references to each other. This allows O(log n) for all operations, but requires additional space and synchronization between heaps.

**Balanced BST Approach**: Use a balanced binary search tree (AVL tree or Red-Black tree) to store elements. This provides O(log n) for all operations with simpler implementation of both ends, but slightly higher constant factors compared to heaps.

**Interval Heaps**: A specialized heap structure where each node contains two elements representing an interval. The minimum element is always in the leftmost position and maximum in the rightmost, allowing simultaneous access to both extremes in O(1) and updates in O(log n).

**Min-Max Heap**: A specialized heap designed specifically for DEPQ operations, where levels alternate between min and max properties. This structure supports both get-min, get-max in O(1) and extract-min, extract-max in O(log n) with the space of a single heap.

### Heap Sort using Priority Queue

Priority queues provide an elegant mechanism for sorting. The heap sort algorithm works as follows:

1. Insert all n elements into a priority queue: O(n log n)
2. Repeatedly extract elements: O(n log n)
3. Total time complexity: O(n log n)

This sorting approach demonstrates the practical utility of priority queues in algorithm design.

## Examples

### Example 1: Binary Heap Operations

Consider inserting the following elements with priorities into a min-heap: 45, 35, 25, 30, 20, 15

**Step-by-step insertion**:

1. Insert 45: Heap = [45]
2. Insert 35: Heap = [45, 35]; Swap 35 with 45 (35 < 45): Heap = [35, 45]
3. Insert 25: Heap = [35, 45, 25]; Swap 25 with 45 (25 < 45): Heap = [35, 45, 25]; Swap 25 with 35 (25 < 35): Heap = [25, 45, 35]
4. Insert 30: Heap = [25, 45, 35, 30]; No swap needed: Heap = [25, 45, 35, 30]
5. Insert 20: Heap = [25, 45, 35, 30, 20]; Swap 20 with 30 (20 < 30): Heap = [25, 45, 35, 20, 30]; Swap 20 with 25 (20 < 25): Heap = [20, 45, 35, 25, 30]
6. Insert 15: Heap = [20, 45, 35, 25, 30, 15]; Swap 15 with 30: Heap = [20, 45, 35, 25, 15, 30]; Swap 15 with 20: Heap = [15, 45, 35, 25, 15, 30]

Final min-heap: [15, 20, 35, 25, 45, 30]

The minimum element 15 is at the root, as expected in a min-heap.

### Example 2: DEPQ Operations

Given a DEPQ with elements (priority, value): (5, A), (3, B), (8, C), (2, D), (7, E)

**Operations sequence**:

1. **GET-MIN()**: Returns D (priority 2) - O(1)
2. **GET-MAX()**: Returns C (priority 8) - O(1)
3. **INSERT(F, 4)**: Insert F with priority 4
4. **EXTRACT-MAX()**: Removes C (priority 8), returns C
5. **EXTRACT-MIN()**: Removes D (priority 2), returns D

After operations, remaining elements: (3, B), (4, F), (5, A), (7, E)

### Example 3: Priority Queue in Dijkstra's Algorithm

In Dijkstra's shortest path algorithm, a priority queue is used to always process the vertex with the smallest known distance. Given a graph with vertices A, B, C, D and edges with weights, the algorithm maintains a priority queue of vertices to process:

1. Initialize: Insert source vertex with distance 0
2. Extract vertex with minimum distance
3. Update distances of neighboring vertices
4. Re-insert updated vertices into the priority queue

The priority queue ensures that vertices are processed in order of their shortest distance from the source, guaranteeing correctness of the algorithm. Time complexity becomes O((V + E) log V) with binary heap implementation.

## Exam Tips

1. **Know the difference between queue and priority queue**: Regular queue follows FIFO order; priority queue follows priority-based order. This distinction is frequently tested in conceptual questions.

2. **Remember time complexities**: For binary heap implementation—INSERT and EXTRACT-MAX/MIN are O(log n), while GET-MAX/MIN is O(1). Know these for both SEPQ and DEPQ.

3. **Understand heap properties**: The heap property (max-heap or min-heap) must be maintained after every operation. Be prepared to trace through heap operations step-by-step.

4. **Know why complete binary tree**: Heaps are implemented as complete binary trees to guarantee O(log n) height, ensuring efficient operations. This is a common exam question.

5. **DEPQ implementations**: Understand the trade-offs between dual heap, balanced BST, interval heap, and min-max heap approaches. Each has different performance characteristics.

6. **Applications matter**: Know real-world applications—CPU scheduling, network packet handling, Dijkstra's algorithm, Huffman coding. Questions often ask for appropriate data structure selection.

7. **Heapify process**: Understand both top-down (sifting up) and bottom-up (sifting down) heap construction methods and their time complexities.

8. **Space complexity**: Binary heap requires O(n) space for n elements. DEPQ with dual heaps requires O(2n) = O(n) space but with higher constant factor.

9. **Priority queue vs sorting**: Remember that heap sort essentially uses a priority queue to achieve O(n log n) sorting. This connection is important.

10. **Balance considerations**: For DEPQ, the balanced BST approach automatically maintains balance, while heap-based approaches require careful maintenance of both ends.