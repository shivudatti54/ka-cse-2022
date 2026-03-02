# Introduction to Different Types of Queues

## Introduction
In the previous module, we explored the fundamental linear data structure known as a queue, which operates on the **First-In-First-Out (FIFO)** principle. While the simple queue is powerful, its static nature and strict ordering can be limiting for certain computational problems. This module delves into advanced variations of the standard queue, each designed to overcome specific limitations and optimize performance for particular use cases in computer science and engineering.

## Core Concepts of Queue Variants

### 1. Simple Queue (Linear Queue)
This is the basic form of a queue where insertion (`enqueue`) happens at the rear and deletion (`dequeue`) occurs at the front.

*   **Limitation:** Once the rear pointer reaches the end of the queue, even if there are empty spaces at the front (after some dequeues), new elements cannot be added. This is known as **"false overflow"** or the inability to utilize empty spaces.

### 2. Circular Queue
A circular queue overcomes the primary limitation of the simple linear queue by treating the array as a circular buffer. The rear and front pointers wrap around to the beginning of the array once they reach the end.

*   **Concept:** The last element points back to the first element, forming a circle.
*   **Operations:**
    *   **Enqueue:** `rear = (rear + 1) % size`
    *   **Dequeue:** `front = (front + 1) % size`
*   **Example:** Imagine a queue of size 4. After enqueuing A, B, C, D and then dequeuing A and B, `front` is at index 2. A new enqueue operation will place the element at `rear = (3 + 1) % 4 = 0`, effectively reusing the space at the start of the array.
*   **Application:** Traffic light systems, CPU scheduling (Round Robin), streaming data buffers.

### 3. Priority Queue
In a priority queue, each element is associated with a **priority**. Dequeueing removes the element with the highest priority (or sometimes the lowest, depending on the implementation). The FIFO order is only maintained for elements with the same priority.

*   **Concept:** Elements are processed based on priority, not just arrival time.
*   **Implementation:** It is often implemented using a **Heap** data structure (e.g., Binary Heap) due to its efficient `O(log n)` insertion and removal of the highest-priority element.
*   **Example:** In a hospital emergency room, patients are treated based on the severity of their condition (priority), not their order of arrival. A patient with a critical injury (high priority) will be seen before a patient with a minor cut (low priority) who arrived earlier.
*   **Application:** Dijkstra's algorithm, Huffman coding, operating system process scheduling.

### 4. Double-Ended Queue (Deque)
Pronounced "deck," a deque is a generalized queue that allows insertion and deletion at **both ends** (front and rear). It provides the flexibility of both a stack (LIFO) and a queue (FIFO).

*   **Operations:**
    *   `insertFront()`, `deleteFront()`
    *   `insertRear()`, `deleteRear()`
*   **Types:**
    *   **Input-Restricted Deque:** Insertion allowed only at the rear, but deletion can be from both ends.
    *   **Output-Restricted Deque:** Deletion allowed only from the front, but insertion can be at both ends.
*   **Application:** Implementing algorithms that require sliding windows (e.g., finding max in all subarrays of size k), undo-redo functionality in software, and palindrome checkers.

## Comparison of Queue Types

| Queue Type         | Insertion (`enqueue`) | Deletion (`dequeue`) | Key Feature                                  |
| ------------------ | --------------------- | -------------------- | -------------------------------------------- |
| **Simple Queue**   | Only at Rear          | Only at Front        | Basic FIFO                                   |
| **Circular Queue** | Only at Rear          | Only at Front        | Efficient memory reuse; circular buffer      |
| **Priority Queue** | At any position*      | Highest Priority     | Elements are processed by priority, not order |
| **Deque**          | **Both Front & Rear** | **Both Front & Rear**| Highly flexible; both stack and queue ops    |

*Insertion position is determined by the element's priority.

## Key Points & Summary

*   **Standard Queue:** Follows strict FIFO order but suffers from inefficient memory usage.
*   **Circular Queue:** Solves the memory wastage problem of a simple queue by connecting the end of the array to its start. It is essential for implementing continuous, efficient buffers.
*   **Priority Queue:** Breaks the strict FIFO rule. Elements are served based on their priority, making it crucial for systems where order of processing is determined by urgency or weight.
*   **Double-Ended Queue (Deque):** Offers the most flexibility, allowing operations at both ends. It can function as a stack, a queue, or something in between.
*   **Choice of Queue:** The selection of an appropriate queue type depends entirely on the application's requirements for memory efficiency, processing order, and operational flexibility. Understanding these variants is fundamental for designing efficient algorithms and systems.