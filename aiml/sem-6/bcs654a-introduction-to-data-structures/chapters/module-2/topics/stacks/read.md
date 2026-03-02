# Introduction to Stacks

## 1. What is a Stack?

A **Stack** is a fundamental linear data structure that follows a particular order in which operations are performed. The order is **LIFO (Last In, First Out)**. This means the last element added to the stack will be the first element to be removed.

Imagine a stack of plates in a cafeteria. You can only take the top plate, and new plates are added to the top. The plate at the bottom of the stack was the first one placed there and will be the last one to be used. This perfectly illustrates the LIFO principle.

Stacks are used in a wide variety of applications, including:

- Function call management in programming languages (the call stack)
- Undo/Redo features in text editors and graphic software
- Expression evaluation and syntax parsing (e.g., checking for balanced parentheses)
- Backtracking algorithms (e.g., maze solving, graph traversals)
- Browser history (the back button)

## 2. Basic Operations on a Stack

The operations on a stack are limited because access is restricted to the top element. The primary operations are:

1.  **`push(item)`**: Adds an element (`item`) to the top of the stack.
2.  **`pop()`**: Removes and returns the top element from the stack. If the stack is empty, it results in an **underflow** condition.
3.  **`peek()`** or **`top()`**: Returns the top element of the stack without removing it. This is used to inspect the top element.
4.  **`isEmpty()`**: Returns `true` if the stack is empty, otherwise `false`.
5.  **`isFull()`**: (For fixed-size implementations) Returns `true` if the stack is full, otherwise `false`.

## 3. Stack Implementation using Arrays

One of the simplest ways to implement a stack is by using an array. We use a pointer, often called `top`, to keep track of the topmost element's index.

### Algorithm and Code

We define a structure (in C) to hold the stack components: the array, the top index, and the maximum capacity.

```c
#define MAX 1000 // Maximum size of the stack

struct Stack {
    int top;          // Index of the top element
    int items[MAX];   // Array to store stack elements
};
```

**a) Initialization (`createStack`)**
We need a function to initialize a new stack. This involves setting the `top` index to `-1`, which signifies an empty stack.

```c
// Function to create an empty stack
void createStack(struct Stack* s) {
    s->top = -1; // Initialize top to -1, indicating the stack is empty
}
```

**b) `isEmpty()` Operation**
This function checks if the stack is empty by verifying if `top` is `-1`.

```c
// Function to check if the stack is empty
int isEmpty(struct Stack* s) {
    return (s->top == -1);
}
```

**c) `isFull()` Operation**
This function checks if the stack is full by verifying if `top` is equal to `MAX - 1`.

```c
// Function to check if the stack is full
int isFull(struct Stack* s) {
    return (s->top == MAX - 1);
}
```

**d) `push(item)` Operation**
This function adds an element to the top of the stack.

1.  Check if the stack is full (to avoid **overflow**).
2.  If not full, increment `top` and place the new item at the `top` index.

```c
// Function to add an item to the stack
void push(struct Stack* s, int item) {
    if (isFull(s)) {
        printf("Stack is FULL! Cannot push %d\n", item);
    } else {
        s->items[++(s->top)] = item; // Increment top, then assign the item
        printf("%d pushed to stack\n", item);
    }
}
```

**e) `pop()` Operation**
This function removes and returns the top element from the stack.

1.  Check if the stack is empty (to avoid **underflow**).
2.  If not empty, return the item at the `top` index and then decrement `top`.

```c
// Function to remove an item from the stack
int pop(struct Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is EMPTY! Cannot pop\n");
        return -1; // Return an error value
    } else {
        return s->items[(s->top)--]; // Return the item, then decrement top
    }
}
```

**f) `peek()` Operation**
This function returns the top element without removing it.

1.  Check if the stack is empty.
2.  If not empty, return the item at the `top` index.

```c
// Function to get the top item without removing it
int peek(struct Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    } else {
        return s->items[s->top];
    }
}
```

### Visual Representation of Stack Operations

Let's visualize the operations on an array-based stack with a capacity of 5.

**Initial State:**

```
Index: [0] [1] [2] [3] [4]
Value:  -   -   -   -   -
Top: -1 (Stack is empty)
```

**Operation: push(10)**

```
Top becomes 0
Index: [0] [1] [2] [3] [4]
Value: 10   -   -   -   -
Top: 0
```

**Operation: push(20)**

```
Top becomes 1
Index: [0] [1] [2] [3] [4]
Value: 10  20   -   -   -
Top: 1
```

**Operation: push(30)**

```
Top becomes 2
Index: [0] [1] [2] [3] [4]
Value: 10  20  30   -   -
Top: 2
```

**Operation: pop()**

```
Returns 30, Top becomes 1
Index: [0] [1] [2] [3] [4]
Value: 10  20  30   -   -  (Value 30 is logically removed)
Top: 1
```

**Operation: push(40)**

```
Top becomes 2, overwrites index 2
Index: [0] [1] [2] [3] [4]
Value: 10  20  40   -   -
Top: 2
```

## 4. Applications of Stacks

Stacks are incredibly versatile. Here are two classic applications:

**a) Function Call Stack:**
The most crucial use of a stack is in program execution. When a function is called, its parameters, return address, and local variables are "pushed" onto a call stack. When a function returns, its frame is "popped" from the stack. This manages the flow of execution and variable scoping.

**b) Balanced Parentheses:**
Stacks are perfect for checking if parentheses in an expression are balanced. The algorithm is:

1.  Traverse the expression.
2.  If an opening bracket (`(`, `{`, `[`) is found, push it onto the stack.
3.  If a closing bracket (`)`, `}`, `]`) is found:
    - Pop the top of the stack.
    - Check if the popped opening bracket matches the closing bracket.
4.  If the stack is empty at the end, the expression is balanced.

_Example: `{([])}` is balanced. `([)]` is not balanced._

## 5. Comparison: Array vs. Linked List Implementation

| Feature            | Array-Based Stack                                                 | Linked List-Based Stack                                                                                                   |
| :----------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Memory Usage**   | Pre-allocates fixed memory. Can lead to overflow or wasted space. | Dynamically allocates memory as needed. More efficient use of memory.                                                     |
| **Flexibility**    | Fixed size. Cannot grow beyond the predefined capacity.           | Dynamic size. Can grow until system memory is exhausted.                                                                  |
| **Performance**    | All operations are **O(1)** (constant time).                      | All operations are **O(1)** (constant time), but involves pointer manipulation and memory allocation overhead for `push`. |
| **Implementation** | Simpler to implement and understand.                              | Slightly more complex due to pointer handling.                                                                            |
| **Use Case**       | When the maximum size of the stack is known beforehand.           | When the size of the stack is unpredictable.                                                                              |

## 6. Exam Tips and Common Pitfalls

- **LIFO Principle:** Always remember Last-In-First-Out. This is the core of every stack operation and related question.
- **Underflow and Overflow:** Always check for `isEmpty()` before `pop()` and for `isFull()` (in array implementation) before `push()` to avoid runtime errors. Not doing so is a common mistake.
- **`peek()` vs `pop()`:** `peek()` only looks at the top element; `pop()` removes it. Don't confuse the two.
- **Tracing Operations:** In exam questions, you will often be asked to show the state of a stack after a series of `push` and `pop` operations. Draw the array and carefully track the `top` pointer.
- **Application Questions:** Be prepared to explain _how_ a stack is used in a specific application (e.g., "Explain how a stack can be used to check for balanced parentheses."). Write the algorithm step-by-step.
- **Complexity Analysis:** Remember that all core stack operations (push, pop, peek, isEmpty) have a **time complexity of O(1)** for both array and linked list implementations.
