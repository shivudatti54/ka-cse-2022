# Circular Queues

## Overview

A circular queue is an improved queue implementation that connects the rear to the front logically, forming a circular structure. This eliminates the memory wastage problem of linear queues by allowing reuse of freed space.

## Key Points

- **Circular Connection**: When rear reaches end, it wraps around to beginning if space available
- **Modulo Arithmetic**: Uses (rear + 1) % MAX and (front + 1) % MAX for circular indexing
- **Full Condition**: (rear + 1) % MAX == front indicates queue is full
- **Empty Condition**: front == -1 or front == rear after dequeue
- **Memory Efficiency**: Reuses freed space, eliminating false overflow problem
- **Enqueue**: rear = (rear + 1) % MAX, then insert element
- **Dequeue**: Retrieve element, then front = (front + 1) % MAX

## Important Concepts

- Rear can be less than front in circular arrangement
- One position always remains empty to distinguish full from empty
- Initialization sets both front and rear to -1
- Wrapping implemented using modulo operator
- Solves linear queue's memory wastage issue
- All operations remain O(1) time complexity

## Notes

- Practice calculating indices using modulo arithmetic
- Draw circular diagrams showing wraparound behavior
- Understand why one position must remain unused
- Be able to identify full vs empty conditions
- Know how circular queue improves upon linear queue
