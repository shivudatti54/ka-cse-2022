# Singly Linked List

## Overview

A singly linked list is the simplest linked list where each node contains data and a pointer to the next node, allowing forward-only traversal. It provides dynamic sizing and efficient insertion/deletion at the cost of sequential access.

## Key Points

- **Unidirectional**: Each node has one next pointer, traversal only in forward direction
- **Node Structure**: Contains data field and next pointer to following node
- **Head Pointer**: Entry point to list, NULL indicates empty list
- **Insert at Beginning**: O(1) operation updating head pointer
- **Insert at End**: O(n) requires traversal unless tail pointer maintained
- **Delete Operations**: O(1) from beginning, O(n) from end or middle
- **Common Algorithms**: Reverse using three pointers, find middle with two-pointer technique

## Important Concepts

- Last node's next pointer is NULL indicating list termination
- Insert at beginning fastest operation, just update head
- Delete requires finding previous node to update its next pointer
- Two-pointer technique finds middle in one pass using slow/fast pointers
- Floyd's cycle detection uses slow/fast pointers to identify loops
- Tail pointer optimization makes end insertions O(1)
- Edge cases include empty list, single node, and position out of bounds

## Notes

- Practice implementing all insertion and deletion operations
- Master pointer manipulation: temp = temp->next for traversal
- Always free memory when deleting nodes to prevent leaks
- Handle edge cases: NULL head, single node, invalid positions
- Draw diagrams showing pointer changes during operations
