# Introduction to Stacks

## Overview

A stack is a linear data structure following the Last-In-First-Out (LIFO) principle where operations are performed only at one end called the top. It is fundamental to many computing applications including function call management and expression evaluation.

## Key Points

- **LIFO Principle**: Last element pushed onto stack is first to be popped off
- **Primary Operations**: Push adds element to top, Pop removes from top, Peek views top without removing
- **Array Implementation**: Uses top pointer index to track topmost element, initialized to -1 for empty stack
- **Overflow Condition**: Occurs when pushing to full stack (top == MAX-1)
- **Underflow Condition**: Occurs when popping from empty stack (top == -1)
- **O(1) Time Complexity**: All operations execute in constant time
- **Applications**: Function call stack, balanced parentheses checking, expression evaluation, backtracking

## Important Concepts

- Stack restricts access to only the top element
- Array implementation simple but fixed size
- Linked list implementation allows dynamic growth
- Checking balanced parentheses uses stack to match opening and closing brackets
- Function call stack manages execution flow and variable scoping
- Both array and linked implementations have O(1) operations

## Notes

- Always check isEmpty before pop to avoid underflow
- Always check isFull before push in array implementation to avoid overflow
- Don't confuse peek (non-destructive) with pop (destructive)
- Practice tracing push/pop operations showing array state and top pointer
- Understand how stack manages nested function calls
