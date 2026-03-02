# Module 2: Different Types of Queues

## Introduction

In the previous module, you learned about the fundamental linear data structure: the queue. A queue follows the **First-In-First-Out (FIFO)** principle, where the first element added is the first one to be removed. While a simple queue is a powerful concept, its basic implementation has limitations in certain computational scenarios. This module explores advanced variations of the standard queue—namely **Circular Queue**, **Priority Queue**, and **Double-Ended Queue (Deque)**. These specialized queues are designed to overcome specific inefficiencies and cater to a wider range of real-world applications, from CPU scheduling to memory management.

## Core Concepts & Types of Queues

### 1. Simple Queue (Linear Queue)
This is the standard FIFO structure with two pointers: `front` and `rear`.
*   **Enqueue:** Adds an element at the `rear`.
*   **Dequeue:** Removes an element from the `front`.
*   **Limitation:** **"False Overflow"** – After several enqueues and dequeues, even if there are empty spaces at the beginning of the array, the `rear` pointer reaches the end and signals overflow, preventing new insertions. This inefficient use of space led to the development of the Circular Queue.

### 2. Circular Queue
A circular queue overcomes the limitation of the simple linear queue by connecting the last position of the array back to the first, forming a conceptual circle.

*   **How it works:** The pointers `front` and `rear` move circularly using modulo arithmetic.
    *   **Enqueue:** `rear = (rear + 1) % size`
    *   **Dequeue:** `front = (front + 1) % size`
*   **Example:** Consider a queue of size 4. After enqueuing A, B, C and dequeuing A and B, `front` is at index 2 and `rear` is at index 3. In a linear queue, you cannot enqueue a new element D. In a circular queue, the next enqueue operation calculates: `(3 + 1) % 4 = 0`. So, element D is placed at index 0, efficiently reusing the empty space.
*   **Advantage:** Eliminates false overflow and utilizes memory efficiently.

### 3. Priority Queue
A priority queue is a special type of queue where each element has an associated **priority**. The element with the highest priority is dequeued first, regardless of the order in which it was inserted. If two elements have the same priority, they are served according to their order in the queue (FIFO).

*   **Implementation:** It can be implemented using arrays, linked lists, or more efficiently with a **heap** data structure.
*   **Types:**
    *   **Ascending Priority Queue:** Elements with *lower* values have higher priority (e.g., value 1 has higher priority than value 5).
    *   **Descending Priority Queue:** Elements with *higher* values have higher priority.
*   **Application:**
    *   **CPU Scheduling:** Processes with higher priority (e.g., system processes) are executed first.
    *   **Dijkstra's Algorithm:** Used to find the shortest path in a graph.

### 4. Double-Ended Queue (Deque)
Pronounced "deck", a deque is a highly flexible queue that allows insertion and deletion of elements from **both ends** (`front` and `rear`). It generalizes both stacks and queues.

*   **Operations:**
    *   `insertFront()`: Add an element at the front.
    *   `insertRear()`: Add an element at the rear (standard enqueue).
    *   `deleteFront()`: Remove an element from the front (standard dequeue).
    *   `deleteRear()`: Remove an element from the rear.
*   **Types:**
    *   **Input-Restricted Deque:** Insertion is allowed only at one end (rear), but deletion is allowed at both ends.
    *   **Output-Restricted Deque:** Deletion is allowed only at one end (front), but insertion is allowed at both ends.
*   **Application:** Can be used as both a stack (LIFO) and a queue (FIFO). Also used in palindrome checkers and undo/redo functionality.

## Key Points & Summary

| Queue Type | Principle | Key Feature | Primary Application |
| :--- | :--- | :--- | :--- |
| **Simple Queue** | FIFO | Basic insert at rear, delete from front. | Simple task scheduling, waiting lists. |
| **Circular Queue** | FIFO | Reuses empty spaces, avoids false overflow. | Memory management, traffic systems, CPU scheduling. |
| **Priority Queue** | Element Priority | Element with highest priority is served first. | CPU Scheduling, algorithms like Huffman coding. |
| **Double Ended Queue (Deque)** | Flexible | Insertion and deletion from both ends. | Palindrome checking, implementing stacks and queues. |

*   The choice of queue type depends entirely on the application's requirements.
*   A **Circular Queue** is essential for efficient memory utilization in fixed-size array implementations.
*   A **Priority Queue** is indispensable for scenarios where processing order is based on urgency or weight, not just arrival time.
*   A **Deque** provides maximum flexibility for algorithms that require access to both ends of a list.

Understanding these different types of queues and their specific use cases is crucial for designing efficient and optimized algorithms and systems in computer science and engineering.