# Quick Sort

## Table of Contents

- [Quick Sort](#quick-sort)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Divide and Conquer Framework](#divide-and-conquer-framework)
  - [Partition Schemes](#partition-schemes)
  - [Pivot Selection Strategies](#pivot-selection-strategies)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Space Complexity Analysis](#space-complexity-analysis)
  - [Randomized Quick Sort](#randomized-quick-sort)
  - [Stability Analysis](#stability-analysis)
- [Examples](#examples)
  - [Example 1: Lomuto Partition Walkthrough](#example-1-lomuto-partition-walkthrough)
  - [Example 2: Recursive Quick Sort Trace](#example-2-recursive-quick-sort-trace)
  - [Example 3: Comparing Worst vs. Average Case](#example-3-comparing-worst-vs-average-case)
- [Exam Tips](#exam-tips)

## Introduction

Quick Sort is one of the most efficient and widely used sorting algorithms in computer science, classified under the **Divide and Conquer** paradigm. Despite being listed in this module, it is important to note that Quick Sort is not a brute force technique; rather, it employs a sophisticated divide-and-conquer strategy that achieves an average-case time complexity of O(n log n). The algorithm works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. These sub-arrays are then sorted recursively, and the results are combined to produce the sorted array.

The elegance of Quick Sort lies in its in-place sorting capability, requiring only O(log n) auxiliary space for the recursion stack on average. However, its performance is highly dependent on the choice of pivot, leading to a worst-case time complexity of O(n²) when poorly implemented. This characteristic makes understanding pivot selection strategies crucial for algorithm designers and software engineers. Quick Sort exhibits excellent cache performance due to its sequential memory access patterns, making it particularly efficient in practice despite its theoretical worst-case bound.

## Key Concepts

### Divide and Conquer Framework

The Quick Sort algorithm follows the classic divide-and-conquer paradigm through three distinct phases. In the **Divide** phase, a pivot element is selected from the array, and the remaining elements are partitioned into two sub-arrays such that all elements less than the pivot are placed in the left sub-array, while all elements greater than the pivot are placed in the right sub-arrays. The **Conquer** phase involves recursively sorting both sub-arrays using the same procedure. Finally, in the **Combine** phase, the sorted sub-arrays are combined with the pivot to produce the fully sorted array—a process that requires no additional work since the partition operation naturally places elements in their correct relative positions.

### Partition Schemes

**Lomuto Partition Scheme**: This scheme, also known as the "stable" partition, always selects the last element as the pivot and maintains two pointers. The algorithm maintains an index `i` for the smaller elements and iterates through the array using index `j`. When `A[j] ≤ pivot`, the algorithm swaps `A[i]` and `A[j]` and increments `i`. Finally, the pivot element is swapped into its correct position at `A[i]`. While simpler to implement, this scheme degrades to O(n²) when the array is already sorted or reverse sorted.

```
LOMUTO-PARTITION(A, lo, hi):
 pivot = A[hi]
 i = lo - 1
 for j = lo to hi - 1:
 if A[j] ≤ pivot:
 i = i + 1
 swap A[i] and A[j]
 swap A[i + 1] and A[hi]
 return i + 1
```

**Hoare Partition Scheme**: Designed by C.A.R. Hoare, this more efficient scheme uses two pointers starting from opposite ends of the array. The left pointer advances while elements are less than the pivot, and the right pointer retreats while elements are greater than the pivot. When both pointers stop, elements are swapped. This scheme performs fewer swaps on average than Lomuto but requires careful handling of edge cases to ensure correctness.

```
HOARE-PARTITION(A, lo, hi):
 pivot = A[lo]
 i = lo - 1
 j = hi + 1
 while True:
 do j = j - 1 while A[j] > pivot
 do i = i + 1 while A[i] < pivot
 if i < j:
 swap A[i] and A[j]
 else:
 return j
```

### Pivot Selection Strategies

The efficiency of Quick Sort critically depends on pivot selection. The **First Element** strategy simply chooses the first element as the pivot, leading to O(n²) behavior on sorted inputs. The **Last Element** strategy (used in Lomuto) suffers from the same issue. The **Random Element** strategy randomly selects a pivot, providing statistical guarantees against worst-case behavior with high probability. The **Median-of-Three** strategy selects the median of the first, middle, and last elements, offering a good compromise between simplicity and performance. The **Median-of-Three Partitioning** technique also helps eliminate the "sorted array" worst-case scenario and provides better average-case performance in practice.

### Time Complexity Analysis

**Worst-Case Analysis**: The worst-case behavior occurs when the pivot selection consistently produces maximally unbalanced partitions—such as when the first or last element is chosen as pivot on a sorted array. This generates the recurrence T(n) = T(n-1) + T(0) + Θ(n), which solves to Θ(n²). The key insight is that the partition step costs Θ(n) and must be performed n times, leading to quadratic behavior.

**Average-Case Analysis**: Under the assumption that all permutations of the input are equally likely, the average-case time complexity can be derived using recurrence relations. The expected position of the pivot is at the median, leading to the recurrence T(n) = 2T(n/2) + Θ(n), which solves to Θ(n log n) using the Master Theorem. More formally, if we let the pivot land at position k with probability 1/n for each k, we get:

T(n) = (1/n) Σ[T(k) + T(n-k-1)] + Θ(n), which simplifies to Θ(n log n)

**Best-Case Analysis**: When the pivot consistently divides the array into two equal halves, we achieve T(n) = 2T(n/2) + Θ(n) = Θ(n log n), representing the optimal performance of Quick Sort.

### Space Complexity Analysis

The space complexity of Quick Sort consists of two components: the auxiliary space for the partition process (O(1) for in-place partitioning) and the stack space for recursion. In the worst case, the recursion depth reaches O(n), requiring O(n) auxiliary space. However, with good pivot selection achieving balanced partitions, the recursion depth is O(log n), resulting in O(log n) space complexity. **Tail Recursion Optimization** can be employed to reduce stack usage by making the recursive call on the smaller subarray first and using iteration for the larger subarray.

### Randomized Quick Sort

Randomized Quick Sort addresses the worst-case behavior by randomly selecting the pivot element. This randomized version provides probabilistic guarantees: for any input, the expected running time is O(n log n), regardless of the input arrangement. The randomization is typically achieved by swapping the randomly selected element with the first or last element before proceeding with the standard partition scheme. This approach transforms the algorithm's behavior from input-dependent to statistically predictable.

### Stability Analysis

Quick Sort is an **unstable** sorting algorithm, meaning that the relative order of equal elements may not be preserved after sorting. This instability arises from the swapping of elements across the pivot during partitioning. For applications requiring stability, alternative algorithms like Merge Sort should be considered. The instability can be problematic in scenarios where the sorted order of equal elements carries semantic meaning, such as sorting records by multiple keys.

## Examples

### Example 1: Lomuto Partition Walkthrough

Consider the array: [7, 2, 1, 6, 8, 5, 3, 4]

Using Lomuto partition with the last element (4) as pivot:

- Initial: i = -1, pivot = 4
- j=0: A[0]=7 > 4, no change
- j=1: A[1]=2 ≤ 4, i=0, swap A[0] and A[1]: [2, 7, 1, 6, 8, 5, 3, 4]
- j=2: A[2]=1 ≤ 4, i=1, swap A[1] and A[2]: [2, 1, 7, 6, 8, 5, 3, 4]
- j=3: A[3]=6 > 4, no change
- j=4: A[4]=8 > 4, no change
- j=5: A[5]=5 > 4, no change
- j=6: A[6]=3 ≤ 4, i=2, swap A[2] and A[6]: [2, 1, 3, 6, 8, 5, 7, 4]
- Final swap: swap A[3] and A[7]: [2, 1, 3, 4, 8, 5, 7, 6]

The pivot (4) is now in its correct sorted position at index 3.

### Example 2: Recursive Quick Sort Trace

Sorting [6, 3, 9, 2, 7, 1, 5] with first-element pivot selection:

**Level 1**: Pivot = 6, partition → [3, 2, 1, 5] | 6 | [9, 7]

- Left subarray: [3, 2, 1, 5]
- Right subarray: [9, 7]

**Level 2 (Left)**: Pivot = 3, partition → [2, 1] | 3 | [5]

- Left: [2, 1], Right: [5]

**Level 2 (Right)**: Pivot = 9, partition → [7] | 9 | []

- Left: [7], Right: []

**Level 3**: [2, 1] → pivot = 2 → [1] | 2 | []

- Result after backtracking: [1, 2, 3, 5, 6, 7, 9]

### Example 3: Comparing Worst vs. Average Case

**Sorted Input** [1, 2, 3, 4, 5, 6] with first-element pivot:

- Pivot 1 → partition: [] | 1 | [2, 3, 4, 5, 6]
- Pivot 2 → partition: [] | 2 | [3, 4, 5, 6]
- ... continues linearly → O(n²)

**Randomized Pivot** on same input:

- Expected pivot near median splits array roughly in half each time
- Recurrence depth: log n levels → O(n log n) expected

## Exam Tips

1. **Remember the recurrence**: Quick Sort follows T(n) = 2T(n/2) + Θ(n) for balanced cases, yielding O(n log n), but T(n) = T(n-1) + Θ(n) in the worst case, yielding O(n²).

2. **Pivot choice matters**: Always consider how pivot selection affects partition balance—randomized or median-of-three strategies prevent worst-case behavior on sorted inputs.

3. **In-place but not stable**: Quick Sort uses O(1) auxiliary space but loses the relative order of equal elements; for stability, use Merge Sort instead.

4. **Stack overflow risk**: In the worst case, recursion depth is O(n); consider iterative implementations or tail recursion optimization for large datasets.

5. **Hoare vs. Lomuto**: Hoare partition typically performs fewer swaps but requires careful implementation; Lomuto is simpler but degrades on sorted arrays.

6. **Practical superiority**: Despite O(n²) worst-case, Quick Sort often outperforms O(n log n) algorithms in practice due to better cache locality and lower constant factors.

7. **Hybrid approaches**: For improved worst-case guarantees, consider Introsort (Quick Sort + Heap Sort switch) or using Quick Sort for smaller subarrays (< 10 elements) where insertion sort excels.
