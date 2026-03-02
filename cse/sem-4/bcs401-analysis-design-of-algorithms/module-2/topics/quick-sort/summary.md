# Quick Sort - Summary

## Key Definitions
- **Pivot**: The element selected from the array around which other elements are partitioned during Quick Sort
- **Partition**: The process of rearranging elements so that elements less than the pivot appear before it, and elements greater than it appear after
- **Divide and Conquer**: Algorithm design paradigm that breaks a problem into subproblems, conquers them recursively, and combines solutions
- **In-place Sorting**: Sorting algorithm that uses O(1) auxiliary space beyond the input array
- **Stable Sorting**: Property ensuring equal elements maintain their relative order after sorting

## Important Formulas
- **Worst-case time complexity**: T(n) = T(n-1) + Θ(n) = Θ(n²)
- **Average-case time complexity**: T(n) = 2T(n/2) + Θ(n) = Θ(n log n)
- **Best-case time complexity**: T(n) = 2T(n/2) + Θ(n) = Θ(n log n)
- **Space complexity**: O(log n) average, O(n) worst case (recursion stack)
- **Pivot position (Lomuto)**: Returns index where pivot is placed after partition

## Key Points
- Quick Sort is a divide-and-conquer algorithm, not a brute force technique
- Partition efficiency determines overall performance; balanced partitions yield O(n log n)
- Lomuto scheme selects last element as pivot, simpler but degrades on sorted input
- Hoare scheme uses two pointers, more efficient but requires careful edge case handling
- Pivot selection strategies (random, median-of-three) prevent worst-case O(n²) behavior
- Randomized Quick Sort provides expected O(n log n) regardless of input arrangement
- Quick Sort is unstable but in-place, making it space-efficient
- Excellent cache performance due to sequential memory access patterns
- Merge Sort is preferred when stability is required; Quick Sort for in-place efficiency
- Introsort combines Quick Sort with Heap Sort to guarantee O(n log n) worst case

## Common Mistakes
- Confusing Quick Sort with brute force algorithms—it is fundamentally divide-and-conquer
- Using first/last element as pivot on sorted input leads to O(n²) performance
- Forgetting that Quick Sort is unstable and may change relative order of equal elements
- Not accounting for recursion stack space in space complexity analysis
- Implementing partition incorrectly and leaving elements on wrong side of pivot
- Applying Quick Sort to linked lists (better suited for Merge Sort due to random access requirements)
- Ignoring tail recursion optimization, causing stack overflow on large inputs