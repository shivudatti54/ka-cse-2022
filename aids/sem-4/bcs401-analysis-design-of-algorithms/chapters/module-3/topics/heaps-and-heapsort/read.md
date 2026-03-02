# Heaps and Heapsort

## Introduction

In the study of sorting algorithms, we often seek methods that are both efficient and optimal in their use of resources. Heapsort is one such algorithm that achieves **O(n log n)** time complexity for worst-case scenarios, making it a reliable choice. Its power derives from its use of a fundamental data structure known as a **heap**. This module will explore the heap data structure, its properties, and how it is used to implement the Heapsort algorithm.

## Core Concepts

### 1. The Heap Data Structure

A **heap** is a specialized **complete binary tree** that satisfies the **heap property**. A complete binary tree is a tree where all levels are completely filled except possibly the last level, which is filled from left to right.

There are two types of heaps:
*   **Max-Heap:** For every node `i` (other than the root), the value of the node is at most the value of its parent. That is, `A[Parent(i)] >= A[i]`. The largest element is at the root.
*   **Min-Heap:** For every node `i` (other than the root), the value of the node is at least the value of its parent. That is, `A[Parent(i)] <= A[i]`. The smallest element is at the root.

Heaps are efficiently represented using **arrays**. For a node at index `i`:
*   **Parent(i):** `floor((i-1)/2)`
*   **Left Child(i):** `2*i + 1`
*   **Right Child(i):** `2*i + 2`

### 2. Heap Operations

The key to maintaining the heap property is the `MAX-HEAPIFY` (or `MIN-HEAPIFY`) operation.

*   **`MAX-HEAPIFY(A, i)`:** This function assumes that the binary trees rooted at `LEFT(i)` and `RIGHT(i)` are max-heaps, but `A[i]` might be smaller than its children. It corrects this violation by letting the value "float down" in the tree, ensuring the max-heap property is restored at index `i` and its subtrees.
    *   **Time Complexity:** O(log n)

*   **`BUILD-MAX-HEAP(A)`:** This procedure builds a max-heap from an unordered array. It starts from the last non-leaf node (index `floor(n/2)-1`) and calls `MAX-HEAPIFY` on each node all the way up to the root.
    *   **Time Complexity:** O(n) – A crucial insight often proven using summation analysis.

### 3. The Heapsort Algorithm

Heapsort uses the max-heap to sort an array in-place. The algorithm proceeds in two main phases:

**Phase 1: Build a Max-Heap**
Convert the input array `A[0..n-1]` into a max-heap using `BUILD-MAX-HEAP`. The maximum element is now at the root, `A[0]`.

**Phase 2: Sort by Extracting Max Elements Repeatedly**
1.  **Swap** the root element (`A[0]`, the current maximum) with the last element in the heap (`A[i]`).
2.  **Decrease** the heap size by one, effectively discarding the now-sorted maximum element from the heap.
3.  The new root likely violates the max-heap property. Call `MAX-HEAPIFY` on the new root (`A[0]`) to restore the max-heap property on the reduced heap `A[0..i-1]`.
4.  **Repeat** steps 1-3 until the heap size is reduced to 1.

**Visual Example:**
Let's sort `[12, 11, 13, 5, 6, 7]`.

1.  **Build Max-Heap:** After building, the array becomes `[13, 11, 12, 5, 6, 7]`.
    Root (13) is the max.
2.  **First Iteration:**
    *   Swap root (13) with last element (7): `[7, 11, 12, 5, 6, 13]`. 13 is now sorted.
    *   Call `MAX-HEAPIFY` on root (7): heap becomes `[12, 11, 7, 5, 6]`.
3.  **Second Iteration:**
    *   Swap root (12) with last unsorted element (6): `[6, 11, 7, 5, 12, 13]`.
    *   `MAX-HEAPIFY` on root (6): heap becomes `[11, 6, 7, 5]`.
4.  This process continues until the entire array is sorted: `[5, 6, 7, 11, 12, 13]`.

### 4. Complexity Analysis

*   **`MAX-HEAPIFY`:** O(log n)
*   **`BUILD-MAX-HEAP`:** O(n)
*   **Heapsort:** It calls `BUILD-MAX-HEAP` once (O(n)) and then calls `MAX-HEAPIFY` `n-1` times (each O(log n)).
    *   **Total Time Complexity:** O(n) + O((n-1) * log n) = **O(n log n)** for all cases (best, average, worst).
*   **Space Complexity:** O(1) – It is an in-place sorting algorithm.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Data Structure** | A **Heap** is a complete binary tree satisfying the max-heap or min-heap property. |
| **Representation** | Efficiently implemented using a simple **array**. |
| **Key Operation** | **`MAX-HEAPIFY`** is crucial for maintaining the heap property. |
| **Algorithm** | **Heapsort** first builds a max-heap from the input and then repeatedly extracts the maximum element. |
| **Time Complexity** | **O(n log n)** for all cases. This is optimal for comparison-based sorting. |
| **Space Complexity** | **O(1)**. It is an **in-place** algorithm. |
| **Advantages** | Guaranteed O(n log n) performance and minimal space usage. |
| **Disadvantages** | Typically slower in practice than well-implemented Quicksort and MergeSort due to more comparisons and poorer cache performance. |
| **Primary Use** | Excellent for scenarios where worst-case performance is critical. Also forms the basis for **Priority Queues**. |