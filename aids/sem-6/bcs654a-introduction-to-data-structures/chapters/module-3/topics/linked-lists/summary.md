# Linked Lists - Summary

## Key Definitions and Concepts

- **Linked List**: A linear data structure where elements (nodes) are stored at non-contiguous memory locations, connected through pointers

- **Self-Referential Structure**: A structure containing a pointer to a structure of the same type, enabling recursive data organization

- **Node**: The fundamental unit of a linked list consisting of a data field and a pointer (or pointers) to the next node(s)

- **Head Pointer**: A pointer variable that marks the beginning of the linked list

- **Circular Linked List**: A variation where the last node points back to the first node instead of NULL

## Important Formulas and Theorems

- **Time Complexity**:
  - Traversal: O(n)
  - Insertion at beginning: O(1)
  - Insertion at end: O(n) without tail pointer, O(1) with tail pointer
  - Deletion at beginning: O(1)
  - Searching: O(n)
  - Reversal in-place: O(n) time, O(1) space

## Key Points

- Linked lists provide dynamic memory allocation unlike fixed-size arrays

- Each node contains data and at least one pointer to the next node

- The last node's pointer is NULL, marking the list end (except circular)

- Insertion and deletion in linked lists do not require shifting elements like arrays

- Linked lists use more memory per element due to pointer storage overhead

- Stack implementation requires only the head pointer (LIFO operations)

- Queue implementation requires both head and tail pointers for O(1) efficiency

- Circular linked lists eliminate NULL checks and enable continuous traversal

- In-place reversal uses three pointers: previous, current, and next

## Common Mistakes to Avoid

- Forgetting to save the next node before modifying pointers during insertion/deletion

- Not handling edge cases: empty list, single node, operations at boundaries

- Losing the head pointer, which makes the entire list inaccessible

- Creating memory leaks by not freeing deleted nodes (though often acceptable in exams)

- Infinite loops when traversing circular lists due to missing termination condition

- Confusing the order of operations when reversing pointers

## Revision Tips

- Practice pointer manipulation by drawing node diagrams for each operation

- Memorize the standard reversal algorithm using three pointers

- Remember that linked lists trade random access efficiency for dynamic size flexibility

- Understand why both head and tail pointers are needed for efficient queue implementation

- Focus on the conceptual difference between static and dynamic allocation