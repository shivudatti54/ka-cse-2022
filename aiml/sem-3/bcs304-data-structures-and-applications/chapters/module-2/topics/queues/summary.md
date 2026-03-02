# QUEUES - Summary

## Key Definitions and Concepts

- **Queue**: A linear data structure that follows FIFO (First In, First Out) principle where elements are added at the REAR and removed from the FRONT.
- **Front**: The position from which elements are removed (first element in queue)
- **Rear**: The position at which elements are added (last element in queue)
- **Enqueue**: Operation to insert an element at the rear of the queue
- **Dequeue**: Operation to remove an element from the front of the queue
- **Overflow**: Condition when queue is full and no more elements can be added
- **Underflow**: Condition when queue is empty and no elements can be removed

## Important Formulas and Theorems

- **Queue Capacity**: For array implementation with MAXSIZE elements, valid indices are 0 to MAXSIZE-1
- **Queue Full Condition**: rear = MAXSIZE - 1
- **Queue Empty Condition**: front = -1 OR front > rear
- **Time Complexity**: All operations (enqueue, dequeue, front) execute in O(1) time
- **Space Complexity**: O(n) where n is the number of elements stored

## Key Points

- Queues maintain strict FIFO ordering: element added first is removed first
- Array implementation uses two pointers: front and rear, initialized to -1
- Linked implementation uses two pointers pointing to head and tail nodes
- front always points to the element to be removed next
- rear always points to where the next element will be inserted
- After dequeue, if front exceeds rear, reset both pointers to -1
- Linked implementation allows dynamic size without capacity restrictions
- Queue is essential for BFS algorithm, CPU scheduling, and request handling

## Common Mistakes to Avoid

- Confusing queue with stack (remember: queue = FIFO, stack = LIFO)
- Forgetting to initialize front and rear to -1 at the start
- Not checking for overflow before enqueue operation
- Not checking for underflow before dequeue operation
- Failing to reset queue state when all elements are dequeued

## Revision Tips

1. Practice tracing queue operations step-by-step with sample sequences
2. Memorize the initial conditions (front = -1, rear = -1) and state conditions
3. Draw diagrams for array and linked implementations to visualize changes
4. Focus on the difference between array and linked implementations
5. Review BFS algorithm to understand practical queue application