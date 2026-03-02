# Singly Linked Lists - Summary

## Key Definitions and Concepts

A SINGLY LINKED LIST is a linear data structure where elements (nodes) are stored in memory non-contiguously, with each node containing a data field and a pointer to the next node. The HEAD is a pointer to the first node, and a NULL pointer indicates the end of the list. A NODE consists of data and a next pointer field, typically implemented using a struct in C.

## Important Formulas and Theorems

- Node structure: struct Node { datatype data; struct Node* next; }
- Time complexity for insertion at beginning: O(1)
- Time complexity for insertion at end: O(n)
- Time complexity for deletion at beginning: O(1)
- Time complexity for deletion at end: O(n)
- Time complexity for search: O(n)
- Space complexity: O(n) for n elements plus O(n) for pointers

## Key Points

- SINGLY LINKED LISTS provide dynamic size allocation unlike fixed-size arrays
- Nodes are allocated individually using malloc() and must be freed using free()
- The last node's next pointer is always NULL
- No random access is possible; traversal from head is required
- Insertion and deletion at the beginning are O(1) operations
- Maintaining a tail pointer makes end operations O(1)
- Memory is not wasted as elements can be added as needed
- Linked lists are ideal for scenarios with frequent insertions and deletions

## Common Mistakes to Avoid

- FORGETTING TO UPDATE THE HEAD POINTER after insertion at the beginning
- NOT CHECKING FOR NULL before accessing node pointers, causing segmentation faults
- LOSING THE POINTER TO THE NEXT NODE before rewiring links during deletion
- NOT FREEING MEMORY when deleting nodes, leading to memory leaks
- TRAVERSING BEYOND NULL, which causes undefined behavior

## Revision Tips

- PRACTICE WRITING linked list functions repeatedly until you can do them without reference
- DRAW DIAGRAMS step by step for each operation to visualize pointer changes
- MEMORIZE TIME COMPLEXITIES for all operations as this is frequently tested
- REVIEW PREVIOUS YEAR QUESTION PAPERS from DU to understand the exam pattern and important topics
- IMPLEMENT ALL OPERATIONS from scratch including reverse, find middle, and count nodes