# Randomized Quicksort - Summary

## Key Definitions and Concepts

- **Randomized Quicksort**: A variant of quicksort that selects the pivot randomly instead of using a fixed strategy, achieving O(n log n) expected time complexity.

- **Pivot**: The element around which the array is partitioned. In randomized quicksort, this is chosen uniformly at random from the array.

- **Partition**: The process of rearranging elements so that all elements smaller than the pivot come before it, and all greater elements come after it.

- **Expected Running Time**: The average running time over all possible random choices (not to be confused with average-case over all possible inputs).

- **Tail Bound**: A probability bound on how much the actual running time deviates from the expected value.

## Important Formulas and Theorems

- **Expected Comparisons**: E[n] = 2n ln n ≈ 1.39 n log₂ n (for large n)
- **Worst-case Time**: O(n²) — unchanged from standard quicksort
- **Expected Time**: O(n log n)
- **Space Complexity**: O(log n) expected, O(n) worst-case (recursion stack)

## Key Points

1. Randomization transforms quicksort from input-sensitive to input-independent in expectation.

2. The worst-case O(n²) still exists but occurs with probability approaching 0 as n grows.

3. Random pivot selection breaks the correlation between input order and running time.

4. Two implementation approaches: random pivot swap before partition OR random shuffle once at start.

5. The expected number of comparisons is very close to merge sort's optimal n log n.

6. Randomized quicksort is in-place, making it memory-efficient compared to merge sort.

7. The algorithm is cache-friendly due to sequential memory access patterns during partitioning.

## Common Mistakes to Avoid

1. **Confusing expected vs average case**: Expected case considers random algorithm choices; average case considers random inputs.

2. **Forgetting to swap random element**: Simply calling a random function isn't enough—you must swap the randomly selected pivot to the designated pivot position before partitioning.

3. **Ignoring space complexity**: The recursion stack can grow to O(n) in worst case; this matters in memory-constrained environments.

4. **Using randomization to hide bugs**: Randomization improves performance but doesn't fix logical errors in the partition or quicksort logic.

## Revision Tips

1. Trace through randomized quicksort by hand with small arrays (n=5-8) using dice or random number generator for pivot selection.

2. Derive the recurrence relation T(n) = T(a·n) + T((1-a)·n) + O(n) and solve it by taking expectation.

3. Memorize the key comparison: standard quicksort on sorted input = n(n+1)/2 comparisons; randomized quicksort on same input ≈ 2n ln n.

4. Practice implementing both Lomuto and Hoare partition schemes with random pivot selection.

5. Review how randomized quicksort demonstrates the power of probability in algorithm design—this concept extends to randomized min-cut, random sampling, and probabilistic data structures.