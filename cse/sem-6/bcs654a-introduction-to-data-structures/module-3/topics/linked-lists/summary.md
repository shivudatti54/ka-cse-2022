# Linked Lists

## Overview

Linked lists are fundamental data structures consisting of nodes connected via pointers, providing dynamic memory allocation and efficient manipulation. They overcome array limitations of fixed size and costly middle insertions through flexible pointer-based connections.

## Key Points

- **Linear Structure**: Elements arranged sequentially but stored non-contiguously in memory
- **Self-Referential**: Node structure contains pointer to same structure type
- **Dynamic Allocation**: Nodes created and destroyed during runtime using malloc/free
- **Pointer-Based Traversal**: Access elements by following next pointers from head
- **Variations**: Singly, doubly, circular, and circular doubly linked lists
- **Head Management**: Head pointer crucial for accessing and manipulating entire list
- **Memory Efficiency**: Allocates only needed space, no pre-allocation required

## Important Concepts

- Singly linked lists allow forward-only traversal with next pointer
- Doubly linked lists enable bidirectional traversal with next and previous pointers
- Circular linked lists have last node pointing to first, no NULL termination
- Operations include insertion, deletion, searching, reversing, and concatenation
- Tail pointer optimization makes end insertions O(1) instead of O(n)
- Common patterns include two-pointer technique for finding middle and detecting cycles

## Notes

- Master pointer manipulation for all linked list operations
- Practice edge cases: empty list, single node, two nodes
- Understand trade-offs between different linked list types
- Remember to free memory when deleting nodes to prevent leaks
- Know when to use linked lists vs arrays based on requirements
