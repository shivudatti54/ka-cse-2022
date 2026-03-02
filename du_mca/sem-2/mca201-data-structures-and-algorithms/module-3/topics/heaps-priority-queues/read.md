# Heaps and Priority Queues

## Introduction
Heaps are specialized tree-based data structures that satisfy the heap property: in a max-heap, parent nodes are greater than or equal to child nodes; in a min-heap, parent nodes are smaller. Priority queues abstract data types that operate on the principle of highest-priority-first removal, making heaps their ideal underlying implementation due to O(1) access to extremal values.

These structures are fundamental in algorithms requiring efficient priority management. Real-world applications include:
- Hospital emergency room triage systems
- Operating system process scheduling
- Dijkstra's shortest path algorithm
- Heap Sort implementation

The combination of O(log n) insertion/extraction and O(1) peek operations makes heaps crucial for performance-critical systems. Understanding their array-based implementation and heapify operations is essential for algorithm optimization.

## Key Concepts
1. **Heap Properties**:
   - Complete binary tree structure
   - Heap property (min/max variant)
   - Array representation: Parent at i → children at 2i+1 and 2i+2

2. **Heap Operations**:
   - **Heapify**: O(n) bottom-up construction
   - **Insert**: O(log n) percolate-up
   - **Extract-Max/Min**: O(log n) percolate-down
   - **Increase/Decrease Key**: Priority modification

3. **Priority Queue ADT**:
   - enqueue() with priority
   - dequeue() highest priority element
   - peek() without removal
   - Implementation variations: Unsorted array, sorted array, heap (most efficient)

4. **Advanced Variants**:
   - Binomial Heaps
   - Fibonacci Heaps (amortized O(1) decrease-key)
   - d-ary Heaps (generalized child count)

## Examples

**Example 1: Max-Heap Construction**
Given array [4, 10, 3, 5, 1], build max-heap:

Step 1: Start from last parent (index 1)
Step 2: Heapify index 1:
10 is larger than children (5 and 1) → valid
Step 3: Heapify index 0:
4 < 10 → swap. New array [10,5,3,4,1]
Final heap: 
      10
     /  \
    5    3
   / \
  4   1

**Example 2: Priority Queue Operations**
Initial max-heap: [9,5,7,1,3]
1. enqueue(8): Add at end → [9,5,7,1,3,8]
   Percolate up: 8 vs parent 7 → valid. Final: [9,5,8,1,3,7]
2. dequeue(): Extract 9. Replace with 7 → [7,5,8,1,3]
   Max-heapify: swap 7 and 8 → [8,5,7,1,3]

**Example 3: Heap Sort**
Array [6,2,9,1,5]:
1. Build max-heap → [9,5,6,1,2]
2. Repeatedly extract max:
   9 → [6,5,2,1] → sorted [9]
   6 → [5,1,2] → sorted [6,9]
   Continue until sorted array [1,2,5,6,9]

## Exam Tips
1. Always verify heap properties after each operation in diagrams
2. Remember array indices start at 0 for left-child calculation: left=2i+1
3. For "build-heap" time complexity, derive using geometric series (O(n))
4. Priority queue implementation comparisons: heaps vs sorted arrays
5. Heap Sort's O(n log n) complexity comes from n extract-max operations
6. In written answers, differentiate between heapify (top-down) and percolate (bottom-up)
7. Real-world applications fetch more marks - mention job schedulers or graph algorithms

Length: 1500-3000 words, MCA (Master of Computer Applications) PG level