# Queues: Implementations

## Introduction

A **queue** is one of the most fundamental abstract data types in computer science, modeling the real-world concept of people waiting in a line. Just as the first person to join a line receives service first, the first element inserted into a queue is the first one to be removed. This First-In-First-Out (FIFO) principle makes queues essential for managing tasks in operating systems, scheduling processes, handling requests in web servers, and implementing breadth-first search algorithms in graph theory.

In the context of the University of Delhi's Data Structures curriculum, understanding queues and their implementations is crucial for developing efficient algorithms. Unlike stacks which follow LIFO (Last-In-First-Out), queues ensure fair ordering of elements. The significance of queues extends beyond theoretical computer science—they are extensively used in printer spooling, CPU task scheduling, breadth-first traversal of trees and graphs, and message queuing systems in distributed computing.

This topic explores the queue data structure in depth, examining both array-based and linked list implementations, analyzing their time and space complexities, and understanding when to use each approach. We will also examine variations like circular queues and priority queues, which address limitations of the basic queue implementation.

## Key Concepts

### Queue as an Abstract Data Type

A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle. Elements are added at one end called the **rear** (or tail) and removed from the other end called the **front** (or head). The fundamental operations on a queue are:

1. **enqueue(item)**: Adds an element to the rear of the queue
2. **dequeue()**: Removes and returns the element at the front of the queue
3. **front()**: Returns the element at the front without removing it
4. **rear()**: Returns the element at the rear without removing it
5. **isEmpty()**: Returns true if the queue contains no elements
6. **isFull()**: Returns true if the queue cannot accommodate more elements

### Array Implementation of Queues

The simplest implementation uses a fixed-size array with two pointers: `front` and `rear`. The `front` pointer tracks the position from which elements will be dequeued, while the `rear` pointer tracks the position where new elements will be inserted.

**Structure Definition:**
```c
#define MAXSIZE 100
typedef struct {
    int items[MAXSIZE];
    int front;
    int rear;
} Queue;
```

**Initialization:**
```c
void initialize(Queue *q) {
    q->front = -1;
    q->rear = -1;
}
```

**Enqueue Operation:**
```c
int enqueue(Queue *q, int item) {
    if (q->rear == MAXSIZE - 1) {
        return 0; // Queue overflow
    }
    if (q->front == -1) {
        q->front = 0;
    }
    q->rear++;
    q->items[q->rear] = item;
    return 1; // Success
}
```

**Dequeue Operation:**
```c
int dequeue(Queue *q, int *item) {
    if (q->front == -1 || q->front > q->rear) {
        return 0; // Queue underflow
    }
    *item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        // Reset queue when empty
        q->front = -1;
        q->rear = -1;
    }
    return 1;
}
```

**Limitations of Linear Queue**: In a linear queue implementation, after several enqueue and dequeue operations, the `rear` pointer reaches the end of the array even if there are empty slots at the beginning. This phenomenon is called "queue overflow" despite having available space—a significant drawback.

### Circular Queue Implementation

The **circular queue** (or ring buffer) solves the limitation of linear queues by connecting the end of the array back to the beginning, forming a circle. When the rear reaches the end of the array, it wraps around to the beginning if space is available.

**Circular Queue Structure:**
```c
typedef struct {
    int items[MAXSIZE];
    int front;
    int rear;
    int size;
} CircularQueue;
```

**Key Differences:**
- `front` always points to the position before the first element
- `rear` always points to the last element
- A queue is empty when `front == -1`
- A queue is full when `(rear + 1) % MAXSIZE == front`

**Circular Enqueue:**
```c
int cir_enqueue(CircularQueue *q, int item) {
    if ((q->rear + 1) % MAXSIZE == q->front) {
        return 0; // Queue full
    }
    if (q->front == -1) {
        q->front = 0;
        q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % MAXSIZE;
    }
    q->items[q->rear] = item;
    q->size++;
    return 1;
}
```

**Circular Dequeue:**
```c
int cir_dequeue(CircularQueue *q, int *item) {
    if (q->front == -1) {
        return 0; // Queue empty
    }
    *item = q->items[q->front];
    if (q->front == q->rear) {
        // Last element being removed
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAXSIZE;
    }
    q->size--;
    return 1;
}
```

### Linked List Implementation of Queue

Linked list implementation provides dynamic memory allocation, eliminating the fixed-size limitation of array-based queues. Each node contains data and a pointer to the next node.

**Node Structure:**
```c
typedef struct node {
    int data;
    struct node *next;
} Node;

typedef struct {
    Node *front;
    Node *rear;
    int count;
} LinkedQueue;
```

**Enqueue Operation:**
```c
void lq_enqueue(LinkedQueue *q, int item) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = item;
    newNode->next = NULL;
    
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
    q->count++;
}
```

**Dequeue Operation:**
```c
int lq_dequeue(LinkedQueue *q, int *item) {
    if (q->front == NULL) {
        return 0; // Queue underflow
    }
    Node *temp = q->front;
    *item = temp->data;
    q->front = temp->next;
    
    if (q->front == NULL) {
        q->rear = NULL;
    }
    free(temp);
    q->count--;
    return 1;
}
```

### Priority Queue

A **priority queue** is a specialized queue where each element has an associated priority. Elements with higher priority are dequeued before elements with lower priority, regardless of their order of insertion. In case of equal priority, FIFO order is maintained.

Priority queues are typically implemented using:
1. **Array/Linked List**: Simple but inefficient for large datasets
2. **Binary Heap**: Most common implementation with O(log n) enqueue and dequeue
3. **Binary Search Tree**: Provides balanced performance

Priority queues are extensively used in Dijkstra's shortest path algorithm, Prim's minimum spanning tree algorithm, task scheduling in operating systems, and Huffman coding for data compression.

## Examples

### Example 1: Simulating Customer Service Queue

**Problem**: A bank service counter uses a queue to manage customer requests. Write a program to simulate this queue with 5 customers arriving and being served.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 10

typedef struct {
    int items[MAX];
    int front, rear;
} Queue;

void init(Queue *q) {
    q->front = q->rear = -1;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

int isFull(Queue *q) {
    return q->rear == MAX - 1;
}

void enqueue(Queue *q, int id) {
    if (isFull(q)) {
        printf("Queue overflow!\n");
        return;
    }
    if (q->front == -1) q->front = 0;
    q->rear++;
    q->items[q->rear] = id;
    printf("Customer %d joined the queue\n", id);
}

int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue underflow!\n");
        return -1;
    }
    int item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = q->rear = -1;
    }
    return item;
}

int main() {
    Queue q;
    init(&q);
    
    // Customers arriving
    printf("=== Customers arriving ===\n");
    enqueue(&q, 101);
    enqueue(&q, 102);
    enqueue(&q, 103);
    enqueue(&q, 104);
    enqueue(&q, 105);
    
    // Customers being served
    printf("\n=== Serving customers (FIFO) ===\n");
    while (!isEmpty(&q)) {
        int customer = dequeue(&q);
        printf("Serving customer %d\n", customer);
    }
    
    return 0;
}
```

**Output:**
```
=== Customers arriving ===
Customer 101 joined the queue
Customer 102 joined the queue
Customer 103 joined the queue
Customer 104 joined the queue
Customer 105 joined the queue

=== Serving customers (FIFO) ===
Serving customer 101
Serving customer 102
Serving customer 103
Serving customer 104
Serving customer 105
```

### Example 2: Circular Queue Demonstration

**Problem**: Implement a circular queue of size 5 and demonstrate how it handles wrap-around.

**Solution:**

```c
#include <stdio.h>
#define SIZE 5

typedef struct {
    int data[SIZE];
    int front, rear;
} CircularQueue;

void cir_init(CircularQueue *q) {
    q->front = q->rear = -1;
}

int cir_isFull(CircularQueue *q) {
    return (q->rear + 1) % SIZE == q->front;
}

int cir_isEmpty(CircularQueue *q) {
    return q->front == -1;
}

void cir_enqueue(CircularQueue *q, int val) {
    if (cir_isFull(q)) {
        printf("Queue is full!\n");
        return;
    }
    if (q->front == -1) {
        q->front = q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % SIZE;
    }
    q->data[q->rear] = val;
    printf("Enqueued: %d (front=%d, rear=%d)\n", val, q->front, q->rear);
}

int cir_dequeue(CircularQueue *q) {
    if (cir_isEmpty(q)) {
        printf("Queue is empty!\n");
        return -1;
    }
    int val = q->data[q->front];
    if (q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front = (q->front + 1) % SIZE;
    }
    return val;
}

int main() {
    CircularQueue q;
    cir_init(&q);
    
    printf("=== Adding 5 elements ===\n");
    for (int i = 1; i <= 5; i++) {
        cir_enqueue(&q, i * 10);
    }
    
    printf("\n=== Trying to add 6th element ===\n");
    cir_enqueue(&q, 60);
    
    printf("\n=== Removing 3 elements ===\n");
    for (int i = 0; i < 3; i++) {
        printf("Dequeued: %d\n", cir_dequeue(&q));
    }
    
    printf("\n=== Adding 3 more elements (wrap-around) ===\n");
    cir_enqueue(&q, 70);
    cir_enqueue(&q, 80);
    cir_enqueue(&q, 90);
    
    printf("\n=== Final state ===\n");
    printf("Front index: %d, Rear index: %d\n", q.front, q.rear);
    
    return 0;
}
```

### Example 3: Application - Breadth-First Search (BFS)

**Problem**: Use a queue to implement BFS traversal on a graph.

**Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    int items[MAX];
    int front, rear;
} Queue;

void init(Queue *q) {
    q->front = q->rear = -1;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

void enqueue(Queue *q, int v) {
    if (q->front == -1) q->front = 0;
    q->items[++q->rear] = v;
}

int dequeue(Queue *q) {
    return q->items[q->front++];
}

// BFS function
void BFS(int graph[MAX][MAX], int vertices, int start) {
    int visited[MAX] = {0};
    Queue q;
    init(&q);
    
    visited[start] = 1;
    enqueue(&q, start);
    
    printf("BFS Traversal: ");
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);
        
        for (int i = 0; i < vertices; i++) {
            if (graph[v][i] && !visited[i]) {
                visited[i] = 1;
                enqueue(&q, i);
            }
        }
    }
    printf("\n");
}

int main() {
    int vertices = 6;
    int graph[MAX][MAX] = {0};
    
    // Add edges (undirected graph)
    int edges[][2] = {{0,1}, {0,2}, {1,3}, {1,4}, {2,4}, {3,5}, {4,5}};
    int numEdges = 7;
    
    for (int i = 0; i < numEdges; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        graph[u][v] = graph[v][u] = 1;
    }
    
    BFS(graph, vertices, 0);
    
    return 0;
}
```

## Exam Tips

1. **Remember the fundamental difference**: In a stack, you add and remove from the same end (top), but in a queue, you add at the rear and remove from the front. This FIFO principle is frequently tested in conceptual questions.

2. **Time complexity matters**: For array-based implementations, enqueue and dequeue are O(1) operations. For linked list implementation, both operations remain O(1). However, circular queues provide space efficiency by utilizing the entire array.

3. **Circular queue conditions**: 
   - Empty: `front == -1`
   - Full: `(rear + 1) % MAXSIZE == front`
   - Never forget the modulo operation when calculating the new rear position.

4. **Common errors to avoid**: 
   - Forgetting to check for overflow before enqueue
   - Forgetting to check for underflow before dequeue  
   - In circular queues, using `rear == MAXSIZE - 1` instead of modular arithmetic

5. **Queue vs Stack applications**: Remember that stacks are used for depth-first search (DFS), expression evaluation, and backtracking. Queues are used for breadth-first search (BFS), level-order tree traversal, and resource scheduling.

6. **Memory considerations**: Array implementation has a fixed maximum size, while linked list implementation can grow dynamically but requires extra memory for storing pointers.

7. **Understand queue underflow and overflow**: Underflow occurs when attempting to remove from an empty queue; overflow occurs when attempting to add to a full queue. Always handle these conditions in practical implementations.

8. **For priority queues**: Elements are removed based on priority, not arrival order. Higher priority elements are dequeued first. This is a common exam topic.