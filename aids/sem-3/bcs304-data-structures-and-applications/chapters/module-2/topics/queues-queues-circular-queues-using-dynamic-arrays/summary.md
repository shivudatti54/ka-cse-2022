### Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues

#### Key Points

- **Queue Definition**:
  - A linear data structure that follows the FIFO (First-In-First-Out) principle.
  - Elements are added to the end and removed from the front.
  - Queues are used in job scheduling, print queues, and messaging systems.
- **Queue Operations**:
  - Enqueue (add element to the end)
  - Dequeue (remove element from the front)
  - Peek (look at the front element without removing it)
  - Empty (check if the queue is empty)
- **Circular Queue**:
  - A type of queue that uses a circular buffer to store elements.
  - Elements are added to the end and removed from the front, wrapping around to the beginning when the end is reached.
  - Circular queues are used in printer queues and network buffers.
- **Dynamic Array Queue**:
  - A queue implemented using dynamic arrays.
  - Elements are added to the end and removed from the front using shifting and resizing techniques.
  - Dynamic array queues are used in many programming languages.
- **Multiple Stacks and Queues**:
  - A data structure that combines multiple queues and stacks.
  - Stacks are used to store elements to be dequeued, while queues are used to store the actual elements.
  - Multiple stacks and queues are used in compiler design and parsing algorithms.
- **Important Formulas and Definitions**:
  - FIFO (First-In-First-Out) principle
  - LIFO (Last-In-First-Out) principle
  - Queue capacity
  - Queue size
- **Theorems**:
  - FIFO principle guarantees that the first element to be added to the queue will be the first to be removed.
  - Circular queues can be implemented using arrays or linked lists.

#### Formulas and Definitions

| Formula/Definition      | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| `Q = {q1, q2, ..., qn}` | A queue represented as a set of elements.                       |
| `ENQUEUE(q, x)`         | Add element `x` to the end of queue `q`.                        |
| `DEQUEUE(q)`            | Remove the front element from queue `q`.                        |
| `PEEK(q)`               | Look at the front element of queue `q` without removing it.     |
| `EMPTY(q)`              | Check if queue `q` is empty.                                    |
| `CAPACITY(q)`           | The maximum number of elements that can be stored in queue `q`. |
| `SIZE(q)`               | The number of elements currently stored in queue `q`.           |
