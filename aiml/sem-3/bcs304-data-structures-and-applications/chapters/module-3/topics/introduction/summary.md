# Introduction to Data Structures - Summary

## Key Definitions and Concepts

- DATA STRUCTURE: A way of organizing and storing data that enables efficient access and modification
- ABSTRACT DATA TYPE (ADT): A mathematical model defining data structure behavior through operations without specifying implementation details
- LINEAR DATA STRUCTURE: Elements arranged sequentially where each element connects to previous and next (arrays, linked lists, stacks, queues)
- NON-LINEAR DATA STRUCTURE: Elements arranged non-sequentially with hierarchical or network relationships (trees, graphs)
- LINKED LIST: A linear data structure with nodes containing data and pointers to next node; memory need not be contiguous

## Important Formulas and Theorems

- Time Complexity of array access by index: O(1)
- Time Complexity of linked list traversal: O(n)
- Time Complexity of insertion at beginning: Array O(n), Linked List O(1)
- Time Complexity of deletion at beginning: Array O(n), Linked List O(1)
- Space overhead for linked list: Extra memory required for storing pointers/references

## Key Points

- Data structures are fundamental to efficient algorithm design and software development
- ADTs separate interface (what operations) from implementation (how operations work)
- Arrays provide fast random access O(1) but inefficient insertions/deletions due to shifting
- Linked lists provide efficient insertions/deletions O(1) but slow random access O(n)
- Linked lists use dynamic memory allocation and do not require contiguous memory
- The choice between data structures depends on the frequency and type of operations required
- Static data structures have fixed size; dynamic data structures can grow/shrink during execution

## Common Mistakes to Avoid

- Confusing the abstract data type with its concrete implementation - a List ADT can be implemented as array or linked list
- Assuming linked lists are always better than arrays - they have trade-offs and specific use cases
- Forgetting that linked list nodes require extra memory for pointers, making them less memory-efficient for small data
- Overlooking the O(n) time complexity for searching in both arrays and unsorted linked lists

## Revision Tips

- Practice writing both array-based and linked list implementations of basic operations
- Create comparison tables for time/space complexity of different data structures
- Draw diagrams to visualize how nodes are connected in linked lists
- Solve previous year DU examination questions on data structure fundamentals
- Remember that the "best" data structure depends entirely on the specific problem requirements