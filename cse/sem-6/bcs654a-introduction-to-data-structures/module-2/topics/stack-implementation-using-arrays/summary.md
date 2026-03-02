# Stack Implementation using Arrays - Summary

## Key Definitions and Concepts

- **Stack**: Linear data structure following LIFO (Last-In-First-Out) principle
- **Array Implementation**: Using contiguous memory allocation with fixed size
- **Top Pointer**: Integer index tracking the topmost element (initialized to -1 for empty stack)
- **Stack Overflow**: Error when pushing to a full stack (`top == MAX-1`)
- **Stack Underflow**: Error when popping from empty stack (`top == -1`)

## Important Formulas and Theorems

```c
// Stack empty condition
if (top == -1)

// Stack full condition
if (top == MAX - 1)

// Push operation formula
stack[++top] = value;

// Pop operation formula
return stack[top--];

// Peek operation
return stack[top];  // Without removal
```

## Key Points

1. Arrays provide O(1) time complexity for all stack operations
2. Requires predefined maximum size (`MAX`) limiting dynamic growth
3. Top pointer starts at -1 (indicates empty stack)
4. Push operation: Check overflow, then increment top before insertion
5. Pop operation: Check underflow, then decrement top after retrieval
6. Memory efficient (no pointers overhead) but fixed capacity
7. Used in system-level implementations like CPU task scheduling
8. Fundamental for understanding recursion and expression evaluation

## Common Mistakes to Avoid

1. Forgetting to check stack full condition before push
2. Not handling stack empty condition during pop/peek
3. Incorrect initialization (top should be -1, not 0)
4. Off-by-one errors in index calculations (MAX vs MAX-1)
5. Returning wrong value in pop (should return stack[top] before decrement)

## Revision Tips

1. **Code Tracing**: Practice dry-running push/pop sequences with index tracking
2. **Diagram Method**: Draw stack diagrams with top pointer positions for different operations
3. **Condition Memorization**: Remember `top == -1` = empty, `top == MAX-1` = full
4. **Comparison Chart**: Create table comparing array vs linked list implementations
5. **Past Papers Focus**: Study previous questions on stack overflow handling and operation sequences

**Exam Focus Areas**: Always mention time complexity (O(1)), write error checks first in code solutions, and practice writing complete functions for push/pop with edge case handling.
