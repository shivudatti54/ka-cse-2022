# Randomized Quicksort - Summary

## Key Definitions and Concepts

- **Randomized Quicksort**: A variant of quicksort that randomly selects the pivot element before each partition operation, ensuring O(n log n) expected running time regardless of input distribution
- **Pivot Selection**: Randomly choosing an index from [low, high] and swapping it with the boundary position before partitioning
- **Expected Running Time**: The average running time over all possible random choices, expressed as O(n log n)
- **Lomuto Partition Scheme**: A partitioning method that maintains a boundary index for elements smaller than pivot

## Important Formulas and Theorems

- **Expected Time Recurrence**: T(n) = (1/n)Σ[T(i-1) + T(n-i)] + Θ(n) where i ranges from 1 to n
- **Solution**: T(n) = O(n log n)
- **Expected Comparisons**: ≈ 2n ln n ≈ 1.39n log₂n
- **Worst-Case Probability**: For n elements, probability of consistently worst-case = 2^(n-1)/n!

## Key Points

- Randomized quicksort addresses the O(n²) worst-case of deterministic quicksort through random pivot selection
- The algorithm remains in-place with O(1) auxiliary space (ignoring recursion stack)
- Randomized quicksort is NOT stable—equal elements may change relative positions
- Expected stack space is O(log n), worst-case is O(n)
- Any element has probability 1/n of being chosen as pivot at each step
- The randomization ensures independence from input distribution
- For practical applications, randomized quicksort is preferred over deterministic versions

## Common Mistakes to Avoid

- Confusing randomization in pivot selection with randomized algorithm execution
- Forgetting that expected time is O(n log n), not guaranteed O(n log n)
- Assuming stability—it is not a stable sorting algorithm
- Confusing space complexity—auxiliary space is O(1) but stack space is O(log n) expected

## Revision Tips

1. Practice tracing through randomized quicksort with different random pivot selections
2. Memorize the expected comparisons formula: 2n ln n
3. Remember that randomization makes the algorithm input-independent
4. Know the comparison: randomized quicksort vs deterministic quicksort vs merge sort
5. Review probability concepts: linearity of expectation is essential for analysis