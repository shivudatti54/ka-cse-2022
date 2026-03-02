# QUEUES

## Introduction

A queue is one of the most fundamental data structures in computer science, embodying the principle of "First In, First Out" (FIFO). Just as people stand in a queue at a ticket counter or a bus stop, the first element added to a queue is the first one to be removed. This ordering property makes queues essential for managing tasks in the order they arrive, ensuring fairness and maintaining sequence in numerous computational scenarios.

In the context of the University of Delhi's Computer Science curriculum, understanding queues is crucial because they form the backbone of many algorithms and system designs. From operating system process scheduling to breadth-first search in graphs, from handling requests in web servers to simulating real-world scenarios, queues appear everywhere. The linear queue, which we will explore in depth, serves as the foundation upon which more complex queue variants like circular queues and priority queues are built.

This topic requires careful study because students often confuse queue operations with those of stacks. While stacks follow LIFO (Last In, First Out), queues maintain strict FIFO ordering. Understanding this fundamental difference, along with proper implementation details, will help you solve problems effectively in your end semester examinations.

## Key Concepts

### Definition of a Queue

A queue is a linear data structure that follows the FIFO (First In, First Out) principle. Elements are added at one end called the REAR (or tail) and removed from the other end called the FRONT (or head). The queue resembles a real-world queue where the person who arrives first gets served first.

Mathematically, a queue Q of size n can be defined as Q = {q₁, q₂, q₃, ..., qₙ} where:
- q₁ is the front element (first to be removed)
- qₙ is the rear element (last to be added)
- Operations maintain the order: if i < j, then qᵢ was added before qⱼ

### Queue Abstract Data Type (ADT)

The Queue ADT defines the interface that any queue implementation must provide:

**Basic Operations:**
- `enqueue(element)` or `insert(element)`: Adds an element to the rear of the queue
- `dequeue()` or `delete()`: Removes and returns the element from the front of the queue
- `front()` or `peek()`: Returns the front element without removing it
- `rear()`: Returns the rear element without removing it
- `isEmpty()`: Returns true if queue contains no elements
- `isFull()`: Returns true if queue has reached maximum capacity (for array implementation)
- `size()`: Returns the number of elements in the queue

### Array Implementation of Queues

The sequential (array) implementation uses a one-dimensional array to store queue elements. Two indices track the front and rear positions.

**Data Members:**
- `MAXSIZE`: Maximum capacity of the queue
- `queue[]`: Array to store elements
- `front`: Index of the front element
- `rear`: Index of the rear element

**Initial State:**
```
front = -1
rear = -1
```

**Algorithm for enqueue(element):**
```
Step 1: If rear = MAXSIZE - 1, then:
        Print "Queue Overflow" and return
Step 2: If front = -1, then:
        front = 0
Step 3: rear = rear + 1
Step 4: queue[rear] = element
Step 5: Return element
```

**Algorithm for dequeue():**
```
Step 1: If front = -1 OR front > rear, then:
        Print "Queue Underflow" and return
Step 2: element = queue[front]
Step 3: front = front + 1
Step 4: If front > rear, then:
        Reset front = -1, rear = -1
Step 5: Return element
```

**Algorithm for front():**
```
Step 1: If front = -1 OR front > rear, then:
        Queue is empty, return special value
Step 2: Return queue[front]
```

### Linked List Implementation of Queues

Dynamic implementation using linked lists overcomes the fixed size limitation of array implementation. Each node contains data and a pointer to the next node.

**Node Structure:**
```
struct Node {
    int data;
    struct Node* next;
}
```

**Data Members:**
- `front`: Pointer to the first node (head)
- `rear`: Pointer to the last node (tail)

**Advantages over Array Implementation:**
- No fixed size limitation
- Memory is allocated dynamically
- No wastage of memory space

**Algorithm for enqueue(element):**
```
Step 1: Create newNode with given element
Step 2: newNode->next = NULL
Step 3: If front = NULL, then:
        front = newNode
        rear = newNode
     Else:
        rear->next = newNode
        rear = newNode
```

**Algorithm for dequeue():**
```
Step 1: If front = NULL, then:
        Print "Queue Underflow" and return
Step 2: temp = front
Step 3: element = temp->data
Step 4: front = front->next
Step 5: If front = NULL, then:
        rear = NULL
Step 6: free(temp)
Step 7: Return element
```

### Applications of Queues

Queues are used extensively in computer science and real-world applications:

1. **CPU Scheduling**: Operating systems use queues to manage processes waiting for CPU time. The ready queue holds processes waiting to be executed.

2. **Disk Scheduling**: Disk I/O requests are queued to optimize access time and reduce seek operations.

3. **Breadth-First Search (BFS)**: Queue is the fundamental data structure used in BFS algorithms for graph traversal.

4. **Print Spooling**: Multiple print jobs are queued and processed in order of arrival.

5. **Web Server Request Handling**: Incoming HTTP requests are queued and processed by server threads.

6. **Call Center Systems**: Customer calls are placed in queues until service representatives become available.

7. **Simulation**: Queues model real-world scenarios like traffic flow, customer checkout lines, and airline check-in counters.

### Queue Variations

While the basic queue follows FIFO, several variations exist:

- **Priority Queue**: Elements are removed based on priority rather than arrival order
- **Double-Ended Queue (Deque)**: Elements can be added or removed from both ends
- **Circular Queue**: The array is treated as circular to efficiently utilize space

## Examples

### Example 1: Array Queue Operations

Consider a queue with MAXSIZE = 5. Perform the following operations step by step:

**Operations:**
1. enqueue(10)
2. enqueue(20)
3. enqueue(30)
4. front()
5. dequeue()
6. enqueue(40)
7. enqueue(50)
8. enqueue(60)

**Solution:**

Initially: front = -1, rear = -1, queue = [_, _, _, _, _]

1. **enqueue(10)**:
   - rear = 0, queue[0] = 10
   - front = 0 (since it was -1)
   - Queue: [10, _, _, _, _]

2. **enqueue(20)**:
   - rear = 1, queue[1] = 20
   - Queue: [10, 20, _, _, _]

3. **enqueue(30)**:
   - rear = 2, queue[2] = 30
   - Queue: [10, 20, 30, _, _]

4. **front()**: Returns queue[front] = queue[0] = 10

5. **dequeue()**:
   - element = queue[0] = 10
   - front = 1
   - Queue: [_, 20, 30, _, _]

6. **enqueue(40)**:
   - rear = 3, queue[3] = 40
   - Queue: [_, 20, 30, 40, _]

7. **enqueue(50)**:
   - rear = 4, queue[4] = 50
   - Queue: [_, 20, 30, 40, 50]

8. **enqueue(60)**:
   - Since rear = 4 = MAXSIZE - 1, Queue Overflow!

**Final State:** Queue contains [_, 20, 30, 40, 50], front = 1, rear = 4

### Example 2: Linked Queue Operations

Consider an empty linked queue. Perform the following operations:

1. enqueue(5)
2. enqueue(15)
3. enqueue(25)
4. dequeue()
5. dequeue()

**Solution:**

1. **enqueue(5)**:
   - Create node with data = 5
   - front = rear = node1
   - Queue: 5 → NULL

2. **enqueue(15)**:
   - Create node with data = 15
   - rear->next = node2, rear = node2
   - Queue: 5 → 15 → NULL

3. **enqueue(25)**:
   - Create node with data = 25
   - rear->next = node3, rear = node3
   - Queue: 5 → 15 → 25 → NULL

4. **dequeue()**:
   - element = 5 (front->data)
   - front = front->next (pointing to node2)
   - Free original node1
   - Queue: 15 → 25 → NULL
   - Returns: 5

5. **dequeue()**:
   - element = 15
   - front = front->next (pointing to node3)
   - Free node2
   - Queue: 25 → NULL
   - rear still points to node3
   - Returns: 15

**Final State:** Queue contains 25, front points to node3, rear points to node3

### Example 3: Application - BFS Traversal

Given a graph with vertices {A, B, C, D, E} and edges: A-B, A-C, B-D, C-D, use BFS starting from vertex A. Show how queue is used.

**Solution:**

**Step 1:** Start with vertex A in queue
- Queue: [A], Visited: {A}

**Step 2:** Dequeue A, add unvisited neighbors B and C
- Queue: [B, C], Visited: {A, B, C}

**Step 3:** Dequeue B, add unvisited neighbor D
- Queue: [C, D], Visited: {A, B, C, D}

**Step 4:** Dequeue C, D already visited
- Queue: [D], Visited: {A, B, C, D}

**Step 5:** Dequeue D, E not connected
- Queue: [], Visited: {A, B, C, D}

**BFS Order:** A, B, C, D

This demonstrates how queue ensures vertices are processed in order of their distance from the source vertex.

## Exam Tips

For your DU semester examinations, keep these essential points in mind:

1. **Distinguish Queue from Stack**: Remember queues use TWO pointers (front and rear) while stacks use only ONE pointer (top). Queue removes from FRONT, adds at REAR.

2. **Initial Conditions Matter**: Always initialize front and rear to -1 for array implementation. A common mistake is forgetting to reset both pointers when the queue becomes empty after multiple operations.

3. **Overflow vs Underflow**: Queue Overflow occurs when trying to add to a full queue (rear = MAXSIZE - 1). Queue Underflow occurs when trying to remove from an empty queue (front = -1 or front > rear).

4. **Wasted Space Problem**: In array implementation, after several dequeues, the front index moves forward potentially leaving unused space at the beginning. This is why circular queues are introduced as an optimization.

5. **Linked vs Array Implementation**: Array implementation has O(1) time for all operations but fixed size. Linked implementation has dynamic size but requires extra memory for pointers.

6. **Write Operations Precisely**: In exams, always show the step-by-step changes to front, rear, and the queue contents after each operation.

7. **Time Complexity**: For both implementations, enqueue and dequeue operations take O(1) constant time, making queues efficient for FIFO operations.

8. **Understand Queue States**: Practice identifying queue states - empty queue (front = -1 or front > rear), full queue (rear = MAXSIZE - 1), and partially filled queue.

9. **Application-Based Questions**: Be prepared to explain or trace through queue applications like BFS, print spooling, or CPU scheduling.

10. **Reset Logic**: After dequeue, if front exceeds rear, reset both front and rear to -1 to mark the queue as empty, otherwise subsequent operations may fail incorrectly.