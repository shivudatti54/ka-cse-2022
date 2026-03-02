# Module 2: Different Types of Queues

## Introduction

In the previous module, you learned about the fundamental Linear Data Structure: the Queue. You learned that it follows the **First-In-First-Out (FIFO)** principle, much like a line of people waiting for a ticket. However, the standard or **Simple Queue** has a significant limitation: once the queue is full, you cannot add a new element, even if spaces are available at the front after some dequeuing. This drawback leads to inefficient memory usage.

To overcome this and other limitations, several variations of the standard queue have been developed. Understanding these different types of queues is crucial for solving complex real-world computing problems efficiently, such as in CPU scheduling, network traffic management, and simulation systems.

---

## Core Concepts of Queue Variations

### 1. Simple Queue (Linear Queue)

This is the basic FIFO structure where insertion happens at the rear and deletion at the front. It can be implemented using a linear array or a linked list.

- **Limitation:** **"False Overflow"** – Once the rear pointer reaches the end of the array, it cannot insert new items, even if spaces are available at the beginning (after dequeues). This inefficient use of space is its primary weakness.

### 2. Circular Queue

The Circular Queue overcomes the limitation of the simple queue by treating the array as a circular structure. The rear and front pointers wrap around to the beginning of the array when they reach the end.

- **How it works:**
- **Initialization:** `front = rear = -1`
- **Enqueue:** `rear = (rear + 1) % size` (The modulo operator `%` enables the circular behavior)
- **Dequeue:** `front = (front + 1) % size`
- **Advantage:** Efficiently utilizes memory by reusing the empty spaces created after dequeue operations.
- **Example:** Think of a circular track; a runner can keep going around after completing a lap.
- **Implementation Note:** You must carefully handle the conditions for checking if the queue is full or empty. A common approach is to sacrifice one array cell to distinguish between the full and empty states.

### 3. Priority Queue

In a Priority Queue, each element is associated with a **priority**. The element with the highest priority is dequeued first, regardless of its order of arrival. If two elements have the same priority, they are served according to their order in the queue (FIFO).

- **Characteristics:**
- **Not a pure FIFO** structure. Dequeue order depends on priority.
- Can be implemented using arrays, linked lists, or more efficiently with a **Heap** data structure (which you will study later).
- **Example:** In a hospital emergency room, patients are treated based on the severity of their condition (priority), not on who arrived first.

### 4. Double-Ended Queue (Deque)

Pronounced "deck", a Deque is a generalized queue that allows insertion and deletion from **both ends** (front and rear). It provides more flexibility than a standard queue.

- **Types of Deque:**
- **Input-Restricted Deque:** Insertion is allowed only at the rear, but deletion can be done from both ends.
- **Output-Restricted Deque:** Deletion is allowed only at the front, but insertion can be done at both ends.
- **Applications:** Excellent for implementing algorithms that require scrolling through data in both directions, undo/redo functionality in software, and palindrome checkers.

---

## Comparison Table

| Type of Queue                  | Insertion At      | Deletion At            | Key Principle      | Major Advantage                         |
| :----------------------------- | :---------------- | :--------------------- | :----------------- | :-------------------------------------- |
| **Simple Queue**               | Rear only         | Front only             | Strict FIFO        | Simple to implement                     |
| **Circular Queue**             | Rear              | Front                  | FIFO (Circular)    | Solves false overflow, memory efficient |
| **Priority Queue**             | Any position\*    | Highest Priority First | Priority-Based     | Processes tasks based on urgency        |
| **Double-Ended Queue (Deque)** | Both Front & Rear | Both Front & Rear      | Flexible FIFO/LIFO | High flexibility in operations          |

_\*Insertion in a priority queue implementation depends on the priority, not a fixed position._

---

## Key Points & Summary

- **Simple Queues** are fundamental but suffer from inefficient memory usage due to "false overflow."
- **Circular Queues** solve this problem by connecting the end of the array back to its start, making them highly efficient for fixed-size implementations.
- **Priority Queues** deviate from strict FIFO. Elements are processed based on their priority, which is critical for task scheduling in operating systems.
- **Double-Ended Queues (Deques)** offer the most flexibility, allowing addition and removal of elements from both ends, making them suitable for a wider range of applications.

**Choosing the right type of queue depends entirely on the application's requirements.** Whether you need strict order, efficient memory use, priority-based processing, or flexibility in operations dictates which queue variant is the optimal choice for your algorithm. Mastering these structures is a key step in designing efficient software systems.
