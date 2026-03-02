# Singly Linked Lists and Chains - Summary

## Key Definitions

- **Singly Linked List (Chain)**: A linear data structure consisting of nodes where each node contains a data element and a pointer to the next node; the last node points to NULL.

- **Head Pointer**: A pointer variable that stores the address of the first node in the linked list.

- **Node**: A structure containing a data field and a link (pointer) field.

- **Linked Queue**: A queue implementation using a singly linked list with front and rear pointers for efficient enqueue/dequeue operations.

## Important Formulas

| Operation             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Insert at Beginning   | O(1)            | O(1)             |
| Insert at End         | O(n)            | O(1)             |
| Delete from Beginning | O(1)            | O(1)             |
| Delete from End       | O(n)            | O(1)             |
| Delete by Value       | O(n)            | O(1)             |
| Search                | O(n)            | O(1)             |
| Traversal             | O(n)            | O(1)             |
| Reverse               | O(n)            | O(1)             |
| Merge Sorted Lists    | O(m + n)        | O(1)             |

## Key Points

1. **Dynamic Size**: Unlike arrays, linked lists grow and shrink dynamically without memory reallocation.

2. **No Random Access**: Linked lists do not support index-based access; traversal from head is required.

3. **Memory Overhead**: Each node requires extra memory for the pointer field (typically 4-8 bytes on modern systems).

4. **Queue Implementation**: Singly linked lists provide optimal O(1) time for queue operations when using front and rear pointers.

5. **Pointer Safety**: Always check for NULL before dereferencing pointers; handle empty list as a special case.

6. **Memory Management**: Every malloc() should have a corresponding free(); failure leads to memory leaks.

7. **Reversal Algorithm**: The iterative reversal uses three pointers (prev, current, next) and runs in O(n) time with O(1) space.

## Common Mistakes

1. **Forgetting NULL Check**: Attempting to access or delete from an empty list (head == NULL) without handling this edge case causes segmentation faults.

2. **Memory Leaks**: When deleting a node, failing to save the next pointer before calling free() loses the reference to the rest of the list.

3. **Lost Head Reference**: Not updating the head pointer after insertions at the beginning causes the list to become unreachable.

4. **Dangling Pointers**: Using a pointer variable after the node it points to has been freed.

5. **Off-by-One Errors**: When inserting at position k, traversing to node k-1 (not k) to maintain correct links; many students incorrectly position the new node.
