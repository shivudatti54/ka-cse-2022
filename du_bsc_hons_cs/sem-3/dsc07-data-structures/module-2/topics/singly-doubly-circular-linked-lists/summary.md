# Singly, Doubly & Circular Linked Lists

## Introduction
Linked lists are fundamental **dynamic linear data structures** that store elements in nodes, with each node containing data and a pointer to the next node. Unlike arrays, they allow efficient insertion/deletion without memory wastage. As per Delhi University NEP 2024 syllabus, understanding linked lists is essential for practicals and theory examinations.

---

## Singly Linked List (SLL)

- **Structure**: Each node has two parts — *data* and *next* pointer
- **Traversal**: Unidirectional (only forward)
- **Memory**: Uses less memory than doubly linked list
- **Operations**:
  - Insertion at beginning, end, or position
  - Deletion from beginning, end, or position
  - Search/Traversal using temporary pointer
- **Limitations**: Cannot traverse backwards; accessing previous node requires traversal from start
- **Time Complexity**: O(n) for search, O(1) for insertion/deletion at head

---

## Doubly Linked List (DLL)

- **Structure**: Each node contains *data*, *next* pointer, and *prev* pointer
- **Traversal**: Bidirectional (both forward and backward)
- **Advantages**: Easy navigation in both directions; efficient for deletion of previous node
- **Operations**:
  - Insertion/Deletion at any position
  - Forward and backward traversal
- **Memory**: Consumes extra memory for previous pointer
- **Time Complexity**: O(n) for search, O(1) for insertion/deletion when node is given

---

## Circular Linked List

- **Last node points back to first node** (forms a circle)
- **Types**: 
  - **Circular Singly**: Single direction with last→first
  - **Circular Doubly**: Both directions; last's prev points to first, first's next points to last
- **Advantages**: 
  - Useful for round-robin scheduling
  - No NULL pointer issues
  - Continuous traversal possible
- **Applications**: Task scheduling, playlist management, circular buffers
- **Considerations**: Must handle base cases carefully (empty list, single node)

---

## Key Differences

| Feature | Singly | Doubly | Circular |
|---------|--------|--------|----------|
| Pointers | 1 (next) | 2 (prev, next) | 1 or 2 |
| Traversal | Forward only | Both directions | Continuous |
| Memory | Less | More | Similar to SLL/DLL |
| Complexity | Simple | Moderate | Slightly complex |

---

## Conclusion
Linked lists form the basis for advanced structures like stacks, queues, and graphs. Mastery of **singly, doubly, and circular linked lists** — their operations, advantages, and trade-offs — is crucial for the Delhi University B.Sc. (Hons) CS NEP 2024 examination and practical implementations.

*Revision Tip*: Practice coding all basic operations (insert, delete, display) for each type to score well in practical and theory sections.