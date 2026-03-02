# Queues: Introduction, Queue Operations, Queue Implementation using Arrays, Different Types of Queues

### Introduction

- A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle.
- It is a collection of elements, known as queue elements or queue items, that are ordered in a particular way.
- The queue is often referred to as a "line" or "queue" in everyday language.
- Elements are added to the end of the queue, and elements are removed from the front of the queue.

### Queue Operations

- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove an element from the front of the queue.
- **Peek**: Look at the element at the front of the queue without removing it.
- **IsEmpty**: Check if the queue is empty.
- **IsFull**: Check if the queue is full.

### Queue Implementation using Arrays

- **Array-Based Queue**: Implemented using an array.
- **Front**: The index of the front element.
- **Rear**: The index of the rear element.
- **Capacity**: The maximum number of elements the queue can hold.

### Different Types of Queues

#### Circular Queues

- A circular queue is a type of queue where the last element is connected to the first element.
- The queue is "circular" because the last element is considered to be at the front of the queue.
- **Circular Queue Formula**: `T = (Q + 1) / 2`
- **Circular Queue Theorem**: The time complexity of enqueue and dequeue operations in a circular queue is O(1).

#### Double-Ended Queues

- A double-ended queue is a type of queue where elements can be added or removed from both ends.
- It is also known as a deque.
- **Deque Formula**: `T = 2Q`
- **Deque Theorem**: The time complexity of enqueue and dequeue operations in a deque is O(1).

#### Priority Queues

- A priority queue is a type of queue where elements are ordered based on their priority.
- Elements with higher priority are dequeued before elements with lower priority.
- **Priority Queue Formula**: `T = (Q + 1) logQ`
- **Priority Queue Theorem**: The time complexity of dequeue operation in a priority queue is O(log Q).

## Important Formulas, Definitions, and Theorems

- **FIFO Principle**: Elements are dequeued in the order they were enqueued.
- **Capacity**: The maximum number of elements the queue can hold.
- **Front**: The index of the front element.
- **Rear**: The index of the rear element.
- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove an element from the front of the queue.
