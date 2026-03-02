# Module 2: Different Types of Queues

## Introduction

In the previous module, you learned about the basic Queue data structure, which operates on the **First-In-First-Out (FIFO)** principle. While a simple queue is foundational, real-world computing problems often demand more flexible and efficient variants. This section explores three such specialized queues: **Circular Queue**, **Priority Queue**, and **Double-Ended Queue (Deque)**. Understanding these variations is crucial for optimizing system performance in areas like CPU scheduling, network traffic management, and simulation modeling.

## Core Concepts of Queue Variants

### 1. Circular Queue
A Circular Queue (or Ring Buffer) overcomes the major limitation of a simple linear queue: **inefficient memory utilization**. In a linear queue, after elements are dequeued from the front, the space they occupied cannot be reused, leading to "false overflow" even when the rear hasn't reached the actual end of the array.

**How it works:**
*   The queue is implemented using a fixed-size array.
*   The front and rear pointers are advanced in a circular manner using the modulo operation (`%`).
*   **Enqueue:** `rear = (rear + 1) % size`
*   **Dequeue:** `front = (front + 1) % size`
*   This allows the pointers to wrap around to the beginning of the array once they reach the end, effectively reusing the vacant spaces.

**Example:**
Consider a circular queue of size 4 (`size = 4`). Initially, `front = rear = -1`.
1.  Enqueue A, B, C: `front = 0`, `rear = 2`. State: `[A, B, C, ]`
2.  Dequeue A: `front = (0 + 1) % 4 = 1`, `rear = 2`. State: `[ , B, C, ]`
3.  Enqueue D: `rear = (2 + 1) % 4 = 3`. State: `[ , B, C, D]`
4.  Enqueue E: `rear = (3 + 1) % 4 = 0`. State: `[E, B, C, D]`. The queue is now full.

**Applications:** CPU Scheduling, Memory Management, Stream Buffering.

### 2. Priority Queue
A Priority Queue is a queue where each element has an associated **priority**. Dequeueing is not based on insertion order (FIFO), but on the **priority** of the elements. The element with the highest priority is served first, regardless of when it was inserted.

**Characteristics:**
*   **Highest Priority Element First:** Can be either the smallest or largest value, depending on the chosen convention (often Min-Heap or Max-Heap).
*   **Same Priority:** Elements with the same priority are typically served according to the FIFO order, making it a stable queue.
*   It is typically implemented using a **Heap** data structure, which allows for efficient O(log n) insertion and removal operations.

**Example:**
Imagine a print queue for a shared printer.
*   Job A (10 pages, Priority: Low) arrives.
*   Job B (2 pages, Priority: High) arrives.
*   Job C (5 pages, Priority: Medium) arrives.
A standard queue would print A -> B -> C. A priority queue will print the highest priority job first: **B (High) -> C (Medium) -> A (Low)**.

**Applications:** Dijkstra's Algorithm, Huffman Coding, Operating System Task Scheduling.

### 3. Double-Ended Queue (Deque)
A Deque (pronounced "deck") is a highly generalised form of a queue that allows insertion and deletion of elements from **both ends** (front and rear). It does not strictly follow the FIFO principle; it provides more flexibility.

**Types of Deque:**
*   **Input-Restricted Deque:** Insertion is allowed only at one end (rear), but deletion is allowed from both ends.
*   **Output-Restricted Deque:** Deletion is allowed only at one end (front), but insertion is allowed from both ends.
*   If no restrictions are applied, it is simply called a Deque.

**Operations:**
*   `insertFront()`
*   `insertRear()`
*   `deleteFront()`
*   `deleteRear()`
*   `getFront()`
*   `getRear()`

**Example:**
A web browser's history can be modeled as a deque. You can add a new page to the rear (visiting a new link). You can also traverse backwards (front) and forwards (rear) through your history.

**Applications:** Implementing Undo-Redo operations, Palindrome Checker, Job-stealing algorithms in multiprocessor systems.

## Key Points & Summary

| Queue Type          | Principle                          | Key Advantage/Use-Case                                  | Common Implementation     |
| :------------------ | :--------------------------------- | :------------------------------------------------------ | :------------------------ |
| **Simple Queue**    | Strict FIFO                        | Basic ordering                                          | Array, Linked List        |
| **Circular Queue**  | FIFO with wrapped memory           | **Efficient memory usage**, avoids false overflow       | Array (using modulo `%`)  |
| **Priority Queue**  | Highest Priority Element First     | **Processing based on urgency/priority**, not just order | Heap, Linked List         |
| **Deque**           | Insert/Delete from both ends       | **High flexibility** for front and rear operations      | Doubly Linked List, Array |

*   Choosing the right type of queue is critical for algorithmic efficiency and system design.
*   **Circular Queues** are essential for resource management in systems with limited, fixed memory.
*   **Priority Queues** are fundamental for algorithms that require processing the "best" or "most urgent" element next.
*   **Deques** provide the versatility needed for complex data manipulation tasks at both ends of the collection.