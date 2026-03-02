# Lists and Chains - Summary

## Key Definitions and Concepts

- **Linked List (Chain)**: A linear data structure where elements (nodes) are stored in non-contiguous memory locations, connected through pointers.

- **Node**: The fundamental unit of a linked list containing a data field and a link (pointer) to the next node.

- **Head (Front)**: The first node of the linked list, serving as the entry point for all operations.

- **NULL Pointer**: A special pointer value (0) indicating the end of the linked list.

- **Singly Linked List**: A chain where each node contains only one pointer pointing to the next node.

## Important Formulas and Theorems

- **Time Complexity - Traversal**: O(n) - must visit each node sequentially
- **Time Complexity - Insertion at Head**: O(1)
- **Time Complexity - Insertion at Tail**: O(n) without tail pointer, O(1) with tail pointer
- **Time Complexity - Deletion**: O(1) at head, O(n) at other positions
- **Space Complexity**: O(n) for n nodes, plus O(n) additional space for pointers

## Key Points

- Linked lists provide dynamic memory allocation, unlike fixed-size arrays
- No memory is wasted in linked lists as nodes are created as needed
- Random access is not possible; traversal is required to reach any node
- Insertion and deletion are efficient (O(1)) at known positions
- Each node requires extra memory for storing the pointer
- Memory must be explicitly managed (malloc/free) in C implementations
- The last node's next pointer is always NULL
- A singly linked list can be converted to a circular linked list by making the last node point to the head

## Common Mistakes to Avoid

1. Forgetting to update the next pointer when inserting or deleting nodes, leaving dangling links
2. Not handling the special case of operations on an empty list
3. Memory leaks caused by not using free() after deleting nodes
4. Confusing the head pointer (which points to first node) with the node itself
5. Not checking for NULL before dereferencing pointers, causing segmentation faults

## Revision Tips

1. Practice drawing node diagrams for each operation—visual understanding is crucial for linked lists
2. Memorize the time complexities of all basic operations for comparison with arrays
3. Write complete C programs implementing linked lists from scratch multiple times
4. Focus on pointer manipulation logic—trace through code with sample inputs
5. Review how linked lists are used in implementing stacks and queues for application-based questions