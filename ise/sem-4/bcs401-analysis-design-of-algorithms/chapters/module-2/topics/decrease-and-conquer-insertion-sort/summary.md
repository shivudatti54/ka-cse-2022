# DECREASE-AND-CONQUER: Insertion Sort

### Overview

- Insertion Sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region.
- It iterates through the unsorted region, inserting each element into its proper position within the sorted region.

### Key Points

- **Time Complexity:**
  - Best-case: O(n) (already sorted)
  - Average-case: O(n^2)
  - Worst-case: O(n^2)
- **Space Complexity:** O(1) (in-place sorting)
- **Stability:** Yes (preserves order of equal elements)

### Insertion Sort Algorithm

1. Initialize the sorted region (current smallest element is at the beginning)
2. Iterate through the unsorted region
3. Compare each element with the current smallest element in the sorted region
4. Shift elements in the sorted region to make room for the current element
5. Insert the current element into its proper position in the sorted region

### Important Formulas and Definitions

- **Big O notation:** a measure of an algorithm's efficiency
- **Time complexity:** the amount of time an algorithm takes to complete as a function of the size of the input
- **Space complexity:** the amount of memory an algorithm uses as a function of the size of the input

### Theorem

- **Insertion Sort Principle:** If the input is partially sorted, Insertion Sort has a better time complexity than other sorting algorithms.

### Revision Tips

- Focus on understanding the algorithm's purpose and behavior
- Review the time and space complexities
- Practice implementing the algorithm to reinforce your understanding
