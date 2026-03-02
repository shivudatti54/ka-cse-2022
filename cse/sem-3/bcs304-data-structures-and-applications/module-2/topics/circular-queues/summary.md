# Circular Queues

=====================================

## Overview

A Circular Queue is a linear data structure following FIFO principle, connecting the first and last array positions to form a circle. It solves the memory wastage problem of linear queues by reusing empty spaces created after dequeuing. All operations (enqueue, dequeue, isEmpty, isFull) execute in O(1) time using modular arithmetic.

## Key Points

- Uses array with two pointers: `front` and `rear`; initial state: both = -1
- Circular increment formula: `(index + 1) % capacity` — wraps pointer from last to first index
- **Sacrifices one slot** — can store only (N-1) elements in queue of capacity N
- First enqueue: sets both front and rear to 0; single element dequeue: resets both to -1
- Enqueue: check full → circular increment rear → insert at array[rear]
- Dequeue: store array[front] → circular increment front → return stored value

## Important Concepts

- **Front (Head)**: Index of next element to dequeue; -1 when empty
- **Rear (Tail)**: Index where next element will be enqueued; -1 when empty
- **Wrap-around**: Pointer moving from last index back to index 0 using modulo
- **isEmpty**: `front == -1 && rear == -1`
- **isFull**: `(rear + 1) % capacity == front`
- **Circular Increment**: `(current + 1) % MAXSIZE` for updating pointers

## Notes

- exam questions frequently ask: trace operations, find front/rear values after sequences
- Always draw array diagrams when solving operation sequences to avoid wrap-around errors
- Key advantage over linear queue: O(1) dequeue without element shifting
- Applications: CPU scheduling (Round Robin), buffering, traffic signals, printer spooling
