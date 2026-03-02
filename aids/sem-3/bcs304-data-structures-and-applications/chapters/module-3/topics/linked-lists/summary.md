# Linked Lists - Summary

## Key Definitions and Concepts

- **Linked List**: A linear data structure where elements (nodes) are stored in non-contiguous memory locations, connected through pointers.
- **Node**: The fundamental unit containing data and a pointer to the next node (and previous node in doubly linked lists).
- **Head/Start**: The pointer to the first node in the list.
- **NULL Pointer**: Marks the end of the list; last node's next pointer is NULL.
- **Singly Linked List (SLL)**: Each node has one pointer pointing to the next node.
- **Doubly Linked List (DLL)**: Each node has two pointers—one to next node and one to previous node.
- **Circular Linked List**: Last node points back to the first node, forming a circular structure.

## Important Formulas and Theorems

- **Node Structure (SLL)**: `struct Node { int data; Node* next; };`
- **Node Structure (DLL)**: `struct Node { int data; Node* prev; Node* next; };`
- **Time Complexity - Search**: O(n)
- **Time Complexity - Insertion at beginning**: O(1)
- **Time Complexity - Insertion at end**: O(n)
- **Time Complexity - Deletion at beginning**: O(1)
- **Time Complexity - Deletion at end**: O(n)
- **Space Complexity per node**: O(1) extra for pointer(s)

## Key Points

- Linked lists provide dynamic memory allocation—no fixed size required unlike arrays.
- No random access: O(i) time required to access i-th element.
- Insertions and deletions at the beginning are O(1)—faster than arrays.
- Each node requires extra memory for pointer storage.
- Traversal requires following next pointers until NULL is reached.
- Memory is allocated from heap at runtime using malloc/new.
- Circular linked lists eliminate NULL termination and support continuous cycling.
- Doubly linked lists enable bidirectional traversal but use more memory.

## Common Mistakes to Avoid

- Forgetting to update head pointer after insertion at the beginning, leaving the new node inaccessible.
- Not checking for NULL before accessing node->next, causing segmentation faults.
- Losing reference to next node before updating pointers during insertion/deletion.
- Not freeing memory after deletion in languages without garbage collection (C/C++).
- Confusing the head pointer (external reference) with internal node pointers.

## Revision Tips

1. Practice drawing node-pointer diagrams for each operation to build visual understanding.
2. Memorize time complexities for all operations—these frequently appear in exams.
3. Write out complete C/C++ code for creating, inserting, and deleting nodes from scratch.
4. Trace through example operations step-by-step without executing code.
5. Compare linked lists with arrays on parameters: random access, insertion/deletion efficiency, memory usage, and cache performance.