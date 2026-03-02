# QUEUES - Summary

## Key Definitions and Concepts

- **Queue**: A linear data structure that follows the FIFO (First-In-First-Out) principle, where elements added first are removed first

- **Enqueue**: The operation of adding an element to the rear of the queue

- **Dequeue**: The operation of removing and returning the element from the front of the queue

- **Front**: The position from which elements are removed (the oldest element)

- **Rear**: The position where new elements are added (the newest element)

## Important Formulas and Theorems

- **Empty Condition**: `front == -1` OR `front > rear`
- **Full Condition**: `rear == MAXSIZE - 1` (for array implementation)
- **Enqueue Operation**: Increment rear, store element at queue[rear]; set front = 0 if first element
- **Dequeue Operation**: Retrieve element at queue[front], increment front; reset to -1 if front > rear
- **Time Complexity**: All operations O(1) for array implementation

## Key Points

1. Queues maintain strict insertion order—elements are processed in the exact order they arrive

2. Two indices (front and rear) track queue boundaries in array implementation

3. Underflow occurs when dequeue is called on an empty queue; overflow occurs when enqueue is called on a full queue

4. The linear queue implementation has a limitation: after dequeuing elements, space at the beginning cannot be reused, leading to false overflow

5. Queues are essential for breadth-first search (BFS) in graphs and trees

6. Real-world applications include CPU task scheduling, print job management, and customer service systems

7. Unlike stacks (LIFO), queues process elements in chronological order

8. The front index always points to the element that will be dequeued next

## Common Mistakes to Avoid

- Confusing front and rear indices—remember front is for removal, rear is for insertion
- Forgetting to check for underflow before dequeue, which can cause undefined behavior
- Not resetting front and rear to -1 when all elements are dequeued, leading to incorrect empty detection
- Mixing up queue and stack terminology in exam answers
- Failing to increment front when dequeuing, causing the same element to be returned multiple times

## Revision Tips

1. Practice manual tracing of queue operations on paper—write the array state, front, and rear after each operation

2. Memorize the empty and full conditions precisely for the linear queue implementation

3. Understand why circular queues solve the space-wasting problem of linear queues

4. Review BFS algorithm to see queues in action for graph traversal

5. Solve previous year DU exam questions on queues to understand the pattern and difficulty level