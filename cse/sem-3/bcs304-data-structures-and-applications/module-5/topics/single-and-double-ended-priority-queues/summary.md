# Single And Double Ended Priority Queues - Summary

## Key Definitions

- **Priority Queue**: An abstract data type where each element has an associated priority, and elements with higher (or lower) priority are served before others

- **Single-Ended Priority Queue (SEPQ)**: A priority queue that allows access to only one extremum (either max or min) efficiently

- **Double-Ended Priority Queue (DEPQ)**: A priority queue allowing efficient access to both maximum and minimum elements simultaneously

- **Binary Heap**: A complete binary tree that satisfies the heap property (max-heap: parent ≥ children; min-heap: parent ≤ children)

- **Min-Max Heap**: A specialized heap structure where levels alternate between min-levels and max-levels, enabling O(1) access to both extremes

## Important Formulas

- **Parent index**: parent(i) = ⌊(i-1)/2⌋
- **Left child index**: left(i) = 2i + 1
- **Right child index**: right(i) = 2i + 2
- **Heap height**: h = ⌊log₂n⌋ for n elements
- **Time complexity**: Insert/Delete = O(log n), GetMax/GetMin = O(1)

## Key Points

1. Priority queues serve elements based on priority rather than insertion order, essential for greedy algorithms

2. Binary heaps provide efficient implementation with O(log n) insertion and deletion, O(1) access to extremum

3. Complete binary tree property enables efficient array representation of heaps

4. Min-max heaps achieve DEPQ functionality in a single structure through alternating min/max levels

5. The heap property must be maintained after every insertion (sift-up) and deletion (sift-down) operation

6. DEPQ requires O(1) time for both GetMax and GetMin, with O(log n) for all update operations

7. Interval heaps represent elements as intervals [min, max] in each node, providing another efficient DEPQ implementation

8. Priority queues are fundamental to Dijkstra's algorithm, Prim's algorithm, Huffman coding, and operating system scheduling

9. Two-heap approach (max-heap + min-heap) can simulate DEPQ behavior with O(log n) operation complexity

10. The choice between SEPQ and DEPQ depends on whether the application requires access to one or both extremes

## Common Mistakes

1. Confusing heap property with binary search tree property - heaps do not support search in O(log n)

2. Forgetting that heap is a complete binary tree - insertions always fill level order from left to right

3. Incorrectly computing parent/child indices, especially off-by-one errors in array implementation

4. Assuming heap sort yields stable sort - heap sort is not stable as equal elements may change relative order

5. Not maintaining balance in dual-heap implementation for median maintenance, leading to skewed performance