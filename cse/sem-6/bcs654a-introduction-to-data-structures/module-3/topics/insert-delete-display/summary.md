# Insert, Delete, Display Operations

## Overview

The fundamental operations of insertion, deletion, and display form the core functionality of linked list manipulation. These operations demonstrate pointer manipulation techniques essential for managing dynamic data structures effectively.

## Key Points

- **Insert Operations**: Add nodes at beginning (O(1)), end (O(n)), or position (O(n))
- **Delete Operations**: Remove nodes from beginning (O(1)), end (O(n)), or by value (O(n))
- **Display Operation**: Traverse and print all nodes sequentially, O(n) time
- **Pointer Updates**: Insertion links new node, deletion bridges gap removing node
- **Memory Allocation**: malloc creates new nodes, free releases deleted nodes
- **Boundary Checks**: Validate operations for empty list and position limits
- **Head Management**: Most operations require updating or passing head pointer

## Important Concepts

- Insert at beginning: create node, point new->next to head, update head to new
- Delete from beginning: save head, update head to head->next, free old head
- Display: traverse from head to NULL, printing each node's data
- Insert at position requires finding previous node to link properly
- Delete by value requires searching and then bridging the gap
- All operations must handle edge cases like empty list and single node

## Notes

- Practice implementing all three operations with complete code
- Draw diagrams showing pointer changes step by step
- Remember pattern: allocate/find, link/bridge, update/free
- Always validate input and check for NULL before operations
- Know time complexities and be able to explain why
