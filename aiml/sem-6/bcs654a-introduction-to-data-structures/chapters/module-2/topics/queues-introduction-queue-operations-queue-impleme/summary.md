# **Queues: Introduction, Queue Operations, Queue Implementation using Arrays, Different Types of Queues**

### Introduction

- **Definition:** A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle, where elements are added at the end and removed from the front.
- **Applicability:** Queues are used in various applications, such as job scheduling, print queues, and online shopping.

### Queue Operations

- **Insertion (Enqueue):** Adding an element to the end of the queue.
- **Deletion (Dequeue):** Removing an element from the front of the queue.
- **Peek (Front):** Viewing the front element of the queue without removing it.
- **Is Empty:** Checking if the queue is empty.

### Queue Implementation using Arrays

- **Circular Queue:** Implementing a queue using an array with a circular pointer to prevent overflow.
- **Double-Ended Queue:** Implementing a queue that supports both insertion and deletion from both ends.

### Different Types of Queues

#### Circular Queues

- **Definition:** A circular queue is a type of queue where the last element is connected to the first element, forming a circle.
- **Applications:** Circular queues are used in printer queues, job scheduling, and online shopping.
- **Operations:**
  - **Enqueue:** Adding an element to the end of the queue.
  - **Dequeue:** Removing an element from the front of the queue.
  - **Peek (Front):** Viewing the front element of the queue without removing it.
  - **Is Full:** Checking if the queue is full.
  - **Is Empty:** Checking if the queue is empty.

#### Double-Ended Queues

- **Definition:** A double-ended queue is a type of queue that supports both insertion and deletion from both ends.
- **Applications:** Double-ended queues are used in applications where data needs to be frequently inserted and deleted from both ends.
- **Operations:**
  - **Insert (Left):** Adding an element to the left of the queue.
  - **Insert (Right):** Adding an element to the right of the queue.
  - **Delete (Left):** Removing an element from the left of the queue.
  - **Delete (Right):** Removing an element from the right of the queue.

#### Priority Queues

- **Definition:** A priority queue is a type of queue where elements are ordered based on their priority.
- **Applications:** Priority queues are used in applications where elements need to be processed based on their priority.
- **Operations:**
  - **Insert (With Priority):** Adding an element to the queue with a specified priority.
  - **Delete (Highest Priority):** Removing the element with the highest priority from the queue.

**Important Formulas, Definitions, and Theorems:**

- **FIFO (First-In-First-Out) Principle:** The order of elements in a queue is determined by the order in which they were added.
- **LIFO (Last-In-First-Out) Principle:** The order of elements in a stack is determined by the order in which they were added.
- **Queue Operations:** Insertion, deletion, peek, and is empty are the basic operations performed on a queue.
