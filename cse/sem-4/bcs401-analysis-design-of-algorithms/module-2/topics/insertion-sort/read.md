# Insertion Sort

## Table of Contents

- [Insertion Sort](#insertion-sort)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Algorithm Description](#algorithm-description)
  - [Pseudocode](#pseudocode)
  - [Correctness Proof Using Loop Invariant](#correctness-proof-using-loop-invariant)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Space Complexity](#space-complexity)
  - [Stability](#stability)
  - [Adaptive Nature](#adaptive-nature)
- [Examples](#examples)
  - [Worked Example 1: Step-by-Step Trace](#worked-example-1-step-by-step-trace)
  - [Worked Example 2: Numerical Problem](#worked-example-2-numerical-problem)
  - [Worked Example 3: Nearly Sorted Input](#worked-example-3-nearly-sorted-input)
- [Comparison with Other Sorting Algorithms](#comparison-with-other-sorting-algorithms)
- [Exam Tips](#exam-tips)

## Introduction

Insertion Sort is a fundamental comparison-based sorting algorithm that builds the final sorted array one element at a time. It is particularly intuitive because it mirrors the way humans often sort physical objects, such as playing cards in their hands. The algorithm iterates through an input array, removing one element per iteration and inserting it into its correct position within the already-sorted portion of the array. This incremental construction approach distinguishes Insertion Sort from divide-and-conquer algorithms like Merge Sort and Quick Sort.

The practical significance of Insertion Sort extends beyond its role as a basic sorting algorithm. It exhibits excellent performance on nearly sorted arrays and small data sets, making it the algorithm of choice in hybrid sorting implementations. For instance, Timsort—the default sorting algorithm in Python and Java—uses Insertion Sort for handling small subarrays. The algorithm's in-place nature, stability, and adaptive behavior further contribute to its continued relevance in modern algorithmic implementations. Understanding Insertion Sort provides a foundation for analyzing more complex sorting algorithms and their design trade-offs.

## Key Concepts

### Algorithm Description

Insertion Sort maintains a invariant: at any point during execution, the portion of the array from index 0 to i-1 is sorted in ascending order. The algorithm proceeds by selecting the element at index i (the "key") and comparing it with each element in the sorted portion, shifting elements one position to the right until the correct position for the key is found. This process continues until the entire array is sorted.

The algorithm can be understood through the card-sorting analogy: when organizing a hand of playing cards, we pick up cards one at a time and insert each into its proper position relative to the cards already held. Initially, we hold no cards; as we pick up each new card, we insert it into the correct position among our existing sorted cards. Similarly, Insertion Sort builds a sorted prefix incrementally.

### Pseudocode

```
INSERTION-SORT(A, n):
 for j ← 2 to n do
 key ← A[j]
 i ← j - 1
 while i > 0 and A[i] > key do
 A[i + 1] ← A[i]
 i ← i - 1
 A[i + 1] ← key
```

Note: This pseudocode uses 1-based indexing for consistency with classical algorithm textbooks. In 0-based implementations, the outer loop runs from j = 1 to n-1, and the inner loop condition becomes i >= 0.

### Correctness Proof Using Loop Invariant

**Theorem:** INSERTION-SORT correctly sorts the array A[1..n] in ascending order.

**Loop Invariant:** At the start of each iteration of the outer loop (for a given value of j), the subarray A[1..j-1] consists of the elements originally in A[1..j-1] but now in sorted order, and each element in A[1..j-1] is less than or equal to every element in A[j..n].

**Proof by Induction:**

_Initialization (j = 2):_ Before the first iteration, the subarray A[1..j-1] contains only A[1], which is trivially sorted. The loop invariant holds.

_Maintenance:_ Consider an iteration with given j. The inner while loop shifts all elements A[i] that are greater than key one position to the right. When the loop terminates, we have A[i] ≤ key < A[i+1] (or i = 0). The key is then inserted at position i+1. Thus, after the insertion, A[1..j] is sorted and contains exactly the elements originally in A[1..j]. All elements in A[1..j] are less than or equal to all elements in A[j+1..n] because the elements from A[j+1..n] are unchanged. The invariant is maintained.

_Termination:_ The loop terminates when j = n+1. By the loop invariant, A[1..n] is sorted and contains all n elements of the original array. ∎

### Time Complexity Analysis

**Worst-Case Analysis:** The worst case occurs when the input array is in reverse sorted order. For each j (from 2 to n), the inner while loop executes j-1 comparisons. The total number of comparisons is:

T(n) = Σ(j=2 to n) (j-1) = Σ(k=1 to n-1) k = (n-1)n/2 = Θ(n²)

Therefore, T(n) = Θ(n²) in the worst case.

**Best-Case Analysis:** The best case occurs when the array is already sorted. For each j, the while condition fails immediately (A[i] ≤ key), resulting in only one comparison per iteration. The total comparisons is n-1, giving T(n) = Θ(n).

**Average-Case Analysis:** Assuming all input permutations are equally likely, the expected number of shifts for position j is (j-1)/2. Summing over all positions:

T(n) = Σ(j=2 to n) (j-1)/2 = (1/2) × Σ(k=1 to n-1) k = (n-1)n/4 = Θ(n²)

Thus, the average-case complexity is Θ(n²), though with a constant factor half that of the worst case.

### Space Complexity

Insertion Sort is an in-place algorithm requiring only O(1) auxiliary space. The algorithm sorts the array by shifting elements within the original array, without allocating additional data structures proportional to the input size.

### Stability

Insertion Sort is a stable sorting algorithm. During the insertion process, equal elements are never passed over; when A[i] ≤ key (rather than A[i] < key), the while loop terminates, preserving the relative order of equal elements.

### Adaptive Nature

Insertion Sort exhibits adaptive behavior—its running time improves for nearly sorted inputs. If the array is k-sorted (every element is within k positions of its final sorted position), Insertion Sort runs in O(nk) time. For k = 1 (already sorted), the time is Θ(n). This adaptive property makes Insertion Sort valuable in hybrid algorithms.

## Examples

### Worked Example 1: Step-by-Step Trace

Trace Insertion Sort on the array A = [5, 2, 4, 6, 1, 3]:

**Initial:** [5, 2, 4, 6, 1, 3]

**j = 2:** key = 2; compare with 5 → shift 5 right; insert 2
Result: [2, 5, 4, 6, 1, 3]

**j = 3:** key = 4; compare with 5 → shift 5 right; compare with 2 → insert 4
Result: [2, 4, 5, 6, 1, 3]

**j = 4:** key = 6; compare with 5 → 6 > 5, no shift; insert 6
Result: [2, 4, 5, 6, 1, 3]

**j = 5:** key = 1; shift 6, 5, 4, 2 right; insert 1
Result: [1, 2, 4, 5, 6, 3]

**j = 6:** key = 3; shift 6, 5, 4 right; compare with 2 → insert 3
Result: [1, 2, 3, 4, 5, 6]

Total comparisons: 1 + 2 + 1 + 4 + 4 = 12

### Worked Example 2: Numerical Problem

**Problem:** For n = 8 elements, calculate the exact number of comparisons made by Insertion Sort when the input is [8, 7, 6, 5, 4, 3, 2, 1] (reverse sorted).

**Solution:**

- j=2: compare 7 with 8 → 1 comparison, shift 8 → 1 shift
- j=3: compare 6 with 8, then 7 → 2 comparisons, shift 8,7 → 2 shifts
- j=4: compare 5 with 8, 7, 6 → 3 comparisons
- j=5: compare 4 with 8, 7, 6, 5 → 4 comparisons
- j=6: compare 3 with 8, 7, 6, 5, 4 → 5 comparisons
- j=7: compare 2 with 8, 7, 6, 5, 4, 3 → 6 comparisons
- j=8: compare 1 with 8, 7, 6, 5, 4, 3, 2 → 7 comparisons

Total comparisons = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 = n(n-1)/2 = 8(7)/2

### Worked Example 3: Nearly Sorted Input

**Problem:** What is the time complexity when sorting [1, 3, 2, 4, 5, 7, 6, 8]?

**Solution:** This array has only two inversions: (3,2) and (7,6).

- Each element at most needs one comparison (except those involved in inversions)
- Total comparisons ≈ n + number of inversions - 1 ≈ 8 + 2 - 1 = 9
- Therefore, T(n) = Θ(n), demonstrating the adaptive nature

## Comparison with Other Sorting Algorithms

| Property     | Insertion Sort | Selection Sort | Merge Sort | Quick Sort |
| ------------ | -------------- | -------------- | ---------- | ---------- |
| Best Case    | Θ(n)           | Θ(n²)          | Θ(n log n) | Θ(n log n) |
| Average Case | Θ(n²)          | Θ(n²)          | Θ(n log n) | Θ(n log n) |
| Worst Case   | Θ(n²)          | Θ(n²)          | Θ(n log n) | Θ(n²)      |
| Space        | O(1)           | O(1)           | O(n)       | O(log n)   |
| Stable       | Yes            | No             | Yes        | No         |
| Adaptive     | Yes            | No             | No         | No         |

## Exam Tips

1. **Loop Invariant Proof**: Be prepared to prove correctness using loop invariants—the initialization, maintenance, and termination phases must all be rigorously argued.

2. **Complexity Derivation**: Memorize the summation formulas for worst-case (n(n-1)/2) and average-case (n(n-1)/4) comparisons; understand how these are derived from the nested loop structure.

3. **Adaptive Property**: Recognize that Insertion Sort runs in Θ(n) time on nearly sorted arrays; this property is exploited in practical hybrid algorithms like Timsort.

4. **Stability Matters**: Remember that Insertion Sort is stable; this is crucial when sorting records by multiple keys where maintaining original order matters.

5. **Space Complexity**: Always state that Insertion Sort is in-place with O(1) auxiliary space—this contrasts with Merge Sort's O(n) requirement.

6. **Pseudocode Indexing**: Pay attention to whether the pseudocode uses 0-based or 1-based indexing, as this affects loop bounds and conditions.

7. **Practical Applications**: In practice, Insertion Sort is used for small subarrays (typically n < 10-20) within divide-and-conquer sorts due to its low overhead and cache efficiency.

8. **Numerical Problems**: Practice calculating exact comparison counts for specific input arrays—these frequently appear in examinations.
