# Introduction to Linked Lists

## What is a Linked List?

A **Linked List** is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations.

## Why Linked Lists?

### Limitations of Arrays

1. **Fixed Size**: Arrays have fixed size, difficult to extend
2. **Memory Waste**: Unused allocated memory is wasted
3. **Insertion/Deletion Cost**: O(n) time for insertion/deletion in middle
4. **Contiguous Memory**: Requires large contiguous memory block

### Advantages of Linked Lists

1. **Dynamic Size**: Can grow or shrink during runtime
2. **Efficient Insertion/Deletion**: O(1) if position is known
3. **No Memory Waste**: Only allocate what's needed
4. **No Contiguous Memory**: Can use scattered memory locations

## Node Structure

Each node in a linked list contains:

1. **Data**: The actual value stored
2. **Pointer/Link**: Reference to the next node

```c
struct Node {
 int data; // Data part
 struct Node* next; // Pointer to next node
};
```

## Types of Linked Lists

### 1. Singly Linked List

- Each node points to the next node
- Last node points to NULL
- Traversal only in forward direction

### 2. Doubly Linked List

- Each node has two pointers: next and previous
- Can traverse in both directions
- Requires more memory

### 3. Circular Linked List

- Last node points back to first node
- No NULL at the end
- Can start from any node

### 4. Circular Doubly Linked List

- Combination of doubly and circular
- Both forward and backward links form circles

## Basic Concepts

### Head Pointer

- Points to the first node of the list
- Entry point for accessing the list
- If head is NULL, list is empty

### Traversal

Process of visiting each node once:

```
Start from head → Follow next pointers → Stop at NULL
```

### Memory Allocation

- Nodes created dynamically using malloc()
- Each node can be anywhere in memory
- Linked together using pointers

## Comparison with Arrays

| Feature      | Array           | Linked List                          |
| ------------ | --------------- | ------------------------------------ |
| Size         | Fixed           | Dynamic                              |
| Memory       | Contiguous      | Non-contiguous                       |
| Access       | O(1) - Random   | O(n) - Sequential                    |
| Insertion    | O(n)            | O(1) at known position               |
| Deletion     | O(n)            | O(1) at known position               |
| Memory Usage | Can waste space | Efficient, but overhead for pointers |

## Applications

1. **Dynamic Memory Allocation**: Free lists in memory managers
2. **Implementation of Stacks and Queues**: Dynamic versions
3. **Polynomial Representation**: Each term as a node
4. **Music/Video Playlists**: Navigate songs
5. **Undo Functionality**: Previous states
6. **Hash Tables**: Chaining for collision handling
7. **Graphs**: Adjacency list representation

## Advantages and Disadvantages

### Advantages

- Dynamic size
- Ease of insertion/deletion
- No memory waste
- Implementation of other data structures

### Disadvantages

- No random access
- Extra memory for pointers
- Not cache friendly
- Traversal is slower than arrays

## Exam Tips

1. Understand node structure thoroughly
2. Know all types of linked lists
3. Understand pointer manipulation
4. Practice drawing linked list diagrams
5. Remember time complexities
6. Know applications and when to use linked lists
7. Understand differences from arrays
