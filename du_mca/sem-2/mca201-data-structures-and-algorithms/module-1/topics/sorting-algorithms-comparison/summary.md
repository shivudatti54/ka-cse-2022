# Sorting Algorithms Comparison - Summary

## Key Definitions and Concepts

- **Sorting**: Arranging elements in a specific order (ascending/descending)
- **Stable Sort**: Preserves relative order of equal elements
- **In-place Sort**: Uses only O(1) auxiliary space
- **Divide and Conquer**: Algorithm design paradigm breaking problems into smaller subproblems
- **Natural Runs**: Pre-sorted sequences in data exploited by TimSort

## Important Formulas and Theorems

- **Lower Bound**: Comparison-based sorting cannot exceed O(n log n) worst-case
- **Master Theorem**: T(n) = 2T(n/2) + O(n) solves to O(n log n) for Merge Sort
- **Quick Sort Recurrence**: Average case T(n) = T(n/9) + T(9n/10) + O(n) = O(n log n)

## Key Points

1. **Time Complexities**: Merge Sort, Quick Sort, and Heap Sort all achieve O(n log n) average case; Bubble, Selection, and Insertion sorts are O(n²).

2. **Stability Matrix**: Stable algorithms are Bubble Sort, Insertion Sort, and Merge Sort; unstable are Selection Sort, Quick Sort, and Heap Sort.

3. **Space Requirements**: Merge Sort needs O(n) auxiliary space; all others are in-place with O(1) stack space.

4. **Best Case Champions**: Insertion Sort and Bubble Sort achieve O(n) on nearly sorted data; other algorithms maintain O(n log n).

5. **Algorithm Selection**: Quick Sort for general-purpose, Merge Sort for stability and linked lists, Heap Sort for guaranteed performance, Insertion Sort for small/nearly sorted data.

6. **Quick Sort Weakness**: Worst-case O(n²) occurs with poor pivot selection (sorted input with first/last element as pivot).

7. **Hybrid Algorithms**: Modern languages use TimSort (Python), Dual-Pivot Quick Sort (Java), and Introsort (C++).

## Common Mistakes to Avoid

1. Confusing average case with worst case—Quick Sort's O(n²) worst-case is often overlooked
2. Assuming stability is always desirable—sometimes stability has performance costs
3. Forgetting that non-comparison sorts (Counting, Radix) can achieve O(n) but with constraints
4. Overlooking auxiliary space requirements in Merge Sort for memory-constrained systems

## Revision Tips

1. Practice tracing sorting algorithms by hand with 5-6 element arrays
2. Create a comparison table and memorize time/space/stability for each algorithm
3. Understand why O(n log n) is the mathematical lower bound for comparison sorts
4. Focus on Quick Sort partition process and Merge Sort merge step—these are frequently examined
5. Review the recurrence relations and practice solving them using the Master Theorem