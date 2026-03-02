# Priority Queues

## Overview

A priority queue is an abstract data type where each element has an associated priority value. Unlike regular FIFO queues, elements are dequeued based on priority rather than insertion order. The element with highest (or lowest) priority is served first, making it essential for Dijkstra's algorithm, CPU scheduling, and Huffman coding.

## Key Points

- Two types: Ascending (Min-PQ) — smallest priority served first; Descending (Max-PQ) — largest priority served first.
- Core operations: `insert(element, priority)`, `deleteMin()/deleteMax()`, `peek()`, `isEmpty()`, `size()`.
- Implementation choice depends on insert vs delete frequency: unsorted for more inserts, sorted for more deletes.
- Sorted array trick: For min-PQ, store in descending priority order so deleteMin is O(1) from end.
- Binary heap is optimal: O(log n) for both insert and delete, O(1) peek, O(n) build time.

## Important Concepts

- **Priority Queue**: ADT where each element has a priority; highest-priority element removed first regardless of insertion order.
- **Min-Priority Queue (Ascending)**: Element with smallest priority value is dequeued first — used in Dijkstra's, Prim's, Huffman.
- **Max-Priority Queue (Descending)**: Element with largest priority value is dequeued first — used in CPU scheduling, emergency systems.
- **Heap**: Binary tree-based implementation providing O(log n) for both insert and delete — standard practical implementation.

## Comparisons

| Implementation     | Insert   | DeleteMin/Max | Peek |
| ------------------ | -------- | ------------- | ---- |
| Unsorted Array     | O(1)     | O(n)          | O(n) |
| Sorted Array       | O(n)     | O(1)          | O(1) |
| Sorted Linked List | O(n)     | O(1)          | O(1) |
| Binary Heap        | O(log n) | O(log n)      | O(1) |

## Notes

- Remember: Min-PQ uses deleteMin() — removes smallest value; Max-PQ uses deleteMax() — removes largest value.
- For exam code questions: Sorted linked list insert traverses to find position, deleteMin removes from head (O(1)).
- Applications to memorize: Dijkstra's (min-distance first), Huffman coding (combine smallest frequencies), CPU scheduling (highest priority first).
- Key difference from regular queue: FIFO vs priority-based ordering.
