# Insertion Sort - Summary

## Key Definitions
- **Loop Invariant**: A condition that holds true before, during, and after each iteration of a loop, used to prove algorithm correctness
- **In-Place Algorithm**: An algorithm that uses only O(1) auxiliary space regardless of input size
- **Stable Sorting Algorithm**: An algorithm that preserves the relative order of equal elements
- **Adaptive Algorithm**: An algorithm whose running time improves based on input characteristics (e.g., pre-sorted arrays)
- **Inversion**: A pair (i, j) such that i < j but A[i] > A[j]

## Important Formulas
- Worst-case comparisons: T(n) = n(n-1)/2 = Θ(n²)
- Average-case comparisons: T(n) = n(n-1)/4 = Θ(n²)
- Best-case comparisons: T(n) = n-1 = Θ(n)
- Space complexity: O(1) auxiliary space

## Key Points
1. Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position
2. The algorithm maintains a sorted prefix (A[1..j-1]) at each iteration of the outer loop
3. Worst-case time complexity is Θ(n²) for reverse-sorted input; best-case is Θ(n) for already sorted input
4. Insertion Sort is stable—equal elements maintain their relative order after sorting
5. The algorithm is adaptive: nearly sorted arrays yield near-linear running time
6. Insertion Sort requires only O(1) extra space, making it memory-efficient
7. Practical hybrid sorts (e.g., Timsort) use Insertion Sort for small subarrays due to low overhead
8. The correctness proof relies on demonstrating that the loop invariant holds at initialization, is maintained, and terminates correctly

## Common Mistakes
1. Using the wrong comparison operator in pseudocode (must be A[i] > key, not A[i] ≥ key, to maintain stability)
2. Confusing 1-based and 0-based indexing in loop bounds
3. Stating that Insertion Sort is always O(n²)—for sorted inputs it is Θ(n)
4. Forgetting that average-case analysis assumes uniform distribution of input permutations
5. Incorrectly calculating summation totals when deriving complexity formulas