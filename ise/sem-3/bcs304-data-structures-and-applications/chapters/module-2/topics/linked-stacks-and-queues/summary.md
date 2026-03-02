# Linked Stacks and Queues - Summary

## Key Definitions and Concepts

- **Linked Stack**: A stack implementation using dynamically allocated nodes where all operations (push/pop) occur at a single point called the top, maintaining LIFO order.

- **Linked Queue**: A queue implementation using dynamically allocated nodes with two pointers (front and rear) where insertions happen at rear and deletions at front, maintaining FIFO order.

- **Node**: The fundamental building block of linked structures containing a data field and a pointer field to the next node.

- **Top Pointer**: In linked stacks, a pointer variable referencing the most recently inserted element.

- **Front/Rear Pointers**: In linked queues, pointers to the deletion and insertion ends respectively.

## Important Formulas and Theorems

- **Time Complexity**: All fundamental operations (push, pop, enqueue, dequeue) execute in O(1) constant time regardless of the number of elements.

- **Space Complexity**: O(n) for n elements, with each node requiring data space plus pointer overhead (typically 4-8 bytes per pointer).

- **Memory Allocation**: Each push/enqueue requires one malloc call; each pop/dequeue requires one free call.

## Key Points

- Linked implementations provide dynamic sizing, eliminating the fixed-capacity limitations of array-based approaches.

- The linked stack requires only one pointer (top), while the linked queue requires two pointers (front and rear).

- Proper pointer manipulation is critical: always update the next pointer BEFORE updating the main structural pointer.

- Stack underflow occurs when attempting to pop from an empty stack; queue underflow occurs when attempting to dequeue from an empty queue.

- Linked implementations can theoretically overflow when system memory is exhausted, though this is rare in practice.

- Every malloc must have a corresponding free to prevent memory leaks.

- When the last element is dequeued from a linked queue, both front and rear must be set to NULL.

- Linked structures enable efficient insertion and deletion without element shifting, unlike array implementations.

## Common Mistakes to Avoid

- Forgetting to set the new node's next pointer before updating top/rear, losing access to the remaining list.

- Not checking for NULL after malloc, which can cause segmentation faults when memory allocation fails.

- Attempting to pop or dequeue from an empty structure without proper underflow checking.

- Creating memory leaks by forgetting to free nodes during deletion operations.

- Confusing front and rear roles in queues or using them inconsistently.

## Revision Tips

- Practice drawing node diagrams for each operation to understand pointer changes visually.

- Memorize the exact sequence of steps for push, pop, enqueue, and dequeue operations.

- Write complete implementation code from scratch multiple times to build muscle memory.

- Create comparison tables between array and linked implementations for quick review.

- Solve previous year examination questions focusing on operation tracing and complexity analysis.