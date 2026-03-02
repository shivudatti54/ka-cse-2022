# Merge Sort

## Table of Contents

- [Merge Sort](#merge-sort)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Divide and Conquer Paradigm](#divide-and-conquer-paradigm)
  - [Recursive Algorithm Structure](#recursive-algorithm-structure)
  - [The Merge Operation](#the-merge-operation)
  - [Time Complexity Proof](#time-complexity-proof)
  - [Space Complexity](#space-complexity)
  - [Stability Analysis](#stability-analysis)
- [Examples](#examples)
  - [Worked Example: Step-by-Step Merge](#worked-example-step-by-step-merge)
  - [Number of Comparisons Analysis](#number-of-comparisons-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Merge Sort is a classic divide-and-conquer algorithm that fundamentally differs from brute-force approaches typically studied in exhaustive search problems. While the current module focuses on Brute Force Approaches (such as the Travelling Salesman Problem using exhaustive search), Merge Sort represents an alternative algorithmic paradigm that systematically breaks problems into smaller subproblems, solves them independently, and combines their solutions. This approach, known as "divide and conquer," achieves efficient sorting in O(n log n) time complexity, making it vastly superior to any brute-force sorting method (which would require O(n!) or O(2^n) comparisons). Understanding Merge Sort provides essential foundation for analyzing recursive algorithms and is particularly valuable in external sorting applications where data cannot fit entirely in memory.

## Key Concepts

### Divide and Conquer Paradigm

The Merge Sort algorithm operates on three fundamental steps:

1. **Divide**: Split the array into two roughly equal halves
2. **Conquer**: Recursively sort each half
3. **Merge**: Combine the two sorted halves into a single sorted array

### Recursive Algorithm Structure

The algorithm can be expressed recursively as follows:

```
MERGE-SORT(A, p, r):
 if p < r:
 q = ⌊(p + r) / 2⌋
 MERGE-SORT(A, p, q)
 MERGE-SORT(A, q + 1, r)
 MERGE(A, p, q, r)
```

### The Merge Operation

The merge procedure combines two sorted subarrays into one sorted array. It uses an auxiliary array and a sentinel value (∞) to simplify boundary conditions:

```
MERGE(A, p, q, r):
 n1 = q - p + 1
 n2 = r - q
 let L[1..n1+1] and R[1..n2+1] be new arrays
 for i = 1 to n1:
 L[i] = A[p + i - 1]
 for j = 1 to n2:
 R[j] = A[q + j]
 L[n1 + 1] = ∞
 R[n2 + 1] = ∞
 i = 1
 j = 1
 for k = p to r:
 if L[i] ≤ R[j]:
 A[k] = L[i]
 i = i + 1
 else:
 A[k] = R[j]
 j = j + 1
```

### Time Complexity Proof

The time complexity can be analyzed using recurrence relations. For an array of size n:

**Base Case**: T(1) = Θ(1) — sorting a single element requires constant time

**Recursive Case**: T(n) = 2T(n/2) + Θ(n) — we solve two subproblems of size n/2 each, and the merge operation takes Θ(n) time

Using the **Master Theorem**: Here a = 2, b = 2, and f(n) = Θ(n). Since f(n) = Θ(n^(log₂2)) = Θ(n^1), we have case 2, giving T(n) = Θ(n log n).

**Proof by Substitution**: Expanding the recurrence:

- T(n) = 2T(n/2) + cn
- T(n) = 2[2T(n/4) + c(n/2)] + cn = 4T(n/4) + 2cn
- Continuing k levels: T(n) = 2^k T(n/2^k) + kcn
- When n/2^k = 1 (i.e., k = log₂n): T(n) = n·T(1) + cn log n = Θ(n log n)

### Space Complexity

Merge Sort requires Θ(n) auxiliary space for the temporary arrays used in merging. This is because we need to store both subarrays being merged simultaneously. The recursion depth is O(log n), adding O(log n) stack space, but this is dominated by the Θ(n) auxiliary space requirement.

### Stability Analysis

Merge Sort is a **stable** sorting algorithm. The stability property holds because during the merge operation, when elements are equal, we preferentially take from the left subarray (L[i] ≤ R[j]). This preserves the relative order of equal elements, making Merge Sort stable — a crucial property when sorting records by multiple keys.

## Examples

### Worked Example: Step-by-Step Merge

Consider sorting the array [38, 27, 43, 3, 9, 82, 10]:

**After recursive division**:

- [38, 27, 43, 3] | [9, 82, 10]
- [38, 27] | [43, 3] | [9, 82] | [10]
- [38] | [27] | [43] | [3] | [9] | [82] | [10]

**Merging phase**:

- [27, 38] | [3, 43] | [9, 82] | [10]
- [3, 27, 38, 43] | [9, 10, 82]
- [3, 9, 10, 27, 38, 43, 82]

**Verification**: The final array is sorted in ascending order.

### Number of Comparisons Analysis

For merging two sorted subarrays of sizes n₁ and n₂, the worst-case number of comparisons is (n₁ + n₂ - 1). For a complete Merge Sort on n elements, this leads to exactly n⌈log₂n⌉ - (2⌈log₂n⌉ - 1) comparisons in the worst case, which is Θ(n log n).

## Exam Tips

1. **Recognize the recurrence**: When asked to analyze Merge Sort, immediately write T(n) = 2T(n/2) + Θ(n) and apply Master Theorem or substitution method.

2. **Distinguish from brute force**: Unlike exhaustive search (which tries all possibilities), Merge Sort systematically divides the problem, achieving polynomial-time complexity.

3. **Remember stability**: Merge Sort is stable; Quick Sort is not. This distinction matters when choosing algorithms for multi-key sorting.

4. **Space trade-off**: Unlike in-place sorting algorithms (Quick Sort), Merge Sort requires O(n) extra space — important consideration for memory-constrained systems.

5. **Bottom-up variant**: Know that an iterative (bottom-up) version exists that starts with subarrays of size 1 and doubles the size each pass, eliminating the need for recursion.

6. **External sorting**: Merge Sort is the algorithm of choice for external sorting (sorting data on disk) due to its predictable sequential access pattern and stability.

7. **Compare with Quick Sort**: While both are O(n log n) on average, Quick Sort is in-place (O(log n) space) but unstable, while Merge Sort is stable but requires O(n) auxiliary space.
