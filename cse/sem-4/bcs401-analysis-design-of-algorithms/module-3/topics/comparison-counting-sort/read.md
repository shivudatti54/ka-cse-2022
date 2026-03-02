# Counting Sort

## Table of Contents

- [Counting Sort](#counting-sort)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Algorithm Overview](#algorithm-overview)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Space Complexity](#space-complexity)
  - [Stability Property](#stability-property)
- [Examples](#examples)
  - [Example 1: Basic Counting Sort Execution](#example-1-basic-counting-sort-execution)
  - [Example 2: Small Range](#example-2-small-range)
- [Exam Tips](#exam-tips)

## Introduction

Counting Sort is an integer sorting algorithm that sorts elements by counting the number of occurrences of each distinct value. Unlike comparison-based sorting algorithms such as Merge Sort or Heap Sort, Counting Sort does not make comparisons between elements to determine their order. Instead, it exploits the fact that the input consists of integers within a known range. This algorithm exemplifies the "Transform-and-Conquer" paradigm, where the problem is transformed into a simpler form (counting frequencies) before solving it. Counting Sort achieves linear time complexity O(n + k), where n is the number of elements and k is the range of input values, making it exceptionally efficient for integer data within bounded ranges.

The algorithm operates in three distinct phases. First, it determines the maximum value in the input array to establish the range k. Second, it counts the occurrences of each value in a separate count array. Third, it reconstructs the sorted output by using the count information to place elements in their correct positions. Counting Sort is a stable sorting algorithm, meaning that elements with equal values maintain their relative order from the input to the output, which is crucial when Counting Sort is used as a subroutine in Radix Sort.

## Key Concepts

### Algorithm Overview

Counting Sort transforms the problem of sorting into a problem of counting, which can be solved in linear time. The fundamental assumption is that the input consists of integers in the range [0, k], where k is reasonably small relative to n. The algorithm uses two additional arrays: a count array C of size k + 1 to store frequencies, and an output array B to store the sorted result.

The pseudocode for Counting Sort is as follows:

```
COUNTING-SORT(A, B, n, k):
 // Input: A[1..n] - array of integers in range [0, k]
 // Output: B[1..n] - sorted array
 // Auxiliary: C[0..k] - count array

 // Phase 1: Initialize count array
 for i = 0 to k:
 C[i] = 0

 // Phase 2: Count occurrences
 for j = 1 to n:
 C[A[j]] = C[A[j]] + 1

 // Phase 3: Transform counts to positions
 for i = 1 to k:
 C[i] = C[i] + C[i - 1]

 // Phase 4: Build output array (traverse backwards for stability)
 for j = n down to 1:
 B[C[A[j]]] = A[j]
 C[A[j]] = C[A[j]] - 1
```

### Time Complexity Analysis

The time complexity of Counting Sort can be formally proven as O(n + k). Let n denote the number of input elements and k denote the range of input values.

**Theorem**: Counting Sort runs in Θ(n + k) time.

**Proof**: The algorithm consists of four distinct loops, each contributing to the overall complexity. The first loop (initialization) iterates k + 1 times, contributing Θ(k). The second loop (counting occurrences) iterates n times, contributing Θ(n). The third loop (transforming counts to cumulative positions) iterates k times, contributing Θ(k). The fourth loop (building the output) iterates n times, contributing Θ(n). Adding these contributions: Θ(k) + Θ(n) + Θ(k) + Θ(n) = Θ(n + k). ∎

When k = O(n), the complexity becomes Θ(n), achieving linear time sorting—impossible for comparison-based algorithms under the Ω(n log n) lower bound.

### Space Complexity

Counting Sort requires additional space for two arrays: the count array C of size k + 1 and the output array B of size n. Therefore, the space complexity is Θ(n + k). When k is large relative to n, this space requirement becomes a significant drawback.

### Stability Property

**Definition**: A sorting algorithm is stable if it preserves the relative order of equal elements.

**Theorem**: Counting Sort is stable.

**Proof**: The stability of Counting Sort is ensured by traversing the input array from right to left during the placement phase (Phase 4). Consider two elements A[i] and A[j] such that A[i] = A[j] and i < j. Since we process from right to left, element A[j] (with larger index) is placed before A[i]. The cumulative count C[A[i]] is decremented after placing A[j], ensuring that A[i] occupies the position immediately before A[j] in the output. Thus, the original relative order of equal elements is preserved. ∎

The stability property is essential when Counting Sort serves as the stable sort subroutine in Radix Sort, where sorting must be performed digit by digit from least significant to most significant.

## Examples

### Example 1: Basic Counting Sort Execution

Consider the input array A = [2, 5, 3, 0, 2, 3, 0, 3] with n = 8 and k = 5.

**Phase 1 (Initialize)**: C = [0, 0, 0, 0, 0, 0]

**Phase 2 (Count)**: After counting: C = [2, 0, 2, 3, 0, 1]

- C[0] = 2 (zeros appear twice)
- C[2] = 2 (twos appear twice)
- C[3] = 3 (threes appear three times)
- C[5] = 1 (five appears once)

**Phase 3 (Cumulative)**: C = [2, 2, 4, 7, 7, 8]

- C[0] = 2
- C[1] = C[1] + C[0] = 0 + 2 = 2
- C[2] = C[2] + C[1] = 2 + 2 = 4
- C[3] = C[3] + C[2] = 3 + 4 = 7

**Phase 4 (Place)**: Traversing from right to left:

- j=8: A[8]=3 → position C[3]=7 → B[7]=3 → C[3]=6
- j=7: A[7]=0 → position C[0]=2 → B[2]=0 → C[0]=1
- j=6: A[6]=3 → position C[3]=6 → B[6]=3 → C[3]=5
- j=5: A[5]=3 → position C[3]=5 → B[5]=3 → C[3]=4
- j=4: A[4]=2 → position C[2]=4 → B[4]=2 → C[2]=3
- j=3: A[3]=3 → position C[3]=4 → B[4]=3 → C[3]=3 (overwrites! stability maintained)
- j=2: A[2]=3 → position C[3]=3 → B[3]=3 → C[3]=2
- j=1: A[1]=2 → position C[2]=3 → B[3]=2 → C[2]=2

Final sorted output: B = [0, 0, 2, 2, 3, 3, 3, 5]

### Example 2: Small Range

Input: A = [1, 4, 1, 2, 7, 5, 2], n = 7, k = 7

After initialization and counting: C = [0, 2, 2, 0, 1, 1, 0, 1]
After cumulative: C = [0, 2, 4, 4, 5, 6, 6, 7]
After placement (right to left): B = [1, 1, 2, 2, 4, 5, 7]

## Exam Tips

1. **Non-Comparison Nature**: Remember that Counting Sort is NOT a comparison-based sort; it achieves linear time by exploiting integer key properties, circumventing the Ω(n log n) comparison lower bound.

2. **Stability for Radix Sort**: When used in Radix Sort, Counting Sort's stability is essential—without it, earlier digit sorts would be disrupted by later digit sorts.

3. **Choice Between O(n log n) and O(n + k)**: Use Counting Sort when k = O(n); otherwise, comparison sorts may be preferable despite their Ω(n log n) lower bound.

4. **Backward Traversal**: The right-to-left traversal in Phase 4 is critical for stability—never skip this detail in exams.

5. **Space-Time Tradeoff**: Counting Sort trades space (Θ(n + k)) for time (Θ(n + k)), making it unsuitable when memory is constrained or k >> n.

6. **Integer Requirement**: Counting Sort applies only to non-negative integers within a bounded range; it cannot directly sort floating-point numbers or strings without modification.

7. **Transform-and-Conquer Interpretation**: The algorithm "transforms" the original array into a frequency count, then "conquers" by reconstructing sorted output from these counts.
