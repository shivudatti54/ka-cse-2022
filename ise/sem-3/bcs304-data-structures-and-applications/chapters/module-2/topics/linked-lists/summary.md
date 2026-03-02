# LINKED LISTS - Summary

## Key Definitions and Concepts

- LINKED LIST: A linear data structure where elements (nodes) are stored in non-contiguous memory locations, connected through pointers. Each node contains a data field and a link field pointing to the next node.

- NODE: The fundamental unit of a linked list, consisting of at least two components: the data (stored information) and the next pointer (address of subsequent node).

- HEAD: The first node in a linked list; the entry point for all operations. If head is NULL, the list is empty.

- CHAIN: A sequence of nodes linked through their next pointers, forming the logical sequence of elements in a linked list.

- SELF-REFERENTIAL STRUCTURE: A structure that contains a pointer to another structure of the same type, enabling node creation.

## Important Formulas and Theorems

- Node structure: `struct Node { data_type data; struct Node* next; };`

- Time complexity for insertion at HEAD: O(1)
- Time complexity for insertion at TAIL: O(n)
- Time complexity for deletion at HEAD: O(1)
- Time complexity for deletion at TAIL: O(n)
- Time complexity for SEARCH: O(n)
- Space complexity per node: O(1) additional for the pointer

## Key Points

1. LINKED LISTS PROVIDE DYNAMIC SIZE - unlike arrays, linked lists can grow and shrink during execution without requiring reallocation.

2. MEMORY IS ALLOCATED FROM THE HEAP - using malloc() for node creation and free() for deletion to prevent memory leaks.

3. NO RANDOM ACCESS - linked lists do not support direct indexing; traversal from head is required to reach any node.

4. SINGLY LINKED LISTS use one pointer per node (next), enabling only forward traversal.

5. DOUBLY LINKED LISTS use two pointers (prev and next), enabling bidirectional traversal at the cost of extra memory.

6. CIRCULAR LINKED LISTS connect the last node back to the first, useful for round-robin scheduling and cyclic processes.

7. LINKED STACKS use insertion/deletion only at HEAD (top), achieving O(1) operations.

8. LINKED QUEUES require both FRONT and REAR pointers for efficient O(1) enqueue and dequeue operations.

## Common Mistakes to Avoid

1. NOT CHECKING FOR NULL: Always verify that pointers are not NULL before dereferencing them; failure causes segmentation faults.

2. FORGETTING TO FREE MEMORY: Not using free() after deletion creates memory leaks that accumulate over time.

3. LOSING THE HEAD POINTER: When inserting at the beginning, ensure the modified head pointer is returned and saved by the calling function.

4. POINTER OVERWRITING BEFORE SAVING: When deleting a node, save its next pointer BEFORE freeing the node, otherwise you lose access to the remainder of the list.

5. MEMORY ALLOCATION FAILURE: Always check if malloc() returns NULL (allocation failure) in production code.

## Revision Tips

1. PRACTICE CODE BY HAND: Write linked list operations multiple times until you can implement them without参考.

2. DRAW DIAGRAMS: Visual representation of nodes and pointers helps understand complex operations and edge cases.

3. MEMORIZE COMPLEXITIES: Create a table of all operations and their time complexities for quick revision.

4. TRACE EXISTING CODE: Practice reading and tracing C code with linked list operations to identify outputs and potential bugs.

5. UNDERSTAND VS MEMORIZE: Focus on WHY operations work rather than memorizing code; examiners test understanding through new problems.