# Queue Operations and Implementation

## 1. Introduction to Queues

A **Queue** is a fundamental linear data structure that follows a particular order in which operations are performed. The order is **First In First Out (FIFO)**. This means the first element added to the queue will be the first one to be removed.

A real-world analogy is a line of people waiting at a ticket counter. The person who arrives first gets served first, and a new person joins the line at the end.

### 1.1. Basic Queue Structure

A queue has two ends:

- **Front (Head):** The end from which elements are removed (dequeued).
- **Rear (Tail):** The end at which new elements are added (enqueued).

```
 Enqueue (Add) -> [ Item 3 | Item 2 | Item 1 ] -> Dequeue (Remove)
 ^ ^
 Rear Front
```

_Figure 1: Visual representation of a Queue's FIFO principle._

## 2. Standard Queue Operations

The primary operations that can be performed on a queue are:

1. **enqueue(item):** Adds an element `item` to the **rear** of the queue.
2. **dequeue():** Removes and returns the element from the **front** of the queue.
3. **peek()** or **front():** Returns the element at the **front** without removing it.
4. **isEmpty():** Checks if the queue is empty. Returns `true` if empty, else `false`.
5. **isFull():** (For fixed-size arrays) Checks if the queue is full.
6. **size()** or **count():** Returns the number of elements currently in the queue.

## 3. Implementation of a Queue using an Array

Implementing a queue using a linear array is straightforward but has a significant limitation: it can lead to inefficient memory usage. Let's explore two common implementations.

### 3.1. Simple Linear Array Implementation

In this approach, we maintain two indices (or pointers):

- `front`: Index of the front element.
- `rear`: Index of the last element.

**Initial State:**

```
front = -1, rear = -1
Queue: [ _, _, _, _, _ ] (Empty)
```

**After enqueue(10), enqueue(20), enqueue(30):**

```
front = 0, rear = 2
Queue: [ 10, 20, 30, _, _ ]
```

**After dequeue() (removes 10):**

```
front = 1, rear = 2
Queue: [ _, 20, 30, _, _ ]
```

_Figure 2: Simple array implementation showing movement of `front` and `rear`._

**The Problem:** As we continue to dequeue, the `front` index moves forward. The spaces before the `front` index become unused and wasted. This is known as the **"Linear Queue" problem**.

### 3.2. Circular Queue Implementation

To solve the problem of wasted space in a linear queue, we use a **Circular Queue**. The array is treated as if it were circularly connected. The last element is connected to the first element.

**Key Modifications:**

- **Enqueue:** `rear = (rear + 1) % capacity`
- **Dequeue:** `front = (front + 1) % capacity`
- **Initialization:** `front = 0`, `rear = -1` (or `front = -1`, `rear = -1` with slightly modified logic)
- **Full Condition:** `(rear + 1) % capacity == front`
- **Empty Condition:** `front == -1` or `front == rear` (implementation specific)

**Visualization of a Circular Queue (Capacity = 5):**

```
Initial: front = 0, rear = -1
Queue: [ _, _, _, _, _ ]

After enqueue(10), enqueue(20), enqueue(30), enqueue(40):
front = 0, rear = 3
Queue: [ 10, 20, 30, 40, _ ]

After dequeue() (removes 10), dequeue() (removes 20):
front = 2, rear = 3
Queue: [ _, _, 30, 40, _ ]

After enqueue(50), enqueue(60):
rear = (3 + 1) % 5 = 4 -> enqueue(50)
rear = (4 + 1) % 5 = 0 -> enqueue(60)
front = 2, rear = 0
Queue: [ 60, _, 30, 40, 50 ]
```

_Figure 3: Circular queue demonstrating efficient use of space._

**C Code Snippet for Circular Queue Operations:**

```c
#include <stdio.h>
#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

int isFull() {
 return (rear + 1) % MAX == front;
}

int isEmpty() {
 return front == -1;
}

void enqueue(int value) {
 if (isFull()) {
 printf("Queue is Full!\n");
 return;
 }
 if (isEmpty()) {
 front = 0;
 }
 rear = (rear + 1) % MAX;
 queue[rear] = value;
 printf("%d enqueued to queue\n", value);
}

int dequeue() {
 if (isEmpty()) {
 printf("Queue is Empty!\n");
 return -1;
 }
 int value = queue[front];
 if (front == rear) { // Last element
 front = rear = -1;
 } else {
 front = (front + 1) % MAX;
 }
 printf("%d dequeued from queue\n", value);
 return value;
}

int peek() {
 if (isEmpty()) {
 printf("Queue is Empty!\n");
 return -1;
 }
 return queue[front];
}
```

## 4. Different Types of Queues

| Queue Type                     | Description                                         | Key Feature                                        | Typical Use Case                           |
| :----------------------------- | :-------------------------------------------------- | :------------------------------------------------- | :----------------------------------------- |
| **Simple Queue**               | Basic FIFO list.                                    | Insert at rear, remove from front.                 | Simple task scheduling.                    |
| **Circular Queue**             | Linear array treated as circular.                   | Solves the memory wastage problem.                 | CPU scheduling, memory management.         |
| **Priority Queue**             | Elements are processed based on priority.           | Highest priority served first (not strictly FIFO). | OS processes, emergency room queues.       |
| **Double-Ended Queue (Deque)** | Insertion and deletion from both ends.              | Not strictly FIFO or LIFO.                         | Web browser history, undo-redo operations. |
| **Input-Restricted Deque**     | A Deque where insertion is allowed only at one end. | More restricted than a general Deque.              | Data streaming with single source.         |
| **Output-Restricted Deque**    | A Deque where deletion is allowed only at one end.  | More restricted than a general Deque.              | Pruning history logs.                      |

## 5. Applications of Queues

Queues are ubiquitous in computer science due to their ability to model real-world waiting lines and buffer data.

1. **CPU Scheduling:** The operating system uses queues (often circular or priority queues) to manage processes waiting for CPU time.
2. **Disk Scheduling:** Requests to read from or write to the disk are managed in a queue.
3. **Breadth-First Search (BFS):** A fundamental graph traversal algorithm that uses a queue to keep track of the nodes to be visited.
4. **Handling Interrupts:** Hardware interrupts are often held in a queue to be processed by the CPU one at a time.
5. **Buffers for I/O Devices:** Data being sent to printers or other I/O devices is often spooled into a queue to handle speed differences between the computer and the device.
6. **Call Center Phone Systems:** Calls are placed in a queue until a service representative becomes available.
7. **Message Queues:** In networking and microservices architecture, messages are often passed between systems using queues for asynchronous communication.

## 6. Comparison: Stack vs. Queue

| Feature                  | **Stack (LIFO)**                                           | **Queue (FIFO)**                      |
| :----------------------- | :--------------------------------------------------------- | :------------------------------------ |
| **Principle**            | Last In, First Out                                         | First In, First Out                   |
| **Insertion Operation**  | Push (on top)                                              | Enqueue (at rear)                     |
| **Removal Operation**    | Pop (from top)                                             | Dequeue (from front)                  |
| **Access Point**         | Only one (Top)                                             | Two (Front and Rear)                  |
| **Analogy**              | Stack of plates                                            | Line of people                        |
| **Typical Applications** | Function call management, undo/redo, expression evaluation | CPU scheduling, BFS, resource sharing |

## 7. Exam Tips and Common Pitfalls

- **Tip 1:** Always check for `isEmpty()` before calling `dequeue()` or `peek()` to avoid runtime errors or undefined behavior.
- **Tip 2:** For array implementation, clearly understand and implement the conditions for `isFull()` and `isEmpty()` correctly, especially for circular queues. A common mistake is getting the modulo arithmetic wrong.
- **Tip 3:** When asked to implement a queue, first decide if a linear or circular array is appropriate based on the problem's memory constraints. A circular queue is almost always the better choice for a fixed-size array.
- **Pitfall 1:** Confusing the `front` and `rear` pointers. Remember: you add at the `rear` and remove from the `front`.
- **Pitfall 2:** Forgetting to handle the special case when the last element is dequeued (i.e., when `front == rear` before dequeueing, the queue becomes empty and pointers must be reset).
- **Pitfall 3:** Assuming a simple linear array implementation is efficient. Always be aware of the memory wastage problem and prefer circular implementation.
