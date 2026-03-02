# Lists and Chains - Summary

## Key Definitions and Concepts

- **Linked List (Chain):** A linear data structure where elements (nodes) are stored in nodes, each containing data and a pointer to the next node
- **Node:** A structure containing data field and pointer field(s); the basic building block of a linked list
- **Head Pointer:** Points to the first node in the list; NULL indicates an empty list
- **Singly Linked List:** Each node has data and pointer to next node only
- **Doubly Linked List:** Each node has data, pointer to next, and pointer to previous node
- **Circular Linked List:** Last node's next pointer points back to the head, forming a circle

## Important Formulas and Theorems

- **Node Structure (Singly):** `struct Node { int data; struct Node* next; };`
- **Node Structure (Doubly):** `struct Node { int data; struct Node* next; struct Node* prev; };`
- **Insertion at beginning:** O(1) time complexity
- **Insertion at end:** O(n) time complexity  
- **Deletion:** O(n) worst case, O(1) for deletion at beginning
- **Search:** O(n) time complexity
- **Space per node:** For singly: data + 1 pointer; For doubly: data + 2 pointers

## Key Points

- Linked lists provide dynamic memory allocation unlike fixed-size arrays
- No memory wastage as nodes are allocated only when needed
- Efficient insertions and deletions without shifting elements
- Random access is slower (O(n)) compared to arrays (O(1))
- Must free memory after deletion to prevent memory leaks
- Always check for NULL pointer before accessing node fields
- The last node's next pointer is NULL (for non-circular lists)
- Head pointer must be passed by reference (pointer to pointer) when modifying the list

## Common Mistakes to Avoid

- Forgetting to update head pointer when inserting/deleting at the beginning
- Not handling the NULL case for empty list operations
- Memory leaks by not using free() after deletion
- Segmentation faults from dereferencing NULL pointers
- Creating infinite loops in circular lists without proper termination condition

## Revision Tips

- Practice drawing node diagrams for each operation (insert/delete)
- Memorize the standard linked list code patterns in C
- Focus on pointer manipulation and tracing exercises
- Review time complexities for all operations
- Solve previous year DU question papers on linked lists