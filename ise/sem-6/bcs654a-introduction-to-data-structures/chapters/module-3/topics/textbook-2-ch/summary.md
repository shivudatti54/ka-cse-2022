# Textbook 2: Ch - Linked Lists

## Introduction

- Linked lists are a fundamental data structure in computer science.
- A linked list is a linear collection of data elements whose order is not given by their physical placement in memory.
- It is a collection of nodes, each of which contains a value and a reference (i.e., a "link") to the next node in the sequence.

## Key Concepts

- **Node**: A node is a fundamental component of a linked list.
- **Head**: The head of a linked list is the first node in the list.
- **Tail**: The tail of a linked list is the last node in the list.
- **Next**: The next field of a node is a reference to the next node in the list.

## Operations

- **Insertion**: Inserting a new node at a specific position in the list.
- **Deletion**: Deleting a node from the list at a specific position.
- **Traversal**: Traversing the list from head to tail.

## Theorems

- **Theorem 1**: A linked list is a dynamic data structure, meaning that nodes can be added or removed from the list at runtime.
- **Theorem 2**: A linked list can be traversed in O(n) time, where n is the number of nodes in the list.

## Formulas

- **Insertion Formula**: To insert a new node at position `i`, update the `next` field of each node from index `i` to `i+1`.
- **Deletion Formula**: To delete a node at position `i`, update the `next` field of each node from index `i` to `i-1`.

## Important Definitions

- **Linked List Data Structure**: A data structure in which each element points to the next element.
- **Self-Referential Structure**: A linked list where each node contains a reference to the next node in the list, as well as a reference to the previous node.

## Self-Referential Structures

- A self-referential linked list is a linked list where each node contains a reference to the previous node in the list.
- This allows for efficient insertion and deletion of nodes at any position in the list.

## Important Operations

- **Insertion at Head**: Inserting a new node at the head of the list.
- **Insertion at Tail**: Inserting a new node at the tail of the list.
- **Deletion at Head**: Deleting the head node from the list.
- **Deletion at Tail**: Deleting the tail node from the list.
