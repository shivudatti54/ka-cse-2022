**Subject: Introduction to Data Structures**
**Module: 5**
**Topic: Sorting Algorithms (A Practical Guide)**

### Introduction

Welcome to Module 5 of our Introduction to Data Structures series. This module shifts focus from organizing data to efficiently ordering it. **Sorting** is a fundamental operation in computer science, crucial for optimizing other algorithms (like searching) and presenting data meaningfully. Here, we will explore three classic and essential sorting algorithms: **Bubble Sort**, **Selection Sort**, and **Insertion Sort**. Understanding these will build a strong foundation for grasping more complex algorithms later.

---

### Core Concepts

#### 1. Bubble Sort

Bubble Sort is a simple comparison-based algorithm. The core idea is to repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. This process is repeated until the list is sorted. With each complete pass, the next largest element "bubbles up" to its correct position at the end of the list.

**How it works:**
1.  Start at the beginning of the array.
2.  Compare the current element with the next element.
3.  If the current element is greater than the next, swap them.
4.  Move to the next element and repeat step 2 until the end of the array is reached. This is one pass.
5.  Repeat the passes until no swaps are needed in a complete pass, indicating the list is sorted.

**Example:**
Sorting `[5, 3, 8, 4, 2]`
*   **Pass 1:** `[3, 5, 4, 2, 8]` (5 and 3 swapped, 5 and 4 swapped, 5 and 2 swapped, 8 is in place)
*   **Pass 2:** `[3, 4, 2, 5, 8]` (4 and 2 swapped)
*   **Pass 3:** `[3, 2, 4, 5, 8]` (3 and 2 swapped)
*   **Pass 4:** `[2, 3, 4, 5, 8]` (No swaps, list sorted)

**Time Complexity:** O(n²) in worst and average cases.

#### 2. Selection Sort

Selection Sort works by dividing the input list into two parts: a sorted sublist of items built from left to right and an unsorted sublist. The algorithm repeatedly finds the smallest (or largest) element from the unsorted sublist and swaps it with the leftmost unsorted element, moving the boundary of the sorted sublist one element to the right.

**How it works:**
1.  Find the smallest element in the unsorted part of the array.
2.  Swap it with the element at the very beginning of the unsorted part.
3.  Now, the first element is part of the sorted sublist.
4.  Repeat the process for the remaining unsorted sublist until the entire array is sorted.

**Example:**
Sorting `[64, 25, 12, 22, 11]`
*   **Pass 1:** Find min=11, swap with 64 → `[11, 25, 12, 22, 64]`
*   **Pass 2:** Find min=12 in unsorted part, swap with 25 → `[11, 12, 25, 22, 64]`
*   **Pass 3:** Find min=22, swap with 25 → `[11, 12, 22, 25, 64]`
*   **Pass 4:** Find min=25, already in place → `[11, 12, 22, 25, 64]` (Sorted)

**Time Complexity:** O(n²) in all cases.

#### 3. Insertion Sort

Insertion Sort builds the final sorted array one element at a time, similar to how you might sort playing cards in your hand. It takes each element from the unsorted part and inserts it into its correct position within the sorted part.

**How it works:**
1.  Start with the second element (index 1), assume the first element is already sorted.
2.  Compare this "key" element with the elements in the sorted sublist to its left.
3.  Shift all larger elements in the sorted sublist one position to the right to make space.
4.  Insert the "key" into its correct position.
5.  Repeat for all subsequent elements in the array.

**Example:**
Sorting `[12, 11, 13, 5, 6]`
*   **Pass 1 (key=11):** Compare 11 & 12, shift 12, insert 11 → `[11, 12, 13, 5, 6]`
*   **Pass 2 (key=13):** Compare 13 & 12, it's larger, so no shift → `[11, 12, 13, 5, 6]`
*   **Pass 3 (key=5):** Compare with 13,12,11; shift all; insert 5 → `[5, 11, 12, 13, 6]`
*   **Pass 4 (key=6):** Compare with 13,12,11,5; shift 13,12,11; insert 6 → `[5, 6, 11, 12, 13]`

**Time Complexity:** O(n²) in worst and average cases, but O(n) in the best case (if the list is already nearly sorted).

---

### Key Points & Summary

| Algorithm     | Time Complexity (Worst/Average) | Best Case | Key Idea                                                                 | Use-Case                                         |
| :------------ | :------------------------------- | :-------- | :----------------------------------------------------------------------- | :----------------------------------------------- |
| **Bubble Sort**  | O(n²)                            | O(n)      | Repeatedly swap adjacent elements that are in the wrong order.           | Educational purposes; not efficient for real data. |
| **Selection Sort** | O(n²)                            | O(n²)     | Repeatedly find the minimum element and put it at the beginning.         | When memory write is a costly operation.           |
| **Insertion Sort** | O(n²)                            | O(n)      | Build the sorted array by inserting one element at a time in its place. | Small datasets, or when the list is nearly sorted. |

**Summary:**
*   **Bubble Sort** is intuitive but inefficient for large datasets. Its primary value is in teaching fundamental sorting concepts.
*   **Selection Sort** is notable for making a minimal number of swaps (only O(n)), which can be useful if writes to memory are expensive.
*   **Insertion Sort** is simple, efficient for small or partially sorted data, and is often used as a building block for more advanced algorithms like Shell Sort.
*   All three are **comparison-based** and **in-place** algorithms (they don't require significant additional memory).
*   While their O(n²) complexity makes them unsuitable for large-scale applications, mastering them is essential for any computer engineer, as they form the conceptual groundwork for understanding more efficient algorithms like Merge Sort and Quick Sort.