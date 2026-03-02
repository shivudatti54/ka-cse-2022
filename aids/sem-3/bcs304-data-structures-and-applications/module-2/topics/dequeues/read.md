# Deques (Double-Ended Queues)


## Table of Contents

- [Deques (Double-Ended Queues)](#deques-double-ended-queues)
- [1. Introduction and Formal Definition](#1-introduction-and-formal-definition)
  - [1.1 Relationship to Other Data Structures](#11-relationship-to-other-data-structures)
  - [1.2 Visual Representation](#12-visual-representation)
  - [1.3 Applications](#13-applications)
- [2. Classification of Deques](#2-classification-of-deques)
  - [2.1 Input-Restricted Deque](#21-input-restricted-deque)
  - [2.2 Output-Restricted Deque](#22-output-restricted-deque)
  - [2.3 Comparative Summary](#23-comparative-summary)
- [3. Abstract Data Type (ADT) Specification](#3-abstract-data-type-adt-specification)
- [4. Array-Based Implementation: Circular Array](#4-array-based-implementation-circular-array)
  - [4.1 Why Circular Array?](#41-why-circular-array)
  - [4.2 Data Structure Definition](#42-data-structure-definition)
  - [4.3 Initialization](#43-initialization)
  - [4.4 Overflow and Underflow Checks](#44-overflow-and-underflow-checks)
  - [4.5 Insertion at Rear](#45-insertion-at-rear)
  - [4.6 Insertion at Front](#46-insertion-at-front)
  - [4.7 Deletion from Front](#47-deletion-from-front)
  - [4.8 Deletion from Rear](#48-deletion-from-rear)
  - [4.9 Time Complexity Analysis](#49-time-complexity-analysis)
- [5. Linked List-Based Implementation](#5-linked-list-based-implementation)
  - [5.1 Node Structure](#51-node-structure)
  - [5.2 Complexity Comparison](#52-complexity-comparison)
- [6. Summary](#6-summary)

## 1. Introduction and Formal Definition

A **deque** (pronounced "deck") is a linear data structure that stands for **Double-Ended Queue**. Formally, a deque is an abstract data type (ADT) that supports insertion and deletion of elements at **both ends** — the front and the rear. This is in contrast to a standard queue, which restricts enqueuing to the rear and dequeuing to the front.

Mathematically, a deque can be defined as an ordered sequence D = ⟨d₁, d₂, ..., dₙ⟩ where operations are permitted at both ends. The structure maintains the relative order of elements unless explicitly removed from either end.

### 1.1 Relationship to Other Data Structures

One of the most important theoretical properties of a deque is its **universality** — it can simulate both stacks and queues:

- **Stack (LIFO)**: A deque can function as a stack by using only `insertFront`/`deleteFront` or only `insertRear`/`deleteRear`.
- **Queue (FIFO)**: A deque can function as a queue by using `insertRear` for enqueue and `insertFront`/`deleteFront` for dequeue.

This relationship is formally stated as:

> **Theorem**: Every stack operation sequence can be replicated using a deque, and every queue operation sequence can be replicated using a deque.

_Proof_: For a stack with operations push(x) and pop(), we can implement push(x) as `insertFront(x)` and pop() as `deleteFront()`. For a queue with enqueue(x) and dequeue(), we can implement enqueue(x) as `insertRear(x)` and dequeue() as `deleteFront()`. ∎

### 1.2 Visual Representation

```
        deleteFront()      deleteRear()
           ←───              ←───
    +----+------+------+------+----+
    | A  |  B   |  C   |  D   | E  |
    +----+------+------+------+----+
      ↑                         ↑
  insertFront()            insertRear()
```

### 1.3 Applications

Deques are fundamental in several algorithmic contexts:

1. **Sliding Window Algorithms**: Maintaining maximum/minimum values in a sliding window of size k requires a deque for O(n) solution.
2. **Palindrome Checking**: Deques allow symmetric comparison from both ends.
3. **Undo-Redo Systems**: Recent operations need both front and rear access.
4. **Task Scheduling**: Priority insertion at front with FIFO processing at rear.

---

## 2. Classification of Deques

Deques can be restricted to create specialized variants that are frequently tested in examinations.

### 2.1 Input-Restricted Deque

An **input-restricted deque** permits insertion only at **one end** (the rear), but deletion is allowed at both ends.

| Operation   | Allowed? |
| ----------- | -------- |
| insertFront | ✗ No     |
| insertRear  | ✓ Yes    |
| deleteFront | ✓ Yes    |
| deleteRear  | ✓ Yes    |

**Use Case**: Print job queue where jobs are always added at the rear, but the administrator may cancel the most recent job (deleteRear) or process the oldest (deleteFront).

### 2.2 Output-Restricted Deque

An **output-restricted deque** permits deletion only at **one end** (the front), but insertion is allowed at both ends.

| Operation   | Allowed? |
| ----------- | -------- |
| insertFront | ✓ Yes    |
| insertRear  | ✓ Yes    |
| deleteFront | ✓ Yes    |
| deleteRear  | ✗ No     |

**Use Case**: Customer service system where tickets are always resolved in order (front), but priority tickets can be inserted at front.

### 2.3 Comparative Summary

| Structure         | insertFront | insertRear | deleteFront | deleteRear |
| ----------------- | ----------- | ---------- | ----------- | ---------- |
| General Deque     | ✓           | ✓          | ✓           | ✓          |
| Input-Restricted  | ✗           | ✓          | ✓           | ✓          |
| Output-Restricted | ✓           | ✓          | ✓           | ✗          |
| Standard Queue    | ✗           | ✓          | ✓           | ✗          |
| Stack             | ✓           | ✗          | ✓           | ✗          |

---

## 3. Abstract Data Type (ADT) Specification

The deque ADT specifies the following operations with their formal semantics:

| Operation        | Precondition    | Postcondition                                      | Complexity |
| ---------------- | --------------- | -------------------------------------------------- | ---------- |
| `insertFront(x)` | deque not full  | x becomes new front element; size ← size + 1       | O(1)       |
| `insertRear(x)`  | deque not full  | x becomes new rear element; size ← size + 1        | O(1)       |
| `deleteFront()`  | deque not empty | returns front element; removes it; size ← size − 1 | O(1)       |
| `deleteRear()`   | deque not empty | returns rear element; removes it; size ← size − 1  | O(1)       |
| `getFront()`     | deque not empty | returns front element without removal              | O(1)       |
| `getRear()`      | deque not empty | returns rear element without removal               | O(1)       |
| `isEmpty()`      | none            | returns true iff size = 0                          | O(1)       |
| `isFull()`       | none            | returns true iff size = MAXSIZE                    | O(1)       |
| `size()`         | none            | returns current element count                      | O(1)       |

**Overflow**: Condition when `isFull()` is true and `insertFront()` or `insertRear()` is attempted.
**Underflow**: Condition when `isEmpty()` is true and `deleteFront()` or `deleteRear()` is attempted.

---

## 4. Array-Based Implementation: Circular Array

The most efficient implementation of a deque uses a **circular array** (also called a ring buffer or circular buffer). This approach achieves O(1) time complexity for all operations by utilizing the array space efficiently.

### 4.1 Why Circular Array?

In a linear array implementation, repeated `insertFront` and `deleteFront` operations would cause the front index to continuously advance, eventually exhausting array space even when slots at the beginning are available. The circular array solves this using modular arithmetic:

$$new\_index = (current\_index \pm 1 + MAX) \bmod MAX$$

This formula correctly wraps indices around the array boundaries.

### 4.2 Data Structure Definition

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 10

typedef struct {
    int data[MAX];    // Fixed-size array storing elements
    int front;       // Index of front element
    int rear;        // Index where next element will be inserted
    int size;        // Current number of elements
} Deque;
```

**Field Descriptions:**

- `data[MAX]`: Fixed-size array with capacity MAX
- `front`: Index of the first element (where deletions occur)
- `rear`: Index one position past the last element (where insertion occurs)
- `size`: Tracks current element count for O(1) size queries

### 4.3 Initialization

```c
void initDeque(Deque *dq) {
    dq->front = -1;
    dq->rear = -1;
    dq->size = 0;
}
```

**Invariant**: After initialization, `front = -1`, `rear = -1`, and `size = 0`. The deque is empty.

### 4.4 Overflow and Underflow Checks

```c
int isFull(Deque *dq) {
    return dq->size == MAX;
}

int isEmpty(Deque *dq) {
    return dq->size == 0;
}
```

### 4.5 Insertion at Rear

```c
int insertRear(Deque *dq, int value) {
    if (isFull(dq)) {
        printf("Overflow: Deque is full\n");
        return 0;
    }

    // First insertion
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else {
        // Circular increment
        dq->rear = (dq->rear + 1) % MAX;
    }

    dq->data[dq->rear] = value;
    dq->size++;
    return 1;
}
```

### 4.6 Insertion at Front

```c
int insertFront(Deque *dq, int value) {
    if (isFull(dq)) {
        printf("Overflow: Deque is full\n");
        return 0;
    }

    // First insertion
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else {
        // Circular decrement: (front - 1 + MAX) % MAX
        dq->front = (dq->front - 1 + MAX) % MAX;
    }

    dq->data[dq->front] = value;
    dq->size++;
    return 1;
}
```

### 4.7 Deletion from Front

```c
int deleteFront(Deque *dq, int *value) {
    if (isEmpty(dq)) {
        printf("Underflow: Deque is empty\n");
        return 0;
    }

    *value = dq->data[dq->front];

    // Single element case
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else {
        dq->front = (dq->front + 1) % MAX;
    }

    dq->size--;
    return 1;
}
```

### 4.8 Deletion from Rear

```c
int deleteRear(Deque *dq, int *value) {
    if (isEmpty(dq)) {
        printf("Underflow: Deque is empty\n");
        return 0;
    }

    *value = dq->data[dq->rear];

    // Single element case
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else {
        // Circular decrement
        dq->rear = (dq->rear - 1 + MAX) % MAX;
    }

    dq->size--;
    return 1;
}
```

### 4.9 Time Complexity Analysis

**Theorem**: All deque operations (insertFront, insertRear, deleteFront, deleteRear) run in O(1) time.

_Proof_: Each operation performs a constant number of arithmetic operations (one or two additions/subtractions and one modulo operation), array accesses, and assignments. Since each of these takes constant time, the total time complexity is O(1). ∎

**Space Complexity**: O(MAX) where MAX is the fixed array size. The deque uses a fixed-size array regardless of the number of elements stored.

---

## 5. Linked List-Based Implementation

For dynamic deque implementation where the size is unknown or unbounded, a doubly linked list provides an alternative representation.

### 5.1 Node Structure

```c
typedef struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
} Node;

typedef struct {
    Node *front;
    Node *rear;
    int size;
} LinkedDeque;
```

### 5.2 Complexity Comparison

| Operation      | Array (Circular) | Linked List  |
| -------------- | ---------------- | ------------ |
| insertFront    | O(1)             | O(1)         |
| insertRear     | O(1)             | O(1)         |
| deleteFront    | O(1)             | O(1)         |
| deleteRear     | O(1)             | O(1)         |
| Space          | O(MAX) fixed     | O(n) dynamic |
| Cache locality | Better           | Worse        |

---

## 6. Summary

The deque is a fundamental data structure that generalizes both stacks and queues. Key takeaways:

1. **Flexibility**: Supports O(1) operations at both ends
2. **Universality**: Can simulate stacks and queues
3. **Implementation**: Circular array provides O(1) operations with efficient space usage
4. **Variants**: Input-restricted and output-restricted deques have specialized applications
5. **Complexity**: All operations maintain constant time O(1) with proper circular handling
