# Introduction to Stacks and Queues

## Overview

Stacks and queues are fundamental linear data structures that organize data with specific access patterns. Stacks follow Last-In-First-Out (LIFO) principle while queues follow First-In-First-Out (FIFO) principle, each serving distinct purposes in computer science applications.

## Key Points

- **Stack LIFO Principle**: Last element added is first to be removed, like a stack of plates
- **Queue FIFO Principle**: First element added is first to be removed, like a waiting line
- **Stack Operations**: Push (add to top), Pop (remove from top), Peek (view top), isEmpty, isFull
- **Queue Operations**: Enqueue (add to rear), Dequeue (remove from front), Front, Rear, isEmpty, isFull
- **Access Restrictions**: Stack allows access only at top, queue allows access at front and rear
- **Implementation Methods**: Both can be implemented using arrays or linked lists
- **Time Complexity**: All basic operations are O(1) for both structures

## Important Concepts

- Stack applications include function calls, expression evaluation, backtracking, undo mechanisms
- Queue applications include CPU scheduling, BFS traversal, print spooling, buffering
- Overflow occurs when adding to full structure, underflow when removing from empty structure
- Stacks enable recursion and depth-first operations
- Queues enable breadth-first operations and fair resource allocation

## Notes

- Clearly understand LIFO vs FIFO principles for exam questions
- Practice tracing operations step-by-step with diagrams
- Know real-world applications for both structures
- Remember to check for empty/full conditions before operations
- Be able to compare and contrast stacks and queues
