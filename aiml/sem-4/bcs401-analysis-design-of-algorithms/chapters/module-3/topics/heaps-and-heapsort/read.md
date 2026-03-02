# Analysis & Design of Algorithms: Module 3 - Heaps and Heapsort

## Introduction

In the quest for efficient sorting algorithms, we often encounter a trade-off between simplicity and performance. While algorithms like Insertion Sort are simple, their O(n²) complexity is inefficient for large datasets. More complex algorithms like Merge Sort offer O(n log n) performance but require additional O(n) space. **Heapsort** elegantly bridges this gap. It is an efficient, in-place sorting algorithm that leverages a powerful data structure called a **heap** to achieve optimal O(n log n) time complexity in the worst case. This section explores the heap data structure and how it enables the Heapsort algorithm.

## Core Concepts

### 1. The Heap Data Structure

A heap is a special **complete binary tree** that satisfies the **heap property**. A complete binary tree is a tree where all levels are completely filled except possibly the last, which is filled from left to right.

There are two kinds of heaps:
*   **Max-Heap:** For every node `i` (other than the root), the value of the parent is greater than or equal to the value of its children.
    `A[Parent(i)] >= A[i]`
*   **Min-Heap:** For every node `i` (other than the root), the value of the parent is less than or equal to the value of its children.
    `A[Parent(i)] <= A[i]`

Heaps are efficiently represented using **arrays**. For a node at index `i`:
*   **Parent Index:** `floor(i/2)`
*   **Left Child Index:** `2i`
*   **Right Child Index:** `2i + 1`

This array representation eliminates the need for pointers, making it very space-efficient.

### 2. Maintaining the Heap Property: `MAX-HEAPIFY`

The core subroutine for managing a heap is `MAX-HEAPIFY`. Its job is to correct a single violation of the max-heap property at a given node `i`. It assumes the binary trees rooted at `LEFT(i)` and `RIGHT(i)` are already max-heaps.

**How it works:**
1.  It compares the element at `i` with its left and right children.
2.  If `i` is the largest, the heap property is already satisfied, and it stops.
3.  Otherwise, it **swaps** the element at `i` with the largest of its children.
4.  The procedure then recursively calls itself on the subtree where the swap occurred (the child index) to ensure the heap property holds there.

**Time Complexity:** O(log n), as it traverses at most the height of the tree.

### 3. Building a Heap: `BUILD-MAX-HEAP`

Given an arbitrary array, we can convert it into a valid max-heap using the `BUILD-MAX-HEAP` procedure. It works by calling `MAX-HEAPIFY` on each node in a **bottom-up** manner.

**Key Insight:** The elements in the subarray `A[floor(n/2)+1 ... n]` are all leaves of the tree. Since a leaf is a heap of size 1, `MAX-HEAPIFY` can be applied starting from the last non-leaf node (index `floor(n/2)`) down to the root (index `1`).

**Time Complexity:** Although it may seem like O(n log n), a tighter analysis shows it runs in **linear time, O(n)**.

### 4. The Heapsort Algorithm

Once we have a max-heap, the largest element is always at the root (`A[1]`). Heapsort exploits this property:

1.  **Build Phase:** Use `BUILD-MAX-HEAP` to build a max-heap from the unsorted input array `A[1..n]`.
2.  **Sort Phase:**
    *   The largest element is at `A[1]`. Swap it with the last element in the heap, `A[n]`. Now, the largest element is in its correct final position.
    *   **Discard** this last element from the heap by decreasing the heap size by one. This may violate the heap property at the root.
    *   Restore the max-heap property for the reduced heap (`A[1..n-1]`) by calling `MAX-HEAPIFY(A, 1)`.
    *   Repeat this process (swap, decrement heap size, heapify) for the remaining elements until the entire array is sorted.

**Example:**
Initial Array: `[5, 3, 17, 10, 84, 19, 6, 22, 9]`
After `BUILD-MAX-HEAP`: `[84, 22, 19, 10, 3, 17, 6, 5, 9]` (visualize this as a tree)
First iteration: Swap 84 and 9. Array becomes `[9, 22, 19, 10, 3, 17, 6, 5, 84]`. Call `MAX-HEAPIFY` on the root. The new max-heap (size 8) is `[22, 10, 19, 9, 3, 17, 6, 5 | 84]`. The process continues.

**Time Complexity:** The `BUILD-MAX-HEAP` step takes O(n). The `MAX-HEAPIFY` call, which takes O(log n), is executed n-1 times. Therefore, the total time complexity of Heapsort is **O(n log n)**.

## Key Points & Summary

| Property | Description |
| :--- | :--- |
| **Underlying Data Structure** | Binary Heap (almost complete binary tree represented as an array). |
| **Heap Property** | Max-Heap: Parent >= Children. Min-Heap: Parent <= Children. |
| **Core Operations** | `MAX-HEAPIFY` (O(log n)), `BUILD-MAX-HEAP` (O(n)). |
| **Algorithm Type** | Comparison-based, In-place, Not stable. |
| **Time Complexity** | **O(n log n)** for all cases (best, average, worst). |
| **Space Complexity** | **O(1)** auxiliary space (in-place). |
| **Advantages** | Optimal worst-case performance, in-place sorting, no reliance on random access (good for linked lists). |
| **Disadvantages** | Not a stable sort, has poor cache performance compared to Quicksort. |
| **Main Application** | Efficient sorting and implementing priority queues. |