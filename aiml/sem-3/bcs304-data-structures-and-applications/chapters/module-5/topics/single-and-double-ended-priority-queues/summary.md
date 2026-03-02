# Single and Double Ended Priority Queues - Summary

## Key Definitions and Concepts

- **Priority Queue**: An abstract data type where each element has an associated priority, and elements with higher priority are dequeued before those with lower priority.

- **Single-Ended Priority Queue (SEPQ)**: Supports operations at only one end - either min-priority queue (get/delete minimum) or max-priority queue (get/delete maximum).

- **Double-Ended Priority Queue (DEPQ)**: Extends SEPQ to support both minimum and maximum operations efficiently on the same data structure.

- **Heap**: A complete binary tree that satisfies the heap property (min-heap or max-heap), commonly used to implement priority queues.

## Important Formulas and Theorems

- **Parent Index**: floor(i/2) for element at index i
- **Left Child**: 2i for element at index i
- **Right Child**: 2i + 1 for element at index i
- **Heap Build Time**: O(n) using bottom-up approach
- **Heap Sort**: O(n log n) time complexity in all cases

## Key Points

1. Binary heaps provide O(log n) INSERT and DELETE operations, O(1) GET-MIN/MAX, and O(n) space.

2. Min-priority queues extract smallest element first; max-priority queues extract largest element first.

3. DEPQ supports GET-MIN, GET-MAX, DELETE-MIN, DELETE-MAX, INSERT, SIZE, and IS-EMPTY operations.

4. Dual heap implementation uses two heaps (min-heap and max-heap) with correspondence pointers for efficient DEPQ.

5. Interval heap is a specialized structure where each node contains two elements forming an interval [min, max].

6. Heapify can be performed bottom-up in O(n) time or top-down during insertions in O(n log n) time.

7. Balanced BST can also implement priority queues with O(log n) operations plus sorted order traversal.

8. Priority queues are fundamental in Dijkstra's algorithm, Prim's algorithm, and CPU job scheduling.

## Common Mistakes to Avoid

1. Confusing min-heap and max-heap properties - remember min-heap stores minimum at root, max-heap stores maximum at root.

2. Forgetting that heap index starts at 1 in array representation, not 0, when calculating child/parent indices.

3. Assuming heap sort is stable - it is NOT a stable sorting algorithm.

4. Using the wrong heapify direction - sift-down for building heap, sift-up for inserting elements.

## Revision Tips

1. Practice drawing heap structures after each insert and delete operation to understand the sift-up and sift-down processes.

2. Memorize the time complexities: O(log n) for insert/delete, O(1) for get, O(n) for building heap.

3. Review the relationship between complete binary tree properties and array representation of heaps.

4. Understand when to use SEPQ versus DEPQ based on application requirements.