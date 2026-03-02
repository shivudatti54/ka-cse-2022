# Introduction to Linked Lists - Summary

## Key Definitions

- **Linked List**: A linear data structure consisting of nodes, where each node contains data and a pointer to the next node
- **Node**: The fundamental building block containing data and link(s) to other nodes
- **Head**: The pointer to the first node in the list; the only external reference to the entire structure
- **NULL Pointer**: A special pointer value indicating the end of the list (None in Python)
- **Singly Linked List**: Contains nodes with only a forward pointer to the next node
- **Doubly Linked List**: Contains nodes with both forward and backward pointers
- **Circular Linked List**: The last node points back to the first node, forming a circle

## Important Formulas

- **Time Complexity - Search**: O(n) where n is the number of nodes
- **Time Complexity - Insertion at beginning**: O(1)
- **Time Complexity - Deletion at beginning**: O(1)
- **Time Complexity - Insertion at end**: O(n) for singly, O(1) for doubly with tail pointer
- **Space Complexity**: O(n) for data + O(n) for pointers = O(n) total

## Key Points

- Linked lists provide dynamic memory allocation, allowing the list to grow and shrink at runtime
- Nodes in a linked list are not stored in contiguous memory locations
- Unlike arrays, linked lists do not allow random access; traversal from the head is required
- Insertion and deletion at known positions are O(1) operations in linked lists
- The head pointer must be preserved to avoid losing access to the entire list
- Memory must be explicitly deallocated to prevent memory leaks
- Linked lists are used as building blocks for stacks, queues, and adjacency list representations of graphs

## Common Mistakes

1. **Forgetting to update the head pointer** when inserting or deleting at the beginning of the list
2. **Not checking for NULL** before accessing node pointers, causing segmentation faults
3. **Losing the reference** to the next node before freeing the current node during deletion
4. **Memory leaks** occurring when the head pointer is overwritten without freeing the original list
5. **Infinite loops** in traversal due to incorrect termination conditions, especially in circular linked lists