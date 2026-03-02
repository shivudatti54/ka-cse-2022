# Stack Implementation using Arrays

## Introduction

Stack implementation using arrays is a fundamental concept in data structure studies that demonstrates how abstract LIFO (Last-In-First-Out) principles translate to concrete programming solutions. Arrays provide a contiguous memory structure that allows O(1) time complexity for core stack operations when implemented correctly, making this approach both efficient and intuitive for beginners.

This implementation forms the basis for understanding more complex dynamic memory implementations (like linked list stacks) and is widely used in system-level programming where memory management is critical. Its fixed-size nature helps students grasp essential error conditions like stack overflow and underflow, which are crucial for robust software development.

Key advantages include:

- Direct element access via index
- Memory efficiency (no pointers required)
- Predictable performance characteristics
- Foundation for CPU stack architecture understanding

## Key Concepts

### Core Components

1. **MAX Constant**: Defines stack capacity

```c
#define MAX 100
```

2. **Stack Array**: Storage for elements

```c
int stack[MAX];
```

3. **Top Pointer**: Tracks current stack top (-1 = empty)

```c
int top = -1;
```

### Fundamental Operations

#### 1. Push Operation

- **Algorithm**:

```c
void push(int value) {
if (top >= MAX-1) {
printf("Stack Overflow");
return;
}
stack[++top] = value;
}
```

- **Time Complexity**: O(1)
- **Error Condition**: Stack Overflow (top == MAX-1)

#### 2. Pop Operation

- **Algorithm**:

```c
int pop() {
if (top <= -1) {
printf("Stack Underflow");
return -1;
}
return stack[top--];
}
```

- **Time Complexity**: O(1)
- **Error Condition**: Stack Underflow (top == -1)

#### 3. Peek Operation

- **Algorithm**:

```c
int peek() {
if (top >= 0) return stack[top];
printf("Stack Empty");
return -1;
}
```

### Memory Diagram

```
Index: 0 1 2 ... MAX-1
 +---+---+---+-----+---+
 | | | | ... | |
 +---+---+---+-----+---+
 ↑
 top
```

- Initial state: top = -1 (all cells empty)
- Full stack: top = MAX-1 (all cells filled)

## Complete C Implementation

```c
#include <stdio.h>
#define MAX 5 // Practical size for demonstration

int stack[MAX];
int top = -1;

void push(int item) {
 if (top == MAX-1) {
 printf("Stack Overflow\n");
 return;
 }
 stack[++top] = item;
}

int pop() {
 if (top == -1) {
 printf("Stack Underflow\n");
 return -1;
 }
 return stack[top--];
}

void display() {
 printf("Current Stack: [ ");
 for(int i=0; i<=top; i++)
 printf("%d ", stack[i]);
 printf("]\n");
}

int main() {
 push(10); push(20); push(30);
 display(); // [10 20 30]
 pop();
 display(); // [10 20]
 return 0;
}
```

## Applications

### Real-World Use Cases

1. **CPU Architecture**: Hardware stacks for function calls
2. **Undo/Redo Systems**: Text editors (sequence of operations)
3. **Backtracking Algorithms**: Maze solving (path memory)
4. **Expression Evaluation**: Postfix notation processing

### Engineering Context

In embedded systems programming, array-based stacks are preferred for:

- Deterministic memory usage
- Avoiding dynamic allocation overhead
- Meeting real-time constraints

## Examples

### Example 1: Stack Operations Sequence

**Operations**: Push(5), Push(8), Pop(), Push(2), Pop(), Pop()

**Solution**:

1. Initial: top = -1
2. Push(5): top=0 → [5]
3. Push(8): top=1 → [5,8]
4. Pop(): Returns 8 → top=0 → [5]
5. Push(2): top=1 → [5,2]
6. Pop(): Returns 2 → top=0 → [5]
7. Pop(): Returns 5 → top=-1 → []

### Example 2: Stack Overflow Handling

**Scenario**: MAX=3, Sequence: Push(1), Push(2), Push(3), Push(4)

**Execution**:

1. Push(1): Success → [1]
2. Push(2): Success → [1,2]
3. Push(3): Success → [1,2,3]
4. Push(4): Stack Overflow → Rejected

## Exam Tips

1. **Overflow/Underflow Conditions**:

- Always check `top == MAX-1` before push
- Check `top == -1` before pop

2. **Time Complexity**:

- All operations (push/pop/peek) are O(1)

3. **Initialization**:

- `top` must be initialized to -1

4. **Array vs Linked List**:

- Arrays: Fixed size, better cache locality
- Linked Lists: Dynamic size, extra pointer overhead

5. **Practical Implementation**:

- Use prefix increment in push (`++top`)
- Use postfix decrement in pop (`top--`)

6. **Error Handling**:

- Return special values (-1) or use exception handling
- Always inform user about overflow/underflow

7. ** Favorite**:

- Be prepared to write complete stack implementation
- Common question: "Show stack status after series of push/pop operations"

8. **Application Questions**:

- Typical scenario: "How stack helps in function call management?"
- Expected answer: Return address storage, parameter passing
