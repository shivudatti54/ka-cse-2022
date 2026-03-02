# Analysis & Design of Algorithms: Selection Sort & Bubble Sort

## Introduction

Welcome to Module 1 of Analysis & Design of Algorithms. This module introduces fundamental algorithm design techniques, starting with two simple yet important sorting algorithms: **Selection Sort** and **Bubble Sort**. While not the most efficient for large datasets, they provide an excellent foundation for understanding key algorithmic concepts like iteration, comparison, swapping, and, most importantly, the analysis of **time complexity**.

---

## Selection Sort

### Core Concept
Selection Sort is an **in-place comparison-based** algorithm. The core idea is straightforward: **repeatedly find the minimum (or maximum) element from the unsorted part of the array and place it at the beginning.** The array is virtually divided into a sorted and an unsorted subarray.

### Algorithm Steps
1. **Initialization:** Start with the entire array as unsorted.
2. **Find Minimum:** Traverse the unsorted subarray to find the smallest element.
3. **Swap:** Swap the smallest element found with the first element of the unsorted subarray.
4. **Boundary Move:** Move the boundary between the sorted and unsorted subarrays one element to the right.
5. **Repeat:** Repeat steps 2-4 until the entire array is sorted.

### Example
Sort the array: `[64, 25, 12, 22, 11]`

*   **Pass 1:** Min element in `[64,25,12,22,11]` is `11`. Swap with first element (`64`). Array becomes `[11, 25, 12, 22, 64]`. Sorted subarray = `[11]`.
*   **Pass 2:** Min element in `[25,12,22,64]` is `12`. Swap with `25`. Array becomes `[11,12,25,22,64]`. Sorted = `[11,12]`.
*   **Pass 3:** Min element in `[25,22,64]` is `22`. Swap with `25`. Array becomes `[11,12,22,25,64]`. Sorted = `[11,12,22]`.
*   **Pass 4:** Min element in `[25,64]` is `25`. No swap needed. Array is now sorted: `[11,12,22,25,64]`.

### Complexity Analysis
*   **Time Complexity:** **O(n²)** in all cases (best, average, worst). This is because it always performs `n(n-1)/2` comparisons, regardless of the initial order of the array.
*   **Space Complexity:** **O(1)** as it only requires a constant amount of additional memory space (for variables like `min_index`, `temp`).

---

## Bubble Sort

### Core Concept
Bubble Sort is another simple **in-place comparison-based** algorithm. The idea is to **repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order.** This pass is repeated until the list is sorted. The larger values "bubble up" to the end of the array with each pass, hence the name.

### Algorithm Steps
1. **Start:** Begin at the start of the array.
2. **Compare & Swap:** Compare the current element with the next element. If they are out of order (`arr[j] > arr[j+1]`), swap them.
3. **Traverse:** Move to the next element and repeat step 2 until the end of the unsorted part is reached.
4. **One Element Sorted:** After each full pass, the largest unsorted element will have "bubbled" to its correct position at the end.
5. **Repeat:** Repeat passes, each time reducing the size of the unsorted subarray by one, until no swaps are needed in a pass (indicating the array is sorted).

### Example (Optimized with early termination)
Sort the array: `[5, 1, 4, 2, 8]`

*   **Pass 1:**
    *   `[5, 1, 4, 2, 8]` → `(5>1)`? Yes. Swap → `[1, 5, 4, 2, 8]`
    *   `[1, 5, 4, 2, 8]` → `(5>4)`? Yes. Swap → `[1, 4, 5, 2, 8]`
    *   `[1, 4, 5, 2, 8]` → `(5>2)`? Yes. Swap → `[1, 4, 2, 5, 8]`
    *   `[1, 4, 2, 5, 8]` → `(5>8)`? No. No swap. Array is now `[1, 4, 2, 5, 8]`. `8` is in its correct place.
*   **Pass 2:**
    *   `[1, 4, 2, 5, 8]` → `(1<4)`? No swap.
    *   `[1, 4, 2, 5, 8]` → `(4>2)`? Yes. Swap → `[1, 2, 4, 5, 8]`
    *   `[1, 2, 4, 5, 8]` → `(4<5)`? No swap. `5` and `8` are already sorted. Array is `[1, 2, 4, 5, 8]`.
*   **Pass 3:** No swaps occur. The algorithm terminates early.

### Complexity Analysis
*   **Time Complexity:**
    *   **Worst & Average Case:** **O(n²)** due to nested loops.
    *   **Best Case (Optimized version):** **O(n)**. This occurs when the input array is already sorted. The algorithm makes one pass, finds no swaps, and terminates.
*   **Space Complexity:** **O(1)** as it is an in-place sorting algorithm.

---

## Key Points & Summary

| Aspect | Selection Sort | Bubble Sort |
| :--- | :--- | :--- |
| **Idea** | Select the min/max element and put it in place. | Repeatedly swap adjacent elements if in wrong order. |
| **Time Complexity** | O(n²) in all cases. | O(n²) average/worst, O(n) best (if optimized). |
| **Space Complexity** | O(1) - In-place. | O(1) - In-place. |
| **Stability** | **Not Stable** (swapping with first element can change order of duplicates). | **Stable** (only swaps adjacent elements, order is preserved). |
| **Use Case** | Useful when memory write is a costly operation, as it makes only O(n) swaps. | Rarely used in practice due to poor average performance. Good for educational purposes. |
| **Key Advantage** | Simple and has the minimum possible number of swaps. | Simple to understand and implement; can detect a sorted list quickly. |

**Conclusion:** Both Selection Sort and Bubble Sort are fundamental algorithms that help build intuition for how sorting works and how we analyze time/space complexity. However, their quadratic time complexity makes them inefficient for sorting large datasets. They serve as a stepping stone to more efficient algorithms like Merge Sort and Quick Sort, which we will study in subsequent modules.