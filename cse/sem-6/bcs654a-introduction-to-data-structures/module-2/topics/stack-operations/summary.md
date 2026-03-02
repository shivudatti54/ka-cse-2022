# Stack Operations

## Overview

Stack operations are restricted to one end called the top, implementing the LIFO principle. The fundamental operations include push, pop, peek, isEmpty, and isFull, all performing in constant O(1) time.

## Key Points

- **Push Operation**: Increments top pointer and adds element at new top position
- **Pop Operation**: Returns element at top and decrements top pointer
- **Peek Operation**: Returns top element without modifying stack structure
- **isEmpty Check**: Verifies if top equals -1 indicating empty stack
- **isFull Check**: Verifies if top equals MAX-1 indicating full stack in array implementation
- **Overflow Prevention**: Check isFull before push to avoid array bounds violation
- **Underflow Prevention**: Check isEmpty before pop to avoid accessing invalid memory

## Important Concepts

- Top pointer initialized to -1 for empty stack
- Push increments top before insertion
- Pop decrements top after retrieval
- All operations have O(1) time complexity
- Error handling crucial to prevent runtime errors
- Stack maintains insertion order with access limited to most recent element

## Notes

- Draw diagrams showing top pointer movement during operations
- Remember to check conditions before performing operations
- Understand difference between peek (read-only) and pop (destructive)
- Practice implementing all operations in code
- Know the sequence: check condition, perform operation, update pointer
