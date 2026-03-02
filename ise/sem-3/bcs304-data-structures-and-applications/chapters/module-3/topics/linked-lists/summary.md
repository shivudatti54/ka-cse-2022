# Linked Lists - Summary

## Key Definitions and Concepts

- LINKED LIST: A linear data structure consisting of nodes, where each node contains a data field and a link field pointing to the next node
- NODE: The basic unit of a linked list containing data and pointer(s) to subsequent nodes
- HEAD: External pointer marking the beginning of the linked list
- SINGLY LINKED LIST: Each node contains one data field and one link field pointing to the next node
- DOUBLY LINKED LIST: Each node contains data, a next pointer, and a previous pointer
- CIRCULAR LINKED LIST: Last node's pointer references the first node, creating a closed loop

## Important Formulas and Theorems

- Time Complexity for insertion at beginning: O(1)
- Time Complexity for insertion at end: O(n) for singly without tail pointer
- Time Complexity for searching: O(n)
- Time Complexity for deletion at beginning: O(1)
- Space Complexity per node: O(data_size + pointer_size)

## Key Points

- Linked lists provide dynamic memory allocation, allowing the list to grow and shrink during execution
- Unlike arrays, linked lists do not support random access—elements must be accessed sequentially
- Insertion and deletion in linked lists are O(1) operations when position is known, unlike O(n) for arrays
- Each node requires additional memory for storing pointers, increasing space overhead compared to arrays
- The head pointer must be maintained properly; losing it means losing access to the entire list
- NULL pointer indicates the end of a singly linked list
- Memory must be explicitly allocated (malloc) and freed (free) in languages like C

## Common Mistakes to Avoid

- Forgetting to update the head pointer when inserting or deleting the first node
- Not checking for NULL before dereferencing pointers, causing segmentation faults
- Creating memory leaks by not freeing nodes when deleting from linked lists
- Losing reference to subsequent nodes before reassigning pointers during insertion/deletion

## Revision Tips

- Practice tracing linked list operations on paper—draw nodes and pointer arrows explicitly
- Memorize time complexities for all basic operations on different list types
- Write and debug linked list code in C to gain hands-on experience with pointer manipulation
- Prepare comparison tables between arrays and linked lists for quick revision
- Review common linked list problems: reversing a list, detecting loops, finding middle element