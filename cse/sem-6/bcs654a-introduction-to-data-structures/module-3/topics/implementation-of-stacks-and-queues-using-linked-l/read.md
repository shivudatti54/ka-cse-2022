# Implementation of Stacks and Queues using Linked Lists

## Introduction

In the previous modules, we learned about implementing stacks and queues using arrays. While array-based implementations are efficient in many scenarios, they suffer from fixed size limitations and inefficient memory usage. Linked lists provide a dynamic alternative that allows these data structures to grow and shrink as needed during program execution.

This section explores how linked lists can be used to implement stacks and queues, leveraging the dynamic memory allocation capabilities we learned about in Module 1.

## Self-Referential Structures Revisited

Before implementing stacks and queues, let's recall the concept of self-referential structures - structures that contain pointers to instances of themselves:

```c
struct Node {
 int data;
 struct Node* next;
};
```

This simple structure forms the foundation for our linked list implementations. Each node contains data and a pointer to the next node in the sequence.

## Stack Implementation using Linked List

### Conceptual Overview

A stack is a Last-In-First-Out (LIFO) data structure where the last element added is the first one removed. In linked list implementation, we typically add and remove elements from the head of the list for efficiency.

```
Stack Operations Visualization:

Initial: NULL
Push(10): 10 -> NULL
Push(20): 20 -> 10 -> NULL
Push(30): 30 -> 20 -> 10 -> NULL
Pop(): 20 -> 10 -> NULL (returns 30)
```

### Stack Node Structure

```c
struct StackNode {
 int data;
 struct StackNode* next;
};
```

### Stack Operations

#### 1. Push Operation

The push operation adds an element to the top of the stack:

```c
void push(struct StackNode** top, int data) {
 struct StackNode* newNode = (struct StackNode*)malloc(sizeof(struct StackNode));
 newNode->data = data;
 newNode->next = *top;
 *top = newNode;
 printf("Pushed %d to stack\n", data);
}
```

#### 2. Pop Operation

The pop operation removes and returns the top element:

```c
int pop(struct StackNode** top) {
 if (*top == NULL) {
 printf("Stack Underflow!\n");
 return INT_MIN;
 }
 struct StackNode* temp = *top;
 int popped = temp->data;
 *top = (*top)->next;
 free(temp);
 return popped;
}
```

#### 3. Peek Operation

The peek operation returns the top element without removing it:

```c
int peek(struct StackNode* top) {
 if (top == NULL) {
 printf("Stack is empty!\n");
 return INT_MIN;
 }
 return top->data;
}
```

#### 4. isEmpty Operation

Checks if the stack is empty:

```c
int isEmpty(struct StackNode* top) {
 return top == NULL;
}
```

### Complete Stack Implementation Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct StackNode {
 int data;
 struct StackNode* next;
};

// Function prototypes
void push(struct StackNode** top, int data);
int pop(struct StackNode** top);
int peek(struct StackNode* top);
int isEmpty(struct StackNode* top);
void display(struct StackNode* top);

int main() {
 struct StackNode* top = NULL;

 push(&top, 10);
 push(&top, 20);
 push(&top, 30);

 printf("Top element is %d\n", peek(top));

 printf("Popped %d from stack\n", pop(&top));
 printf("Popped %d from stack\n", pop(&top));

 display(top);

 return 0;
}

// Implementation of all stack functions goes here
```

## Queue Implementation using Linked List

### Conceptual Overview

A queue is a First-In-First-Out (FIFO) data structure where the first element added is the first one removed. In linked list implementation, we maintain both front and rear pointers.

```
Queue Operations Visualization:

Initial: Front = NULL, Rear = NULL
Enqueue(10): Front = 10 -> NULL, Rear = 10
Enqueue(20): Front = 10 -> 20 -> NULL, Rear = 20
Enqueue(30): Front = 10 -> 20 -> 30 -> NULL, Rear = 30
Dequeue(): Front = 20 -> 30 -> NULL, Rear = 30 (returns 10)
```

### Queue Node Structure

```c
struct QueueNode {
 int data;
 struct QueueNode* next;
};

struct Queue {
 struct QueueNode *front, *rear;
};
```

### Queue Operations

#### 1. Enqueue Operation

The enqueue operation adds an element to the rear of the queue:

```c
void enqueue(struct Queue* q, int data) {
 struct QueueNode* newNode = (struct QueueNode*)malloc(sizeof(struct QueueNode));
 newNode->data = data;
 newNode->next = NULL;

 if (q->rear == NULL) {
 q->front = q->rear = newNode;
 return;
 }

 q->rear->next = newNode;
 q->rear = newNode;
}
```

#### 2. Dequeue Operation

The dequeue operation removes and returns the front element:

```c
int dequeue(struct Queue* q) {
 if (q->front == NULL) {
 printf("Queue Underflow!\n");
 return INT_MIN;
 }

 struct QueueNode* temp = q->front;
 int dequeued = temp->data;
 q->front = q->front->next;

 if (q->front == NULL) {
 q->rear = NULL;
 }

 free(temp);
 return dequeued;
}
```

#### 3. Other Queue Operations

```c
// Check if queue is empty
int isEmpty(struct Queue* q) {
 return q->front == NULL;
}

// Get front element without removing it
int front(struct Queue* q) {
 if (isEmpty(q)) {
 printf("Queue is empty!\n");
 return INT_MIN;
 }
 return q->front->data;
}

// Get rear element without removing it
int rear(struct Queue* q) {
 if (isEmpty(q)) {
 printf("Queue is empty!\n");
 return INT_MIN;
 }
 return q->rear->data;
}
```

### Complete Queue Implementation Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct QueueNode {
 int data;
 struct QueueNode* next;
};

struct Queue {
 struct QueueNode *front, *rear;
};

// Function prototypes
struct Queue* createQueue();
void enqueue(struct Queue* q, int data);
int dequeue(struct Queue* q);
int isEmpty(struct Queue* q);
int front(struct Queue* q);
int rear(struct Queue* q);
void display(struct Queue* q);

int main() {
 struct Queue* q = createQueue();

 enqueue(q, 10);
 enqueue(q, 20);
 enqueue(q, 30);

 printf("Front element is %d\n", front(q));
 printf("Rear element is %d\n", rear(q));

 printf("Dequeued %d from queue\n", dequeue(q));
 printf("Dequeued %d from queue\n", dequeue(q));

 display(q);

 return 0;
}

// Implementation of all queue functions goes here
```

## Comparison: Array vs Linked List Implementation

| Aspect                        | Array Implementation         | Linked List Implementation       |
| ----------------------------- | ---------------------------- | -------------------------------- |
| **Memory Usage**              | Fixed size, may waste memory | Dynamic, uses only needed memory |
| **Flexibility**               | Fixed capacity               | Can grow/shrink as needed        |
| **Performance**               | O(1) for all operations      | O(1) for all operations          |
| **Memory Management**         | Static allocation            | Dynamic allocation required      |
| **Implementation Complexity** | Simpler                      | More complex due to pointers     |
| **Memory Overhead**           | No overhead                  | Extra memory for pointers        |

## Advantages of Linked List Implementation

1. **Dynamic Size**: Can grow and shrink as needed during program execution
2. **Efficient Memory Usage**: Only uses memory needed for current elements
3. **No Fixed Capacity**: Unlike arrays, doesn't have a predetermined size limit
4. **Efficient Operations**: All stack and queue operations are O(1) time complexity

## Disadvantages of Linked List Implementation

1. **Memory Overhead**: Each node requires extra memory for pointers
2. **Implementation Complexity**: More complex than array implementation
3. **Pointer Management**: Requires careful handling to avoid memory leaks
4. **Cache Performance**: Non-contiguous memory may have worse cache performance

## Applications

### Stack Applications using Linked List

- Function call stack implementation
- Expression evaluation and syntax parsing
- Undo/Redo functionality in applications
- Backtracking algorithms

### Queue Applications using Linked List

- CPU scheduling algorithms
- Print job scheduling
- Breadth-First Search (BFS) in graphs
- Buffer management in operating systems

## Memory Management Considerations

When implementing stacks and queues with linked lists, proper memory management is crucial:

1. **Always free memory**: When popping or dequeuing, always free the node memory
2. **Check for NULL pointers**: Always validate pointers before dereferencing
3. **Avoid memory leaks**: Ensure all allocated memory is properly freed
4. **Handle edge cases**: Consider empty list scenarios in all operations

## Exam Tips

1. **Understand Pointer Manipulation**: Be comfortable with pointer operations as they form the core of linked list implementations
2. **Draw Diagrams**: Visualize operations with diagrams to understand pointer changes
3. **Practice Edge Cases**: Always test with empty, single-element, and multiple-element scenarios
4. **Memory Management**: Remember to free allocated memory in pop/dequeue operations
5. **Time Complexity**: All operations (push, pop, enqueue, dequeue) should be O(1)
6. **Compare Implementations**: Be prepared to discuss advantages/disadvantages vs array implementation
