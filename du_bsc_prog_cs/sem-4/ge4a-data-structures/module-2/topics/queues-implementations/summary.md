# Queues: Implementations - Summary

## Key Definitions and Concepts

- **Queue**: A linear data structure following FIFO (First-In-First-Out) principle where elements are added at the rear and removed from the front.
- **Front**: The position from which elements are removed (served first)
- **Rear**: The position where new elements are added (tail of the queue)
- **Circular Queue**: An array-based queue that connects the end of the array to the beginning, utilizing all available space efficiently.
- **Priority Queue**: A queue variant where each element has an associated priority; higher priority elements are dequeued first.

## Important Formulas and Theorems

| Operation | Linear Queue | Circular Queue |
|-----------|--------------|----------------|
| Empty Condition | `front == -1` | `front == -1` |
| Full Condition | `rear == MAXSIZE - 1` | `(rear + 1) % MAXSIZE == front` |
| Enqueue Time | O(1) | O(1) |
| Dequeue Time | O(1) | O(1) |

**Space Complexity**: O(n) where n is the maximum queue size for array-based; O(n) for linked list with n nodes stored.

## Key Points

- Queues follow FIFO: First element inserted is the first element removed.
- Basic operations: enqueue (insert at rear), dequeue (remove from front), front, rear, isEmpty, isFull.
- Linear queues suffer from "phantom overflow" where the queue appears full despite empty slots at the beginning.
- Circular queues solve the space wastage problem using modular arithmetic.
- Linked list implementation provides dynamic sizing but requires extra memory for pointers.
- Queues are essential for BFS traversal, level-order tree traversal, CPU scheduling, and print spooling.
- Priority queues remove elements based on priority rather than arrival order.

## Common Mistakes to Avoid

1. **Forgetting overflow/underflow checks**: Always verify queue state before enqueue or dequeue operations.
2. **Incorrect circular queue conditions**: Using wrong formulas for full/empty states is the most common error.
3. **Not resetting pointers**: After completely emptying a linear queue, remember to reset front and rear to -1.
4. **Confusing front and rear**: Remember that insertion happens at rear, deletion at front.

## Revision Tips

1. **Practice implementing both array and linked list versions** - this is frequently asked in practical exams.
2. **Memorize the circular queue formulas** - the modular arithmetic is crucial for correct implementation.
3. **Draw diagrams** - visualize how front and rear pointers move during enqueue and dequeue operations.
4. **Know real-world applications** - connecting theory to applications (like BFS, printer queues) helps in viva voce.
5. **Compare with stacks** - understanding similarities and differences with stacks reinforces conceptual clarity.