# Stack Operations and Implementation

## Introduction to Stacks

A stack is a fundamental linear data structure that follows the **Last-In-First-Out (LIFO)** principle. This means the last element added to the stack will be the first one to be removed. Stacks are used extensively in computer science for various applications, including function call management, expression evaluation, undo mechanisms, and more.

Think of a stack like a pile of plates: you can only add or remove plates from the top. The basic operations performed on a stack are:

- **Push**: Add an element to the top of the stack
- **Pop**: Remove the top element from the stack

## Stack Operations

### 1. Push Operation

The push operation adds a new element to the top of the stack. Before pushing, we must check if the stack has available space (unless using dynamic memory).

**Algorithm:**

```
1. Check if stack is full (stack overflow condition)
2. If full, display error and exit
3. If not full, increment top pointer
4. Add new element at top position
```

### 2. Pop Operation

The pop operation removes the top element from the stack. Before popping, we must check if the stack is empty.

**Algorithm:**

```
1. Check if stack is empty (stack underflow condition)
2. If empty, display error and exit
3. If not empty, access element at top position
4. Decrement top pointer
5. Return accessed element
```

### 3. Peek Operation

The peek operation allows viewing the top element without removing it from the stack.

**Algorithm:**

```
1. Check if stack is empty
2. If empty, display error
3. If not empty, return element at top position
```

### 4. isEmpty Operation

Checks if the stack contains any elements.

**Algorithm:**

```
1. If top == -1, return true
2. Else, return false
```

### 5. isFull Operation

Checks if the stack has reached its maximum capacity.

**Algorithm:**

```
1. If top == MAX_SIZE - 1, return true
2. Else, return false
```

## Stack Implementation Using Arrays

Arrays provide a simple and efficient way to implement stacks. The implementation requires:

- An array to store stack elements
- A variable 'top' to track the top element position
- A constant 'MAX' to define maximum stack size

### C Implementation

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 5

int stack[MAX];
int top = -1;

// Push operation
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push %d\n", value);
        return;
    }
    top++;
    stack[top] = value;
    printf("Pushed %d onto stack\n", value);
}

// Pop operation
int pop() {
    if (top == -1) {
        printf("Stack Underflow! Cannot pop\n");
        return -1;
    }
    int value = stack[top];
    top--;
    printf("Popped %d from stack\n", value);
    return value;
}

// Peek operation
int peek() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack[top];
}

// Check if stack is empty
int isEmpty() {
    return top == -1;
}

// Check if stack is full
int isFull() {
    return top == MAX - 1;
}

// Display stack elements
void display() {
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}
```

### Stack Visualization

Let's visualize the stack operations with ASCII diagrams:

**Initial State:**

```
Top: -1
Stack: [ ][ ][ ][ ][ ]
```

**After push(10):**

```
Top: 0
Stack: [10][ ][ ][ ][ ]
```

**After push(20):**

```
Top: 1
Stack: [10][20][ ][ ][ ]
```

**After push(30):**

```
Top: 2
Stack: [10][20][30][ ][ ]
```

**After pop():**

```
Top: 1
Stack: [10][20][ ][ ][ ]  // Returns 30
```

## Time Complexity Analysis

| Operation | Time Complexity | Description                       |
| --------- | --------------- | --------------------------------- |
| Push      | O(1)            | Constant time - direct access     |
| Pop       | O(1)            | Constant time - direct access     |
| Peek      | O(1)            | Constant time - direct access     |
| isEmpty   | O(1)            | Constant time - simple comparison |
| isFull    | O(1)            | Constant time - simple comparison |

## Space Complexity

- The space complexity is O(n) where n is the maximum size of the stack
- Fixed memory allocation regardless of actual usage

## Applications of Stacks

1. **Function Call Management**: The call stack stores information about active subroutines
2. **Expression Evaluation**: Converting infix to postfix/prefix notation and evaluation
3. **Undo/Redo Operations**: Text editors and software applications
4. **Backtracking Algorithms**: Maze solving, puzzle games
5. **Syntax Parsing**: Compiler design for checking balanced parentheses
6. **Browser History**: Back button functionality uses stack principle

## Comparison: Array vs Linked List Implementation

| Aspect                    | Array Implementation                 | Linked List Implementation                     |
| ------------------------- | ------------------------------------ | ---------------------------------------------- |
| Memory Usage              | Fixed size, may waste space          | Dynamic allocation, efficient memory use       |
| Flexibility               | Limited by array size                | Can grow as needed (until memory exhausted)    |
| Performance               | All operations O(1)                  | All operations O(1) with proper implementation |
| Memory Overhead           | Minimal (just array and top pointer) | Additional pointer storage per element         |
| Implementation Complexity | Simple                               | Moderately complex                             |

## Common Errors and Solutions

1. **Stack Overflow**: Trying to push when stack is full
   - Solution: Check isFull() before push operation

2. **Stack Underflow**: Trying to pop when stack is empty
   - Solution: Check isEmpty() before pop operation

3. **Memory Wastage**: Fixed array size may not be fully utilized
   - Solution: Use dynamic arrays or linked list implementation

## Exam Tips

1. **Remember LIFO Principle**: Always think "last in, first out" when solving stack problems
2. **Visualize Operations**: Draw the stack before and after each operation in diagram questions
3. **Check Boundaries**: Always verify stack empty/full conditions in implementation questions
4. **Time Complexity**: All basic operations are O(1) - this is frequently tested
5. **Application Questions**: Be prepared to explain real-world uses of stacks with examples
6. **Code Tracing**: Practice tracing through stack operation sequences to predict final state
