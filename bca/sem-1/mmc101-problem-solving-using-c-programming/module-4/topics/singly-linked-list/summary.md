# Singly Linked List - Summary

## Key Definitions and Concepts

- **Node**: The fundamental building block of a linked list, consisting of data and a pointer to the next node.
- **Head Pointer**: A pointer variable that stores the address of the first node in the list; serves as the entry point.
- **Self-referential Structure**: A structure that contains a pointer to another structure of the same type.
- **NULL Pointer**: A sentinel value indicating the end of the list; the last node's next pointer is always NULL.
- **Dynamic Memory Allocation**: Memory allocated at runtime using malloc() from the heap memory.

## Important Formulas and Theorems

- **Node Structure**: `struct Node { int data; struct Node *next; };`
- **Time Complexity - Insertion at Beginning**: O(1)
- **Time Complexity - Insertion at End**: O(n)
- **Time Complexity - Deletion at Beginning**: O(1)
- **Time Complexity - Search**: O(n)
- **Space Complexity**: O(n) where n is the number of nodes (each node requires memory for data + pointer)

## Key Points

- Singly linked lists provide dynamic size, unlike arrays with fixed dimensions.
- Each node contains data and exactly one link (pointer to next node).
- Linked lists allow O(1) insertion and deletion at the beginning; arrays require O(n) for the same operations.
- No random access is possible—you must traverse from the head to reach any node.
- Memory is allocated one node at a time, and unused nodes should be freed to prevent memory leaks.
- The last node's next pointer must be NULL to mark the list end.
- Passing the head pointer to functions that modify the list requires passing its address (use struct Node**).

## Common Mistakes to Avoid

- Forgetting to check if malloc() returned NULL before using the allocated memory.
- Not updating the head pointer when inserting/deleting the first node (requires passing pointer-to-pointer).
- Losing the reference to the rest of the list by updating next pointers in the wrong order.
- Using a node after it has been freed (dangling pointer problem).
- Not setting the new node's next pointer to NULL when inserting at the end.

## Revision Tips

1. Practice writing the node structure definition and basic create/display functions until they become automatic.

2. Trace through insertion and deletion operations by drawing boxes and arrows on paper—this reinforces pointer manipulation concepts.

3. Memorize the standard linked list functions and their implementations; exams frequently ask to write these from memory.

4. Focus on understanding why certain operations work rather than just memorizing code; this helps in debugging and adapting to new problems.