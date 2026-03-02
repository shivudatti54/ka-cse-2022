# Double-Ended and Priority Queues

## Introduction to Variations of the Queue

A standard queue operates on a **First-In-First-Out (FIFO)** principle, where elements are added at the rear and removed from the front. While this is ideal for many scenarios like print job scheduling or customer service lines, some applications require more flexible data access. This leads us to two important extensions of the basic queue: the **Double-Ended Queue (Deque)** and the **Priority Queue**.

## 1. Double-Ended Queues (Deque)

### 1.1. What is a Deque?

A **Double-Ended Queue (Deque**, pronounced "deck") is a linear data structure that allows insertion and deletion of elements from **both ends** (front and rear). It does not adhere strictly to the FIFO principle of a standard queue, as elements can be added or removed from either side. Think of it as a hybrid between a stack (LIFO) and a queue (FIFO).

### 1.2. Types of Deques

There are two main variations:

- **Input-Restricted Deque:** Insertion is allowed only at one end (e.g., only at the rear), but deletion is allowed from both ends.
- **Output-Restricted Deque:** Deletion is allowed only from one end (e.g., only from the front), but insertion is allowed at both ends.

A general deque has no such restrictions.

### 1.3. Core Operations on a Deque

The primary operations for a deque are:

- `insertFront(element)`: Adds an element to the front of the deque.
- `insertRear(element)`: Adds an element to the rear of the deque.
- `deleteFront()`: Removes and returns the element from the front of the deque.
- `deleteRear()`: Removes and returns the element from the rear of the deque.
- `getFront()`: Returns the element at the front without removing it.
- `getRear()`: Returns the element at the rear without removing it.
- `isEmpty()`: Checks if the deque is empty.
- `isFull()`: Checks if the deque is full (for array-based implementation).

### 1.4. Implementation using Arrays

Implementing a deque using an array requires careful management of the `front` and `rear` pointers to avoid overflow and underflow. A **circular array** is the most efficient approach to utilize the allocated space fully.

**Initialization:**

- Declare an array `arr[]` of size `n`.
- Initialize `front = -1` and `rear = -1`.

**Insertion at Rear:** Similar to a standard circular queue.

1. Check if the deque is full.
2. If empty (`front == -1`), set `front = rear = 0`.
3. Otherwise, set `rear = (rear + 1) % n`.
4. Place the element at `arr[rear]`.

**Insertion at Front:** This is the unique operation for deques.

1. Check if the deque is full.
2. If empty (`front == -1`), set `front = rear = 0`.
3. Otherwise, set `front = (front - 1 + n) % n`. (This moves the front pointer backwards, wrapping around to the end of the array if necessary).
4. Place the element at `arr[front]`.

**Deletion from Front:** Similar to a standard circular queue.

1. Check if the deque is empty.
2. Store the element at `arr[front]`.
3. If only one element exists (`front == rear`), set `front = rear = -1`.
4. Otherwise, set `front = (front + 1) % n`.

**Deletion from Rear:** This is the other unique operation.

1. Check if the deque is empty.
2. Store the element at `arr[rear]`.
3. If only one element exists (`front == rear`), set `front = rear = -1`.
4. Otherwise, set `rear = (rear - 1 + n) % n`. (This moves the rear pointer backwards).

**Example Operations:**
Let's perform operations on a deque of size 5.

```
Initial state: [ _, _, _, _, _ ] | front = -1, rear = -1

insertRear(10): [10, _, _, _, _] | front=0, rear=0
insertFront(20): [10, _, _, _, 20] | front=4, rear=0 (front wraps around)
insertRear(30): [10, 30, _, _, 20] | front=4, rear=1 (rear moves forward)
deleteFront(): [10, 30, _, _, _] | front=0, rear=1 (front becomes 0 after deletion from previous front=4)
deleteRear(): [10, _, _, _, _] | front=0, rear=0 (rear moves back to 0)
```

### 1.5. Applications of Deques

- **Undo/Redo Operations:** Actions can be pushed onto a deque from one end, and undo/redo pops them from the same or opposite end.
- **Palindrome Checker:** A deque is a perfect data structure to check if a string is a palindrome. You can compare characters by removing them from both ends simultaneously.
- **Job Stealing Algorithm:** In multiprocessor scheduling, a processor can "steal" a job from the front of another processor's deque, which is implemented as a work-stealing algorithm.
- **Web Browser History:** The history of visited URLs can be managed using a deque, allowing navigation backwards and forwards.

## 2. Priority Queues

### 2.1. What is a Priority Queue?

A **Priority Queue** is an abstract data type that operates differently from a standard FIFO queue. In a priority queue, each element is associated with a **priority**. Elements are served based on their priority, not on the order in which they were added. The element with the **highest priority** (or sometimes the lowest) is always the next to be removed.

### 2.2. Characteristics

- **Order of Processing:** Highest (or lowest) priority element is dequeued first.
- **Non-Linear:** While often implemented using linear structures like arrays, the logical processing order is not linear.
- **Duplicate Priorities:** If two elements have the same priority, they are typically served according to their existing order (e.g., FIFO order).

### 2.3. Implementation of Priority Queues

Priority queues can be implemented using arrays, linked lists, or, most efficiently, using a **heap** data structure (a type of binary tree).

#### A) Implementation using a Simple Array

An unsorted array is simple but inefficient for deletions.

- **Enqueue (Insertion):** The new element is always added at the end of the array. Time Complexity: **O(1)**.
- **Dequeue (Deletion):** The entire array must be searched to find the element with the highest priority. After removal, other elements may need to be shifted. Time Complexity: **O(n)**.

#### B) Implementation using a Sorted Array

A sorted array makes deletion efficient but insertion slow.

- **Enqueue (Insertion):** The new element must be inserted in its correct position to maintain the sorted order (by priority), requiring shifting of elements. Time Complexity: **O(n)**.
- **Dequeue (Deletion):** The highest priority element is always at the end (or beginning) of the array and can be removed easily. Time Complexity: **O(1)**.

#### C) Implementation using a Linked List

A sorted linked list offers a trade-off.

- **Enqueue (Insertion):** Requires traversing the list to find the correct position for the new element. Time Complexity: **O(n)**.
- **Dequeue (Deletion):** Removing the highest priority element from the head of the list is very efficient. Time Complexity: **O(1)**.

**Comparison of Implementation Strategies:**

| Implementation         | Enqueue (Insert) | Dequeue (Delete) | Best Use Case                                           |
| :--------------------- | :--------------: | :--------------: | :------------------------------------------------------ |
| **Unsorted Array**     |       O(1)       |       O(n)       | When insertion is frequent, and deletion is infrequent. |
| **Sorted Array**       |       O(n)       |       O(1)       | When deletion is frequent, and insertion is infrequent. |
| **Sorted Linked List** |       O(n)       |       O(1)       | Dynamic memory, avoids shifting overhead of arrays.     |
| **Binary Heap**        |     O(log n)     |     O(log n)     | Most efficient for a mix of both operations.            |

_Note: Heap implementation is covered in the Trees module._

### 2.4. Applications of Priority Queues

- **CPU Scheduling:** In operating systems, processes are often scheduled based on their priority (e.g., in priority scheduling algorithms).
- **Dijkstra's Algorithm:** This graph algorithm for finding the shortest path uses a priority queue to always select the vertex with the smallest known distance.
- **Huffman Coding:** A lossless data compression algorithm that uses a priority queue to build an optimal prefix-free binary tree.
- **Data Compression:** Used in various compression algorithms to handle frequency of characters or symbols.
- **Simulation Systems:** Events are processed based on their scheduled time (priority).

## Exam Tips

1. **Visualize Operations:** Draw the array and track the `front` and `rear` pointers for every deque operation. This prevents off-by-one errors.
2. **Circular Array is Key:** Remember the modulo arithmetic `(index + 1) % size` and `(index - 1 + size) % size` for moving pointers in a circular array implementation. This is a common exam question.
3. **Distinguish Types:** Be clear on the difference between a simple queue, a circular queue, a deque, and a priority queue. A table comparing their properties is a good revision tool.
4. **Priority Queue ≠ Sorted List:** Understand that while a sorted list can implement a priority queue, it is not the definition of it. The defining feature is the _semantics_ of removing the highest priority element.
5. **Analyze Complexity:** For priority queues, be prepared to explain and compare the time complexity of different implementation strategies (array vs. linked list). This is a favorite question for longer answers.
6. **Relate to Applications:** For a 5-10 mark question, you might be asked to explain the data structure with an example. Knowing a real-world application (like CPU scheduling for priority queues) will make your answer stand out.
