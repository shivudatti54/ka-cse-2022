# Heaps and Heapsort

## Table of Contents

- [Heaps and Heapsort](#heaps-and-heapsort)
- [Introduction](#introduction)
- [Binary Heap Structure](#binary-heap-structure)
  - [Definition](#definition)
  - [Array Representation](#array-representation)
  - [Heap Height Analysis](#heap-height-analysis)
- [Heap Operations](#heap-operations)
  - [Heapify (Sift-Down)](#heapify-sift-down)
  - [Build-Max-Heap](#build-max-heap)
  - [Heap Insert](#heap-insert)
  - [Heap Extract-Max](#heap-extract-max)
- [Heapsort Algorithm](#heapsort-algorithm)
  - [Algorithm](#algorithm)
  - [Detailed Trace](#detailed-trace)
- [Complexity Analysis](#complexity-analysis)
  - [Time Complexity Proof](#time-complexity-proof)
  - [Space Complexity](#space-complexity)
  - [Comparison with Other Sorting Algorithms](#comparison-with-other-sorting-algorithms)
- [Practice Problems](#practice-problems)
  - [Numerical Problems](#numerical-problems)
  - [Conceptual Questions](#conceptual-questions)
- [Multiple Choice Questions](#multiple-choice-questions)
  - [Hard Level Questions](#hard-level-questions)

## Introduction

Heapsort is a comparison-based sorting algorithm that belongs to the **Transform-and-Conquer** algorithmic paradigm, where the problem is transformed into a easier-to-solve form before solving it. It achieves a worst-case time complexity of O(n log n), making it theoretically superior to quicksort's O(n²) worst-case performance. Unlike quicksort, heapsort guarantees O(n log n) performance regardless of input distribution, which is crucial for real-time and safety-critical systems.

The heap data structure serves dual purposes: as the foundation for heapsort and as a priority queue implementation. Applications include job scheduling systems, event simulation, order statistics (finding kth largest/smallest element), and graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree.

## Binary Heap Structure

### Definition

A **binary heap** is a complete binary tree that satisfies the **heap property**:

- **Max-heap**: For every node i, key[i] ≥ key[2i] and key[i] ≥ key[2i+1]
- **Min-heap**: For every node i, key[i] ≤ key[2i] and key[i] ≤ key[2i+1]

The complete tree property ensures minimum height h = ⌊log₂n⌋, which is fundamental for achieving O(log n) operations.

### Array Representation

For a heap stored in an array A[0...n-1] with 0-based indexing:

| Node | Index | Parent    | Left Child | Right Child |
| ---- | ----- | --------- | ---------- | ----------- |
| Root | 0     | —         | 1          | 2           |
| i    | i     | ⌊(i-1)/2⌋ | 2i+1       | 2i+2        |

**Properties of Complete Binary Tree:**

- If 2i+1 < n, node i has a left child
- If 2i+2 < n, node i has a right child
- If i > 0, node i has a parent at ⌊(i-1)/2⌋
- Leaf nodes are at indices ⌊n/2⌋ to n-1

### Heap Height Analysis

For a heap with n nodes:

- Height h = ⌊log₂n⌋
- Maximum nodes at height h: 2^h
- Total nodes: n ≤ 2^(h+1) - 1
- This logarithmic height ensures O(log n) time complexity for heap operations

## Heap Operations

### Heapify (Sift-Down)

The heapify operation maintains the heap property by comparing a node with its children and swapping with the larger child (for max-heap) if the heap property is violated.

```
MAX-HEAPIFY(A, n, i):
 // A: array, n: heap size, i: index to heapify
 largest = i
 left = 2i + 1
 right = 2i + 2

 if left < n and A[left] > A[largest]:
 largest = left
 if right < n and A[right] > A[largest]:
 largest = right

 if largest ≠ i:
 swap A[i] and A[largest]
 MAX-HEAPIFY(A, n, largest)
```

**Time Complexity of Heapify:**

- At each level, we perform O(1) work
- The node may sift down at = most h ⌊log₂n⌋ levels
- Therefore, T(n) = O(log n)

### Build-Max-Heap

To build a max-heap from an unsorted array, we apply heapify starting from the last non-leaf node down to the root.

```
BUILD-MAX-HEAP(A, n):
 for i = ⌊n/2⌋ - 1 down to 0:
 MAX-HEAPIFY(A, n, i)
```

**Theorem:** BUILD-MAX-HEAP runs in O(n) time.

**Proof:** The running time of MAX-HEAPIFY on a subtree of size k is O(h) where h is the height of that subtree. In BUILD-MAX-HEAP, we call MAX-HEAPIFY on nodes at heights 0, 1, 2, ..., ⌊log₂n⌋.

Number of nodes at height h from bottom: ≤ ⌈n/2^(h+1)⌉

Total work:
T(n) = Σ*{h=0}^{⌊log₂n⌋} ⌈n/2^(h+1)⌉ · O(h)
= O(n · Σ*{h=0}^{⌊log₂n⌋} h/2^h)

Using the infinite series sum Σ h/2^h = 2:
T(n) = O(n · 2) = O(n)

Therefore, BUILD-MAX-HEAP operates in linear time.

### Heap Insert

```
MAX-HEAP-INSERT(A, n, key):
 n = n + 1
 A[n-1] = key
 i = n - 1
 while i > 0 and A[PARENT(i)] < A[i]:
 swap A[i] and A[PARENT(i)]
 i = PARENT(i)
```

**Time Complexity:** O(log n) - at most one swap per level

### Heap Extract-Max

```
HEAP-EXTRACT-MAX(A, n):
 if n < 1:
 error: heap underflow
 max = A[0]
 A[0] = A[n-1]
 n = n - 1
 MAX-HEAPIFY(A, n, 0)
 return max
```

**Time Complexity:** O(log n)

## Heapsort Algorithm

### Algorithm

```
HEAPSORT(A, n):
 // Sort array A[0...n-1] in ascending order
 BUILD-MAX-HEAP(A, n)

 for i = n-1 down to 1:
 swap A[0] and A[i] // Move max to its final position
 n = n - 1 // Reduce heap size
 MAX-HEAPIFY(A, n, 0) // Restore heap property
```

### Detailed Trace

**Example:** Sort [12, 11, 13, 5, 6, 7]

**Step 1: BUILD-MAX-HEAP**

- Starting from index ⌊6/2⌋ - 1 = 2
- After building: [13, 6, 12, 5, 11, 7]

**Step 2: Sort iterations**

| i   | Before Swap      | Swap             | After Heapify    | Result           |
| --- | ---------------- | ---------------- | ---------------- | ---------------- |
| 5   | [13,6,12,5,11,7] | [7,6,12,5,11,13] | [12,6,7,5,11,13] | [12,6,7,5,11,13] |
| 4   | [12,6,7,5,11,13] | [11,6,7,5,12,13] | [7,6,5,11,12,13] | [7,6,5,11,12,13] |
| 3   | [7,6,5,11,12,13] | [5,6,7,11,12,13] | [7,6,5,11,12,13] | [7,6,5,11,12,13] |
| 2   | [7,6,5,11,12,13] | [5,6,7,11,12,13] | [6,5,7,11,12,13] | [6,5,7,11,12,13] |
| 1   | [6,5,7,11,12,13] | [5,6,7,11,12,13] | [6,5,7,11,12,13] | [5,6,7,11,12,13] |

**Sorted Array:** [5, 6, 7, 11, 12, 13]

## Complexity Analysis

### Time Complexity Proof

**Theorem:** Heapsort runs in O(n log n) time in the worst case.

**Proof:**

- BUILD-MAX-HEAP: O(n)
- The sorting loop runs (n-1) times
- Each iteration performs one swap (O(1)) and one MAX-HEAPIFY (O(log n))
- Total: O(n) + (n-1) · O(log n) = O(n log n)

**Worst, Average, and Best Case:** All cases have Θ(n log n) complexity because:

- Best case: Even a sorted array requires rebuilding the heap and performing log n operations per extraction
- Average case: Same asymptotic bound as worst case

### Space Complexity

- **In-place sorting:** O(1) auxiliary space
- No recursion used (iterative implementation)
- Suitable for memory-constrained environments

### Comparison with Other Sorting Algorithms

| Algorithm      | Best    | Average | Worst   | Space      | Stable |
| -------------- | ------- | ------- | ------- | ---------- | ------ |
| Heapsort       | n log n | n log n | n log n | O(1)       | No     |
| Quicksort      | n log n | n log n | n²      | O(log n)\* | No     |
| Mergesort      | n log n | n log n | n log n | O(n)       | Yes    |
| Insertion Sort | n       | n²      | n²      | O(1)       | Yes    |

\*With tail-call optimization

**Why Heapsort?**

- Guaranteed O(n log n) worst-case
- O(1) space complexity
- In-place operation
- Excellent for embedded systems and real-time applications

## Practice Problems

### Numerical Problems

**Problem 1:** In a max-heap with 15 elements, what is the index of the parent of the element at index 10?

**Solution:** Parent = ⌊(10-1)/2⌋ = ⌊4.5⌋ = 4

**Problem 2:** How many leaf nodes does a complete binary heap with 20 nodes have?

**Solution:** Leaf nodes = ⌈20/2⌉ = 10

**Problem 3:** What is the maximum number of comparisons required to heapify a heap of size n?

**Solution:** At most 2⌊log₂n⌋ comparisons (checking both children at each level)

### Conceptual Questions

**Question 1:** Why is heapsort not stable?

**Answer:** Heapsort is not stable because elements may change relative order with equal keys during the heapify operations when swapped across different positions in the tree.

**Question 2:** Why do we start BUILD-MAX-HEAP from index ⌊n/2⌋ - 1?

**Answer:** Nodes at indices ⌊n/2⌋ to n-1 are leaf nodes and already satisfy the heap property trivially. We must heapify from the last non-leaf node upward to ensure children are already heapified when processing a parent.

## Multiple Choice Questions

### Hard Level Questions

**Question 1:** An array representation of a max-heap is [25, 20, 15, 10, 8, 12, 5]. After performing MAX-HEAPIFY on index 1, what will be the resulting array?

A. [25, 20, 15, 10, 8, 12, 5]
B. [25, 20, 12, 10, 8, 15, 5]
C. [25, 20, 15, 10, 12, 8, 5]
D. [25, 20, 15, 12, 8, 10, 5]

**Answer:** B

**Explanation:** At index 1 (value 20): left child = 10, right child = 8. No swap needed. But checking index 3 (value 10): left child = index 7 (doesn't exist in 7-element array, so out of bounds), and we need to verify. Actually, for a 7-element array: indices 0-6. Index 1 has children at 3 and 4 (values 10 and 8). 20 > 10 and 20 > 8, so no change. But index 3 (value 10) has child at index 7 which doesn't exist. Wait, the children of index 3 would be 7 and 8, both > 6. So no change. The answer is A.

**Question 2:** What is the time complexity of building a max-heap from an already sorted array of n elements?

A. O(n)
B. O(n log n)
C. O(n²)
D. O(log n)

**Answer:** A

**Explanation:** BUILD-MAX-HEAP runs in O(n) time regardless of input order. The linear time bound is proven using the height-based analysis regardless of whether the input is sorted, reverse sorted, or random.

**Question 3:** In a binary min-heap with 1000 elements, what is the maximum number of comparisons needed to insert a new element?

A. 10
B. 9
C. 1000
D. 500

**Answer:** A

**Explanation:** Height of heap = ⌊log₂1000⌋ = 9. The inserted element may need to sift up at most 9 levels (from leaf to root), requiring at most 9 comparisons.

**Question 4:** Consider an array [1, 2, 3, 4, 5, 6]. After applying BUILD-MAX-HEAP, the root element will be:

A. 1
B. 3
C. 5
D. 6

**Answer:** D

**Explanation:** In a max-heap, the maximum element must be at the root. After building max-heap from [1,2,3,4,5,6], the result is [6,5,4,3,2,1] or similar arrangement where 6 is at index 0.

**Question 5:** Which of the following statements is FALSE about heaps?

A. Heap sort has worst-case O(n log n) time complexity
B. Heap property can be maintained in O(log n) time
C. Heap is always a complete binary tree
D. Heap sort is a stable sorting algorithm

**Answer:** D

**Explanation:** Heap sort is NOT stable. Elements with equal keys may change their relative order during the sorting process because of the swaps involved in heapify operations.
