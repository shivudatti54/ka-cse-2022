# Selection Sort and Bubble Sort

## Introduction

Sorting algorithms constitute a fundamental pillar of computer science, serving as essential building blocks for numerous computational tasks and forming an integral component of algorithm analysis curricula. Among the simplest yet pedagogically significant sorting algorithms are Selection Sort and Bubble Sort, both of which are traditionally covered in introductory modules of algorithm design and analysis. While these algorithms may not exhibit optimal performance characteristics for large-scale datasets, their thorough understanding remains crucial for several compelling reasons.

First, these algorithms provide a solid foundation for comprehending fundamental algorithm design principles, including nested loop structures, compare-and-swap operations, in-place sorting techniques, and the mathematical analysis of algorithmic complexity. Second, they serve as conceptual building blocks for more sophisticated sorting algorithms such as Quick Sort, Merge Sort, and Heap Sort, wherein similar comparison-based strategies are employed with advanced optimizations. Third, despite their O(n²) time complexity in the worst and average cases, both algorithms possess specific operational niches where they outperform more complex methods, particularly for small datasets, nearly sorted arrays, or environments with severe memory constraints.

In this comprehensive module, we shall conduct a rigorous analysis of both algorithms, examining their correctness through formal proof methodologies, deriving their time and space complexities through mathematical analysis, and exploring their practical applications and optimization strategies. We shall also investigate the mathematical foundations that establish their correctness and efficiency bounds.

## Key Concepts

### Selection Sort

Selection Sort represents a fundamental comparison-based sorting algorithm that operates by systematically dividing the input array into two distinct regions: a sorted region occupying the left portion and an unsorted region occupying the remaining right portion. Initially, the sorted region remains empty while the unsorted region encompasses the entire array. The algorithm iteratively selects the minimum (or maximum, depending on sorting order) element from the unsorted region and relocates it to the end of the sorted region through a single swap operation.

**Algorithm Steps:**

1. Initialize the boundary index i = 0, marking the start of the unsorted region
2. Assume arr[i] as the current minimum element
3. Traverse indices j from i+1 to n-1, comparing each element with the current minimum
4. If arr[j] < current minimum, update the minimum to arr[j]
5. After completing the scan, if the minimum differs from arr[i], swap arr[i] with arr[min_index]
6. Increment i by 1 and repeat steps 2-5 until i reaches n-1

**Formal Correctness Proof Using Loop Invariant:**

We prove the correctness of Selection Sort through the method of loop invariants. A loop invariant is a condition that holds true before, during, and after each iteration of the loop, providing mathematical assurance of algorithm correctness.

_Invariant Statement:_ At the start of each iteration of the outer loop (with current index i), the subarray arr[0..i-1] contains the i smallest elements of the original array, arranged in sorted order: arr[0] ≤ arr[1] ≤ ... ≤ arr[i-1].

_Proof of Invariant Maintenance:_ Suppose the invariant holds at the beginning of iteration i. The algorithm scans the unsorted subarray arr[i..n-1] to locate the minimum element. Let min_index denote the index of this minimum element. Upon swapping arr[i] with arr[min_index], the element at position i becomes the smallest remaining element. Since arr[0..i-1] already contains the i smallest elements in sorted order (by the invariant hypothesis), and arr[i] now holds the (i+1)th smallest element, the subarray arr[0..i] is sorted and contains the (i+1) smallest elements. Thus, the invariant is maintained for the next iteration.

_Proof of Initialization:_ Before the first iteration (i = 0), the sorted region is empty. The empty set trivially contains the 0 smallest elements in sorted order, satisfying the invariant.

_Proof of Termination:_ The algorithm terminates when i = n. At this point, the invariant states that arr[0..n-1] contains all n elements in sorted order, proving correctness.

**Time Complexity Derivation:**

The algorithm comprises two nested loops. The outer loop executes n-1 times. For each iteration i of the outer loop, the inner scanning loop examines n-i-1 elements. Therefore, the total number of comparisons T(n) is given by:

T(n) = Σ\_{i=0}^{n-2} (n - i - 1) = (n-1) + (n-2) + ... + 1 = n(n-1)/2

This simplifies to Θ(n²) comparisons in all cases—whether the input is already sorted, reverse sorted, or randomly ordered. The number of swaps is at most n-1, making Selection Sort particularly efficient in scenarios where memory write operations are significantly more expensive than read operations, such as in certain embedded systems or flash memory environments.

- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity:** O(1) — the algorithm operates in-place, requiring only a constant amount of auxiliary space

### Bubble Sort

Bubble Sort represents another fundamental comparison-based sorting algorithm that employs a straightforward yet effective strategy of repeatedly traversing the array, comparing adjacent elements, and exchanging them when they violate the desired ordering relationship. The algorithm derives its name from the manner in which larger elements progressively "bubble up" toward their correct positions at the end of the array with each complete pass.

**Algorithm Steps:**

1. Set flag swapped = true to indicate the commencement of sorting process
2. While swapped is true, execute the following:
   a. Set swapped = false initially
   b. For each adjacent pair (j from 0 to n-i-2):

- If arr[j] > arr[j+1], swap these elements
- Set swapped = true to record that an exchange occurred
  c. If no swaps occurred in this pass, terminate early (optimization)

**Formal Correctness Proof Using Loop Invariant:**

We establish Bubble Sort's correctness through a refined loop invariant approach.

_Invariant Statement:_ After k complete passes through the array (where a pass processes all adjacent pairs from index 0 to n-k-2), the k largest elements are guaranteed to occupy their final sorted positions at indices n-k through n-1, and each is greater than or equal to all elements in the unsorted portion.

_Proof of Maintenance:_ During a single pass, each adjacent pair (arr[j], arr[j+1]) is compared, and if arr[j] > arr[j+1], they are exchanged. This exchange ensures that the larger element moves one position toward the end. By induction, after processing all pairs, the largest element in the unsorted region must reach the last available position. Thus, after pass k, the k largest elements are correctly positioned.

_Proof of Initialization:_ Before the first pass (k = 0), no elements have been sorted. The empty set of sorted elements trivially satisfies the invariant.

_Proof of Termination:_ The algorithm terminates when a complete pass occurs without any swaps, indicating that all adjacent pairs are in correct order, which means the entire array is sorted. Alternatively, termination occurs after n-1 passes, at which point all n elements are positioned correctly.

**Time Complexity Analysis with Optimizations:**

_Standard Bubble Sort:_ The algorithm performs (n-1) + (n-2) + ... + 1 = n(n-1)/2 comparisons in the worst case, yielding Θ(n²) time complexity.

_Optimized Bubble Sort (Early Termination):_

- Best Case: O(n) — when the array is already sorted, only one pass is required
- Average Case: O(n²)
- Worst Case: O(n²) — when the array is reverse sorted

**Space Complexity:** O(1) — in-place sorting algorithm

### Comparative Analysis

| Aspect                    | Selection Sort | Bubble Sort (Optimized) |
| ------------------------- | -------------- | ----------------------- |
| Time Complexity (Best)    | O(n²)          | O(n)                    |
| Time Complexity (Average) | O(n²)          | O(n²)                   |
| Time Complexity (Worst)   | O(n²)          | O(n²)                   |
| Space Complexity          | O(1)           | O(1)                    |
| Number of Swaps           | O(n)           | O(n²) in worst case     |
| Adaptive                  | No             | Yes                     |
| Stable                    | No             | Yes                     |

**Stability Analysis:** A sorting algorithm is considered stable if it preserves the relative order of elements with equal keys. Bubble Sort maintains stability because it exclusively swaps adjacent elements, ensuring that equal-valued elements never change their relative positions. Conversely, Selection Sort is unstable because it may swap non-adjacent elements, potentially altering the relative order of equal elements. This instability can be critical in applications where multiple attributes are sorted sequentially.

## Worked Examples

### Example 1: Selection Sort Execution

**Input:** arr = [64, 25, 12, 22, 11]

**Pass 1:** Find minimum in arr[0..4]

- Minimum = 11 (index 4)
- Swap arr[0] ↔ arr[4]
- Result: [11, 25, 12, 22, 64]

**Pass 2:** Find minimum in arr[1..4]

- Minimum = 12 (index 2)
- Swap arr[1] ↔ arr[2]
- Result: [11, 12, 25, 22, 64]

**Pass 3:** Find minimum in arr[2..4]

- Minimum = 22 (index 3)
- Swap arr[2] ↔ arr[3]
- Result: [11, 12, 22, 25, 64]

**Pass 4:** Find minimum in arr[3..4]

- Minimum = 25 (index 3, no swap needed)
- Result: [11, 12, 22, 25, 64]

Total comparisons: 4 + 3 + 2 + 1 = 10 = 5(5-1)/2
Total swaps: 3

### Example 2: Optimized Bubble Sort Execution

**Input:** arr = [5, 1, 4, 2, 8]

**Pass 1:** Compare adjacent pairs

- (5,1): swap → [1, 5, 4, 2, 8]
- (5,4): swap → [1, 4, 5, 2, 8]
- (5,2): swap → [1, 2, 5, 4, 8]
- (5,8): no swap
- swapped = true

**Pass 2:**

- (1,2): no swap
- (2,5): swap → [1, 2, 4, 5, 8]
- (4,5): no swap
- (5,8): no swap
- swapped = true

**Pass 3:**

- (1,2): no swap
- (2,4): no swap
- (4,5): no swap
- (5,8): no swap
- swapped = false → Algorithm terminates

Total passes: 3 (instead of 5 for n=5)
This demonstrates the adaptive nature of optimized Bubble Sort on partially sorted data.

## Numerical Problem Solving

**Problem:** For an array of n = 10 elements, calculate the exact number of comparisons performed by Selection Sort and determine how many comparisons are saved when Bubble Sort (with early termination optimization) is applied to an already sorted array.

_Solution:_ Selection Sort always performs n(n-1)/2 = 10(9)/2 = 45 comparisons regardless of input order. For Bubble Sort on an already sorted array, only one pass is required with n-1 = 9 comparisons. Therefore, Bubble Sort saves 45 - 9 = 36 comparisons in this best-case scenario.
