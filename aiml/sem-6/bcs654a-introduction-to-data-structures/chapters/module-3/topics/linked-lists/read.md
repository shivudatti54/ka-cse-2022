# Introduction to Linked Lists

## What is a Linked List?

A **linked list** is a linear data structure where elements are stored in **nodes**, and each node contains:
1. **Data** - The actual value stored
2. **Pointer(s)** - Reference to the next (and/or previous) node

Unlike arrays, linked list elements are **not stored contiguously** in memory.

```
Array:        [10][20][30][40][50]
              Contiguous memory locations

Linked List:  [10|→] → [20|→] → [30|→] → [40|→] → [50|NULL]
              Scattered in memory, connected by pointers
```

## Node Structure

```c
// Basic node for singly linked list
struct Node {
    int data;           // Data part
    struct Node *next;  // Pointer to next node
};
```

## Visualization

```
HEAD
  ↓
┌────┬────┐   ┌────┬────┐   ┌────┬────┐
│ 10 │ ──→│──→│ 20 │ ──→│──→│ 30 │NULL│
└────┴────┘   └────┴────┘   └────┴────┘
 data  next    data  next    data  next
```

## Types of Linked Lists

| Type | Description | Pointers per Node |
|------|-------------|-------------------|
| **Singly** | Each node points to next | 1 (next) |
| **Doubly** | Each node points to next and previous | 2 (next, prev) |
| **Circular** | Last node points back to first | 1 or 2 |
| **Circular Doubly** | Doubly linked + circular | 2 (next, prev) |

## Arrays vs Linked Lists

| Aspect | Array | Linked List |
|--------|-------|-------------|
| **Memory** | Contiguous | Non-contiguous |
| **Size** | Fixed (static) | Dynamic |
| **Access** | O(1) random access | O(n) sequential |
| **Insert/Delete** | O(n) - shifting | O(1) - with pointer |
| **Memory overhead** | None | Pointer per node |
| **Cache performance** | Excellent | Poor |

## Key Operations

| Operation | Time Complexity |
|-----------|-----------------|
| Access by index | O(n) |
| Search | O(n) |
| Insert at beginning | O(1) |
| Insert at end | O(n) or O(1)* |
| Insert at position | O(n) |
| Delete from beginning | O(1) |
| Delete from end | O(n) or O(1)* |
| Delete from position | O(n) |

*O(1) if tail pointer is maintained

## Basic Implementation

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node *next;
};

// Create a new node
struct Node* createNode(int data) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Print the list
void printList(struct Node *head) {
    struct Node *current = head;
    while(current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    // Create nodes
    struct Node *head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
    
    // Print: 10 -> 20 -> 30 -> NULL
    printList(head);
    
    return 0;
}
```

## Memory Allocation

Each node is allocated separately on the **heap**:

```
Stack:               Heap:
┌──────┐            ┌────────────┐
│ head │────────────→│ 10 │ next │──┐
└──────┘            └────────────┘  │
                           ↓        │
                    ┌────────────┐←─┘
                    │ 20 │ next │──┐
                    └────────────┘  │
                           ↓        │
                    ┌────────────┐←─┘
                    │ 30 │ NULL │
                    └────────────┘
```

## Advantages of Linked Lists

1. **Dynamic Size** - Can grow/shrink at runtime
2. **Efficient Insertions/Deletions** - O(1) with pointer (no shifting)
3. **No Memory Wastage** - Allocate exactly what's needed
4. **Easy Implementation of Stacks/Queues** - Natural fit

## Disadvantages of Linked Lists

1. **No Random Access** - Must traverse from head
2. **Extra Memory** - Pointer overhead per node
3. **Poor Cache Performance** - Non-contiguous memory
4. **Reverse Traversal** - Difficult in singly linked list

## When to Use Linked Lists

**Use when:**
- Frequent insertions/deletions
- Size is unknown or varies greatly
- Random access is not needed
- Implementing stacks, queues, graphs

**Avoid when:**
- Frequent random access needed
- Memory is constrained (pointer overhead)
- Cache performance is critical
- Simple sequential storage suffices

## Real-World Applications

1. **Music Players** - Playlist (next/previous songs)
2. **Web Browsers** - Back/Forward navigation
3. **Image Viewers** - Previous/Next image
4. **Undo Functionality** - In text editors
5. **Memory Management** - Free list in OS
6. **Hash Tables** - Chaining for collision resolution

## Key Points

1. Linked lists trade random access for efficient insertions
2. Always keep track of the head pointer
3. NULL indicates end of list
4. Memory must be freed manually (in C/C++)
5. Linked lists are building blocks for more complex structures
