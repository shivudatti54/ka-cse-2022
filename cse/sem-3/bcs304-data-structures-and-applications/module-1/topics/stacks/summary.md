# Stacks

## Overview

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It supports operations like push, pop, peek, isEmpty, and isFull. Stacks are widely used in function call management, expression evaluation, parenthesis matching, backtracking, and more.

## Key Points

- A stack can be implemented using a fixed-size array with a top index.
- The top index is -1 when the stack is empty.
- Overflow occurs when trying to push onto a full stack (top == MAX - 1).
- Underflow occurs when trying to pop from an empty stack (top == -1).
- All core stack operations (push, pop, peek) have a time complexity of O(1).
- The space complexity of an array-based stack is O(n), where n is the maximum size.

## Important Concepts

- **LIFO (Last In, First Out)**: The principle that the last element added to the stack is the first one to be removed.
- **Overflow**: When the stack is full and cannot accommodate more elements.
- **Underflow**: When the stack is empty and there are no elements to remove.
- **Top**: The index that points to the most recently added element.

## Notes

- Be prepared to write the complete array-based stack implementation from scratch.
- Practice writing the parenthesis matching program without reference.
- Always check for overflow before push and underflow before pop in your code.
- Know the difference between `peek` and `pop`.
- List at least 4-5 applications of stacks when asked, including function call management, expression evaluation, parenthesis matching, backtracking, and string reversal.
- Understand that all core stack operations are O(1) and be able to justify this.
- Prefer the struct approach when implementing a stack.
