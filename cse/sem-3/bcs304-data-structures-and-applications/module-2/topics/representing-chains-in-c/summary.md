# Representing Chains in C

## Overview

A chain (singly linked list) is a dynamic data structure consisting of nodes, where each node stores data and a pointer to the next node. Unlike arrays, chains allocate memory node-by-node on the heap at runtime, allowing flexible growth without contiguous memory. Each node is independently allocated and linked via pointers.

## Key Points

- **Node Structure**: Self-referential struct containing data and next pointer
- **typedef Usage**: Write `typedef struct Node { int data; struct Node *next; } Node;` for cleaner code
- **NULL Marker**: Last node's next pointer is NULL to indicate end of chain
- **malloc with sizeof**: `Node *newNode = (Node *)malloc(sizeof(Node));` allocates memory
- **NULL Check**: Always check `if (newNode == NULL)` after malloc — failure causes segmentation fault
- **Arrow Operator**: `newNode->data` accesses struct members through pointer
- **Head Pointer**: Stores address of first node; losing it loses entire chain
- **Time Complexities**: Insert/delete at beginning O(1), at end/position O(n), search O(n)
- **Three-Pointer Reverse**: Use prev, current, next to reverse links one at a time

## Important Concepts

- **Self-referential Structure**: A struct containing a pointer to its own type, enabling node linking
- **Dynamic Memory Allocation**: Runtime memory allocation via malloc, stored on heap
- **Memory Leak**: Unreachable allocated memory when pointers are lost; prevented by free()
- **Traversal Pattern**: Start at head, process node, move to next until NULL
- **Head Gateway**: Head pointer is the entry point — functions modifying head must return new head

## Notes

- exams require writing struct Node definition from memory — practice this
- Always include NULL check after malloc in exam code for full marks
- Remember: insert/delete at position k requires pointer to node at position k-1
- When freeing chain, save `next` before calling `free(current)` to avoid losing rest of chain
- Draw diagrams in exams to visualize pointer changes and catch errors
- Edge cases: empty chain, single-node chain, insert/delete at first position
