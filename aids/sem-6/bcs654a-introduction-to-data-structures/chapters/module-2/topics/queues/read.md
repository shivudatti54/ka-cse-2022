# Introduction to Queues

## What is a Queue?

A **queue** is a fundamental linear data structure that follows the **First-In-First-Out (FIFO)** principle. This means the first element added to the queue will be the first one to be removed. Queues are analogous to real-world waiting lines, such as customers at a ticket counter or cars at a toll booth, where the first person/car to arrive is the first to be served.

### Key Characteristics of Queues

- **Ordered Collection**: Elements are maintained in a specific sequence.
- **FIFO Principle**: First element inserted is the first to be removed.
- **Two Ends**: Operations are performed at two different ends:
  - **Rear/Back**: For insertion (enqueue) operations.
  - **Front**: For deletion (dequeue) operations.

## Basic Queue Operations

A queue typically supports the following fundamental operations:

1.  **Enqueue**: Adds an element to the rear of the queue.
2.  **Dequeue**: Removes and returns the element from the front of the queue.
3.  **Peek/Front**: Returns the element at the front without removing it.
4.  **isEmpty**: Checks if the queue is empty.
5.  **isFull**: Checks if the queue is full (primarily in array-based implementations with fixed size).

### Operation Visualization

Let's visualize these operations with a simple example:

**Initial State:** `[ ]` (Empty Queue)

1.  Enqueue(10): `[10]` (Front=Rear=10)
2.  Enqueue(20): `[10, 20]` (Front=10, Rear=20)
3.  Enqueue(30): `[10, 20, 30]` (Front=10, Rear=30)
4.  Dequeue(): Returns 10. Queue becomes `[20, 30]` (Front=20, Rear=30)
5.  Peek(): Returns 20. Queue remains `[20, 30]`
6.  Dequeue(): Returns 20. Queue becomes `[30]` (Front=Rear=30)
7.  Dequeue(): Returns 30. Queue becomes `[ ]` (Empty)

```
Operation         Queue State         Output
---------         -----------         ------
Initial           [ ]                 -
enqueue(10)       [10]               -
enqueue(20)       [10, 20]           -
enqueue(30)       [10, 20, 30]       -
dequeue()         [20, 30]           10
peek()            [20, 30]           20
dequeue()         [30]               20
dequeue()         [ ]                30
isEmpty()         [ ]                True
```

## Implementation of Queues using Arrays

Implementing a queue using an array is straightforward but comes with a significant challenge: **memory wastage**. Let's explore a simple implementation and its drawback.

### Simple Array Implementation

We use an array `arr[]` of a fixed size `MAX`, and two integer variables `front` and `rear` to track the respective indices.

**Initialization:**

- `front = -1`
- `rear = -1`

**C Code Snippet:**

```c
#include <stdio.h>
#define MAX 5

int queue[MAX];
int front = -1;
int rear = -1;

void enqueue(int value) {
    if (rear == MAX - 1) {
        printf("Queue is Full (Overflow)\n");
    } else {
        if (front == -1) { // If queue is initially empty
            front = 0;
        }
        rear++;
        queue[rear] = value;
        printf("%d enqueued to queue\n", value);
    }
}

int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue is Empty (Underflow)\n");
        return -1;
    } else {
        int value = queue[front];
        front++;
        if (front > rear) { // Reset after last dequeue
            front = rear = -1;
        }
        printf("%d dequeued from queue\n", value);
        return value;
    }
}

int peek() {
    if (front == -1 || front > rear) {
        printf("Queue is Empty\n");
        return -1;
    } else {
        return queue[front];
    }
}

int isEmpty() {
    return (front == -1 || front > rear);
}
```

### The Limitation: Memory Wastage

In the simple implementation above, after several enqueue and dequeue operations, the `front` index moves forward. Once `rear` reaches `MAX-1`, even if there are empty slots at the beginning of the array (because elements were dequeued), new elements cannot be added. This leads to inefficient memory usage.

**Example:**
MAX = 3. Operations: enqueue(10), enqueue(20), enqueue(30), dequeue(), dequeue().
The queue state becomes `[ , , 30]` with `front=2` and `rear=2`. There are two free slots at indices 0 and 1, but calling `enqueue(40)` will result in an overflow error because `rear == MAX-1` is true.

```
Initial Array: [ -, -, - ]  front=-1, rear=-1
enqueue(10):   [10, -, - ]  front=0, rear=0
enqueue(20):   [10, 20, - ] front=0, rear=1
enqueue(30):   [10, 20, 30] front=0, rear=2
dequeue():     [ -, 20, 30] front=1, rear=2
dequeue():     [ -, -, 30]  front=2, rear=2
// Cannot enqueue(40) now! Wasted space.
```

This problem is solved by the **Circular Queue** concept, which is covered in the next part of the syllabus.

## Types of Queues

The syllabus introduces different variations of the standard queue to overcome limitations and serve specific purposes.

| Queue Type                     | Key Characteristic                                                                    | Primary Use Case                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Linear Queue**               | Simple sequential storage. Suffers from memory wastage.                               | Basic understanding of FIFO principle.                                              |
| **Circular Queue**             | Rear and front are connected logically, utilizing empty spaces. Efficient memory use. | Systems where resources are reused (e.g., CPU scheduling, traffic signal cycles).   |
| **Double-Ended Queue (Deque)** | Insertion and deletion can occur at both the front and the rear. Highly flexible.     | Algorithms requiring flexible access (e.g., A-Steal scheduler, palindrome checker). |
| **Priority Queue**             | Elements are processed based on priority, not just FIFO order.                        | Scheduling tasks (OS), Dijkstra's algorithm, Huffman coding.                        |

## Applications of Queues

Queues are indispensable in computer science for managing data in a ordered, FIFO manner.

1.  **CPU Scheduling:** Operating systems use queues (like the ready queue) to manage processes waiting for the CPU.
2.  **Disk Scheduling:** Requests for reading/writing to a disk are often managed in a queue.
3.  **Breadth-First Search (BFS):** A fundamental graph traversal algorithm that uses a queue to keep track of nodes to be visited.
4.  **Handling Interrupts:** Hardware interrupts are often held in a queue to be processed by the CPU one at a time.
5.  **Print Spooling:** Documents sent to a printer are placed in a queue (print spooler) and printed in the order they were received.
6.  **Buffering for I/O Devices:** Data streams from devices like keyboards or network cards are often buffered using queues.
7.  **Call Center Systems:** Incoming calls are placed in a queue until a customer service representative becomes available.

## Queue vs. Stack

It's crucial to understand the difference between queues and their counterpart from this module, stacks.

| Feature             | Queue (FIFO)                            | Stack (LIFO)                                  |
| ------------------- | --------------------------------------- | --------------------------------------------- |
| **Order Principle** | First-In-First-Out                      | Last-In-First-Out                             |
| **Insertion**       | At the **Rear** only (Enqueue)          | At the **Top** only (Push)                    |
| **Deletion**        | From the **Front** only (Dequeue)       | From the **Top** only (Pop)                   |
| **Analogies**       | Ticket counter line, people in a queue. | Stack of plates, pile of books.               |
| **Applications**    | BFS, Scheduling, Buffering.             | Function call stack, DFS, Expression parsing. |

## Exam Tips

1.  **FIFO is Key:** Always remember the core FIFO principle. Most exam questions test your understanding of the order of insertion and removal.
2.  **Trace Operations:** Practice tracing a sequence of enqueue and dequeue operations on paper. Draw the state of the array, `front`, and `rear` after each step. This is a common exam question.
3.  **Identify the Problem:** Be able to explain why a simple linear array implementation leads to memory wastage. Understanding the problem is the first step to understanding the solution (Circular Queues).
4.  **Know the Applications:** Memorize 2-3 key applications for queues (e.g., BFS, CPU Scheduling). You will often be asked to name them.
5.  **Contrast with Stacks:** Be prepared to compare and contrast queues and stacks in a short or long answer question. Use a table format in your answer for clarity.
6.  **Watch for Underflow/Overflow:** Always check for empty queue (`isEmpty`) before a `dequeue` and for a full queue (`isFull`) before an `enqueue` in your code answers.
