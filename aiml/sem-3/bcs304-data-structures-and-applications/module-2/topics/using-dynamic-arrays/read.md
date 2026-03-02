# Queues Using Dynamic Arrays


## Table of Contents

- [Queues Using Dynamic Arrays](#queues-using-dynamic-arrays)
- [1. Introduction](#1-introduction)
- [2. Limitations of Fixed-Size Queue Implementations](#2-limitations-of-fixed-size-queue-implementations)
  - [2.1 Overflow Condition](#21-overflow-condition)
  - [2.2 Wasted Memory in Linear Queues](#22-wasted-memory-in-linear-queues)
  - [2.3 Capacity Selection Problem](#23-capacity-selection-problem)
- [3. Circular Queue: Foundation for Dynamic Implementation](#3-circular-queue-foundation-for-dynamic-implementation)
  - [3.1 Mathematical Formulation](#31-mathematical-formulation)
- [4. Dynamic Circular Queue: Design Principles](#4-dynamic-circular-queue-design-principles)
  - [4.1 Doubling Strategy: Theoretical Justification](#41-doubling-strategy-theoretical-justification)
  - [4.2 Data Structure Definition](#42-data-structure-definition)
- [5. Complete Implementation in C](#5-complete-implementation-in-c)
  - [5.1 Queue Initialization](#51-queue-initialization)
  - [5.2 State Verification Functions](#52-state-verification-functions)
  - [5.3 Resize Operation (Capacity Doubling)](#53-resize-operation-capacity-doubling)
  - [5.4 Enqueue Operation](#54-enqueue-operation)
  - [5.5 Dequeue Operation](#55-dequeue-operation)
  - [5.6 Peek Operation](#56-peek-operation)
  - [5.7 Queue Destruction](#57-queue-destruction)
  - [5.8 Demonstration Program](#58-demonstration-program)
- [6. Complexity Analysis](#6-complexity-analysis)
  - [6.1 Time Complexity](#61-time-complexity)
  - [6.2 Space Complexity](#62-space-complexity)
- [7. Comparative Analysis: Dynamic Array vs. Linked List Implementation](#7-comparative-analysis-dynamic-array-vs-linked-list-implementation)
- [8. Summary](#8-summary)

## 1. Introduction

A **queue** is a fundamental linear data structure that adheres to the **FIFO (First In, First Out)** principle, wherein elements are inserted at the rear (enqueue operation) and removed from the front (dequeue operation). The implementation of queues using static (fixed-size) arrays presents several inherent limitations that constrain their practical utility in real-world applications. This document presents a comprehensive treatment of queue implementation using dynamic arrays, specifically the **dynamic circular queue** employing the **doubling strategy** for automatic capacity expansion.

The significance of dynamic array-based queue implementation lies in achieving a balance between the cache-friendly, contiguous memory layout of arrays and the flexibility of unbounded capacity. This approach enables queues to grow and shrink according to runtime requirements while maintaining O(1) amortized time complexity for primary operations.

## 2. Limitations of Fixed-Size Queue Implementations

When a queue is implemented using a statically allocated array of predetermined size $N$, several fundamental problems emerge that motivate the adoption of dynamic strategies.

### 2.1 Overflow Condition

In a fixed-size array implementation, the queue becomes incapable of accepting new elements once the underlying storage is exhausted. Formally, if the queue contains $N$ elements where $N$ equals the array capacity, any subsequent `enqueue` operation must necessarily fail, resulting in an **overflow** condition. This limitation is particularly problematic when the maximum queue size cannot be accurately predicted at compile time.

### 2.2 Wasted Memory in Linear Queues

A naive linear queue implementation suffers from a critical inefficiency: after repeated enqueue and dequeue operations, the front index advances progressively toward the rear, leaving unused (and inaccessible) slots at the beginning of the array. The occupied region of the queue "drifts" toward the end of the array, and while elements could theoretically be shifted leftward to reclaim space, such shifting operations introduce O(n) overhead, defeating the purpose of array-based efficiency.

### 2.3 Capacity Selection Problem

The programmer must determine an appropriate array capacity at compile time. This presents a dual-edged challenge: an undersized array leads to frequent overflow conditions, while an oversized array results in unnecessary memory consumption. Neither outcome is desirable in memory-constrained environments or in applications with unpredictable workload patterns.

## 3. Circular Queue: Foundation for Dynamic Implementation

The **circular queue** (also termed a ring buffer) addresses the space wastage problem by treating the array as a circular structure wherein the last position connects back to the first. This conceptual wrapping eliminates the need for element shifting and enables efficient utilization of the entire allocated storage.

### 3.1 Mathematical Formulation

Given an array of capacity $C$, the circular queue maintains two indices: `front` (pointing to the first element) and `rear` (pointing to the next available insertion position). All index arithmetic is performed modulo $C$.

The fundamental operations are defined as follows:

- **Advance index**: Given current index $i$, the next index is computed as $(i + 1) \bmod C$
- **Queue size**: The number of elements currently stored is calculated as $(rear - front + C) \bmod C$
- **Empty condition**: The queue is empty when $front == rear$
- **Full condition**: The queue is full when $(rear + 1) \bmod C == front$

The convention of leaving one slot unused in a circular queue enables unambiguous distinction between the empty and full states without requiring an additional flag variable.

## 4. Dynamic Circular Queue: Design Principles

A **dynamic circular queue** extends the circular queue concept by incorporating automatic memory reallocation when capacity limits are approached. The predominant strategy employs **capacity doubling**, wherein the underlying array is replaced with a larger array (typically twice the current capacity) when an enqueue operation encounters a full queue.

### 4.1 Doubling Strategy: Theoretical Justification

The choice of doubling the capacity (rather than incrementing by a fixed amount) provides crucial amortized performance guarantees. If the queue capacity is increased by a factor of $k > 1$ each time resizing occurs, the total cost of $n$ successive enqueue operations can be analyzed using aggregate analysis or the potential method.

Consider a sequence of $n$ enqueue operations. Let $c_i$ denote the cost of the $i$-th operation (where $c_i = 1$ for regular operations and $c_i = i$ when resizing occurs). The total cost is:

$$\sum_{i=1}^{n} c_i = n + (1 + 2 + 4 + \cdots + 2^{\lfloor \log_2 n \rfloor})$$

Summing this geometric series yields:

$$= n + (2^{\lfloor \log_2 n \rfloor + 1} - 1) < n + 2n$$

Therefore, the amortized cost per operation is lessn = 3 than 3, establishing O(1) amortized time complexity. This analysis demonstrates that while individual resizing operations are expensive (O(n)), they occur infrequently enough to guarantee constant average cost per operation.

### 4.2 Data Structure Definition

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *data;       // Pointer to dynamically allocated array
    int front;       // Index of the front element
    int rear;        // Index of the next available insertion position
    int capacity;    // Current allocated capacity
    int size;        // Number of elements currently in the queue
} DynamicQueue;
```

The structure maintains a `size` field to enable O(1) determination of the queue state, eliminating the need to leave one slot unused and thereby maximizing memory efficiency.

## 5. Complete Implementation in C

### 5.1 Queue Initialization

```c
DynamicQueue* createQueue(int initialCapacity) {
    // Validate input capacity
    if (initialCapacity <= 0) {
        initialCapacity = 1;  // Minimum capacity of 1
    }

    DynamicQueue *q = (DynamicQueue *)malloc(sizeof(DynamicQueue));
    if (q == NULL) {
        fprintf(stderr, "Error: Memory allocation failed for queue structure\n");
        exit(EXIT_FAILURE);
    }

    q->data = (int *)malloc(initialCapacity * sizeof(int));
    if (q->data == NULL) {
        fprintf(stderr, "Error: Memory allocation failed for array\n");
        free(q);
        exit(EXIT_FAILURE);
    }

    q->front = 0;
    q->rear = 0;
    q->capacity = initialCapacity;
    q->size = 0;

    return q;
}
```

### 5.2 State Verification Functions

```c
bool isEmpty(DynamicQueue *q) {
    return (q->size == 0);
}

bool isFull(DynamicQueue *q) {
    return (q->size == q->capacity);
}
```

### 5.3 Resize Operation (Capacity Doubling)

The resize operation constitutes the critical mechanism enabling dynamic growth. When invoked, it allocates a new array of doubled capacity and copies existing elements in their logical (front-to-rear) order into the new array's sequential positions.

```c
void resizeQueue(DynamicQueue *q) {
    int newCapacity = q->capacity * 2;

    int *newData = (int *)malloc(newCapacity * sizeof(int));
    if (newData == NULL) {
        fprintf(stderr, "Error: Memory allocation failed during resize\n");
        exit(EXIT_FAILURE);
    }

    // Copy elements in logical order: front to rear
    // The source indices may wrap around; destination is sequential
    for (int i = 0; i < q->size; i++) {
        int srcIndex = (q->front + i) % q->capacity;
        newData[i] = q->data[srcIndex];
    }

    // Deallocate old array
    free(q->data);

    // Update structure state
    q->data = newData;
    q->front = 0;
    q->rear = q->size;
    q->capacity = newCapacity;
}
```

### 5.4 Enqueue Operation

```c
void enqueue(DynamicQueue *q, int value) {
    // Check for overflow and resize if necessary
    if (isFull(q)) {
        resizeQueue(q);
    }

    // Insert element at rear position
    q->data[q->rear] = value;

    // Advance rear index circularly
    q->rear = (q->rear + 1) % q->capacity;

    // Increment size counter
    q->size++;
}
```

### 5.5 Dequeue Operation

```c
int dequeue(DynamicQueue *q) {
    if (isEmpty(q)) {
        fprintf(stderr, "Error: Queue underflow - cannot dequeue from empty queue\n");
        exit(EXIT_FAILURE);
    }

    // Retrieve element at front position
    int value = q->data[q->front];

    // Advance front index circularly
    q->front = (q->front + 1) % q->capacity;

    // Decrement size counter
    q->size--;

    return value;
}
```

### 5.6 Peek Operation

```c
int peek(DynamicQueue *q) {
    if (isEmpty(q)) {
        fprintf(stderr, "Error: Cannot peek - queue is empty\n");
        exit(EXIT_FAILURE);
    }
    return q->data[q->front];
}
```

### 5.7 Queue Destruction

```c
void destroyQueue(DynamicQueue *q) {
    if (q != NULL) {
        if (q->data != NULL) {
            free(q->data);
            q->data = NULL;
        }
        q->front = 0;
        q->rear = 0;
        q->size = 0;
        q->capacity = 0;
        free(q);
    }
}
```

### 5.8 Demonstration Program

```c
int main(void) {
    DynamicQueue *q = createQueue(4);

    printf("=== Dynamic Queue Demonstration ===\n\n");

    // Enqueue elements to demonstrate initial capacity and resizing
    printf("Enqueuing: 10, 20, 30, 40 (capacity = 4)\n");
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    enqueue(q, 40);
    printf("Queue size: %d, Capacity: %d\n\n", q->size, q->capacity);

    // This enqueue triggers resizing to capacity 8
    printf("Enqueuing: 50 (triggers resize 4 -> 8)\n");
    enqueue(q, 50);
    printf("Queue size: %d, Capacity: %d\n\n", q->size, q->capacity);

    // Dequeue operations
    printf("Dequeuing two elements:\n");
    printf("Dequeued: %d\n", dequeue(q));
    printf("Dequeued: %d\n", dequeue(q));
    printf("Queue size: %d, Capacity: %d\n\n", q->size, q->capacity);

    // Additional enqueue operations
    printf("Enqueuing: 60, 70, 80\n");
    enqueue(q, 60);
    enqueue(q, 70);
    enqueue(q, 80);
    printf("Queue size: %d, Capacity: %d\n\n", q->size, q->capacity);

    // Display queue contents
    printf("Front element (peek): %d\n", peek(q));

    destroyQueue(q);
    return 0;
}
```

## 6. Complexity Analysis

### 6.1 Time Complexity

| Operation | Best Case | Worst Case | Amortized Case |
| --------- | --------- | ---------- | -------------- |
| `enqueue` | O(1)      | O(n)       | O(1)           |
| `dequeue` | O(1)      | O(1)       | O(1)           |
| `peek`    | O(1)      | O(1)       | O(1)           |
| `isEmpty` | O(1)      | O(1)       | O(1)           |
| `isFull`  | O(1)      | O(1)       | O(1)           |

The **amortized O(1)** complexity for `enqueue` is established through aggregate analysis, as demonstrated in Section 4.1. Each element is copied at most once during every doubling operation, and the total number of times any element is copied is bounded by O(log n) for n total enqueue operations.

### 6.2 Space Complexity

The space complexity of the dynamic queue is O(capacity), which equals O(n) where n represents the maximum number of elements ever stored. The memory overhead includes the data array (n integers) plus the queue structure (constant overhead of 4 integers). The **space utilization** varies between 25% and 100% during operation: after resizing, utilization drops to approximately 50% and gradually increases until the next resize triggers.

## 7. Comparative Analysis: Dynamic Array vs. Linked List Implementation

Both dynamic array and linked list approaches provide O(1) amortized enqueue and O(1) dequeue operations, yet they exhibit distinct performance characteristics:

| Criterion                 | Dynamic Array Queue          | Linked List Queue             |
| ------------------------- | ---------------------------- | ----------------------------- |
| Cache Performance         | Superior (contiguous memory) | Inferior (scattered nodes)    |
| Memory Overhead           | O(n) - data only             | O(n) + O(n) - data + pointers |
| Resizing Cost             | O(n) periodic                | N/A - grows incrementally     |
| Memory Allocation         | Fewer calls (doubling)       | Frequent (per-node)           |
| Implementation Complexity | Moderate                     | Higher                        |

The dynamic array implementation generally outperforms linked list queues in practice due to superior cache locality, despite the periodic resizing overhead.

## 8. Summary

The dynamic circular queue represents an elegant solution to the limitations of fixed-size queue implementations. By employing the doubling strategy for capacity management, this data structure achieves O(1) amortized time complexity for enqueue operations while maintaining the cache-friendly properties of array-based storage. The mathematical analysis using aggregate methods confirms that the occasional O(n) resizing cost is sufficiently infrequent to guarantee constant average performance. This implementation serves as a canonical example of how amortized analysis enables the design of efficient, practical data structures.
