# Implementation of Stacks and Queues Using Linked Lists


## Table of Contents

- [Implementation of Stacks and Queues Using Linked Lists](#implementation-of-stacks-and-queues-using-linked-lists)
- [1. Introduction and Theoretical Foundations](#1-introduction-and-theoretical-foundations)
- [2. Mathematical Analysis: Array vs. Linked Implementations](#2-mathematical-analysis-array-vs-linked-implementations)
  - [2.1 Complexity Comparison](#21-complexity-comparison)
  - [2.2 Space-Time Tradeoff Analysis](#22-space-time-tradeoff-analysis)
- [3. Self-Referential Structures](#3-self-referential-structures)
- [4. Stack Implementation Using Linked Lists](#4-stack-implementation-using-linked-lists)
  - [4.1 Conceptual Foundation](#41-conceptual-foundation)
  - [4.2 Data Structure Definition](#42-data-structure-definition)
  - [4.3 Push Operation: Formal Specification and Correctness Proof](#43-push-operation-formal-specification-and-correctness-proof)
  - [4.4 Implementation Code](#44-implementation-code)
  - [4.5 Pop Operation: Formal Specification and Correctness Proof](#45-pop-operation-formal-specification-and-correctness-proof)
  - [4.6 Implementation Code](#46-implementation-code)
  - [4.7 Auxiliary Operations](#47-auxiliary-operations)
- [5. Queue Implementation Using Linked Lists](#5-queue-implementation-using-linked-lists)
  - [5.1 Conceptual Foundation](#51-conceptual-foundation)
  - [5.2 Data Structure Definition](#52-data-structure-definition)
  - [5.3 Enqueue Operation: Formal Specification](#53-enqueue-operation-formal-specification)
  - [5.4 Dequeue Operation: Formal Specification](#54-dequeue-operation-formal-specification)
  - [5.5 Implementation Code](#55-implementation-code)
- [6. Memory Management Considerations](#6-memory-management-considerations)
  - [6.1 Memory Leak Prevention](#61-memory-leak-prevention)
  - [6.2 Dynamic Memory Lifecycle](#62-dynamic-memory-lifecycle)
- [7. Comparative Analysis](#7-comparative-analysis)
  - [7.1 Advantages of Linked Implementations](#71-advantages-of-linked-implementations)
  - [7.2 Disadvantages](#72-disadvantages)

## 1. Introduction and Theoretical Foundations

The array-based implementations of stacks and queues, while exhibiting O(1) time complexity for primary operations, possess inherent limitations that render them unsuitable for scenarios requiring dynamic memory allocation. Specifically, array implementations necessitate the declaration of a fixed size at compile time, which introduces two fundamental problems: **memory waste** when the allocated space exceeds actual requirements, and **overflow conditions** when the demand for storage surpasses the pre-allocated capacity.

Linked list implementations provide an elegant solution to these limitations through **dynamic memory allocation** utilizing `malloc()` and `free()` functions from the C standard library. The key advantage lies in the ability to allocate memory at runtime, allowing the data structure to grow and shrink according to actual computational demands. This implementation approach is particularly valuable in scenarios where the maximum required size cannot be accurately predicted during system design.

The theoretical foundation for linked implementations rests upon **self-referential structures**, which constitute the cornerstone of all linked data structures. Understanding this concept is essential for comprehending how nodes are constructed and interconnected within the memory hierarchy.

## 2. Mathematical Analysis: Array vs. Linked Implementations

### 2.1 Complexity Comparison

Let n represent the number of elements in the data structure. The following table presents a rigorous complexity analysis:

| Operation                 | Array Implementation | Linked Implementation |
| ------------------------- | -------------------- | --------------------- |
| Push/Enqueue (Worst Case) | O(1)                 | O(1)                  |
| Pop/Dequeue (Worst Case)  | O(1)                 | O(1)                  |
| Space Complexity          | O(N_max) fixed       | O(n) dynamic          |
| Access by Index           | O(1)                 | O(n)                  |

### 2.2 Space-Time Tradeoff Analysis

For array implementations with capacity N_max, the space utilization ratio is n/N_max, which may approach zero for small n but large N_max. Conversely, linked implementations incur additional overhead due to the storage of pointer variables. Specifically, for each node in a linked implementation, we require storage for the data element plus one pointer (typically 4-8 bytes depending on architecture), resulting in a space overhead factor of (sizeof(data) + sizeof(pointer))/sizeof(data).

## 3. Self-Referential Structures

A **self-referential structure** is a data structure that contains a member which is a pointer to an instance of the same structure type. This recursive definition enables the creation of linked node chains.

```c
struct Node {
    int data;               /* Data field storing the element value */
    struct Node* next;      /* Pointer to the next node in the sequence */
};
```

**Theorem 1 (Node Representation)**: Any node in a singly linked list can be uniquely identified by a pointer to its memory location, and the entire list can be traversed by following next pointers starting from the head node.

_Proof_: By definition of the self-referential structure, each node contains a pointer to exactly one other node (or NULL for the terminal node). Starting from the head pointer and applying the transition function f(p) = p->next repeatedly generates a sequence that terminates at NULL after exactly k steps, where k equals the number of nodes in the list. ∎

## 4. Stack Implementation Using Linked Lists

### 4.1 Conceptual Foundation

A **stack** is a Last-In-First-Out (LIFO) abstract data type where elements are added and removed from a single end termed the **top**. The fundamental operations are:

- **Push**: Insert element at the top
- **Pop**: Remove and return element from the top
- **Peek**: Return top element without removal

For optimal O(1) time complexity, we implement the stack such that all operations occur at the **head** of the linked list. This choice eliminates the need for traversal, as adding or removing at the head requires only constant-time pointer manipulation.

### 4.2 Data Structure Definition

```c
typedef struct StackNode {
    int data;                   /* Element stored in the node */
    struct StackNode* next;     /* Pointer to subsequent node */
} StackNode;
```

### 4.3 Push Operation: Formal Specification and Correctness Proof

**Algorithm Push(S, x)**:

```
1. newNode ← allocate(sizeof(StackNode))
2. if newNode = NULL then
3.     return FAILURE (memory overflow)
4. newNode.data ← x
5. newNode.next ← S.top
6. S.top ← newNode
7. return SUCCESS
```

**Theorem 2 (Push Correctness)**: After executing Push(S, x), the element x becomes the top of stack S, and the relative order of all existing elements is preserved.

_Proof_: We prove this by analyzing the pointer manipulations. Prior to the operation, let the list be represented as: top → n₁ → n₂ → ... → nₖ → NULL. After executing steps 4-6, we have: newNode.data = x, newNode.next = old_top, and top = newNode. The new list becomes: top → x → n₁ → n₂ → ... → nₖ → NULL. Since x is now the first node reachable from top, it is the top element by definition. All original nodes remain in their original sequence following x, thus preserving relative ordering. ∎

**Time Complexity Analysis**: The push operation consists of a constant number of elementary operations (memory allocation, pointer assignments, and conditional check). Since each operation executes in O(1) time, the total time complexity is T(n) = O(1).

### 4.4 Implementation Code

```c
void push(StackNode** top_ref, int data) {
    /* Allocate memory for new node */
    StackNode* newNode = (StackNode*)malloc(sizeof(StackNode));

    /* Validate memory allocation */
    if (newNode == NULL) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        return;
    }

    /* Initialize node fields */
    newNode->data = data;
    newNode->next = (*top_ref);  /* Current top becomes next */

    /* Update top pointer */
    *top_ref = newNode;
}
```

### 4.5 Pop Operation: Formal Specification and Correctness Proof

**Algorithm Pop(S)**:

```
1. if S.top = NULL then
2.     return UNDERFLOW
3. temp ← S.top
4. x ← temp.data
5. S.top ← temp.next
6. free(temp)
7. return x
```

**Theorem 3 (Pop Correctness)**: Pop(S) returns the element most recently pushed onto S and removes it from the stack, leaving the remaining elements in their original relative order.

_Proof_: The proof follows from the invariant that the stack top always points to the most recently inserted element. Step 1 checks the precondition (stack non-empty). Step 3 captures the top node, step 4 extracts its data value x, step 5 updates the top pointer to the next element, and step 6 deallocates the removed node. Since the linked list maintains the remaining nodes in their original sequence through the next pointers, the relative order of surviving elements is preserved. ∎

**Time Complexity Analysis**: The pop operation performs a constant number of pointer manipulations and one memory deallocation, all in O(1) time. Therefore, T(n) = O(1).

### 4.6 Implementation Code

```c
int pop(StackNode** top_ref) {
    /* Check for underflow condition */
    if (*top_ref == NULL) {
        printf("Stack Underflow: Cannot pop from empty stack\n");
        return INT_MIN;  /* Sentinel value for error condition */
    }

    /* Store top node and retrieve data */
    StackNode* temp = *top_ref;
    int popped = temp->data;

    /* Advance top pointer */
    *top_ref = temp->next;

    /* Deallocate memory to prevent leaks */
    free(temp);

    return popped;
}
```

### 4.7 Auxiliary Operations

```c
/* Peek: Return top element without removal */
int peek(StackNode* top) {
    if (top == NULL) {
        printf("Stack is empty\n");
        return INT_MIN;
    }
    return top->data;
}

/* isEmpty: Check whether stack is empty */
int isEmpty(StackNode* top) {
    return (top == NULL);
}
```

## 5. Queue Implementation Using Linked Lists

### 5.1 Conceptual Foundation

A **queue** is a First-In-First-Out (FIFO) abstract data type where elements are enqueued at the **rear** and dequeued from the **front**. The fundamental operations are:

- **Enqueue**: Insert element at the rear
- **Dequeue**: Remove and return element from the front

The linked implementation requires maintaining **two pointers**: `front` (head of list) for efficient dequeue operations and `rear` (tail of list) for efficient enqueue operations. This dual-pointer approach ensures O(1) time complexity for both operations.

### 5.2 Data Structure Definition

```c
typedef struct QueueNode {
    int data;                   /* Element stored in the node */
    struct QueueNode* next;     /* Pointer to subsequent node */
} QueueNode;

typedef struct Queue {
    QueueNode* front;           /* Pointer to front (dequeue end) */
    QueueNode* rear;            /* Pointer to rear (enqueue end) */
} Queue;
```

### 5.3 Enqueue Operation: Formal Specification

**Algorithm Enqueue(Q, x)**:

```
1. newNode ← allocate(sizeof(QueueNode))
2. if newNode = NULL then
3.     return FAILURE
4. newNode.data ← x
5. newNode.next ← NULL
6. if Q.rear = NULL then
7.     Q.front ← Q.rear ← newNode
8. else
9.     Q.rear.next ← newNode
10.    Q.rear ← newNode
11. return SUCCESS
```

**Theorem 4 (Enqueue Correctness)**: After Enqueue(Q, x), the element x becomes the rear element of Q, and all existing elements maintain their relative FIFO ordering.

_Proof_: The proof considers two cases. If the queue is empty (Q.rear = NULL), step 7 sets both front and rear to newNode, establishing x as the sole element. If the queue is non-empty, step 9 attaches newNode to the current rear's next pointer, and step 10 updates rear to newNode. In both cases, x becomes accessible only after all existing elements have been dequeued, preserving FIFO ordering. ∎

**Time Complexity**: All operations are constant-time pointer assignments; therefore, T(n) = O(1).

### 5.4 Dequeue Operation: Formal Specification

**Algorithm Dequeue(Q)**:

```
1. if Q.front = NULL then
2.     return UNDERFLOW
3. temp ← Q.front
4. x ← temp.data
5. Q.front ← temp.next
6. if Q.front = NULL then
7.     Q.rear ← NULL
8. free(temp)
9. return x
```

**Theorem 5 (Dequeue Correctness)**: Dequeue(Q) returns and removes the front element of Q while maintaining the FIFO property for remaining elements.

_Proof_: Step 1 verifies queue non-emptiness. Steps 3-4 capture and extract the front element. Step 5 advances the front pointer to the next node. Step 6-7 handle the special case where the queue becomes empty after removal (setting rear to NULL). The remaining elements are still linked through their next pointers in their original sequence, thus maintaining FIFO ordering. ∎

### 5.5 Implementation Code

```c
/* Initialize empty queue */
void initQueue(Queue* q) {
    q->front = q->rear = NULL;
}

/* Enqueue operation */
void enqueue(Queue* q, int data) {
    QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));

    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    newNode->data = data;
    newNode->next = NULL;

    if (q->rear == NULL) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

/* Dequeue operation */
int dequeue(Queue* q) {
    if (q->front == NULL) {
        printf("Queue Underflow\n");
        return INT_MIN;
    }

    QueueNode* temp = q->front;
    int dequeued = temp->data;

    q->front = temp->next;

    if (q->front == NULL) {
        q->rear = NULL;
    }

    free(temp);
    return dequeued;
}
```

## 6. Memory Management Considerations

### 6.1 Memory Leak Prevention

**Critical Theorem**: Every successful malloc() must have a corresponding free() to prevent memory leaks.

In the context of stack and queue implementations, memory is allocated during push/enqueue operations and must be explicitly deallocated during pop/dequeue operations. Failure to do so results in **memory leaks**, where allocated memory remains inaccessible to the system even after the program terminates.

### 6.2 Dynamic Memory Lifecycle

```
Allocation Phase:    malloc() → Node created → Inserted into structure
Deallocation Phase:  Node removed → free() → Memory returned to heap
```

## 7. Comparative Analysis

### 7.1 Advantages of Linked Implementations

1. **Dynamic sizing**: No capacity limitations beyond available heap memory
2. **Memory efficiency**: No pre-allocation of unused space
3. **No overflow risk**: Limited only by system memory constraints

### 7.2 Disadvantages

1. **Pointer overhead**: Additional memory for storing addresses
2. **Cache inefficiency**: Non-contiguous memory allocation
3. **Complexity**: More intricate implementation compared to arrays
