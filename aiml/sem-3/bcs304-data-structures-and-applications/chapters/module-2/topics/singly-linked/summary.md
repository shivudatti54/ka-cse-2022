# Singly Linked Lists - Summary

## Key Definitions and Concepts

A SINGLY LINKED LIST is a linear data structure where elements (called nodes) are stored in non-contiguous memory locations, with each node containing a data field and a pointer to the next node. The HEAD is the first node, and the LAST NODE contains NULL in its next pointer to indicate the end of the list. Each node consists of two components: the DATA FIELD (stores actual information) and the LINK/NEXT POINTER (stores address of the next node).

## Important Formulas and Theorems

Time Complexities for Singly Linked List Operations:
- Insertion at beginning: O(1)
- Insertion at end: O(n)
- Deletion at beginning: O(1)
- Deletion at end: O(n)
- Searching: O(n)
- Traversal: O(n)
- Space Complexity: O(n) where n is number of nodes

## Key Points

- Linked lists provide DYNAMIC MEMORY ALLOCATION unlike fixed-size arrays, allowing efficient memory utilization.
- Nodes are typically created using malloc() in C or new operator in C++.
- The LAST NODE always points to NULL to indicate list termination.
- Insertion at the beginning requires updating the head pointer, while insertion at the end requires traversal to find the last node.
- Deletion requires maintaining both current and previous pointers to properly adjust links.
- Singly linked lists can ONLY be traversed in one direction (forward), unlike doubly linked lists.
- Memory leaks can occur if nodes are not properly freed after deletion.
- Advantages over arrays: efficient insertion/deletion, no memory wastage, variable size.
- Disadvantages compared to arrays: no random access, extra memory for pointers, no cache locality.

## Common Mistakes to Avoid

Failing to check for NULL pointers before accessing node data leads to segmentation faults. Forgetting to update the head pointer when inserting or deleting the first node breaks the list structure. Not maintaining the previous pointer during traversal causes loss of reference to preceding nodes. Attempting to traverse backward in a singly linked list is impossible without additional pointers.

## Revision Tips

Draw DIAGRAMS when solving linked list problems to visualize pointer changes clearly. Practice all three insertion positions (beginning, middle, end) and all deletion scenarios. Memorize the time complexities as they frequently appear in comparison questions. Review pointer manipulation in C thoroughly, especially the arrow operator (->) and address-of operator (&). Write code for creating, traversing, inserting, and deleting nodes until these operations become automatic.