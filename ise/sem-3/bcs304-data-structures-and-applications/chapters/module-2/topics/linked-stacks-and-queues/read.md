# Linked Stacks and Queues

## Introduction

Data structures form the backbone of efficient algorithm design, and among the fundamental linear data structures, stacks and queues occupy a position of paramount importance. While array-based implementations provide straightforward approaches, they suffer from critical limitations: fixed size constraints, inefficient memory utilization, and expensive resize operations. Linked implementations of stacks and queues emerge as elegant solutions to these challenges, offering dynamic memory allocation, constant-time operations, and optimal space utilization.

In the context of the University of Delhi's Computer Science curriculum, understanding linked stacks and queues is essential for several reasons. First, these structures demonstrate how dynamic memory allocation transforms fundamental data structures into flexible, scalable tools. Second, they serve as building blocks for more complex data structures like linked lists, trees, and graphs. Third, practical applications ranging from expression evaluation and backtracking algorithms to task scheduling and breadth-first search rely heavily on these implementations.

This topic explores the theoretical foundations and practical implementations of linked stacks and queues, examining their structural components, operational complexities, advantages over array-based approaches, and real-world applications. Through careful analysis of algorithms and implementations in C, students will develop a comprehensive understanding that prepares them for both theoretical examinations and practical programming challenges.

## Key Concepts

### Understanding Linked Representations

A linked data structure utilizes dynamically allocated nodes, where each node contains both data and a pointer (or reference) to adjacent nodes. Unlike arrays that require contiguous memory allocation, linked structures allocate memory as needed during program execution. This fundamental difference enables linked stacks and queues to overcome the fixed-size limitations of their array-based counterparts.

The node structure for a singly linked implementation consists of two components: a data field storing the element value, and a link field storing the address of the next node. In C, this translates to a structure with the following general form:

```c
typedef struct node {
    datatype data;
    struct node* next;
} Node;
```

The datatype can be int, float, char, or even a more complex structure depending on the application requirements.

### Linked Stack Implementation

A linked stack maintains its elements in a LIFO (Last In, First Out) order, with operations restricted to one end called the top. The linked implementation uses a single pointer, typically named top, that always points to the most recently inserted node. When the stack is empty, top contains NULL.

**Structure Definition:**
```c
typedef struct stack {
    Node* top;
    int size;
} Stack;
```

**Push Operation (Insertion at Top):**
The push operation creates a new node, populates it with the element to be inserted, and links it to the current top node. The algorithm proceeds as follows: allocate memory for a new node, check for allocation failure, assign the data value, set the new node's next pointer to point to the current top, and finally update the top pointer to reference the new node. This operation executes in constant time O(1) regardless of the number of elements in the stack.

**Pop Operation (Deletion from Top):**
The pop operation removes and returns the element at the top of the stack. The process involves checking for stack underflow (empty stack), retrieving the data from the top node, temporarily storing the top pointer, moving the top pointer to the next node, freeing the memory of the removed node, and returning the retrieved data. Like push, pop operates in O(1) time.

**Stack Underflow and Overflow:**
In linked implementations, stack overflow (inability to insert due to memory exhaustion) is theoretically possible but practically rare in modern computing environments with abundant memory. However, stack underflow (attempting to pop from an empty stack) remains a critical condition that must be handled appropriately through error checking.

### Linked Queue Implementation

A linked queue maintains FIFO (First In, First Out) order, with insertions occurring at the rear and deletions from the front. Unlike the linked stack that requires only one pointer, the linked queue necessitates two pointers: front (or head) pointing to the node from which elements are deleted, and rear (or tail) pointing to the node at which new elements are inserted.

**Structure Definition:**
```c
typedef struct queue {
    Node* front;
    Node* rear;
    int size;
} Queue;
```

**Enqueue Operation (Insertion at Rear):**
The enqueue operation adds an element to the rear of the queue. When the queue is empty, both front and rear point to the newly created node. When the queue contains elements, the new node is linked after the current rear node, and the rear pointer is updated. This operation also completes in O(1) time.

**Dequeue Operation (Deletion from Front):**
The dequeue operation removes the element at the front of the queue. The algorithm checks for queue underflow (empty queue), retrieves data from the front node, advances the front pointer to the next node, frees the memory of the removed node, and updates the rear pointer if the queue becomes empty. This operation similarly executes in O(1) time.

### Circular Linked Queues

An alternative implementation uses a circular linked structure where the rear node's next pointer points back to the front node, creating a circular relationship. This approach simplifies implementation in certain scenarios and can improve cache performance. However, the standard two-pointer approach remains more common and equally efficient.

### Memory Management Considerations

Linked implementations require explicit memory management through dynamic allocation (malloc in C) during insertion and deallocation (free in C) during deletion. This responsibility places additional burden on programmers but provides precise control over memory usage. Key considerations include:

**Memory Leaks:** Failing to free memory during deletion operations leads to memory leaks that can exhaust available memory over time. Each pop or dequeue must free the removed node's memory.

**Dangling Pointers:** After freeing a node, any pointers previously referencing that memory become dangling pointers. Programmers must ensure no active pointers reference freed memory.

**Allocation Failure:** Dynamic memory allocation can fail when system memory is exhausted. Robust implementations check malloc return values and handle allocation failures gracefully.

### Complexity Analysis

The primary advantage of linked implementations lies in their consistent O(1) time complexity for all fundamental operations. Unlike array-based implementations that may require O(n) time for resizing, linked structures maintain constant-time operations regardless of size. Space complexity is O(n) where n represents the number of elements, with each node requiring additional overhead for the pointer

### Example field.

## Examples 1: Implementing a Linked Stack for Expression Evaluation

Consider implementing a stack to evaluate postfix expressions. The stack stores intermediate results during evaluation.

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct node {
    int data;
    struct node* next;
} Node;

typedef struct stack {
    Node* top;
} Stack;

void initStack(Stack* s) {
    s->top = NULL;
}

int isEmpty(Stack* s) {
    return s->top == NULL;
}

void push(Stack* s, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = s->top;
    s->top = newNode;
}

int pop(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack Underflow\n");
        return -1;
    }
    Node* temp = s->top;
    int value = temp->data;
    s->top = temp->next;
    free(temp);
    return value;
}

int evaluatePostfix(char* expr) {
    Stack s;
    initStack(&s);
    
    for (int i = 0; expr[i]; i++) {
        if (isdigit(expr[i])) {
            push(&s, expr[i] - '0');
        } else if (expr[i] == '+' || expr[i] == '-' || 
                   expr[i] == '*' || expr[i] == '/') {
            int b = pop(&s);
            int a = pop(&s);
            int result;
            switch(expr[i]) {
                case '+': result = a + b; break;
                case '-': result = a - b; break;
                case '*': result = a * b; break;
                case '/': result = a / b; break;
            }
            push(&s, result);
        }
    }
    return pop(&s);
}

int main() {
    char expr[] = "6523+8*+3+*";
    printf("Result: %d\n", evaluatePostfix(expr));
    return 0;
}
```

This example demonstrates how the linked stack enables dynamic sizing while maintaining efficient operations throughout the evaluation process.

### Example 2: Implementing a Linked Queue for Task Scheduling

A print queue in an operating system represents a practical application of linked queues. Multiple print jobs enter the queue and are processed in FIFO order.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct task {
    int taskId;
    char documentName[50];
    int pages;
    struct task* next;
} Task;

typedef struct queue {
    Task* front;
    Task* rear;
} Queue;

void initQueue(Queue* q) {
    q->front = q->rear = NULL;
}

int isEmpty(Queue* q) {
    return q->front == NULL;
}

void enqueue(Queue* q, int id, char* name, int pages) {
    Task* newTask = (Task*)malloc(sizeof(Task));
    newTask->taskId = id;
    strcpy(newTask->documentName, name);
    newTask->pages = pages;
    newTask->next = NULL;
    
    if (q->rear == NULL) {
        q->front = q->rear = newTask;
    } else {
        q->rear->next = newTask;
        q->rear = newTask;
    }
    printf("Task %d (%s, %d pages) added to queue\n", 
           id, name, pages);
}

void dequeue(Queue* q) {
    if (isEmpty(q)) {
        printf("Queue Underflow - No tasks pending\n");
        return;
    }
    
    Task* temp = q->front;
    printf("Processing Task %d (%s, %d pages)\n", 
           temp->taskId, temp->documentName, temp->pages);
    
    q->front = temp->next;
    
    if (q->front == NULL) {
        q->rear = NULL;
    }
    
    free(temp);
}

int main() {
    Queue printQueue;
    initQueue(&printQueue);
    
    enqueue(&printQueue, 1, "Resume.pdf", 2);
    enqueue(&printQueue, 2, "Report.doc", 15);
    enqueue(&printQueue, 3, "Notes.txt", 5);
    
    dequeue(&printQueue);
    dequeue(&printQueue);
    dequeue(&printQueue);
    dequeue(&printQueue);
    
    return 0;
}
```

This example illustrates the queue's ability to manage tasks efficiently, ensuring fair scheduling based on arrival order.

### Example 3: Handling Edge Cases in Linked Implementations

Consider implementing functions that handle edge cases properly:

```c
// Function to check if stack is empty without modifying it
int stackEmpty(Stack* s) {
    return s->top == NULL;
}

// Function to get top element without removing it
int stackTop(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1; // or some error indicator
    }
    return s->top->data;
}

// Function to free all nodes (cleanup)
void destroyStack(Stack* s) {
    while (!isEmpty(s)) {
        pop(s);
    }
}

// Function to display stack contents (for debugging)
void displayStack(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack (top to bottom): ");
    Node* current = s->top;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
```

These utility functions demonstrate proper handling of edge cases and resource management in linked implementations.

## Exam Tips

1. **Understand the Difference Between Array and Linked Implementations**: In examinations, frequently compare array-based and linked implementations. Remember that linked implementations provide dynamic sizing and consistent O(1) operations but require explicit memory management and use extra memory for pointers.

2. **Trace Operations Step by Step**: Examination questions often require tracing operations. Practice drawing node diagrams and updating pointers visually. Remember the golden rule for linked stacks: new node's next points to current top, then update top. For queues: new node becomes rear's next, then update rear.

3. **Remember Pointer Update Order**: A common error involves incorrect pointer update sequences. When pushing onto a stack, the new node's next must be set BEFORE updating top. When dequeuing from a queue, advance front BEFORE freeing the old node.

4. **Identify Underflow and Overflow Conditions**: Know when each error condition occurs. Stack underflow happens on pop when empty; queue underflow occurs on dequeue when empty. Overflow in linked implementations is theoretical but occurs when malloc returns NULL.

5. **Analyze Time and Space Complexity**: Be prepared to provide complexity analysis. For linked stacks and queues, all operations (push/pop, enqueue/dequeue) are O(1) time. Space is O(n) for n elements, plus O(n) overhead for pointers.

6. **Implement Cleanup Functions**: Many exam questions test understanding of memory management. Know how to write functions that free all nodes to prevent memory leaks, especially when destroying entire data structures.

7. **Understand Queue Front and Rear Dynamics**: Remember that in a linked queue, front always points to the deletion point and rear to the insertion point. When the last element is dequeued, both front and rear become NULL.

8. **Practice C Syntax for Structs and Pointers**: Examination implementations require comfortable use of struct definitions, typedef, pointer notation, malloc, and free. Common syntax errors lose valuable marks.