# Randomized Quicksort

## Introduction

Quicksort is one of the most widely used sorting algorithms in computer science, known for its average-case time complexity of O(n log n) and in-place sorting capability. However, the standard quicksort algorithm exhibits a worst-case time complexity of O(n²) when the input array is already sorted or nearly sorted. This worst-case behavior occurs because the pivot selection is deterministic, always choosing the first or last element as the pivot.

**Randomized Quicksort** addresses this fundamental weakness by introducing randomness into the pivot selection process. Instead of deterministically choosing a pivot, the algorithm randomly selects an element from the array as the pivot. This randomization ensures that the expected running time remains O(n log n) regardless of the input distribution, making the algorithm robust and reliable for practical applications.

In the context of the University of Delhi's Computer Science program, understanding randomized quicksort is essential for several reasons. First, it demonstrates how randomization can be used as a algorithmic technique to improve worst-case performance. Second, it provides deep insights into probabilistic analysis of algorithms. Third, it is a favorite topic in campus placement interviews and competitive examinations like GATE. This algorithm elegantly combines divide-and-conquer with randomization, making it a cornerstone of modern algorithm design.

## Key Concepts

### Standard Quicksort and Its Limitations

The standard quicksort algorithm works by selecting a pivot element, partitioning the array around the pivot (elements smaller than pivot on the left, elements greater on the right), and recursively sorting the sub-arrays. The efficiency of quicksort heavily depends on how well the pivot divides the array. Ideally, the pivot should be the median element, splitting the array into two nearly equal halves.

In the deterministic version, when the pivot is always chosen as the first element, a sorted or nearly sorted input produces highly unbalanced partitions, leading to O(n²) time complexity. This happens because each partition only reduces the problem size by one element, creating a recursion tree of height n.

### Randomized Pivot Selection

The key innovation in randomized quicksort is the random selection of the pivot. Before each partition step, the algorithm randomly selects an index from the range [low, high] and swaps the element at that index with the element at the high (or low) position before proceeding with the standard partition procedure.

This simple randomization fundamentally changes the behavior of the algorithm:

1. **Probabilistic Guarantee**: For any input distribution, the expected number of comparisons is O(n log n)
2. **Independence of Input**: The running time no longer depends on the specific input arrangement
3. **Practical Reliability**: The probability of worst-case behavior becomes vanishingly small

### Analysis of Randomized Quicksort

The analysis of randomized quicksort relies on probabilistic techniques. Let T(n) be the expected running time for sorting n elements. When we randomly select a pivot, any element has equal probability (1/n) of being chosen as the pivot. If the i-th smallest element is chosen as pivot, we create two subproblems of sizes i-1 and n-i.

The expected value of T(n) satisfies the recurrence:

**T(n) = (1/n) Σ [T(i-1) + T(n-i)] + Θ(n)** for i=1 to n

Through careful mathematical analysis, this recurrence solves to T(n) = O(n log n). The linearity of expectation and indicator random variables are the key tools used in this analysis.

### Partition Algorithm

The partition procedure in randomized quicksort works as follows:
1. Generate a random index between low and high (inclusive)
2. Swap the element at the random index with the element at high
3. Use the standard Lomuto or Hoare partition scheme
4. Return the final position of the pivot

The Lomuto partition scheme maintains an index `i` for the boundary of elements smaller than pivot, and iterates through the array with index `j`, swapping elements when they are smaller than the pivot.

## Examples

### Example 1: Sorting a Small Array

Let's trace through randomized quicksort on the array: **[5, 2, 9, 1, 7, 6, 3]**

**First Iteration:**
- Random pivot selected: let's say index 3 (value 1)
- After swapping: **[5, 2, 9, 1, 7, 6, 3]** (pivot at end)
- After partition: **[1, 2, 9, 5, 7, 6, 3]** → pivot at position 0
- Array becomes: **[1] | [2, 9, 5, 7, 6, 3]**

**Second Iteration (on [2, 9, 5, 7, 6, 3]):**
- Random pivot selected: let's say index 5 (value 3)
- After partition: **[2, 3, 9, 5, 7, 6, 9]** → pivot at position 1
- Array becomes: **[2, 3] | [9, 5, 7, 6]**

The process continues recursively until the array is fully sorted. Each random pivot selection introduces randomness that prevents the worst-case scenario from occurring consistently.

### Example 2: Analyzing Worst-Case Probability

What is the probability that randomized quicksort performs as badly as the deterministic version on a sorted array of size 10?

For the worst case to occur at every level, the random pivot must always select either the smallest or largest element at each recursion level. The probability of this happening is:

- At first level (n=10): 2/10 = 1/5
- At second level (n=9): 2/9
- At third level (n=8): 2/8 = 1/4

Probability = (2/10) × (2/9) × (2/8) × ... × (2/2) = 2⁹/(10!) ≈ 0.00000003%

This negligible probability demonstrates why randomized quicksort is practically immune to worst-case behavior.

### Example 3: Expected Number of Comparisons

For an array of n elements, the expected number of comparisons in randomized quicksort is approximately 2n ln n ≈ 1.39n log₂n.

For n = 1000:
- Expected comparisons ≈ 2 × 1000 × ln(1000) ≈ 13,820
- Worst-case comparisons = n(n-1)/2 ≈ 499,500

The ratio of worst-case to expected is approximately 36:1, highlighting the dramatic improvement randomization provides.

## Exam Tips

1. **Understand the Difference**: Clearly distinguish between deterministic quicksort and randomized quicksort—randomization is in pivot selection, not in the sorting logic itself.

2. **Analysis is Key**: Be prepared to write the recurrence relation for expected running time and solve it using the substitution method or recursion tree method.

3. **Probability in Analysis**: Know how to use linearity of expectation and indicator random variables in algorithm analysis—these are frequently asked in DU exams.

4. **Space Complexity**: Remember that randomized quicksort requires O(log n) expected stack space due to recursion, but O(n) in worst case.

5. **Stability**: Randomized quicksort is NOT stable because elements may be swapped across the partition boundary arbitrarily.

6. **In-Place Property**: Despite randomization, it remains an in-place sorting algorithm requiring only O(1) auxiliary space.

7. **Practical Advantages**: For practical implementation, randomized quicksort is preferred over deterministic quicksort because it eliminates the dependence on input distribution.

8. **Comparison with Other Algorithms**: Know when to use quicksort (average-case efficient, in-place) versus merge sort (stable, O(n log n) guaranteed) versus heap sort (O(n log n) worst-case).