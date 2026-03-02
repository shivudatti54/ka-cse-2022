# Linked Lists - Summary

## Key Definitions and Concepts

- LINKED LIST: A linear dynamic data structure where elements (nodes) are stored in separate memory locations and connected through pointers

- NODE: The fundamental building block containing data and a pointer (or pointers in doubly linked lists) to the next/previous node

- HEAD: The first node in a linked list; serves as the entry point to access the entire list

- SINGLY LINKED LIST: Each node contains data and one pointer to the next node; traversal is one-directional

- DOUBLY LINKED LIST: Each node contains data and two pointers (next and previous); allows bidirectional traversal

- CIRCULAR LINKED LIST: The last node points back to the first node, forming a closed loop

## Important Formulas and Theorems

- Node Structure (Singly): struct Node { data_type data; struct Node *next; }

- Node Structure (Doubly): struct Node { struct Node *prev; data_type data; struct Node *next; }

- Time Complexity - Search: O(n)
- Time Complexity - Insertion at beginning: O(1)
- Time Complexity - Insertion at end: O(n) without tail pointer
- Time Complexity - Deletion at beginning: O(1)
- Time Complexity - Deletion at end: O(n)

## Key Points

- Linked lists provide dynamic size allocation unlike fixed-size arrays
- Memory is allocated at runtime using malloc() and must be freed using free()
- No random access is possible; must traverse sequentially from head
- Insertion and deletion at known positions are O(1) operations
- Linked lists use more memory than arrays due to pointer storage overhead
- The head pointer must be preserved to maintain access to the list
- NULL pointer indicates the end of the list
- Circular linked lists eliminate the NULL end marker

## Common Mistakes to Avoid

- NOT CHECKING FOR NULL before accessing node->next causes segmentation faults
- LOSING THE HEAD POINTER by reassigning it before saving the reference
- FORGETTING TO FREE memory of deleted nodes causes memory leaks
- NOT handling edge cases like empty list or single node operations
- REVERSING pointer assignment order during insertion causes loss of the list

## Revision Tips

- Practice drawing before and after diagrams for all operations
- Write complete C programs to implement all operations from scratch
- Compare linked lists with arrays for different operation complexities
- Focus on pointer manipulation logic—draw pointers explicitly
- Memorize time complexities as they frequently appear in exam questions