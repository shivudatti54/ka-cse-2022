# **QUEUES: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

### Introduction

---

- A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle.
- It is a collection of elements that are added and removed from one end, known as the "back" of the queue.

### Key Concepts

---

#### Queues

- Definition: A linear data structure that follows the FIFO principle.
- Operations:
  - Enqueue: add an element to the back of the queue
  - Dequeue: remove an element from the front of the queue
  - Peek: look at the front element without removing it

#### Circular Queues

- Definition: A type of queue that uses a circular array to store elements.
- Operations:
  - Enqueue: add an element to the back of the queue
  - Dequeue: remove an element from the front of the queue
  - Peek: look at the front element without removing it
  - IsEmpty: check if the queue is empty

#### Dynamic Arrays

- Definition: A data structure that can resize itself automatically.
- Operations:
  - Enqueue: add an element to the end of the array
  - Dequeue: remove an element from the beginning of the array
  - Resize: increase or decrease the size of the array

#### Multiple Stacks and Queues

- Definition: A data structure that combines two or more stacks and queues.
- Operations:
  - Push: add an element to the top of a stack
  - Pop: remove an element from the top of a stack
  - Enqueue: add an element to the back of the queue
  - Dequeue: remove an element from the front of the queue

### Formulas and Definitions

---

#### Queue Formulas

- `Q = [q0, q1, ..., qn]` (queue notation)
- `Q[i] = q0 + i` (accessing an element in the queue)

#### Circular Queue Formulas

- `CQ = [c0, c1, ..., cn]` (circular queue notation)
- `CQ[i] = c0 + i mod n` (accessing an element in the circular queue)

### Important Theorems

---

#### FIFO Theorem

- If `Q` is a queue, then `Q[i] = q0 + i` for some integer `i`.

Note: This summary is a concise revision guide and is not intended to be a comprehensive textbook.
