# Linked Lists - Summary

## Key Definitions and Concepts

- **Node**: The fundamental building block of a linked list containing a data field and a link field (pointer to the next node).
- **Head (Start)**: A pointer variable that points to the first node of the linked list.
- **Singly Linked List**: A linear list where each node contains data and a pointer to the next node; traversal is unidirectional.
- **Doubly Linked List**: Each node contains data, a pointer to the next node, and a pointer to the previous node, allowing bidirectional traversal.
- **Circular Linked List**: The last node points back to the first node, forming a circular structure.

## Important Formulas and Theorems

- **Time Complexity - Insertion at beginning**: O(1) — only head pointer needs updating
- **Time Complexity - Insertion at end**: O(n) — requires traversal without tail pointer
- **Time Complexity - Deletion**: O(n) for finding node, O(1) for deletion once found (at beginning)
- **Time Complexity - Search**: O(n) — linear search required
- **Space Complexity**: O(n) where n is the number of nodes (each node requires additional pointer storage)
- **Reversal Algorithm**: Uses three pointers (prev, curr, next) to reverse links in a single pass with O(n) time and O(1) space

## Key Points

- Linked lists provide dynamic memory allocation, growing and shrinking as needed without predetermined size limits.
- Unlike arrays, linked lists do not require contiguous memory allocation.
- Insertion and deletion operations in linked lists do not require element shifting, unlike arrays.
- The head pointer must never be lost; losing it means losing access to the entire list.
- NULL pointer indicates the end of a linked list in singly linked lists.
- Circular linked lists eliminate the need for NULL checks during traversal in circular applications.
- Doubly linked lists require more memory but provide efficient backward traversal.

## Common Mistakes to Avoid

- Forgetting to update the head pointer when inserting or deleting the first node, resulting in a disconnected list.
- Not checking for NULL before accessing node->next, causing segmentation faults.
- Losing the reference to the next node before reassigning pointers during insertion/deletion.
- Not freeing memory after deletion, leading to memory leaks in C programs.
- Confusing the tail pointer with the head pointer in operations.

## Revision Tips

- Practice drawing node diagrams with arrows to visualize pointer changes during operations.
- Memorize the order of pointer updates: save the next node, reverse the link, move pointers forward.
- Focus on understanding when to use each type of linked list based on application requirements.
- Review previous DU examination questions on linked list operations and implementations.
- Write and execute C programs to reinforce theoretical concepts through practical experience.