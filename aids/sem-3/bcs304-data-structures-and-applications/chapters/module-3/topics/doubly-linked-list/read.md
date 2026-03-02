# Doubly Linked List

## Overview

A **Doubly Linked List** is a linked list where each node contains:

1. **Data** - The value stored
2. **Next** - Pointer to the next node
3. **Prev** - Pointer to the previous node

This allows **bidirectional traversal** (forward and backward).

```
NULL ← [10|↔] ⇆ [20|↔] ⇆ [30|↔] → NULL
        HEAD                    TAIL
```

## Node Structure

```c
struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};
```

## Visualization

```
          prev  data  next
           │     │     │
           ▼     ▼     ▼
NULL ← ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ → NULL
       │ ← │ 10 │ →   │ ⇆  │ ← │ 20 │ →   │ ⇆  │ ← │ 30 │ →   │
       └──────────────┘    └──────────────┘    └──────────────┘
              ↑                                        ↑
            HEAD                                     TAIL
```

## Advantages over Singly Linked List

| Feature                     | Singly       | Doubly               |
| --------------------------- | ------------ | -------------------- |
| Traversal                   | Forward only | Both directions      |
| Delete node (given pointer) | O(n)         | O(1)                 |
| Insert before node          | O(n)         | O(1)                 |
| Delete from end             | O(n)         | O(1)\*               |
| Memory per node             | Less         | More (extra pointer) |

\*With tail pointer

## Operations

### Create Node

```c
struct Node* createNode(int data) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}
```

### Insert at Beginning - O(1)

```c
void insertAtBeginning(struct Node **head, int data) {
    struct Node *newNode = createNode(data);

    if(*head == NULL) {
        *head = newNode;
        return;
    }

    newNode->next = *head;
    (*head)->prev = newNode;
    *head = newNode;
}
```

**Steps:**

1. Create new node
2. Point newNode->next to current head
3. Point head->prev to newNode
4. Update head to newNode

### Insert at End - O(1) with tail

```c
void insertAtEnd(struct Node **head, struct Node **tail, int data) {
    struct Node *newNode = createNode(data);

    if(*head == NULL) {
        *head = *tail = newNode;
        return;
    }

    newNode->prev = *tail;
    (*tail)->next = newNode;
    *tail = newNode;
}

// Without tail pointer: O(n)
void insertAtEndSlow(struct Node **head, int data) {
    struct Node *newNode = createNode(data);

    if(*head == NULL) {
        *head = newNode;
        return;
    }

    struct Node *temp = *head;
    while(temp->next != NULL) {
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->prev = temp;
}
```

### Insert at Position - O(n)

```c
void insertAtPosition(struct Node **head, int data, int position) {
    if(position == 0) {
        insertAtBeginning(head, data);
        return;
    }

    struct Node *newNode = createNode(data);
    struct Node *temp = *head;

    // Traverse to position - 1
    for(int i = 0; i < position - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if(temp == NULL) {
        printf("Position out of bounds\n");
        free(newNode);
        return;
    }

    newNode->next = temp->next;
    newNode->prev = temp;

    if(temp->next != NULL) {
        temp->next->prev = newNode;
    }
    temp->next = newNode;
}
```

### Delete from Beginning - O(1)

```c
void deleteFromBeginning(struct Node **head) {
    if(*head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = *head;
    *head = (*head)->next;

    if(*head != NULL) {
        (*head)->prev = NULL;
    }

    free(temp);
}
```

### Delete from End - O(1) with tail

```c
void deleteFromEnd(struct Node **head, struct Node **tail) {
    if(*tail == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = *tail;
    *tail = (*tail)->prev;

    if(*tail != NULL) {
        (*tail)->next = NULL;
    } else {
        *head = NULL;  // List became empty
    }

    free(temp);
}
```

### Delete by Value - O(n)

```c
void deleteByValue(struct Node **head, struct Node **tail, int value) {
    struct Node *temp = *head;

    // Find the node
    while(temp != NULL && temp->data != value) {
        temp = temp->next;
    }

    if(temp == NULL) {
        printf("Value not found\n");
        return;
    }

    // Update head if deleting first node
    if(temp == *head) {
        *head = temp->next;
    }

    // Update tail if deleting last node
    if(temp == *tail) {
        *tail = temp->prev;
    }

    // Update adjacent nodes' pointers
    if(temp->prev != NULL) {
        temp->prev->next = temp->next;
    }

    if(temp->next != NULL) {
        temp->next->prev = temp->prev;
    }

    free(temp);
}
```

### Delete Given Node - O(1)

```c
// Powerful operation - delete node in O(1) if you have pointer to it
void deleteNode(struct Node **head, struct Node **tail, struct Node *node) {
    if(node == NULL) return;

    // Update head
    if(node == *head) {
        *head = node->next;
    }

    // Update tail
    if(node == *tail) {
        *tail = node->prev;
    }

    // Update prev node's next
    if(node->prev != NULL) {
        node->prev->next = node->next;
    }

    // Update next node's prev
    if(node->next != NULL) {
        node->next->prev = node->prev;
    }

    free(node);
}
```

### Reverse Traversal - O(n)

```c
void printReverse(struct Node *tail) {
    struct Node *temp = tail;

    printf("Reverse: ");
    while(temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->prev;
    }
    printf("NULL\n");
}
```

### Reverse the List - O(n)

```c
void reverse(struct Node **head, struct Node **tail) {
    struct Node *current = *head;
    struct Node *temp = NULL;

    // Swap prev and next for all nodes
    while(current != NULL) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;  // Move to next (which is now prev)
    }

    // Swap head and tail
    temp = *head;
    *head = *tail;
    *tail = temp;
}
```

## Time Complexity Summary

| Operation             | Singly   | Doubly | Notes                        |
| --------------------- | -------- | ------ | ---------------------------- |
| Insert at beginning   | O(1)     | O(1)   |                              |
| Insert at end         | O(n)     | O(1)\* | \*With tail                  |
| Insert after node     | O(1)     | O(1)   | If node pointer given        |
| Insert before node    | O(n)     | O(1)   | Advantage of doubly          |
| Delete from beginning | O(1)     | O(1)   |                              |
| Delete from end       | O(n)     | O(1)\* | \*With tail                  |
| Delete given node     | O(n)     | O(1)   | Major advantage              |
| Reverse traversal     | O(n)\*\* | O(n)   | \*\*Requires stack in singly |
| Search                | O(n)     | O(n)   |                              |

## Space Complexity

- **Per node:** O(1) - but 50% more memory than singly (extra pointer)
- **Total list:** O(n)

## When to Use Doubly Linked List

**Use when:**

- Need bidirectional traversal
- Frequent deletions when you have pointer to node
- Implementing LRU cache
- Navigation features (forward/back)
- Undo/Redo functionality

**Avoid when:**

- Memory is constrained
- Only forward traversal needed
- Simple stack/queue implementation

## Applications

1. **Browser History** - Back and forward navigation
2. **Music Player** - Previous and next track
3. **LRU Cache** - Efficient removal with hash map
4. **Text Editors** - Undo/redo operations
5. **Memory Allocators** - Free list management
