# Multiple Stacks and Queues - Summary

## Key Definitions and Concepts

- **Two Stacks in One Array**: Implementation technique where two stacks grow from opposite ends of a shared array, with Stack 1 growing from left (index 0) and Stack 2 from right (index n-1).

- **Circular Queue**: A queue implemented in circular fashion using modulo arithmetic, allowing wrap-around and 100% space utilization.

- **Deque (Double-Ended Queue)**: A linear data structure allowing insertion and deletion at both front and rear ends.

- **Priority Queue**: A queue where each element has an associated priority; elements with higher priority are dequeued first regardless of insertion order.

## Important Formulas and Theorems

- **Two Stacks Overflow Condition**: `top1 + 1 == top2`
- **Circular Queue Enqueue**: `rear = (rear + 1) % MAX_SIZE`
- **Circular Queue Dequeue**: `front = (front + 1) % MAX_SIZE`
- **Circular Queue Full Condition**: `(rear + 1) % MAX_SIZE == front`
- **Circular Queue Empty Condition**: `front == -1` or `front == (rear + 1) % MAX_SIZE`

## Key Points

- Two stacks in one array maximize space utilization by growing from opposite ends
- Circular queue solves the problem of space wastage in linear queues
- A circular queue of size n can hold maximum n-1 elements to distinguish full from empty
- Deque supports four operations: insertFront, insertRear, deleteFront, deleteRear
- Input-restricted deque allows deletion from both ends but insertion at only one end
- Output-restricted deque allows insertion at both ends but deletion from only one end
- Priority queues can be implemented using arrays, linked lists, heaps, or BSTs
- Binary heap implementation provides O(log n) complexity for both insert and delete operations

## Common Mistakes to Avoid

- Forgetting that circular queue array size should be one more than maximum expected elements
- Confusing the overflow condition (checking before push) with underflow condition (checking before pop)
- Not initializing front and rear pointers correctly in circular queue implementation
- Assuming priority queues follow strict FIFO order - they follow priority order instead

## Revision Tips

- Practice writing the overflow and underflow conditions for both stacks and queues
- Remember the key advantage of circular queue: space efficiency through wrap-around
- Understand when to use each type: stacks for LIFO, queues for FIFO, priority queues for priority-based processing
- Review time complexities: Array-based priority queue has O(n) deletion, heap-based has O(log n)
