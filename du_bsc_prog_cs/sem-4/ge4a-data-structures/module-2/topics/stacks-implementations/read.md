# Stacks and Implementations

## Introduction

A **stack** is one of the most fundamental and widely used abstract data types in computer science. It follows the **Last In, First Out (LIFO)** principle, meaning that the last element added to the stack is the first one to be removed. This simple yet powerful concept forms the backbone of many algorithmic solutions and is essential for understanding more complex data structures.

Stacks are ubiquitous in computing applications. They are used in function call management (the call stack), expression evaluation and syntax parsing, undo mechanisms in text editors, backtracking algorithms, and memory management. Understanding stacks deeply is crucial for any computer science student, as they appear frequently in technical interviews, competitive programming, and real-world software development.

In this topic, we will explore the theoretical concept of a stack, examine its essential operations, and dive into two primary implementation approaches: **array-based (static)** and **linked list-based (dynamic)** implementations. We will analyze the time and space complexities of each implementation and discuss practical applications where stacks play a critical role.

## Key Concepts

### Stack Definition and Properties

A stack is an abstract data type (ADT) that supports two primary operations:
- **push(element)**: Adds an element to the top of the stack
- **pop()**: Removes and returns the element from the top of the stack

Additionally, stacks typically support helper operations:
- **peek()** or **top()**: Returns the top element without removing it
- **isEmpty()**: Checks whether the stack is empty
- **isFull()**: Checks whether the stack is full (for array implementation)
- **size()**: Returns the number of elements in the stack

The defining characteristic of a stack is the **LIFO** property. Imagine a stack of plates in a cafeteria — you can only add or remove plates from the top. Similarly, in a stack data structure, you can only access the most recently added element.

### Stack as an Abstract Data Type (ADT)

An Abstract Data Type (ADT) defines the behavior of a data structure without specifying its implementation details. For a stack, the ADT specification includes:

```
Data:
- A collection of elements
- A pointer/index to the top element

Operations:
- push(item): Add item to the top
- pop(): Remove and return top element
- peek(): Return top element without removal
- isEmpty(): Return true if stack is empty
- isFull(): Return true if stack is full (array implementation)
- size(): Return number of elements
```

### Array-Based (Static) Implementation

In the array-based implementation, we use a fixed-size array to store stack elements. We maintain a **top** index that points to the current top element. This implementation is straightforward but has a fixed capacity.

**Characteristics:**
- Fixed maximum size (determined at initialization)
- Memory is allocated contiguously
- Simple to implement
- Risk of stack overflow if capacity is exceeded

**Implementation Details:**
- Array `stack[]` of size `MAX_SIZE`
- Integer `top` initialized to -1 (indicating empty stack)
- When pushing: increment top, store element at `stack[top]`
- When popping: retrieve element at `stack[top]`, decrement top

### Linked List-Based (Dynamic) Implementation

In the linked list-based implementation, we use a singly linked list where each node contains data and a pointer to the next node. The top of the stack is represented by the head of the linked list. This implementation grows and shrinks dynamically.

**Characteristics:**
- Dynamic size (limited only by available memory)
- No memory wastage
- Slightly more complex implementation
- Each node requires extra memory for the pointer

**Implementation Details:**
- Node structure: `data` + `next` pointer
- `top` points to the first node (head)
- Push: Create new node, point it to current top, update top
- Pop: Get data from top node, move top to next node, free old node

### Time and Space Complexity Analysis

| Operation | Array Implementation | Linked List Implementation |
|-----------|---------------------|---------------------------|
| Push      | O(1)                | O(1)                      |
| Pop       | O(1)                | O(1)                      |
| Peek      | O(1)                | O(1)                      |
| isEmpty   | O(1)                | O(1)                      |

**Space Complexity:**
- Array: O(n) where n is the maximum capacity
- Linked List: O(n) for n elements, but with higher overhead per element

### Applications of Stacks

1. **Function Call Management**: The call stack stores return addresses, local variables, and parameters during function calls
2. **Expression Evaluation**: Converting infix to postfix/prefix expressions and evaluating postfix expressions
3. **Undo Mechanisms**: Text editors use stacks to track changes for undo operations
4. **Backtracking Algorithms**: Depth-first search uses stacks to explore paths
5. **Parenthesis Matching**: Checking if brackets are balanced in expressions
6. **Memory Management**: Stack memory allocation in programs

## Examples

### Example 1: Array-Based Stack Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int arr[MAX_SIZE];
    int top;
} Stack;

// Initialize stack
void initStack(Stack *s) {
    s->top = -1;
}

// Check if stack is empty
bool isEmpty(Stack *s) {
    return s->top == -1;
}

// Check if stack is full
bool isFull(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

// Push operation
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack Overflow! Cannot push %d\n", value);
        return;
    }
    s->arr[++(s->top)] = value;
    printf("Pushed %d to stack\n", value);
}

// Pop operation
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow!\n");
        return -1;
    }
    return s->arr[(s->top)--];
}

// Peek operation
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->arr[s->top];
}

// Main function to demonstrate
int main() {
    Stack s;
    initStack(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Is empty: %s\n", isEmpty(&s) ? "Yes" : "No");
    
    return 0;
}
```

**Output:**
```
Pushed 10 to stack
Pushed 20 to stack
Pushed 30 to stack
Top element: 30
Popped: 30
Popped: 20
Is empty: No
```

### Example 2: Linked List-Based Stack Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *top;
} StackLL;

// Initialize stack
void initStack(StackLL *s) {
    s->top = NULL;
}

// Check if empty
bool isEmpty(StackLL *s) {
    return s->top == NULL;
}

// Push operation
void push(StackLL *s, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    newNode->data = value;
    newNode->next = s->top;
    s->top = newNode;
    printf("Pushed %d to stack\n", value);
}

// Pop operation
int pop(StackLL *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow!\n");
        return -1;
    }
    Node *temp = s->top;
    int value = temp->data;
    s->top = temp->next;
    free(temp);
    return value;
}

// Peek operation
int peek(StackLL *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->top->data;
}

// Main function to demonstrate
int main() {
    StackLL s;
    initStack(&s);
    
    push(&s, 100);
    push(&s, 200);
    push(&s, 300);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Is empty: %s\n", isEmpty(&s) ? "Yes" : "No");
    
    return 0;
}
```

### Example 3: Balancing Parenthesis Using Stack

A classic application of stacks is checking whether an expression has balanced parentheses.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    char arr[MAX_SIZE];
    int top;
} Stack;

void initStack(Stack *s) { s->top = -1; }
bool isEmpty(Stack *s) { return s->top == -1; }
bool isFull(Stack *s) { return s->top == MAX_SIZE - 1; }

void push(Stack *s, char c) { s->arr[++(s->top)] = c; }
char pop(Stack *s) { return s->arr[(s->top)--]; }
char peek(Stack *s) { return s->arr[s->top]; }

bool isBalanced(char *expr) {
    Stack s;
    initStack(&s);
    
    for (int i = 0; i < strlen(expr); i++) {
        char ch = expr[i];
        
        if (ch == '(' || ch == '[' || ch == '{') {
            push(&s, ch);
        }
        else if (ch == ')' || ch == ']' || ch == '}') {
            if (isEmpty(&s)) return false;
            
            char top = pop(&s);
            if ((ch == ')' && top != '(') ||
                (ch == ']' && top != '[') ||
                (ch == '}' && top != '{')) {
                return false;
            }
        }
    }
    return isEmpty(&s);
}

int main() {
    char expr1[] = "((a+b)*(c-d))";
    char expr2[] = "((a+b)*(c-d)";
    
    printf("%s is %s\n", expr1, isBalanced(expr1) ? "Balanced" : "Not Balanced");
    printf("%s is %s\n", expr2, isBalanced(expr2) ? "Balanced" : "Not Balanced");
    
    return 0;
}
```

**Output:**
```
((a+b)*(c-d)) is Balanced
((a+b)*(c-d) is Not Balanced
```

## Exam Tips

1. **Remember LIFO Property**: The Last In, First Out principle is fundamental to understanding stack behavior. Always think about which element is accessible at any point.

2. **Know Your Implementations**: Be thorough with both array-based and linked list-based implementations. Understand when to use each—array for fixed-size, predictable requirements; linked list for dynamic size needs.

3. **Time Complexities Are Constant**: All primary stack operations (push, pop, peek, isEmpty) have O(1) time complexity. This is a key advantage of stacks.

4. **Overflow vs Underflow**: Remember the difference—stack overflow occurs when trying to push into a full stack; stack underflow occurs when trying to pop from an empty stack.

5. **Diagram It Out**: In exams, draw stack diagrams to visualize push and pop operations. This helps avoid errors and demonstrates clear understanding to evaluators.

6. **Applications Matter**: Be prepared to explain at least 3-4 real-world applications of stacks (function calls, expression evaluation, undo mechanism, parenthesis matching).

7. **Practice Implementation**: Write stack implementations from scratch in C. Understand how `top` pointer works in both array and linked list versions.

8. **Edge Cases**: Always consider edge cases—what happens when you pop all elements? What happens when the array is full? These show attention to detail.

9. **Space Analysis**: Remember that array implementation wastes memory if the stack doesn't fill up, while linked list has overhead per node (the pointer).

10. **Applications in Algorithms**: Stacks are essential in depth-first search (DFS), tower of Hanoi, and expression conversion algorithms. Know these for algorithm-focused questions.