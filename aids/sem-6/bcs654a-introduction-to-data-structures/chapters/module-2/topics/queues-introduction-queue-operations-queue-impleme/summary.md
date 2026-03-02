# **Queues: Introduction, Queue Operations, and Implementation**

### Introduction

- A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
- It's a collection of elements that are added to the end of the queue and removed from the front.
- It's also known as a line or a queue of people waiting for something.

### Queue Operations

- **Enqueue (Add)**: Add an element to the end of the queue.
- **Dequeue (Remove)**: Remove an element from the front of the queue.
- **Peek (Front)**: Display the element at the front of the queue without removing it.
- **Is Empty**: Check if the queue is empty.
- **Size**: Get the number of elements in the queue.

### Queue Implementation using Arrays

- **Array Queue**: A queue implemented using an array.
- **Front**: The index of the first element in the queue.
- **Rear**: The index of the last element in the queue.
- **Capacity**: The maximum number of elements the queue can hold.

### Different Types of Queues

#### Circular Queues

- **Circular Buffer**: A queue that uses a circular buffer to store elements.
- **Circular Buffer Implementation**: Circular queues can be implemented using an array and two pointers (front and rear).
- **Operations**: Enqueue, Dequeue, Peek, Is Empty, Size.

#### Double-Ended Queues

- **Deque**: A data structure that can add or remove elements from both ends.
- **Operations**: Add (Enqueue) from front, Remove (Dequeue) from front, Add (Enqueue) from rear, Remove (Dequeue) from rear.
- **Implementation**: A deque can be implemented using two arrays or a single array with two pointers.

#### Priority Queues

- **Priority Queue**: A queue where elements have priority.
- **Operations**: Enqueue, Dequeue, Peek, Is Empty, Size.
- **Implementation**: Priority queues can be implemented using a binary heap or a binary search tree.

### Theorems and Formulas

- **FIFO Theorem**: Last-In-First-Out.
- **LCM (Least Common Multiple) Formula**: Used in circular queue implementation.
- **Priority Queue Theorem**: Elements with higher priority are dequeued first.
