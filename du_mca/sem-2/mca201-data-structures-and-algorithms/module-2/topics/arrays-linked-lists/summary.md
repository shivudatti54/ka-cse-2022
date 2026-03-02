# Arrays and Linked Lists - Summary

## Key Definitions and Concepts

- **Array**: A contiguous memory data structure storing elements of the same type, accessible via indices.
- **Linked List**: A linear data structure with nodes containing data and pointers to the next (and optionally previous) node.
- **Singly Linked List**: Each node has data and a pointer to the next node.
- **Doubly Linked List**: Each node has data, next pointer, and previous pointer.
- **Circular Linked List**: Last node points back to the first node, forming a cycle.
- **Dynamic Array**: An array that can resize during runtime when capacity is exceeded.
- **Floyd's Cycle Detection**: An algorithm using two pointers at different speeds to detect loops.

## Important Formulas and Theorems

- **Array Element Address**: `Address(arr[i]) = Base_Address + i × element_size`
- **2D Array Address (Row-Major)**: `Address(a[i][j]) = BA + (i×n + j) × element_size`
- **Amortized Insertion Cost**: O(1) for dynamic arrays despite occasional O(n) resize
- **Floyd's Algorithm**: If cycle exists, fast and slow pointers will meet within O(n) iterations

## Key Points

- Arrays provide O(1) random access but O(n) insertions/deletions; linked lists provide O(1) insertions/deletions at ends but O(n) access.
- Linked lists use more memory due to pointer overhead but eliminate fragmentation.
- Arrays have better cache locality due to contiguous memory; linked lists have poor cache performance.
- Doubly linked lists allow bidirectional traversal but use double the pointer memory.
- Dynamic arrays use geometric progression (typically 2×) for resizing to achieve amortized O(1) insertion.
- Reversing a linked list can be done iteratively (O(n), O(1) space) or recursively (O(n), O(n) space).
- The choice between arrays and linked lists depends on the dominant operations in your application.

## Common Mistakes to Avoid

1. **Forgetting NULL checks**: Not checking for NULL before accessing node->next can cause segmentation faults.
2. **Memory leaks**: In C/C++, failing to free deleted nodes or properly managing malloc/free.
3. **Off-by-one errors**: Confusing 0-based vs 1-based indexing, particularly in array bounds.
4. **Pointer referencing**: Confusing between pointer value (address) and dereferenced value (data).
5. **Infinite loops**: Not properly updating pointers in traversal, especially in cycle detection scenarios.

## Revision Tips

1. Practice writing linked list operations (insert, delete, reverse) from memory repeatedly.
2. Trace through code examples with actual values to understand pointer manipulations.
3. Create comparison tables for time/space complexities of all operations.
4. Solve previous year DU examination questions on this topic.
5. Implement both array and linked list versions of the same problem to understand trade-offs.