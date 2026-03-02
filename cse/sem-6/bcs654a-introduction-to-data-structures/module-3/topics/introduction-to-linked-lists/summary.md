# Introduction to Linked Lists

## Overview

A linked list is a linear data structure where elements are stored in nodes, each pointing to the next node in sequence. Unlike arrays, nodes are not stored contiguously in memory, enabling dynamic size and efficient insertion/deletion operations.

## Key Points

- **Node Structure**: Each node contains data part and pointer to next node
- **Dynamic Size**: Can grow or shrink during runtime using dynamic memory allocation
- **Non-Contiguous Memory**: Nodes can be scattered in memory, connected via pointers
- **Head Pointer**: Points to first node, serves as entry point, NULL indicates empty list
- **Types**: Singly (one direction), doubly (bidirectional), circular (last connects to first)
- **Efficient Operations**: O(1) insertion/deletion at known position vs O(n) for arrays
- **Memory Usage**: No wasted space but overhead for storing pointer in each node

## Important Concepts

- Arrays have fixed size and require contiguous memory, linked lists overcome both limitations
- Traversal starts from head, follows next pointers until reaching NULL
- Random access not possible, must traverse sequentially making access O(n)
- Applications include dynamic memory allocation, stack/queue implementation, polynomial representation
- Each node created dynamically using malloc() in C
- Disadvantages include no random access, extra memory for pointers, not cache-friendly

## Notes

- Understand node structure with data and next pointer thoroughly
- Know all four types of linked lists and their characteristics
- Practice drawing linked list diagrams showing nodes and pointers
- Remember time complexities: access O(n), insertion/deletion O(1) at known position
- Be able to compare advantages and disadvantages vs arrays
