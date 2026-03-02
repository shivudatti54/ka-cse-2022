# Priority Queues

## What is a Priority Queue?

An abstract data type where each element has a priority. Elements are served based on priority, not arrival order.

## Operations

| Operation                   | Description                    | Heap Time |
| --------------------------- | ------------------------------ | --------- |
| insert(item, priority)      | Add with priority              | O(log n)  |
| extractMax() / extractMin() | Remove highest/lowest priority | O(log n)  |
| peek()                      | View highest/lowest priority   | O(1)      |
| changePriority()            | Update priority                | O(log n)  |

## Implementation Options

| Implementation  | Insert   | Extract    | Peek |
| --------------- | -------- | ---------- | ---- |
| Unsorted Array  | O(1)     | O(n)       | O(n) |
| Sorted Array    | O(n)     | O(1)       | O(1) |
| **Binary Heap** | O(log n) | O(log n)   | O(1) |
| Fibonacci Heap  | O(1)\*   | O(log n)\* | O(1) |

\*Amortized

## Applications

1. **Dijkstra's Algorithm**: Extract minimum distance vertex
2. **Prim's MST**: Extract minimum weight edge
3. **Huffman Coding**: Build frequency-based tree
4. **Job Scheduling**: Process highest priority task
5. **Event Simulation**: Process earliest event
6. **A\* Search**: Best-first pathfinding

## Common Problems

### Top K Elements

```python
import heapq
def top_k(nums, k):
 return heapq.nlargest(k, nums)
```

### Merge K Sorted Lists

```python
def merge_k_lists(lists):
 heap = []
 for i, lst in enumerate(lists):
 if lst:
 heapq.heappush(heap, (lst[0], i, 0))

 result = []
 while heap:
 val, list_idx, elem_idx = heapq.heappop(heap)
 result.append(val)
 if elem_idx + 1 < len(lists[list_idx]):
 heapq.heappush(heap, (lists[list_idx][elem_idx+1], list_idx, elem_idx+1))
 return result
```

### Running Median

Use two heaps: max-heap for lower half, min-heap for upper half.

> **Exam Tip**: Priority queue = heap in most cases. Know when to use min-heap vs max-heap.
