# Queues

## Overview

A queue is a linear data structure that follows the **First-In-First-Out (FIFO)** principle, meaning the first element added is the first one removed. Elements are inserted at the rear and removed from the front. Queues are essential in computer science for managing tasks, scheduling resources, and implementing breadth-first search algorithms.

## Key Points

- **FIFO Principle**: First element inserted is first to be removed—no exceptions
- **Two Ends**: Rear for insertion (enqueue), front for deletion (dequeue)
- **Operations**: enqueue, dequeue, peek, isEmpty, isFull
- **Time Complexity**: O(1) for all basic operations
- **Array Issue**: Linear queue suffers memory wastage—front advances but cannot reuse empty slots
- **Types**: Linear, Circular (solves wastage), Deque (double-ended), Priority (priority-based)

## Important Concepts

- **Overflow**: Error when attempting to add to a full queue (rear == MAX-1)
- **Underflow**: Error when attempting to remove from an empty queue (front > rear)
- **Peek**: Returns front element without removing it
- **Circular Queue**: Rear wraps around to beginning, reusing empty slots
- **Deque**: Insertion/deletion allowed at both front and rear
- **Priority Queue**: Higher priority elements dequeued first, regardless of insertion order

## Notes

- **Exam Tip**: Practice tracing operation sequences—draw array state after each enqueue/dequeue
- **Memory Wastage**: In linear queue, after several dequeues, rear reaches end even with empty slots at front
- **Applications**: CPU scheduling, BFS, print spooling, disk scheduling, buffer management
- **Stack vs Queue**: Stack is LIFO (push/pop at top), Queue is FIFO (enqueue at rear, dequeue at front)
