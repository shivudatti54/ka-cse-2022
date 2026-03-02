# Queues: Abstract Data Type and Implementations

## Introduction

A **Queue** is one of the most fundamental abstract data types in computer science, representing a linear collection of elements that follows the **FIFO (First-In-First-Out)** principle. Just as people stand in a queue at a ticket counter, the first person to join the queue is the first one to be served. This characteristic makes queues essential for managing tasks in the order they arrive, ensuring fairness and systematic processing.

In the context of the University of Delhi's Data Structures curriculum, understanding queues is crucial because they form the backbone of many real-world computing applications. From operating system task scheduling to breadth-first search algorithms in graphs, from print job spooling to handling requests in web servers, queues are ubiquitous in computer science. This topic explores the queue as an abstract data type (ADT), its various implementations, and the trade-offs between them.

This module builds upon the concepts learned in previous topics, particularly arrays and linked lists, and provides the foundation for understanding more complex data structures like trees and graphs that frequently utilize queue operations.

## Key Concepts

### Queue as an Abstract Data Type

A queue is defined as an ordered collection of elements with two primary operations:
- **enqueue (or push)**: Add an element to the rear (tail) of the queue
- **dequeue (or pop)**: Remove and return the element from the front (head) of the queue

Additional operations typically include:
- **front (or peek)**: View the element at the front without removing it
- **isEmpty**: Check whether the queue contains any elements
- **size**: Return the number of elements in the queue

The queue ADT can be formally specified as:

```
Data: A linear sequence of elements
Operations:
- enqueue(x): Insert element x at the rear
- dequeue(): Remove and return the front element
- front(): Return the front element without removal
- isEmpty(): Return true if queue is empty, false otherwise
- size(): Return the number of elements
```

### Types of Queues

**Simple Queue (Linear Queue)**: The basic queue implementation where elements are arranged linearly and both pointers (front and rear) move forward during enqueue and dequeue operations. A significant drawback is that after several enqueue-dequeue cycles, the rear pointer reaches the end of the array even if there is empty space at the beginning—this is called "queue overflow" despite available memory.

**Circular Queue**: An optimized implementation where the front and rear pointers wrap around to the beginning of the array when they reach the end. This effectively utilizes the available space in the array. The circular queue is implemented using modular arithmetic: `rear = (rear + 1) % MAXSIZE` and `front = (front + 1) % MAXSIZE`.

**Priority Queue**: In this variant, each element is associated with a priority. Elements with higher priority are dequeued before elements with lower priority, regardless of their order of insertion. This is commonly implemented using a heap data structure.

**Double-Ended Queue (Deque)**: Allows insertion and deletion from both ends of the queue. It combines the properties of both stacks and queues.

### Array-Based Implementation (Linear Queue)

The simplest implementation uses a fixed-size array with two indices: `front` and `rear`. Initially, both are set to -1 (or 0 depending on convention). When enqueueing, we increment `rear` and place the element at that index. When dequeueing, we increment `front` and return the element at that index.

**Pseudocode for Array-based Queue**:

```python
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if self.rear == self.capacity - 1:
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.array[self.rear] = item
    
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return None
        item = self.array[self.front]
        self.front += 1
        return item
```

### Circular Queue Implementation

Circular queues solve the space utilization problem of linear queues by treating the array as circular. The key difference is how we check for overflow and empty conditions, and how we calculate the next position using modulo operator.

**Key conditions for circular queue**:
- **Empty condition**: `front == -1` or `front == (rear + 1) % MAXSIZE` (depending on implementation)
- **Full condition**: `(rear + 1) % MAXSIZE == front`
- **Queue size**: `(rear - front + MAXSIZE) % MAXSIZE + 1`

### Linked List-Based Implementation

Using a linked list, we can implement a dynamic queue that can grow and shrink as needed. In this implementation:
- Each node contains data and a pointer to the next node
- The `front` pointer points to the node at the head (for dequeue)
- The `rear` pointer points to the node at the tail (for enqueue)

This implementation avoids the fixed-size limitation of arrays and provides efficient O(1) time complexity for both enqueue and dequeue operations.

### Time Complexity Analysis

| Operation | Array (Linear) | Array (Circular) | Linked List |
|-----------|---------------|------------------|-------------|
| enqueue   | O(1)          | O(1)             | O(1)        |
| dequeue   | O(1)          | O(1)             | O(1)        |
| front     | O(1)          | O(1)             | O(1)        |
| isEmpty   | O(1)          | O(1)             | O(1)        |

The linked list implementation provides O(1) for all operations because we maintain direct pointers to both ends. The linear array implementation has O(n) space utilization issue but O(1) time for operations.

## Examples

### Example 1: Simulating Customer Service at a Bank

**Problem**: A bank has a single counter where customers arrive for service. Customers are served in the order they arrive. Simulate this using a queue data structure with the following operations:
1. Customer A arrives (enqueue)
2. Customer B arrives (enqueue)
3. Customer C arrives (enqueue)
4. First customer is served (dequeue)
5. Customer D arrives (enqueue)
6. Second customer is served (dequeue)

**Solution**: Let us trace through the queue operations step by step.

Initially: Queue = [ ], front = -1, rear = -1

Step 1 (A arrives): Queue = [A], front = 0, rear = 0

Step 2 (B arrives): Queue = [A, B], front = 0, rear = 1

Step 3 (C arrives): Queue = [A, B, C], front = 0, rear = 2

Step 4 (A served): Dequeue A → Queue = [B, C], front = 1, rear = 2. A is served.

Step 5 (D arrives): Queue = [B, C, D], front = 1, rear = 3

Step 6 (B served): Dequeue B → Queue = [C, D], front = 2, rear = 3. B is served.

**Result**: The order of service is A, then B—exactly matching the FIFO principle.

### Example 2: Implementing a Circular Queue

**Problem**: Implement a circular queue with capacity 5 and perform the following operations: enqueue(10), enqueue(20), enqueue(30), dequeue(), dequeue(), enqueue(40), enqueue(50), enqueue(60), enqueue(70).

**Solution**:

MAXSIZE = 5, initial state: front = 0, rear = -1, Queue array initialized

1. **enqueue(10)**: rear = (rear + 1) % 5 = 0; Queue[0] = 10
2. **enqueue(20)**: rear = 1; Queue[1] = 20
3. **enqueue(30)**: rear = 2; Queue[2] = 30
4. **dequeue()**: element = Queue[0] = 10; front = (front + 1) % 5 = 1
5. **dequeue()**: element = Queue[1] = 20; front = 2
   - Queue state: [ -, -, 30, -, - ], front = 2, rear = 2
6. **enqueue(40)**: rear = 3; Queue[3] = 40
7. **enqueue(50)**: rear = 4; Queue[4] = 50
8. **enqueue(60)**: rear = (4 + 1) % 5 = 0; Queue[0] = 60
   - Check: (rear + 1) % MAXSIZE == front → (0 + 1) % 5 = 1 ≠ front (2), so queue not full
9. **enqueue(70)**: rear = 1; Queue[1] = 70
   - Check: (1 + 1) % 5 = 2 == front, so queue is now FULL

**Final State**: Queue = [60, 70, 30, 40, 50], front = 2, rear = 1, FULL

### Example 3: Application in Breadth-First Search (BFS)

**Problem**: Demonstrate how a queue is used in BFS traversal of a graph starting from node A.

**Graph Structure**:
```
    A
   / \
  B   C
 / \   \
D   E   F
```

**Solution**: BFS uses a queue to explore nodes level by level.

1. Start: Enqueue starting node A → Queue = [A], visited = {A}
2. Dequeue A, visit neighbors B, C → Queue = [B, C], visited = {A, B, C}
3. Dequeue B, visit neighbors D, E → Queue = [C, D, E], visited = {A, B, C, D, E}
4. Dequeue C, visit neighbor F → Queue = [D, E, F], visited = {A, B, C, D, E, F}
5. Dequeue D (no unvisited neighbors) → Queue = [E, F]
6. Dequeue E (no unvisited neighbors) → Queue = [F]
7. Dequeue F (no unvisited neighbors) → Queue = [ ]

**BFS Order**: A → B → C → D → E → F

This demonstrates the queue's critical role in level-order traversal, which is essential for finding shortest paths in unweighted graphs.

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Understand the difference between linear and circular queues**: Circular queues solve the space wastage problem in linear queues by allowing the rear pointer to wrap around. Know when each is appropriate.

2. **Master the overflow and underflow conditions**: For linear queues, overflow occurs when rear = MAXSIZE - 1. For circular queues, overflow occurs when (rear + 1) % MAXSIZE == front. Underflow occurs when front > rear (linear) or front == rear (circular with a flag).

3. **Know all time complexities**: In interviews and exams, you must be able to state the time complexity for enqueue, dequeue, front, and isEmpty operations for each implementation type.

4. **Practice circular queue calculations**: The modular arithmetic is often tested. Remember: `(rear - front + MAXSIZE) % MAXSIZE + 1` gives the current size.

5. **Differentiate between Queue ADT and its implementation**: The ADT defines the logical behavior (FIFO), while implementations (array, linked list, circular) are different ways to achieve this behavior.

6. **Real-world applications are important**: Be prepared to explain where queues are used (CPU scheduling, BFS, print spooling, message queues).

7. **Understand space complexity**: Array-based implementations have fixed space O(n), while linked list implementations use O(n) space but with additional memory overhead for pointers.