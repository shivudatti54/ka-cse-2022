# Queue Operations

## Overview

Queue operations implement the FIFO principle with enqueue adding elements at rear and dequeue removing from front. These operations maintain the first-in-first-out ordering essential for scheduling and buffering applications.

## Key Points

- **Enqueue Operation**: Increments rear pointer and inserts element at queue[rear] position
- **Dequeue Operation**: Retrieves element at front position and increments front pointer
- **Front/Peek Operation**: Returns element at front without removing it
- **isEmpty Check**: Verifies if front == -1 or front > rear
- **isFull Check**: Verifies if rear == MAX-1 in array implementation
- **Initialization**: Both front and rear set to -1 for empty queue
- **Special Case**: First enqueue sets front to 0 if queue was empty

## Important Concepts

- Enqueue at rear maintains insertion order
- Dequeue from front maintains FIFO property
- Front pointer advances forward with each dequeue
- When front > rear, queue becomes logically empty
- Reset front and rear to -1 after last dequeue
- All operations execute in O(1) constant time

## Notes

- Draw diagrams showing front and rear pointer movements
- Understand special case when enqueueing to empty queue
- Practice implementing error checking before operations
- Know the sequence: check condition, update pointer, perform operation
- Remember simple implementation limitation with false overflow
