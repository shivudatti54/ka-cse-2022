# Insertion Sort, Selection Sort, and Bubble Sort - Summary

## Key Definitions and Concepts

- **Sorting:** The process of arranging elements in a specified order (ascending or descending)
- **In-place Sorting:** Sorting algorithms that use only O(1) extra space
- **Stable Sorting:** When equal elements maintain their relative original positions after sorting
- **Adaptive Sorting:** Algorithms that run faster when input is already substantially sorted

## Important Formulas and Theorems

| Algorithm | Best Case | Worst Case | Average Case | Space |
|-----------|-----------|------------|--------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

## Key Points

- All three algorithms are comparison-based sorts with O(n²) worst-case complexity
- Bubble Sort repeatedly swaps adjacent elements if in wrong order; largest elements "bubble" to end
- Selection Sort finds minimum element in unsorted portion and places it at the beginning; exactly (n-1) swaps
- Insertion Sort builds sorted array one element at a time; efficient for nearly sorted data (adaptive)
- All three algorithms have O(1) space complexity (in-place sorting)
- Bubble Sort and Insertion Sort are stable; Selection Sort is unstable
- Selection Sort always performs O(n²) comparisons regardless of initial order
- Insertion Sort is practical for small datasets and nearly sorted arrays

## Common Mistakes to Avoid

1. **Confusing best-case complexity:** Many students incorrectly state selection sort has O(n) best case—it is O(n²) in all cases
2. **Forgetting the early termination:** Bubble sort can terminate early if no swaps occur, giving O(n) best case
3. **Mixing up stability:** Selection sort is often mistakenly considered stable; it is unstable
4. **Incorrect loop boundaries:** Common off-by-one errors in implementing nested loops, especially in bubble sort's inner loop

## Revision Tips

1. Practice tracing algorithms by hand with 5-6 element arrays until you can do it without errors
2. Create a comparison table and memorize the complexities—this appears in almost every exam
3. Understand WHY each algorithm works conceptually, not just memorize steps
4. Remember: for nearly sorted data, insertion sort outperforms the other two significantly
5. Focus on the number of swaps: selection sort has minimum swaps (n-1), bubble sort can have many