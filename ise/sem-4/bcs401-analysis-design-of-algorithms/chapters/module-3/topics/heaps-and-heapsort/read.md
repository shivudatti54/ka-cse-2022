# Analysis & Design of Algorithms: Heaps and Heapsort

## Introduction

Welcome to Module 3! This section introduces one of the most elegant and efficient data structures used in algorithm design: the **Heap**. A heap is a special tree-based data structure that satisfies the _heap property_. It serves as the foundation for an efficient, in-place sorting algorithm called **Heapsort**, which is a comparison-based algorithm with an optimal worst-case time complexity of O(n log n). Understanding heaps is also crucial for implementing priority queues, which are essential for algorithms like Dijkstra's and Prim's.

## Core Concepts

### 1. What is a Heap?

A heap is a nearly complete binary tree that satisfies the **heap property**. There are two kinds of heaps:

- **Max-Heap:** For every node `i` (other than the root), the value of the parent is **greater than or equal to** the value of its children. `A[Parent(i)] >= A[i]`
- **Min-Heap:** For every node `i` (other than the root), the value of the parent is **less than or equal to** the value of its children. `A[Parent(i)] <= A[i]`

Heaps are typically represented as arrays. For a node at index `i` in a 1-indexed array (or `i=0` for 0-indexed):

- **Parent Index:** `floor(i/2)`
- **Left Child Index:** `2i`
- **Right Child Index:** `2i + 1`

This array representation allows us to navigate the tree structure without explicit pointers.

### 2. The `MAX-HEAPIFY` Procedure

This is a fundamental operation to maintain the max-heap property. It assumes that the binary trees rooted at the left and right children of node `i` are max-heaps, but `A[i]` might be smaller than one of its children. `MAX-HEAPIFY` lets the value "float down" in the tree until the heap property is restored.

**Algorithm Steps (`MAX-HEAPIFY(A, i)`):**

1.  `l = LEFT(i)`
2.  `r = RIGHT(i)`
3.  Find the largest value among `A[i]`, `A[l]`, and `A[r]`.
4.  If the largest is not `i`, swap `A[i]` with `A[largest]`.
5.  Recursively call `MAX-HEAPIFY` on the affected subtree (index `largest`).

**Time Complexity:** O(log n), as it traverses at most the height of the tree.

### 3. The `BUILD-MAX-HEAP` Procedure

This procedure builds a max-heap from an unsorted array. It works by calling `MAX-HEAPIFY` on all non-leaf nodes in a **bottom-up** manner, starting from the last non-leaf node down to the root.

**Algorithm Steps (`BUILD-MAX-HEAP(A)`):**

1.  `n = A.length`
2.  The last non-leaf node is at index `floor(n/2)`.
3.  **For** `i = floor(n/2)` **downto** `1`:
    - `MAX-HEAPIFY(A, i)`

**Time Complexity:** O(n). Although `MAX-HEAPIFY` is O(log n) and is called O(n) times, a tighter analysis shows the overall cost is linear.

### 4. The Heapsort Algorithm

Heapsort leverages the max-heap to sort an array in-place. The algorithm consists of two main phases:

**Phase 1: Build a Max-Heap**

- Use `BUILD-MAX-HEAP(A)` to create a max-heap from the unsorted input array. The maximum element is now at the root (`A[1]`).

**Phase 2: Extract Elements**

- The root element (the largest) is swapped with the last element in the heap.
- The heap size is reduced by one (effectively removing the largest element from the heap and placing it in its correct sorted position).
- The `MAX-HEAPIFY` is called on the new root to restore the max-heap property in the reduced heap.
- This process is repeated until the entire array is sorted.

**Algorithm Steps (`HEAPSORT(A)`):**

1.  `BUILD-MAX-HEAP(A)` // Phase 1
2.  `n = A.length`
3.  **For** `i = n` **downto** `2`:
    - Swap `A[1]` with `A[i]` // Move current max to its final position
    - `heap_size = heap_size - 1` // Reduce heap size
    - `MAX-HEAPIFY(A, 1)` // Restore max-heap property on the new root

**Example:**
Let's sort `[4, 1, 3, 2, 16, 9]` using Heapsort.

- **Build Max-Heap:** After `BUILD-MAX-HEAP`, the array becomes `[16, 4, 9, 2, 1, 3]`.
- **Iteration 1:** Swap `16` (root) and `3` (last). Array: `[3, 4, 9, 2, 1, 16]`. Call `MAX-HEAPIFY` on `3`. New heap: `[9, 4, 3, 2, 1 | 16]`.
- **Iteration 2:** Swap `9` and `1`. Array: `[1, 4, 3, 2, 9, 16]`. Call `MAX-HEAPIFY` on `1`. New heap: `[4, 2, 3, 1 | 9, 16]`.
- This continues until the sorted array `[1, 2, 3, 4, 9, 16]` is achieved.

**Time Complexity:** O(n log n) for all cases (best, average, worst). This is optimal for comparison-based sorting algorithms.

## Key Points & Summary

| Aspect               | Description                                                                                                                   |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Data Structure**   | A heap is a complete binary tree satisfying the heap property (max-heap or min-heap).                                         |
| **Representation**   | Efficiently implemented as an array.                                                                                          |
| **Core Operation**   | `MAX-HEAPIFY` maintains the heap property in O(log n) time.                                                                   |
| **Building a Heap**  | `BUILD-MAX-HEAP` constructs a heap from an unsorted array in O(n) time.                                                       |
| **Heapsort**         | An efficient, **in-place** sorting algorithm with a **O(n log n)** worst-case time complexity.                                |
| **Advantages**       | In-place, optimal worst-case performance, no reliance on input data being partially sorted.                                   |
| **Disadvantages**    | Typically slower in practice on average than well-implemented QuickSort due to more comparisons and poorer cache performance. |
| **Main Application** | **Priority Queues** (for efficient extraction of min/max), but also serves as a reliable sorting algorithm.                   |

Heapsort is a brilliant demonstration of how a clever data structure can be used to design a powerful and theoretically optimal algorithm.
