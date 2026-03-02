# LINKED LISTS

## Introduction

Linked Lists represent one of the most fundamental and versatile data structures in computer science, forming the backbone of dynamic memory management and hierarchical data organization. Unlike static arrays that allocate contiguous memory blocks, linked lists provide a flexible mechanism for storing collections of elements where the size can grow or shrink during program execution. This dynamic nature makes linked lists particularly valuable in scenarios where the number of elements is unknown in advance or frequently changes.

In the context of the University of Delhi's Computer Science curriculum, linked lists serve as a prerequisite understanding for more complex data structures like stacks, queues, trees, and graphs. The concept of node allocation and deallocation introduces students to critical memory management concepts that are essential for efficient program design. Furthermore, linked lists exemplify the principle of indirect addressing—a fundamental concept in computer science where data elements are connected through pointers rather than physical contiguity. Understanding linked lists develops analytical skills essential for algorithm design and helps students appreciate the trade-offs between different data structure implementations in terms of time complexity, space efficiency, and operational flexibility.

## Key Concepts

### Definition and Structure

A linked list is a linear data structure where elements, called nodes, are stored in memory with each node containing two components: the actual data and a pointer (or reference) to the next node in the sequence. This pointer-based organization eliminates the need for contiguous memory allocation and allows for efficient insertions and deletions without reorganizing the entire structure.

The basic building block of a linked list is the NODE, which typically consists of two fields:

- DATA FIELD: Stores the actual information or value
- LINK (or NEXT) FIELD: Contains the memory address of the next node

The entire linked list is accessed through a external pointer called HEAD, which points to the first node in the list. If the HEAD pointer is NULL, the list is empty. The last node in the list has its link field set to NULL, indicating the end of the chain.

### Types of Linked Lists

SINGLY LINKED LIST represents the simplest form where each node contains data and a single pointer to the next node. Navigation is strictly forward—from the head to the tail. This structure is memory-efficient but limits reverse traversal.

DOUBLY LINKED LIST enhances the singly linked list by adding a previous pointer to each node, enabling bidirectional traversal. While requiring more memory per node (two pointers instead of one), operations like backward traversal and deletion become more efficient.

CIRCULAR LINKED LIST modifies the linear structure by connecting the last node back to the first, creating a closed loop. This variant is useful in applications requiring cyclic behavior, such as round-robin scheduling.

### Basic Operations

INSERTION operations in linked lists include three primary scenarios: inserting at the beginning (O(1) time), inserting at the end (O(n) time for singly, O(1) with tail pointer), and inserting at a specific position (O(n) time to locate position). Unlike arrays, insertion does not require shifting elements—it simply involves adjusting pointer references.

DELETION operations similarly include removing from the beginning (O(1)), removing from the end (O(n) for singly without tail), and removing from a specific position. The key advantage over arrays is that deletion also avoids element shifting, with only pointer adjustment required.

TRAVERSAL involves visiting each node sequentially to process or display its contents. This requires O(n) time complexity as each node must be accessed exactly once.

SEARCHING in a linked list requires sequential traversal until the target is found or the list ends, resulting in O(n) worst-case time complexity. Unlike binary search on sorted arrays, linked lists cannot support efficient random access.

### Memory Representation

When implementing linked lists in languages like C, nodes are typically created dynamically using memory allocation functions. Each node is allocated from the heap (dynamic memory), and the pointers store memory addresses. The allocation can be visualized as nodes scattered across memory locations, connected through their link fields. This non-contiguous storage is both an advantage (flexible size) and a disadvantage (no cache locality, higher memory overhead per node).

## Examples

### Example 1: Creating a Singly Linked List

Consider creating a linked list to store the numbers 10, 20, and 30.

Step 1: Create first node with data 10, link = NULL
```
Node 1: [10 | NULL]
head -> Node 1
```

Step 2: Create second node with data 20, link = NULL
```
Node 1: [10 | address_of_Node2] -> Node 2: [20 | NULL]
head -> Node 1 -> Node 2
```

Step 3: Create third node with data 30, link = NULL
```
Node 1: [10 | address_of_Node2] -> Node 2: [20 | address_of_Node3] -> Node 3: [30 | NULL]
```

### Example 2: Inserting a Node at the Beginning

Given an existing list: 20 -> 30 -> NULL, insert 10 at the beginning.

Initial State:
```
head -> [20 | *] -> [30 | NULL]
```

Step-by-step:
1. Allocate new node: newNode = malloc(sizeof(Node))
2. Set newNode->data = 10
3. Set newNode->link = head (points to node containing 20)
4. Update head = newNode

Final State:
```
head -> [10 | *] -> [20 | *] -> [30 | NULL]
```

### Example 3: Deleting a Node from Middle

Given list: 10 -> 20 -> 30 -> NULL, delete node containing 20.

Initial State:
```
head -> [10 | *p2] -> [20 | *p3] -> [30 | NULL]
           p2             p3
```

Step-by-step:
1. Locate node to delete (20) and its predecessor (10)
2. Set predecessor's link to point to the node after the one being deleted: p2->link = p3
3. Free the memory of node containing 20

Final State:
```
head -> [10 | *p3] -> [30 | NULL]
```

## Exam Tips

For DU semester examinations, several key points require focused preparation. UNDERSTAND POINTER MANIPULATION thoroughly—questions frequently test your understanding of how pointer assignments affect the linked list structure. Always draw diagrams to visualize pointer changes during operations.

TIME COMPLEXITY ANALYSIS carries significant weight. Remember: insertion at beginning is O(1), searching is O(n), and traversal is O(n). Be prepared to justify these complexities in examination answers.

MEMORY ALLOCATION AND DEALLOCATION is another critical area. Understand the difference between stack and heap allocation, and ensure you free dynamically allocated memory to prevent memory leaks. The examiner may ask about malloc() and free() functions.

POINTER ARITHMETIC IN LINKED LISTS differs from array pointer arithmetic. In arrays, pointers increment by element size; in linked lists, you follow the next pointer rather than performing arithmetic operations.

EDGE CASES demand attention: empty list, single node, insertion at beginning/end, deletion from empty list, and deletion of first/last node. Your code must handle these scenarios correctly.

TRACE ALGORITHMS by hand—examination questions often require you to trace through linked list operations showing the state of the list after each step. Practice this extensively.

WHEN COMPARING WITH ARRAYS, remember the trade-offs: arrays provide O(1) random access but O(n) insertion/deletion; linked lists provide O(1) insertion/deletion at known positions but no random access. This comparison is a common examination question.

FOR CODING QUESTIONS, always initialize pointers properly and check for NULL before dereferencing. Common errors include dangling pointers, memory leaks, and segmentation faults from invalid pointer access.