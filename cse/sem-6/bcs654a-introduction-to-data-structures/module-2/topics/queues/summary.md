# Introduction to Queues

## Overview

A queue is a linear data structure following the First-In-First-Out (FIFO) principle where elements are inserted at the rear and removed from the front. It models real-world waiting lines and is essential for scheduling and buffering applications.

## Key Points

- **FIFO Principle**: First element added is first to be removed, like a waiting line
- **Two-End Operations**: Insertion at rear (enqueue), deletion from front (dequeue)
- **Basic Operations**: Enqueue, Dequeue, Peek/Front, isEmpty, isFull
- **Array Implementation**: Uses front and rear pointers initialized to -1
- **Memory Wastage Problem**: Simple array implementation wastes space as front moves forward
- **Queue Types**: Linear, Circular, Double-ended (Deque), Priority Queue
- **Applications**: CPU scheduling, BFS traversal, disk scheduling, print spooling, buffering

## Important Concepts

- Front pointer tracks first element for removal
- Rear pointer tracks last element for insertion
- Simple array implementation suffers from false overflow when rear reaches end despite available space
- Circular queue solves memory wastage problem
- All basic operations are O(1) time complexity
- Overflow when rear == MAX-1, underflow when front > rear or front == -1

## Notes

- Practice tracing enqueue/dequeue operations showing front and rear movements
- Understand limitation of simple array implementation
- Know applications like BFS and CPU scheduling
- Be able to compare queue (FIFO) with stack (LIFO)
- Remember to check empty/full conditions before operations
