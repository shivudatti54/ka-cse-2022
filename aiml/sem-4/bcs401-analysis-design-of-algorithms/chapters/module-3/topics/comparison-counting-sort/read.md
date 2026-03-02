# Comparison Counting Sort

## Introduction
Comparison Counting Sort is a fundamental non-comparison based sorting algorithm, particularly useful for sorting integers within a specific, limited range. Unlike comparison sorts like QuickSort or MergeSort, which rely on comparing elements to each other, Counting Sort uses a counting technique to determine the position of each element in the sorted output. This unique approach allows it to achieve a linear time complexity, a significant advantage in the right scenarios.

## Core Concepts

### 1. The Basic Idea
The algorithm works by counting the number of occurrences of each distinct element in the input array. It then uses these counts to compute the starting positions (or indices) for each value in the sorted output array. Finally, it places each element from the input array into its correct position in the output array.

### 2. Algorithm Steps
Given an array `A[0..n-1]` of integers with a known range `[0, k]`:

1.  **Count Array Initialization:** Create a count array `C[0..k]` of size `k+1`. Initialize all its values to zero.
2.  **Frequency Count:** Traverse the input array `A`. For each element `A[i]`, increment the count `C[A[i]]` by 1. Now, `C[x]` contains the number of times `x` appears in `A`.
3.  **Cumulative Count Transformation:** Modify the count array `C` such that each element `C[i]` now contains the number of elements *less than or equal to* `i`. This is done by performing a cumulative sum: `C[i] = C[i] + C[i-1]` for `i` from 1 to `k`.
4.  **Build Output Array:** Create an output array `B[0..n-1]`. Traverse the input array `A` from the end to the beginning (this preserves stability). For each element `A[i]`:
    *   Use its value to index into the count array: `pos = C[A[i]] - 1`.
    *   Place `A[i]` into `B[pos]`.
    *   Decrement `C[A[i]]` by 1.

### 3. Example
Let's sort the array `A = [4, 2, 2, 8, 3, 3, 1]` with range `k=8`.

*   **Step 1 & 2: Frequency Count**
    Initialize `C[0..8]` to zeros. After counting frequencies:
    `C = [0, 1, 2, 2, 1, 0, 0, 0, 1]`
    (Index:0, Value:0; Index:1, Value:1; Index:2, Value:2; ... Index:8, Value:1)

*   **Step 3: Cumulative Count**
    Compute cumulative sums: `C[i] += C[i-1]`.
    `C = [0, 1, 3, 5, 6, 6, 6, 6, 7]`
    This means there are 0 elements <=0, 1 element <=1, 3 elements <=2, etc.

*   **Step 4: Build Output (Process A from right to left)**
    *   `A[6] = 1` -> `pos = C[1]-1 = 1-1 = 0` -> `B[0]=1`. Decrement `C[1]` to 0.
    *   `A[5] = 3` -> `pos = C[3]-1 = 5-1 = 4` -> `B[4]=3`. Decrement `C[3]` to 4.
    *   `A[4] = 3` -> `pos = C[3]-1 = 4-1 = 3` -> `B[3]=3`. Decrement `C[3]` to 3.
    *   `A[3] = 8` -> `pos = C[8]-1 = 7-1 = 6` -> `B[6]=8`. Decrement `C[8]` to 6.
    *   `A[2] = 2` -> `pos = C[2]-1 = 3-1 = 2` -> `B[2]=2`. Decrement `C[2]` to 2.
    *   `A[1] = 2` -> `pos = C[2]-1 = 2-1 = 1` -> `B[1]=2`. Decrement `C[2]` to 1.
    *   `A[0] = 4` -> `pos = C[4]-1 = 6-1 = 5` -> `B[5]=4`. Decrement `C[4]` to 5.

    The sorted output array is `B = [1, 2, 2, 3, 3, 4, 8]`.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Time Complexity** | **O(n + k)**, where `n` is the number of elements and `k` is the range of input. This is linear, making it very efficient if `k` is not significantly larger than `n` (e.g., `k = O(n)`). |
| **Space Complexity** | **O(n + k)**. It requires additional space for the output array (`n`) and the count array (`k+1`). |
| **Stability** | **Yes.** The algorithm is stable because elements with the same value are placed in the output array in the same order they appeared in the input (achieved by processing the input from the end). Stability is crucial for satellite data. |
| **In-place?** | **No.** Counting Sort is not an in-place algorithm as it requires significant additional memory. |
| **Best Use Case** | Ideal for sorting integers or objects with small integer keys when the range of potential values (`k`) is known and not too large. |
| **Limitations** | It is not a comparison sort and cannot be applied easily to non-integer data (e.g., strings or floats) without significant modification. Performance degrades if the range `k` is very large compared to `n` (e.g., sorting [1, 1000000]). |

**In conclusion,** Comparison Counting Sort is a powerful, stable, linear-time sorting algorithm. Its effectiveness is highly dependent on the nature of the input data, shining brightest when sorting integers within a bounded and manageable range.