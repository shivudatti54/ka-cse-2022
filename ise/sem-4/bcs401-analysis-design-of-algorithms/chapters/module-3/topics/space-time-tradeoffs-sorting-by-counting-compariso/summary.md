# **Space-Time Tradeoffs: Sorting by Counting: Comparison Counting Sort**

### Key Points

- **Comparison Counting Sort**: A sorting algorithm that sorts elements by counting the number of comparisons required to sort an array.
- **Time Complexity**: O(n + k), where n is the number of elements and k is the range of input values.
- **Space Complexity**: O(n + k), as it requires auxiliary arrays to store counts and sorted elements.
- **Stability**: Stable sorting algorithm.
- **Best Case**: O(n + k) time complexity, when all elements have the same value.
- **Worst Case**: O(n log k) time complexity, when elements are sorted in reverse order.
- **Average Case**: O(n log k) time complexity.

### Important Formulas and Definitions

- **Counting Sort Formula**: `count[i] = 0` for `i = 0` to `k-1`, `count[j] += 1` for `j = 0` to `n-1` where `arr[j] == i`, `arr[k-1] = 0`
- **Sorted Array Formula**: `for (i = 1 to k-1) { if (count[i - 1] == 0) arr[k-1] = i; for (j = k-1 to i-1) { count[j]--; if (count[j] == 0) arr[j] = i; } }`
- **Comparison Counting Sort Theorem**: "The time complexity of comparison counting sort is O(n + k), where n is the number of elements and k is the range of input values."

### Theorems

- **Comparison Counting Sort Theorem**: "If the range of input values (k) is less than or equal to n, then comparison counting sort has a time complexity of O(n + k)".
- **Space Complexity Theorem**: "The space complexity of comparison counting sort is O(n + k), where n is the number of elements and k is the range of input values".

### Quick Revision Points

- Compare counting sort is a stable sorting algorithm.
- Time complexity is O(n + k) in the best case, O(n log k) in the worst case, and O(n log k) in the average case.
- Space complexity is O(n + k).
- Comparison counting sort is suitable for sorting integers within a fixed range.
