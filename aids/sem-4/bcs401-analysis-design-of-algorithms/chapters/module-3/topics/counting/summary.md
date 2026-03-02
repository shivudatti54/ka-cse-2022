# Counting Sort - Summary

## Key Definitions and Concepts

- **Counting Sort**: A non-comparison based sorting algorithm that sorts elements by counting occurrences of each distinct value and using that information to place elements in sorted order.
- **Stable Sort**: A sorting algorithm that preserves the relative order of equal elements in the input and output.
- **Distribution-based Sort**: Sorting algorithms that distribute elements into buckets or counts rather than comparing elements directly.
- **Auxiliary Array**: Additional memory (counting array) used by the algorithm beyond the input and output arrays.

## Important Formulas and Theorems

- **Time Complexity**: T(n) = O(n + k) where n = number of elements, k = range of input values
- **Space Complexity**: S(n) = O(n + k) for the counting array and output array
- **Linear Time Condition**: When k = O(n), Counting Sort runs in O(n) time
- **Lower Bound Bypass**: Comparison-based sorts have Ω(n log n) lower bound; Counting Sort bypasses this by not using comparisons

## Key Points

- Counting Sort works only with integers or values that can be mapped to non-negative integers within a bounded range
- The algorithm uses three passes: counting frequencies, computing cumulative counts, and placing elements in output
- Processing input from right to left ensures stability, preserving relative order of equal elements
- When k is significantly larger than n, the algorithm becomes impractical due to high space requirements
- Counting Sort is often used as the inner algorithm in Radix Sort for sorting multi-digit integers
- The algorithm is not in-place as it requires auxiliary arrays proportional to input size plus range

## Common Mistakes to Avoid

- Forgetting to initialize the counting array with zeros before counting
- Using forward iteration instead of reverse iteration when placing elements, which breaks stability
- Failing to find the maximum value to determine the range k
- Confusing the cumulative count step — it must accumulate, not just copy counts
- Assuming Counting Sort works directly on floating-point numbers without transformation

## Revision Tips

- Trace through the algorithm step-by-step with a small example to reinforce understanding
- Memorize the three main steps: Count → Cumulative → Place
- Remember that "reverse iteration" is key to stability
- Practice time complexity analysis for different values of k relative to n
- Review the comparison between Counting Sort and comparison-based sorts for exam questions