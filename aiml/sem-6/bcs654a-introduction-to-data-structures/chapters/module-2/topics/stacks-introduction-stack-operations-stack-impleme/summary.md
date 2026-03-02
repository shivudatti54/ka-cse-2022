# Stacks: Introduction, Stack Operations, Stack Implementation using Arrays, Applications of Stacks

### Introduction

- A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
- In a stack, elements are added and removed from the top.
- Stacks can be implemented using arrays, linked lists, or other data structures.

### Stack Operations

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes an element from the top of the stack.
- **Peek** (or **Top**): Returns the element at the top of the stack without removing it.
- **IsEmpty**: Checks if the stack is empty.
- **Size**: Returns the number of elements in the stack.

### Stack Implementation using Arrays

- **Stack**: An array-based implementation of a stack.
- **Stack Operations**:
  - Push: `stack.push(element) = [element] + stack`
  - Pop: `stack.pop() = stack[0]`
  - Peek: `stack.peek() = stack[0]`
  - IsEmpty: `stack.isEmpty() = stack.length == 0`
  - Size: `stack.size() = stack.length`

### Applications of Stacks

- **Evaluating postfix expressions**: Stacks can be used to evaluate postfix expressions by parsing the expression from left to right.
- **Implementing recursive functions**: Stacks can be used to implement recursive functions iteratively.
- **Parser**
- **Compiler**: Stacks are used to parse the syntax of programming languages.
- **Undo/Redo**: Stacks can be used to implement undo/redo functionality in applications.

Important Formulas and Definitions:

- **Base case**: A recursive function's termination condition.
- **Recursive case**: A recursive function's recursive call.
- **Recursion**: A function that calls itself in its own definition.

Theorems:

- **Stack Invariance**: The state of the stack remains the same after a series of operations.
- **Euler's Formula**: A mathematical formula that describes the relationship between the size of a stack and the number of operations performed on it.
