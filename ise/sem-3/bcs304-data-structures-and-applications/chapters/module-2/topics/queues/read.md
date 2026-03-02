# QUEUES

## Introduction

A queue is a fundamental linear data structure in computer science that follows the FIFO (First-In-First-Out) principle. Unlike stacks where the last element added is the first to be removed, a queue ensures that elements are processed in the exact order they were inserted. The name "queue" intuitively evokes the concept of people waiting in a line—the first person to join the line is the first person to be served.

Queues are ubiquitous in computer systems and real-world applications. In operating systems, queues manage print jobs sent to printers, ensuring documents are printed in the order they were submitted. CPU task scheduling uses queues to manage processes waiting for execution. Network routers employ queues to handle data packets when traffic is heavy. In algorithm design, queues are essential for breadth-first search (BFS) traversal in graphs and trees. Understanding queues is crucial for any computer science student, as they form the backbone of many computational processes and help solve complex problems efficiently.

This chapter explores the queue abstract data type (ADT), its operations, implementation using arrays, and various applications. We will examine both theoretical concepts and practical implementation details, preparing you for university examinations and real-world programming scenarios.

## Key Concepts

### Queue Abstract Data Type (ADT)

A queue is an abstract data type that represents a collection of elements with two primary operations: insertion at the rear (enqueue) and deletion from the front (dequeue). The queue ADT maintains the FIFO ordering property, meaning the element that has been in the queue longest is always at the front and will be the next one removed.

The fundamental operations supported by a queue are:

**enqueue(item)**: Adds an element to the rear of the queue. This operation is sometimes called "push" or "insert," but in queue terminology, "enqueue" is the standard term.

**dequeue()**: Removes and returns the element at the front of the queue. This operation fails if the queue is empty.

**front()**: Returns the element at the front of the queue without removing it. This allows inspection of the next element to be dequeued.

**rear()**: Returns the element at the rear of the queue without removing it. This is useful for understanding the most recently added element.

**isEmpty()**: Returns true if the queue contains no elements, false otherwise. This is essential for preventing underflow errors.

**isFull()**: Returns true if the queue cannot accept more elements, false otherwise. This applies primarily to array-based implementations with fixed capacity.

**size()**: Returns the number of elements currently in the queue.

### Linear Queue Implementation Using Arrays

The simplest implementation of a queue uses a linear array. We maintain two indices: front points to the position from which elements will be removed, and rear points to the position where the next element will be inserted.

Consider a queue with capacity MAXSIZE implemented in an array queue[MAXSIZE]. Initially, we set front = -1 and rear = -1 to indicate an empty queue.

When we enqueue an element, we first check if the queue is full (rear == MAXSIZE - 1). If not full, we increment rear and store the element at queue[rear]. If this is the first element being added (front == -1), we also set front = 0.

When we dequeue an element, we first check if the queue is empty (front == -1 or front > rear). If not empty, we retrieve the element at queue[front]. Then we increment front. If front exceeds rear after this increment, we reset both front and rear to -1 to indicate the queue is now empty.

Let us trace through an example to understand better. Starting with an empty queue where front = -1 and rear = -1, we enqueue 10: rear becomes 0, queue[0] = 10, and front becomes 0. Enqueue 20: rear becomes 1, queue[1] = 20. Enqueue 30: rear becomes 2, queue[2] = 30. The queue now has front = 0 and rear = 2, with elements [10, 20, 30].

Now, we dequeue: element 10 is returned, front becomes 1. Dequeue again: element 20 is returned, front becomes 2. Dequeue again: element 30 is returned, front becomes 3. Since front > rear, we reset both to -1, and the queue is empty again.

### The Overflow and Underflow Problems

In array-based queue implementation, two critical issues arise:

**Overflow**: Occurs when attempting to enqueue an element into a full queue. In our linear implementation, overflow happens when rear == MAXSIZE - 1. This is a genuine limitation of fixed-size arrays.

**Underflow**: Occurs when attempting to dequeue or access front from an empty queue. Underflow happens when front == -1 or front > rear. This must be handled gracefully to prevent program crashes.

The key challenge with linear queue implementation is that even if elements are dequeued and space becomes available at the beginning of the array, we cannot use that space because rear has already reached the end. This is called "queue overflow" even when the queue logically has space—an inefficient scenario.

### Memory Representation

In C, a queue implemented using arrays can be represented with a structure containing the array, front index, rear index, and capacity. Here is a typical representation:

```c
#define MAXSIZE 100

typedef struct {
    int items[MAXSIZE];
    int front;
    int rear;
} Queue;
```

The front and rear indices track the queue state. When front equals rear, the queue could be either empty or full, depending on the implementation approach. Some implementations use a convention where front == rear indicates an empty queue, while (rear + 1) % MAXSIZE == front indicates a full queue—this is the circular queue approach, covered in the next chapter.

### Queue Applications

Queues appear in numerous computational scenarios:

**Breadth-First Search (BFS)**: Graph traversal algorithms use queues to explore vertices level by level. Starting from a source vertex, we enqueue all adjacent vertices, then process them in order.

**CPU Scheduling**: Operating systems use queues to manage processes waiting for CPU time. The ready queue holds processes ready to execute, while I/O waiting queues hold processes waiting for input/output operations.

**Print Queue**: When multiple users send documents to a network printer, a print queue ensures documents are printed in the order they were submitted.

**Breadth-First Traversal in Trees**: Level-order traversal of binary trees uses queues to visit nodes level by level, starting from the root.

**Task Scheduling**: Many applications use queues to manage background tasks, web requests, or message processing in a First-Come-First-Served manner.

**Simulation**: Queues model real-world waiting lines in simulation software, helping analyze customer wait times, service efficiency, and system performance.

## Examples

### Example 1: Simulating a Ticket Counter Queue

Consider a movie theater ticket counter where customers arrive at different times. We simulate this using a queue data structure to ensure fair service in order of arrival.

**Problem**: A ticket counter processes customers in FIFO order. At time intervals, new customers arrive, and the counter serves one customer. Write a program to simulate this process.

**Solution**:

```c
#include <stdio.h>
#include <string.h>
#define MAX 50

typedef struct {
    char name[30];
    int arrivalTime;
    int tickets;
} Customer;

typedef struct {
    Customer data[MAX];
    int front, rear;
} Queue;

void initQueue(Queue *q) {
    q->front = q->rear = -1;
}

int isEmpty(Queue *q) {
    return q->front == -1 || q->front > q->rear;
}

int isFull(Queue *q) {
    return q->rear == MAX - 1;
}

void enqueue(Queue *q, Customer c) {
    if (isFull(q)) {
        printf("Queue full, customer %s waiting...\n", c.name);
        return;
    }
    if (q->front == -1) q->front = 0;
    q->rear++;
    q->data[q->rear] = c;
    printf("Customer %s joined queue at time %d\n", c.name, c.arrivalTime);
}

Customer dequeue(Queue *q) {
    Customer empty = {"", -1, -1};
    if (isEmpty(q)) {
        printf("Queue empty\n");
        return empty;
    }
    Customer c = q->data[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = q->rear = -1;
    }
    return c;
}

int main() {
    Queue q;
    initQueue(&q);
    
    // Customers arriving at different times
    enqueue(&q, (Customer){"Alice", 1, 2});
    enqueue(&q, (Customer){"Bob", 2, 1});
    enqueue(&q, (Customer){"Charlie", 3, 3});
    
    printf("\nServing customers in order:\n");
    while (!isEmpty(&q)) {
        Customer c = dequeue(&q);
        printf("Serving %s (%d tickets)\n", c.name, c.tickets);
    }
    return 0;
}
```

This example demonstrates how queues maintain order and handle customer service fairly.

### Example 2: Queue Operations Trace

Given a queue with MAXSIZE = 5, trace through the following operations:

1. enqueue(10)
2. enqueue(20)
3. enqueue(30)
4. front()
5. dequeue()
6. dequeue()
7. enqueue(40)
8. enqueue(50)
9. enqueue(60)
10. dequeue()
11. isEmpty()

**Step-by-step solution**:

Initial state: front = -1, rear = -1, queue = []

1. enqueue(10): rear = 0, queue[0] = 10, front = 0
   Queue: [10], front = 0, rear = 0

2. enqueue(20): rear = 1, queue[1] = 20
   Queue: [10, 20], front = 0, rear = 1

3. enqueue(30): rear = 2, queue[2] = 30
   Queue: [10, 20, 30], front = 0, rear = 2

4. front(): Returns queue[0] = 10
   Output: 10

5. dequeue(): Returns 10, front becomes 1
   Queue: [20, 30], front = 1, rear = 2

6. dequeue(): Returns 20, front becomes 2
   Queue: [30], front = 2, rear = 2

7. enqueue(40): rear = 3, queue[3] = 40
   Queue: [30, 40], front = 2, rear = 3

8. enqueue(50): rear = 4, queue[4] = 50
   Queue: [30, 40, 50], front = 2, rear = 4

9. enqueue(60): Queue is full (rear = 4 = MAXSIZE - 1)
   Output: Queue Overflow

10. dequeue(): Returns 30, front becomes 3
    Queue: [40, 50], front = 3, rear = 4

11. isEmpty(): front (3) < rear (4), so queue is not empty
    Output: False (or 0)

### Example 3: Application in BFS Traversal

A queue is essential for breadth-first search. Given a graph represented as adjacency matrix, BFS uses a queue to visit all neighbors before moving to the next level.

**Algorithm**:
1. Start with source vertex, mark it visited, enqueue it
2. While queue is not empty:
   a. Dequeue vertex
   b. Visit all unvisited neighbors, mark them, enqueue them

For a simple graph with vertices 0, 1, 2, 3, 4 where edges exist between (0,1), (0,2), (1,3), (2,3), (3,4), starting BFS from vertex 0:
- Enqueue 0: Queue = [0]
- Dequeue 0, visit neighbors 1, 2: Enqueue 1, 2 → Queue = [1, 2]
- Dequeue 1, visit neighbor 3: Enqueue 3 → Queue = [2, 3]
- Dequeue 2 (no new neighbors): Queue = [3]
- Dequeue 3, visit neighbor 4: Enqueue 4 → Queue = [4]
- Dequeue 4: Queue = []

BFS Order: 0 → 1 → 2 → 3 → 4

## Exam Tips

For DU semester examinations, keep these essential points in mind:

1. **Remember FIFO Principle**: Always emphasize that queues follow First-In-First-Out ordering, unlike stacks which are LIFO. This distinction is frequently tested in conceptual questions.

2. **Index Manipulation**: The key operations involve manipulating front and rear indices correctly. Practice incrementing front dequeuing and rear when enqueuing.

3. **Empty when and Full Conditions**: Memorize the conditions for empty (front == -1 or front > rear) and full (rear == MAXSIZE - 1) states. Understand why resetting both indices to -1 when all elements are dequeued is necessary.

4. **Overflow vs Underflow**: Know when each error occurs—overflow when inserting into a full queue, underflow when deleting from an empty queue. Both must be handled to prevent undefined behavior.

5. **Queue vs Stack**: In exam questions, carefully read whether the problem describes queue or stack behavior. The key difference is removal order: queue removes from front, stack removes from top.

6. **Time Complexity**: All queue operations (enqueue, dequeue, front, isEmpty) are O(1) in constant time for array implementation. This is important for algorithm analysis questions.

7. **Applications Knowledge**: Be prepared to explain real-world applications of queues—print queues, CPU scheduling, BFS, and message passing systems. Such questions test your understanding of practical implementation.

8. **Initialization**: Always initialize front and rear to -1 when creating an empty queue. Failing to do so leads to unpredictable behavior.

9. **Circular Queue Preview**: Understand the limitation of linear queues (wasted space after dequeuing), as this leads naturally to the concept of circular queues covered in the next topic.

10. **Dry Run Practice**: Practice manual tracing of queue operations—examiners frequently ask you to show the state of queue after a sequence of operations.