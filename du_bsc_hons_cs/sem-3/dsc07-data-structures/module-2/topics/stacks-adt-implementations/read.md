# Stacks ADT Implementations

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction to Stacks

A **Stack** is one of the most fundamental abstract data types (ADT) in computer science. It represents a linear collection of elements that follows the **Last-In-First-Out (LIFO)** principle — meaning the last element added to the stack is the first one to be removed.

Think of a stack like a pile of plates in a cafeteria: you add new plates on top (push), and when you need a plate, you take it from the top (pop). You cannot directly access or remove plates from the bottom without removing all plates above them first.

### Delhi University Syllabus Context

This topic aligns with the **Data Structures** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science, Semester III/IV. Students are expected to understand both the theoretical concepts of stacks and their practical implementations using arrays and linked lists.

---

## 2. Real-World Relevance and Applications

Stacks are not just theoretical constructs — they have numerous practical applications:

| Application Domain | Real-World Example |
|--------------------|--------------------|
| **Function Call Management** | When a function is called, its return address is pushed onto the stack; when it returns, the address is popped |
| **Expression Evaluation** | Converting infix to postfix/prefix expressions and evaluating them |
| **Undo Mechanisms** | Text editors use stacks to keep track of actions for undo operations |
| **Browser History** | The "Back" button uses a stack to remember previously visited pages |
| **Parentheses Matching** | Compiler syntax checking uses stacks to verify balanced parentheses |
| **Depth-First Search (DFS)** | Graph traversal algorithm uses stacks |
| **Recursion Implementation** | Underlying mechanism for recursive function calls |

---

## 3. Stack ADT Operations

The abstract data type for a stack typically includes the following operations:

### Primary Operations

- **push(element)**: Adds an element to the top of the stack. If the stack is full, it results in a **stack overflow** condition.
- **pop()**: Removes and returns the element from the top of the stack. If the stack is empty, it results in a **stack underflow** condition.
- **peek()** or **top()**: Returns the top element without removing it.

### Auxiliary Operations

- **isEmpty()**: Returns true if the stack contains no elements.
- **isFull()**: Returns true if the stack cannot accommodate more elements (applicable for array implementation).
- **size()**: Returns the number of elements currently in the stack.

---

## 4. Implementation Using Arrays (Static Implementation)

The array-based implementation uses a fixed-size array to store stack elements. We maintain a variable `top` that tracks the index of the topmost element.

### Characteristics

- **Fixed Size**: The maximum capacity is determined at the time of creation.
- **Memory Efficient**: No extra memory for pointers.
- **Simple Implementation**: Easy to understand and implement.

### Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int items[MAX_SIZE];
    int top;
} Stack;

// Initialize stack
void initialize(Stack *s) {
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

// Push element onto stack
bool push(Stack *s, int element) {
    if (isFull(s)) {
        printf("Stack Overflow! Cannot push %d\n", element);
        return false;
    }
    s->items[++s->top] = element;
    return true;
}

// Pop element from stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow! Stack is empty.\n");
        return -1;
    }
    return s->items[s->top--];
}

// Peek at top element
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty.\n");
        return -1;
    }
    return s->items[s->top];
}

// Get size of stack
int size(Stack *s) {
    return s->top + 1;
}

// Main function to demonstrate
int main() {
    Stack s;
    initialize(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Stack size: %d\n", size(&s));
    
    return 0;
}
```

---

## 5. Implementation Using Linked Lists (Dynamic Implementation)

The linked list implementation uses dynamic memory allocation, allowing the stack to grow and shrink as needed. Each node contains data and a pointer to the next node.

### Characteristics

- **Dynamic Size**: Can grow and shrink during execution (limited only by available memory).
- **No Overflow** (unless system runs out of memory).
- **Uses Extra Memory**: Each node requires additional memory for the pointer.

### Implementation in C

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
    int size;
} LinkedListStack;

// Initialize stack
void initialize(LinkedListStack *s) {
    s->top = NULL;
    s->size = 0;
}

// Check if stack is empty
bool isEmpty(LinkedListStack *s) {
    return s->top == NULL;
}

// Push element onto stack
void push(LinkedListStack *s, int element) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    newNode->data = element;
    newNode->next = s->top;
    s->top = newNode;
    s->size++;
}

// Pop element from stack
int pop(LinkedListStack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow! Stack is empty.\n");
        return -1;
    }
    Node *temp = s->top;
    int poppedValue = temp->data;
    s->top = temp->next;
    free(temp);
    s->size--;
    return poppedValue;
}

// Peek at top element
int peek(LinkedListStack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty.\n");
        return -1;
    }
    return s->top->data;
}

// Get size of stack
int size(LinkedListStack *s) {
    return s->size;
}

// Main function to demonstrate
int main() {
    LinkedListStack s;
    initialize(&s);
    
    push(&s, 100);
    push(&s, 200);
    push(&s, 300);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Stack size: %d\n", size(&s));
    
    return 0;
}
```

---

## 6. Complexity Analysis

Understanding the time and space complexity is crucial for the Delhi University examination.

| Operation | Array Implementation | Linked List Implementation |
|-----------|----------------------|---------------------------|
| **push()** | O(1) | O(1) |
| **pop()** | O(1) | O(1) |
| **peek()** | O(1) | O(1) |
| **isEmpty()** | O(1) | O(1) |
| **Space Complexity** | O(n) — fixed | O(n) — dynamic + overhead for pointers |

### Key Points

- Both implementations provide **O(1)** time complexity for the primary operations (push, pop, peek).
- Array implementation has a size limitation but uses less memory per element.
- Linked list implementation can handle more elements but requires extra memory for storing pointers.

---

## 7. Comparison: Array vs Linked List Implementation

| Aspect | Array Implementation | Linked List Implementation |
|--------|---------------------|---------------------------|
| **Memory** | Fixed size, pre-allocated | Dynamic, grows as needed |
| **Overflow** | Occurs when array is full | Only if heap memory exhausted |
| **Memory Overhead** | Less (no pointers) | More (pointer per node) |
| **Implementation** | Simpler | More complex |
| **Performance** | Faster (no malloc/free) | Slower (dynamic allocation) |
| **Flexibility** | Limited by fixed size | Highly flexible |

---

## 8. Practical Coding Exercises

### Exercise 1: Stack for Balanced Parentheses

Write a program to check if an expression has balanced parentheses using a stack.

```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) {
    stack[++top] = c;
}

char pop() {
    return stack[top--];
}

bool isBalanced(char *expr) {
    top = -1;
    for (int i = 0; i < strlen(expr); i++) {
        char c = expr[i];
        if (c == '(' || c == '{' || c == '[') {
            push(c);
        } else if (c == ')' || c == '}' || c == ']') {
            if (top == -1) return false;
            char topChar = pop();
            if ((c == ')' && topChar != '(') ||
                (c == '}' && topChar != '{') ||
                (c == ']' && topChar != '[')) {
                return false;
            }
        }
    }
    return top == -1;
}

int main() {
    char expr[] = "{([()])}";
    if (isBalanced(expr))
        printf("Balanced\n");
    else
        printf("Not Balanced\n");
    return 0;
}
```

### Exercise 2: Reverse a String Using Stack

```c
#include <stdio.h>
#include <string.h>
#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) {
    stack[++top] = c;
}

char pop() {
    return stack[top--];
}

int main() {
    char str[] = "DELHI UNIVERSITY";
    int len = strlen(str);
    
    // Push all characters
    for (int i = 0; i < len; i++) {
        push(str[i]);
    }
    
    // Pop and print
    printf("Reversed string: ");
    while (top != -1) {
        printf("%c", pop());
    }
    printf("\n");
    
    return 0;
}
```

---

## 9. Multiple Choice Questions

### Easy (Level 1)

**Q1. Which principle does a Stack follow?**
- A) First In First Out
- B) Last In First Out
- C) First In Last Out
- D) None of the above

**Answer: B) Last In First Out**

---

**Q2. In an array-based stack implementation, what does 'top' represent?**
- A) The index of the first element
- B) The index of the last element
- C) The size of the stack
- D) The middle element

**Answer: B) The index of the last element**

---

### Medium (Level 2)

**Q3. What is the time complexity of the pop operation in a stack implemented using a linked list?**
- A) O(n)
- B) O(log n)
- C) O(1)
- D) O(n²)

**Answer: C) O(1)**

---

**Q4. In array implementation of stack, stack overflow occurs when:**
- A) top == -1
- B) top == MAX_SIZE - 1
- C) top == 0
- D) top < -1

**Answer: B) top == MAX_SIZE - 1**

---

### Hard (Level 3)

**Q5. A stack of size 5 contains elements: 10, 20, 30 (30 at top). After executing pop() twice and push(40), what will be the element at the bottom of the stack?**
- A) 10
- B) 20
- C) 30
- D) 40

**Answer: A) 10**

*Explanation: Initial stack (bottom to top): 10 → 20 → 30*
- *After pop(): 10 → 20 (top is 20)*
- *After second pop(): 10 (top is 10)*
- *After push(40): 10 → 40 (top is 40)*
- *Bottom element remains 10.*

---

**Q6. Which of the following operations is NOT typically part of the Stack ADT?**
- A) push()
- B) pop()
- C) enqueue()
- D) peek()

**Answer: C) enqueue()**

*Explanation: enqueue() is an operation of Queue ADT, not Stack. Stack uses push() and pop() for insertion and deletion.*

---

## 10. Flashcards for Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What is the fundamental principle of a Stack? | Last-In-First-Out (LIFO) |
| 2 | What is stack overflow? | When we try to push into a full stack |
| 3 | What is stack underflow? | When we try to pop from an empty stack |
| 4 | What is the time complexity of push/pop in stack? | O(1) — Constant time |
| 5 | Which implementation uses extra memory for pointers? | Linked List Implementation |
| 6 | What data structure is used for function call management? | Stack |
| 7 | Which operation returns top element without removing it? | peek() or top() |
| 8 | What is the maximum number of elements in array-based stack? | Defined by MAX_SIZE constant |
| 9 | In array implementation, initial value of top is? | -1 (indicates empty stack) |
| 10 | Which traversal algorithm uses stack? | Depth-First Search (DFS) |

---

## 11. Key Takeaways

1. **Stack Definition**: A LIFO (Last-In-First-Out) abstract data type fundamental to computer science.

2. **Two Main Implementations**:
   - **Array-based**: Fixed size, efficient memory usage, O(1) operations
   - **Linked List-based**: Dynamic size, uses extra memory for pointers, O(1) operations

3. **Primary Operations**: push() — adds element to top; pop() — removes element from top; peek() — views top element without removal.

4. **Complexity**: All primary operations (push, pop, peek) execute in O(1) time complexity for both implementations.

5. **Real-World Applications**: Function call management, expression evaluation, undo mechanisms, browser history, DFS traversal.

6. **Common Errors to Avoid**: Forgetting to check for stack overflow before pushing, forgetting to check for stack underflow before popping.

7. **Delhi University Exam Focus**: Understand the differences between implementations, know the complexity analysis, and be able to write stack operations in C/C++.

---

*Prepared for BSc (Hons) Computer Science — Delhi University, NEP 2024 UGCF Curriculum*