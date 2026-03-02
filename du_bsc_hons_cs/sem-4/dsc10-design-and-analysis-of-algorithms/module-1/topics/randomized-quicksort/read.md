# Randomized Quicksort

## Introduction

Quicksort is one of the most widely used sorting algorithms in computer science, known for its in-place sorting capability and average-case time complexity of O(n log n). However, the standard quicksort algorithm suffers from a critical weakness: it exhibits worst-case time complexity of O(n²) when the input array is already sorted or reverse-sorted, and the pivot selection strategy is naive (e.g., always choosing the first or last element). This worst-case behavior can be catastrophic in real-world applications where security and performance guarantees are paramount.

**Randomized Quicksort** addresses this fundamental weakness by introducing randomness into the algorithm's pivot selection process. Instead of using a fixed strategy (like picking the first element), randomized quicksort selects the pivot uniformly at random from the array elements. This simple change transforms the algorithm's theoretical guarantees: while the worst-case time complexity remains O(n²), the probability of encountering this worst case becomes negligible for sufficiently large inputs. The expected running time becomes O(n log n), making randomized quicksort a preferred choice in practical implementations and competitive programming.

In the context of the University of Delhi's Computer Science program, understanding randomized quicksort is essential not only for algorithm design but also for appreciating how probability theory can be applied to improve algorithmic performance. This topic also serves as a foundation for understanding randomized algorithms, which have profound applications in cryptography, data structures, and computational geometry.

## Key Concepts

### 1. Standard Quicksort and Its Limitations

The standard quicksort algorithm works by:
- Selecting a **pivot** element from the array
- **Partitioning** the array around the pivot: elements smaller than pivot go to the left, elements greater go to the right
- **Recursively** sorting the left and right subarrays

The partition operation runs in O(n) time. If the pivot consistently divides the array into roughly equal halves, we get the optimal O(n log n) time complexity. However, if the pivot is always the smallest or largest element (as in sorted arrays with first-element pivot selection), we get O(n²) time.

### 2. Randomization Strategy

In randomized quicksort, we make one key modification: **select the pivot randomly**. This can be done in two ways:

1. **Random Pivot Selection**: Before partitioning, randomly select an index from the array and swap that element with the first (or last) element, then proceed with standard partitioning.

2. **Random Permutation**: Randomly shuffle the entire array once at the beginning, then apply standard quicksort. This is equivalent to random pivot selection in expectation.

### 3. The Partition Operation

The partition procedure (Lomuto partition scheme) works as follows:
```
partition(A, low, high):
    pivot = A[high]  // choose last element as pivot after random swap
    i = low - 1
    for j = low to high - 1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i] and A[j]
    swap A[i + 1] and A[high]
    return i + 1
```

The Hoare partition is more efficient but slightly more complex to implement correctly.

### 4. Expected Running Time Analysis

The power of randomization lies in the expected running time analysis. For randomized quicksort:

**Key Insight**: For any input, the probability that a randomly chosen pivot ranks among the top k or bottom k elements is at most 2k/n for any fixed k.

This leads to the recurrence relation:
- T(n) = T(a·n) + T((1-a)·n) + O(n)

Where a is the random fraction representing the pivot's position. Taking expectation over all possible pivot choices and solving gives us **E[T(n)] = O(n log n)**.

### 5. Probability Bounds

Using Chernoff bounds or Markov's inequality, we can prove stronger statements:
- The probability that randomized quicksort takes more than c·n log n time (for c > 1) decreases exponentially with n
- The worst-case O(n²) still exists but occurs with probability less than 1/n for reasonable constants

This is a fundamental concept in **randomized algorithms**: we trade worst-case guarantees for high-probability guarantees.

### 6. Tail Bounds and Concentration

One of the remarkable properties of randomized quicksort is that its performance concentrates around the mean. We can show:
- Pr[T(n) > c·n log n] ≤ 1/n^c' for some c' > 0
- This means almost all random choices lead to good performance

## Examples

### Example 1: Tracing Randomized Quicksort

Consider the array: A = [7, 2, 9, 1, 5, 3, 8, 6]

**Step 1**: Randomly select pivot. Let's say we randomly pick index 3 (value 1) and swap with last element.
A = [7, 2, 9, 6, 5, 3, 8, 1]

**Step 2**: Partition around pivot 1:
- After partition: [1, 2, 9, 6, 5, 3, 8, 7]
- Pivot position: 0

**Step 3**: Recursively sort left (empty) and right [2, 9, 6, 5, 3, 8, 7]

**Step 4**: New random pivot, say index 5 (value 3):
A = [2, 3, 9, 6, 5, 8, 7]

**Step 5**: Partition around 3:
- Result: [2, 3, 9, 6, 5, 8, 7]
- Pivot position: 1

**Step 6**: Continue recursively...

The key observation: even with this unlucky first pivot, the algorithm continues with randomness and maintains good expected performance.

### Example 2: Expected Comparison Count

Let n = 8. For standard quicksort on sorted input [1,2,3,4,5,6,7,8] with first-element pivot:
- Pivot 1: partitions as [1][2,3,4,5,6,7,8]
- Pivot 2: partitions as [2][3,4,5,6,7,8]
- ...and so on
- Total comparisons: n + (n-1) + ... + 1 = n(n+1)/2 = 36

For randomized quicksort on the same input:
- Expected number of comparisons: 2n ln n ≈ 2(8)(2.079) ≈ 33.3
- This is a significant improvement even in this small example!

### Example 3: Probability Calculation

For n = 1000, what's the probability that randomized quicksort takes more than 10·n log n time?

Using tail bounds, we can show:
Pr[T(n) > 10·n log n] ≤ 1/n^4 (approximately)

This means even for n = 1000, the probability is less than 10^-12 — essentially zero in practice!

## Exam Tips

1. **Remember the key difference**: Standard quicksort has O(n²) worst-case; randomized quicksort has O(n²) worst-case but O(n log n) expected time. Know how to prove this.

2. **Pivot selection is crucial**: In randomized quicksort, always randomly select the pivot before partitioning. This can be done by swapping a random element to the first/last position.

3. **Understand the recurrence**: T(n) = T(a·n) + T((1-a)·n) + O(n), where a is uniformly distributed in [0,1]. The expectation E[a] = 1/2 leads to the O(n log n) solution.

4. **Know why randomization helps**: Random pivot selection ensures independence from input distribution. The algorithm performs well on any input, not just random ones.

5. **Space complexity**: Both standard and randomized quicksort use O(log n) expected space for the recursion stack (worst case O(n)).

6. **Compare with other sorting algorithms**: Merge sort is O(n log n) guaranteed but uses O(n) extra space. Heap sort is O(n log n) guaranteed but has worse cache performance. Randomized quicksort balances average-case performance with in-place sorting.

7. **Tail probability matters**: In exams, be prepared to discuss how randomized quicksort achieves concentration around the mean — the probability of bad performance decreases exponentially.