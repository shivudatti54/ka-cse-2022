# Introduction to Stacks and Queues

## Overview

Stacks and Queues are fundamental linear data structures that are widely used in computer science and programming. Both are abstract data types that organize data in specific ways, but they differ in how elements are added and removed.

## Stack Data Structure

### Definition

A **Stack** is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle. This means the last element added to the stack is the first one to be removed.

**Real-world analogy:** A stack of plates - you can only add or remove plates from the top.

### Basic Operations

1. **Push**: Add an element to the top of the stack
2. **Pop**: Remove and return the top element
3. **Peek/Top**: Return the top element without removing it
4. **isEmpty**: Check if stack is empty
5. **isFull**: Check if stack is full (for array implementation)

### Applications of Stacks

- Function call management (call stack)
- Expression evaluation and conversion
- Backtracking algorithms
- Undo mechanism in editors
- Browser back button
- Syntax parsing in compilers

## Queue Data Structure

### Definition

A **Queue** is a linear data structure that follows the **First-In-First-Out (FIFO)** principle. This means the first element added to the queue is the first one to be removed.

**Real-world analogy:** A line of people waiting - first person in line is served first.

### Basic Operations

1. **Enqueue**: Add an element to the rear of the queue
2. **Dequeue**: Remove and return the front element
3. **Front**: Return the front element without removing it
4. **Rear**: Return the rear element
5. **isEmpty**: Check if queue is empty
6. **isFull**: Check if queue is full (for array implementation)

### Applications of Queues

- CPU scheduling
- Disk scheduling
- Print job scheduling
- BFS traversal in graphs
- Handling requests in web servers
- Simulation of real-world queues

## Comparison: Stack vs Queue

| Feature      | Stack                   | Queue                 |
| ------------ | ----------------------- | --------------------- |
| Principle    | LIFO                    | FIFO                  |
| Insertion    | Top (Push)              | Rear (Enqueue)        |
| Deletion     | Top (Pop)               | Front (Dequeue)       |
| Access       | Only top element        | Front and rear        |
| Applications | Recursion, backtracking | Scheduling, buffering |

## Importance in Data Structures

Both stacks and queues are essential building blocks for:

- More complex data structures
- Algorithm implementation
- System programming
- Application development

Understanding these structures is crucial for solving many programming problems efficiently.

## Exam Tips

1. Understand LIFO vs FIFO principles clearly
2. Know all basic operations and their time complexities
3. Be able to implement using both arrays and linked lists
4. Remember real-world applications
5. Practice drawing diagrams for operations
6. Understand overflow and underflow conditions
