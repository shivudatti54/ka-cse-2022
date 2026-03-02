# **INTRODUCTION TO QUEUES**

Queues are a fundamental data structure in computer science, used to manage a collection of elements in a First-In-First-Out (FIFO) order. The concept of a queue dates back to the early days of computer science, when it was used in punch card systems to manage the order in which cards were processed.

## **HISTORICAL CONTEXT**

In the early 20th century, the concept of a queue was first introduced in the context of postal services. The United States Postal Service used a queue to manage the order in which mail was delivered. Similarly, in the context of computer science, queues were used in the early days of computer networks to manage the order in which packets were transmitted.

## **QUEUE OPERATIONS**

A queue is a data structure that supports the following operations:

- **Enqueue**: adds an element to the end of the queue.
- **Dequeue**: removes an element from the front of the queue.
- **Peek**: returns the element at the front of the queue without removing it.
- **IsEmpty**: checks if the queue is empty.

## **QUEUE IMPLEMENTATION USING ARRAYS**

One common implementation of a queue using arrays is through the use of a circular buffer. Here's an example implementation:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* elements;
    int front;
    int rear;
    int size;
    int capacity;
} Queue;

Queue* createQueue(int capacity) {
    Queue* q = (Queue*) malloc(sizeof(Queue));
    q->elements = (int*) malloc(sizeof(int) * capacity);
    q->front = 0;
    q->rear = 0;
    q->size = 0;
    q->capacity = capacity;
    return q;
}

int enqueue(Queue* q, int element) {
    if (q->size == q->capacity) {
        printf("Queue is full\n");
        return -1;
    }
    q->elements[q->rear] = element;
    q->rear = (q->rear + 1) % q->capacity;
    q->size++;
    return 0;
}

int dequeue(Queue* q) {
    if (q->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int element = q->elements[q->front];
    q->elements[q->front] = 0;
    q->front = (q->front + 1) % q->capacity;
    q->size--;
    return element;
}
```

This implementation uses a circular buffer to store the elements of the queue. The `enqueue` function adds an element to the end of the queue, while the `dequeue` function removes an element from the front of the queue.

## **DIFFERENT TYPES OF QUEUES**

### Circular Queues

A circular queue is a type of queue where the last element is connected to the first element, forming a circle. This type of queue is useful in scenarios where the last element needs to be accessed frequently.

Here's an example implementation of a circular queue:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* elements;
    int front;
    int rear;
    int size;
    int capacity;
} CircularQueue;

CircularQueue* createCircularQueue(int capacity) {
    CircularQueue* q = (CircularQueue*) malloc(sizeof(CircularQueue));
    q->elements = (int*) malloc(sizeof(int) * capacity);
    q->front = 0;
    q->rear = 0;
    q->size = 0;
    q->capacity = capacity;
    return q;
}

int enqueue(CircularQueue* q, int element) {
    if (q->size == q->capacity) {
        printf("Queue is full\n");
        return -1;
    }
    q->elements[q->rear] = element;
    q->rear = (q->rear + 1) % q->capacity;
    q->size++;
    return 0;
}

int dequeue(CircularQueue* q) {
    if (q->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int element = q->elements[q->front];
    q->elements[q->front] = 0;
    q->front = (q->front + 1) % q->capacity;
    q->size--;
    return element;
}
```

### Double-Ended Queues

A double-ended queue is a type of queue that allows elements to be added and removed from both ends.

Here's an example implementation of a double-ended queue:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* elements;
    int front;
    int rear;
    int size;
    int capacity;
} DoubleEndedQueue;

DoubleEndedQueue* createDoubleEndedQueue(int capacity) {
    DoubleEndedQueue* q = (DoubleEndedQueue*) malloc(sizeof(DoubleEndedQueue));
    q->elements = (int*) malloc(sizeof(int) * capacity);
    q->front = 0;
    q->rear = 0;
    q->size = 0;
    q->capacity = capacity;
    return q;
}

int enqueue(DoubleEndedQueue* q, int element) {
    if (q->size == q->capacity) {
        printf("Queue is full\n");
        return -1;
    }
    q->elements[q->rear] = element;
    q->rear = (q->rear + 1) % q->capacity;
    q->size++;
    return 0;
}

int dequeue(DoubleEndedQueue* q) {
    if (q->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int element = q->elements[q->front];
    q->elements[q->front] = 0;
    q->front = (q->front + 1) % q->capacity;
    q->size--;
    return element;
}

int dequeueFromRight(DoubleEndedQueue* q) {
    if (q->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int element = q->elements[q->rear - 1];
    q->elements[q->rear - 1] = 0;
    q->rear--;
    q->size--;
    return element;
}
```

### Priority Queue

A priority queue is a type of queue where elements are ordered based on their priority.

Here's an example implementation of a priority queue:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* elements;
    int size;
} PriorityQueue;

PriorityQueue* createPriorityQueue() {
    PriorityQueue* q = (PriorityQueue*) malloc(sizeof(PriorityQueue));
    q->elements = (int*) malloc(sizeof(int));
    q->size = 0;
    return q;
}

int enqueue(PriorityQueue* q, int element, int priority) {
    q->elements = realloc(q->elements, sizeof(int) * (q->size + 1));
    q->elements[q->size] = element;
    q->elements[q->size + 1] = priority;
    q->size++;
    quicksort(q->elements, 0, q->size - 1);
    return 0;
}

int dequeue(PriorityQueue* q) {
    if (q->size == 0) {
        printf("Queue is empty\n");
        return -1;
    }
    int element = q->elements[0];
    q->elements = realloc(q->elements, sizeof(int) * (q->size - 1));
    q->size--;
    qsort(q->elements, 0, q->size - 1);
    return element;
}

void quicksort(int* arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quicksort(arr, low, pivot - 1);
        quicksort(arr, pivot + 1, high);
    }
}

int partition(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}
```

## **CASE STUDIES AND APPLICATIONS**

### Job Scheduling

A job scheduling problem is a classic example of a priority queue. In this problem, we have a set of jobs that need to be executed on a computer. Each job has a priority level associated with it, and we need to schedule the jobs in the order of their priority levels.

### Network Routing

In network routing, we have a set of nodes that need to be connected. We can use a priority queue to schedule the nodes in the order of their priority levels. The node with the highest priority level gets connected first.

### Database Query Optimization

In database query optimization, we have a set of queries that need to be executed on a database. We can use a priority queue to schedule the queries in the order of their priority levels.

### Real-Time Systems

In real-time systems, we have a set of tasks that need to be executed within a certain time limit. We can use a priority queue to schedule the tasks in the order of their priority levels.

## **FURTHER READING**

- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms in C++" by Robert Sedgewick and Kevin Wayne
- "The Art of Computer Programming" by Donald E. Knuth
- "Algorithms" by Robert Sedgewick and Kevin Wayne

## **DIAGRAMS AND FIGURES**

- A diagram of a queue and its operations
- A diagram of a circular queue
- A diagram of a double-ended queue
- A diagram of a priority queue

## **CONCLUSION**

In conclusion, queues are a fundamental data structure in computer science, and they have a wide range of applications in real-world systems. In this article, we have discussed the concept of queues, their operations, and different types of queues such as circular queues, double-ended queues, and priority queues. We have also provided example implementations of these queues and discussed case studies and applications of queues.
