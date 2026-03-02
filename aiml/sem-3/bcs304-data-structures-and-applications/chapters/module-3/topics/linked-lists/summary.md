# Linked Lists - Summary

## Key Definitions and Concepts

- **Linked List:** A linear data structure where elements (nodes) are stored non-contiguously, with each node containing data and a pointer to the next node.
- **Node:** The fundamental unit of a linked list, comprising a data field and a pointer field.
- **Head:** The first node in a linked list; serves as the entry point for all operations.
- **Tail:** The last node in a linked list, whose pointer field is NULL.
- **Dynamic Memory Allocation:** Memory allocation at runtime using malloc() (C) or new (C++).

## Important Formulas and Theorems

- **Node Structure (C):** `struct Node { int data; struct Node* next; };`
- **Time Complexity - Insertion at Beginning:** O(1)
- **Time Complexity - Insertion at End:** O(n) without tail pointer, O(1) with tail pointer
- **Time Complexity - Deletion at Beginning:** O(1)
- **Time Complexity - Traversal/Search:** O(n)
- **Space Complexity for n nodes:** O(n) for data + O(n) overhead for pointers

## Key Points

- Linked lists provide dynamic memory allocation, solving the fixed-size limitation of arrays.
- Each node requires extra memory for storing the pointer, creating overhead compared to arrays.
- Unlike arrays, linked lists do not support random access—elements must be accessed sequentially.
- Insertion and deletion at the beginning are O(1) operations, making linked lists ideal for stack implementation.
- Circular linked lists eliminate the NULL end-marker, useful for round-robin scheduling.
- Doubly linked lists allow bidirectional traversal but require maintaining two pointers per node.
- Memory leaks can occur if malloc() is not paired with free() for each dynamically allocated node.

## Common Mistakes to Avoid

- Forgetting to update the head pointer when inserting or deleting the first node.
- Not handling the NULL condition properly, leading to segmentation faults.
- Losing the reference to subsequent nodes before re-linking pointers during insertion/deletion.
- Assuming O(1) time for insertion at the end without maintaining a tail pointer.
- Not checking for empty list conditions before performing operations.

## Revision Tips

- Practice drawing node diagrams with arrows showing pointer connections for each operation.
- Memorize the three main cases for insertion/deletion: at beginning, at end, and at a middle position.
- Write and dry-run code for reversing a linked list—it frequently appears in exams.
- Compare linked lists with arrays side-by-side to understand trade-offs clearly.
- Solve at least 5-10 previous year questions on linked list operations to understand exam patterns.