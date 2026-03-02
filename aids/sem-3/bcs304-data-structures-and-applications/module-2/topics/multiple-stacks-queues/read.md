# Multiple Stacks and Queues


## Table of Contents

- [Multiple Stacks and Queues](#multiple-stacks-and-queues)
- [Introduction](#introduction)
- [1. Two Stacks in One Array](#1-two-stacks-in-one-array)
  - [1.1 Problem Definition and Fundamental Approach](#11-problem-definition-and-fundamental-approach)
  - [1.2 Algorithm Specifications](#12-algorithm-specifications)
  - [1.3 Complexity Analysis](#13-complexity-analysis)
  - [1.4 Correctness Proof](#14-correctness-proof)
- [2. Multiple Stacks in an Array](#2-multiple-stacks-in-an-array)
  - [2.1 Fixed Division Approach](#21-fixed-division-approach)
  - [2.2 Variable Division Approach (Linked Representation)](#22-variable-division-approach-linked-representation)
  - [2.3 Comparison of Approaches](#23-comparison-of-approaches)
- [3. Multiple Queues in an Array](#3-multiple-queues-in-an-array)
  - [3.1 Problem Definition](#31-problem-definition)
  - [3.2 Circular Queue Fundamentals](#32-circular-queue-fundamentals)
  - [3.3 Implementation of Circular Queue](#33-implementation-of-circular-queue)
  - [3.4 Multiple Queues Implementation](#34-multiple-queues-implementation)
- [4. Deque (Double-Ended Queue)](#4-deque-double-ended-queue)
  - [4.1 Definition and Properties](#41-definition-and-properties)
  - [4.2 Types of Deques](#42-types-of-deques)
  - [4.3 Implementation Using Circular Array](#43-implementation-using-circular-array)
  - [4.4 Time Complexity Analysis](#44-time-complexity-analysis)
- [5. Priority Queue](#5-priority-queue)
  - [5.1 Definition and Classification](#51-definition-and-classification)
  - [5.2 Implementation Methods and Complexity](#52-implementation-methods-and-complexity)
  - [5.3 Binary Heap Implementation](#53-binary-heap-implementation)
- [6. Practical Applications](#6-practical-applications)
  - [6.1 Multiple Stacks Applications](#61-multiple-stacks-applications)
  - [6.2 Multiple Queues Applications](#62-multiple-queues-applications)
  - [6.3 Priority Queue Applications](#63-priority-queue-applications)

## Introduction

Data structures form the foundation of computer science, and efficient management of multiple data collections is essential for solving complex computational problems. While fundamental stacks and queues represent basic linear data structures, practical computing scenarios frequently demand simultaneous management of multiple stacks and queues. This module provides a comprehensive examination of representing, implementing, and applying multiple stacks and queues, which are indispensable in expression evaluation, memory management, scheduling algorithms, and graph traversal operations.

The significance of multiple stacks becomes evident in programming language implementation, particularly for handling nested function calls where each invocation requires its own stack frame. Similarly, multiple queues serve critical roles in operating system task scheduling, where distinct priority levels or job categories necessitate concurrent management. This analysis explores efficient implementation techniques emphasizing optimal space utilization and favorable time complexity characteristics.

## 1. Two Stacks in One Array

### 1.1 Problem Definition and Fundamental Approach

The challenge of representing two stacks within a single array of size n requires careful space management. The elegant solution exploits the principle of growing stacks from opposite ends of the array—Stack 1 expands rightward from index 0 while Stack 2 expands leftward from index n-1. Overflow occurs precisely when the top pointers cross, indicating no remaining space between the two stacks.

**Data Members:**

```
- stackArray[0...n-1]: Array of size n to store elements
- top1: Integer pointer to top of Stack 1 (initialized to -1)
- top2: Integer pointer to top of Stack 2 (initialized to n)
```

**Theorem 1.1 (Space Utilization):** The two-stack implementation achieves 100% space utilization, as the array remains fully utilized until overflow occurs.

_Proof:_ The stacks occupy contiguous regions from opposite ends. Stack 1 uses indices [0, top1] and Stack 2 uses indices [top2, n-1]. These regions are mutually exclusive and collectively exhaustive until top1 + 1 = top2, at which point no unused indices remain. ∎

### 1.2 Algorithm Specifications

**Push Operation:**

```
Procedure push(stackNumber, item)
    if top1 + 1 == top2 then
        print "Overflow: No space available"
        return ERROR
    end if

    if stackNumber == 1 then
        top1 = top1 + 1
        stackArray[top1] = item
    else
        top2 = top2 - 1
        stackArray[top2] = item
    end if
    return SUCCESS
End Procedure
```

**Pop Operation:**

```
Procedure pop(stackNumber)
    if stackNumber == 1 then
        if top1 == -1 then
            print "Underflow: Stack 1 empty"
            return ERROR
        end if
        item = stackArray[top1]
        top1 = top1 - 1
    else
        if top2 == n then
            print "Underflow: Stack 2 empty"
            return ERROR
        end if
        item = stackArray[top2]
        top2 = top2 + 1
    end if
    return item
End Procedure
```

### 1.3 Complexity Analysis

**Time Complexity:** All operations (push, pop, peek, isEmpty, isFull) execute in O(1) constant time, as each involves a constant number of pointer manipulations and array accesses.

**Space Complexity:** The data structure requires O(n) space for the array plus O(1) additional space for pointers, yielding a total of O(n) space complexity.

### 1.4 Correctness Proof

**Theorem 1.2 (Push Correctness):** The push operation correctly inserts an element into the specified stack without affecting the other stack.

_Proof:_ Consider push to Stack 1. The operation first verifies overflow condition top1 + 1 == top2. If false, there exists at least one unused index between the stacks. Incrementing top1 and storing the item at stackArray[top1] places the element at the correct position adjacent to existing Stack 1 elements. The operation does not modify top2 or any indices in Stack 2's region [top2, n-1]. Symmetric reasoning applies to Stack 2. ∎

## 2. Multiple Stacks in an Array

### 2.1 Fixed Division Approach

For m stacks within an array of size n, the fixed division approach allocates approximately n/m positions to each stack. If elements are indexed from 0 to n-1, stack i occupies positions from i×⌊n/m⌋ to (i+1)×⌊n/m⌋ - 1.

**Theorem 2.1 (Fixed Division Overflow Condition):** In fixed division, stack i overflows when its element count exceeds ⌊n/m⌋, regardless of available space in other stack regions.

_Proof:_ Each stack i is confined to its allocated boundary [L_i, U_i] where L_i = i×⌊n/m⌋ and U_i = (i+1)×⌊n/m⌋ - 1. Push operations within stack i can only increment its top pointer within [L_i, U_i]. Once top_i exceeds U_i, overflow occurs even if other stacks contain unused capacity in their respective regions. ∎

**Space Inefficiency Example:** Consider m = 3 stacks in array n = 9. Each stack receives 3 positions. If Stack 1 contains 1 element, Stack 2 contains 1 element, and Stack 3 requires 7 elements, Stack 3 overflows despite only using 2 + 1 = 3 positions while 6 positions remain available.

### 2.2 Variable Division Approach (Linked Representation)

Variable division addresses space inefficiency by allowing stacks to share available space dynamically. This implementation uses linked allocation where each element contains both data and a pointer to the previous element.

**Data Structure:**

```
struct Node {
    int data;
    struct Node* next;
}

struct StackHeader {
    struct Node* top;
    int elementCount;
}
```

**Overflow Handling:** Unlike array-based implementations, linked representation technically never overflows unless system memory is exhausted. However, this comes at the cost of additional memory for pointer storage and reduced cache performance.

### 2.3 Comparison of Approaches

| Criterion                 | Fixed Division                          | Variable Division            |
| ------------------------- | --------------------------------------- | ---------------------------- |
| Space Utilization         | Poor (potential internal fragmentation) | Excellent (100% utilization) |
| Time Complexity           | O(1) for all operations                 | O(1) for all operations      |
| Memory Overhead           | No extra memory                         | O(m) pointers per element    |
| Cache Performance         | Excellent (contiguous memory)           | Poor (scattered allocations) |
| Implementation Complexity | Simple                                  | Moderate                     |
| Overflow Condition        | Deterministic (array bounds)            | System-dependent (heap)      |

## 3. Multiple Queues in an Array

### 3.1 Problem Definition

Multiple queues in a single array present distinct challenges from multiple stacks. Unlike stacks where LIFO behavior naturally separates elements, queues require maintaining relative ordering across potentially interleaved operations. The circular queue variant provides the foundation for efficient multiple queue implementation.

### 3.2 Circular Queue Fundamentals

The circular queue eliminates the space waste inherent in linear queues by allowing the rear pointer to wrap around to the beginning when it reaches the array's end.

**State Conditions:**

- Empty: `front == -1` or more commonly `front == (rear + 1) % MAX`
- Full: `(rear + 1) % MAX == front`
- Note: Array size must be MAX, where usable capacity is MAX - 1 elements

**Theorem 3.1 (Space Utilization):** Circular queue achieves 100% space utilization.

_Proof:_ In linear queue, after k enqueue and k-1 dequeue operations with array size n, rear = n-1 and front = k-1. Despite available space at indices [0, k-2], further enqueue fails. Circular queue wraps rear using modulo arithmetic: after rear = n-1, next enqueue sets rear = (n-1 + 1) % n = 0, successfully utilizing previously dequeued positions. ∎

### 3.3 Implementation of Circular Queue

```c
#define MAX 100

struct CircularQueue {
    int queue[MAX];
    int front;
    int rear;
};

void initQueue(struct CircularQueue* q) {
    q->front = q->rear = -1;
}

int isFull(struct CircularQueue* q) {
    return ((q->rear + 1) % MAX) == q->front;
}

int isEmpty(struct CircularQueue* q) {
    return q->front == -1;
}

void enqueue(struct CircularQueue* q, int item) {
    if (isFull(q)) {
        printf("Queue Overflow\n");
        return;
    }
    if (q->front == -1) {
        q->front = q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % MAX;
    }
    q->queue[q->rear] = item;
}

int dequeue(struct CircularQueue* q) {
    if (isEmpty(q)) {
        printf("Queue Underflow\n");
        return -1;
    }
    int item = q->queue[q->front];
    if (q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX;
    }
    return item;
}
```

### 3.4 Multiple Queues Implementation

For k queues in a single array, we employ a divide-and-conquer strategy similar to multiple stacks but with circular queue mechanics:

**Method 1: Fixed Segments with Circular Pointers**

- Divide array into k roughly equal segments
- Each queue i maintains separate front_i and rear_i pointers
- Each queue operates circularly within its segment
- Overflow occurs when queue i's segment is full, even if other segments have space

**Method 2: Shared Pool with Overflow Links**

- All queues share a common pool of available indices
- When a segment overflows, elements overflow to available space in other segments
- Requires maintaining additional overflow chains
- More complex but improves space utilization

**Theorem 3.2 (Multiple Queue Space Complexity):** With k queues each of capacity c, worst-case space utilization is at most (k×c - k + 1)/n where n is array size.

_Proof:_ Each circular queue segment of capacity c wastes at most 1 position (distinguishing full from empty). For k queues, maximum wasted positions = k. Total usable elements = n - k. Usable capacity per queue averages (n - k)/k. ∎

## 4. Deque (Double-Ended Queue)

### 4.1 Definition and Properties

A deque permits insertion and deletion at both the front and rear ends, combining stack and queue functionality. This versatile data structure supports four fundamental operations with O(1) time complexity.

**Formal Definition:** A deque D is an abstract data type defining operations: insertFront(D, x), insertRear(D, x), deleteFront(D), deleteRear(D), each executing in constant time.

### 4.2 Types of Deques

**Input-Restricted Deque (IRDQ):**

- Insertion permitted only at one end (typically rear)
- Deletion permitted at both front and rear
- Applications: Scheduling with single insertion point

**Output-Restricted Deque (ORDQ):**

- Deletion permitted only at one end (typically front)
- Insertion permitted at both front and rear
- Applications: Palindrome checking, certain scheduling algorithms

### 4.3 Implementation Using Circular Array

```c
struct Deque {
    int arr[MAX];
    int front;
    int rear;
};

void insertFront(struct Deque* d, int item) {
    if ((d->front - 1 + MAX) % MAX == d->rear) {
        printf("Deque Full\n");
        return;
    }
    if (d->front == -1) {
        d->front = d->rear = 0;
    } else {
        d->front = (d->front - 1 + MAX) % MAX;
    }
    d->arr[d->front] = item;
}

void insertRear(struct Deque* d, int item) {
    if ((d->rear + 1) % MAX == d->front) {
        printf("Deque Full\n");
        return;
    }
    if (d->front == -1) {
        d->front = d->rear = 0;
    } else {
        d->rear = (d->rear + 1) % MAX;
    }
    d->arr[d->rear] = item;
}
```

### 4.4 Time Complexity Analysis

| Operation   | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| insertFront | O(1)            | O(n)             |
| insertRear  | O(1)            | O(n)             |
| deleteFront | O(1)            | O(n)             |
| deleteRear  | O(1)            | O(n)             |
| getFront    | O(1)            | O(n)             |
| getRear     | O(1)            | O(n)             |

## 5. Priority Queue

### 5.1 Definition and Classification

A priority queue associates each element with a priority value, with element removal based on priority rather than insertion order. This data structure is fundamental to scheduling algorithms, Dijkstra's shortest path, and Huffman coding.

**Definition 5.1 (Priority Queue):** A priority queue P is a set of elements where each element e has an associated key priority(e). The deleteMin operation removes and returns the element with minimum priority (for min-heap) or maximum priority (for max-heap).

**Classification:**

1. **Ascending Priority Queue (Min-Priority Queue):** Removes element with smallest priority value first
2. **Descending Priority Queue (Max-Priority Queue):** Removes element with largest priority value first

### 5.2 Implementation Methods and Complexity

**Array/Linked List Implementation:**

- Insert: O(1) (append at end)
- Delete Min/Max: O(n) (linear search for extremum)
- Space: O(n)

**Binary Heap Implementation:**

- Insert: O(log n) (heapify up)
- Delete Min/Max: O(log n) (heapify down)
- Build Heap: O(n) (Floyd's algorithm)
- Space: O(n)
- Preferred method for practical applications

**Theorem 5.1 (Heap Height Bound):** A binary heap containing n elements has height ⌊log₂ n⌋.

_Proof:_ A complete binary tree of height h contains at most 2^h nodes at the deepest level and at most 2^(h+1) - 1 total nodes. For n nodes, 2^h ≤ n < 2^(h+1), implying h = ⌊log₂ n⌋. ∎

### 5.3 Binary Heap Implementation

```c
#define MAX_HEAP 100

struct PriorityQueue {
    int heap[MAX_HEAP];
    int size;
};

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapifyUp(struct PriorityQueue* pq, int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (pq->heap[index] > pq->heap[parent]) {
            swap(&pq->heap[index], &pq->heap[parent]);
            index = parent;
        } else {
            break;
        }
    }
}

void insert(struct PriorityQueue* pq, int item) {
    if (pq->size == MAX_HEAP) {
        printf("Heap Overflow\n");
        return;
    }
    pq->heap[pq->size] = item;
    heapifyUp(pq, pq->size);
    pq->size++;
}

void heapifyDown(struct PriorityQueue* pq, int index) {
    int largest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < pq->size && pq->heap[left] > pq->heap[largest])
        largest = left;
    if (right < pq->size && pq->heap[right] > pq->heap[largest])
        largest = right;

    if (largest != index) {
        swap(&pq->heap[index], &pq->heap[largest]);
        heapifyDown(pq, largest);
    }
}

int deleteMax(struct PriorityQueue* pq) {
    if (pq->size == 0) {
        printf("Heap Underflow\n");
        return -1;
    }
    int max = pq->heap[0];
    pq->heap[0] = pq->heap[pq->size - 1];
    pq->size--;
    heapifyDown(pq, 0);
    return max;
}
```

## 6. Practical Applications

### 6.1 Multiple Stacks Applications

- **Function Call Management:** Each function call creates a new stack frame; recursive depth limited by stack space
- **Expression Evaluation:** Operands and operators managed on separate stacks
- **Undo Mechanisms:** Multiple undo operations in text editors

### 6.2 Multiple Queues Applications

- **CPU Scheduling:** Multiple priority queues for different process types
- **Network Packet Scheduling:** Quality of Service (QoS) with multiple queues
- **Breadth-First Search:** Level-order tree traversals

### 6.3 Priority Queue Applications

- **Dijkstra's Algorithm:** Extract-min for shortest path computation
- **Prim's Algorithm:** Minimum spanning tree construction
- ** Huffman Coding:** Building optimal prefix codes
- **Operating System Scheduling:** Process priority management
