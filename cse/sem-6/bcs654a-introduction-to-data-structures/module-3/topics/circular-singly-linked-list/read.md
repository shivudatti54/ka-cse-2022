# Circular Singly Linked List

## Introduction

A Circular Singly Linked List (CSLL) is a variation of the standard Singly Linked List where the last node points back to the first node instead of containing a NULL pointer. This circular connection forms a closed loop, enabling continuous traversal from any node in the list.

In a traditional Singly Linked List, traversal starts at the head and proceeds linearly until the NULL terminator is reached. In contrast, a Circular Linked List has no natural beginning or end, which requires careful management to avoid infinite loops during traversal.

### Key Characteristics:

- The `next` pointer of the last node points to the first node (head)
- Can be traversed starting from any node until returning to the starting point
- Requires special handling for operations like insertion and deletion
- Often maintains a pointer to the last node (tail) for efficient operations

## Structure and Representation

Each node in a Circular Singly Linked List contains two parts:

1. **Data**: The actual value stored in the node
2. **Next Pointer**: A pointer/reference to the next node in the sequence

The last node's next pointer points to the first node, creating the circular connection.

```c
// Node structure in C
struct Node {
 int data;
 struct Node* next;
};
```

### Visual Representation:

```
 +---+---+ +---+---+ +---+---+
 | 1 | •----->| 2 | •----->| 3 | •----+
 +---+---+ +---+---+ +---+---+ |
 ^ |
 | |
 +-----------------------------------+
```

In this diagram:

- Three nodes contain values 1, 2, and 3
- Each node's next pointer points to the subsequent node
- The last node (3) points back to the first node (1)
- The list forms a continuous loop

## Comparison with Other Linked Lists

| Feature                   | Singly Linked List       | Circular Singly Linked List | Doubly Linked List     |
| ------------------------- | ------------------------ | --------------------------- | ---------------------- |
| Direction                 | Forward only             | Forward only (circular)     | Bidirectional          |
| Last node points to       | NULL                     | First node                  | NULL                   |
| Memory overhead           | Low                      | Low                         | Higher (extra pointer) |
| Traversal                 | Linear from head to NULL | Continuous loop             | Both directions        |
| Implementation complexity | Moderate                 | Moderate                    | Higher                 |

## Operations on Circular Singly Linked List

### 1. Insertion Operations

#### a) Insertion at the Beginning

To insert a node at the beginning of a circular list:

1. Create a new node with the given data
2. If the list is empty, make the new node point to itself
3. If the list is not empty:

- Traverse to the last node (which points to the first node)
- Set the new node's next to the current first node
- Update the last node's next to point to the new node

4. Update the head pointer to point to the new node

```c
void insertAtBeginning(struct Node** head_ref, int data) {
 struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
 struct Node* temp = *head_ref;
 new_node->data = data;

 if (*head_ref == NULL) {
 new_node->next = new_node;
 *head_ref = new_node;
 return;
 }

 while (temp->next != *head_ref) {
 temp = temp->next;
 }

 temp->next = new_node;
 new_node->next = *head_ref;
 *head_ref = new_node;
}
```

#### b) Insertion at the End

To insert a node at the end of a circular list:

1. Create a new node with the given data
2. If the list is empty, make the new node point to itself and set as head
3. If the list is not empty:

- Traverse to the last node (which points to the first node)
- Set the last node's next to point to the new node
- Set the new node's next to point to the first node

```c
void insertAtEnd(struct Node** head_ref, int data) {
 struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
 struct Node* temp = *head_ref;
 new_node->data = data;

 if (*head_ref == NULL) {
 new_node->next = new_node;
 *head_ref = new_node;
 return;
 }

 while (temp->next != *head_ref) {
 temp = temp->next;
 }

 temp->next = new_node;
 new_node->next = *head_ref;
}
```

#### c) Insertion after a Specific Node

To insert a node after a given node:

1. Create a new node with the given data
2. Set the new node's next to point to the next node of the given node
3. Set the given node's next to point to the new node

```c
void insertAfter(struct Node* prev_node, int data) {
 if (prev_node == NULL) {
 printf("Previous node cannot be NULL");
 return;
 }

 struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
 new_node->data = data;
 new_node->next = prev_node->next;
 prev_node->next = new_node;
}
```

### 2. Deletion Operations

#### a) Deletion from the Beginning

To delete the first node:

1. If the list is empty, return
2. If the list has only one node, delete it and set head to NULL
3. Otherwise:

- Traverse to the last node (which points to the first node)
- Update the last node's next to point to the second node
- Delete the first node and update the head pointer

```c
void deleteFromBeginning(struct Node** head_ref) {
 if (*head_ref == NULL) return;

 if ((*head_ref)->next == *head_ref) {
 free(*head_ref);
 *head_ref = NULL;
 return;
 }

 struct Node* temp = *head_ref;
 struct Node* last = *head_ref;

 while (last->next != *head_ref) {
 last = last->next;
 }

 last->next = (*head_ref)->next;
 *head_ref = (*head_ref)->next;
 free(temp);
}
```

#### b) Deletion from the End

To delete the last node:

1. If the list is empty, return
2. If the list has only one node, delete it and set head to NULL
3. Otherwise:

- Traverse to the second last node
- Update the second last node's next to point to the first node
- Delete the last node

```c
void deleteFromEnd(struct Node** head_ref) {
 if (*head_ref == NULL) return;

 if ((*head_ref)->next == *head_ref) {
 free(*head_ref);
 *head_ref = NULL;
 return;
 }

 struct Node* temp = *head_ref;
 struct Node* prev = NULL;

 while (temp->next != *head_ref) {
 prev = temp;
 temp = temp->next;
 }

 prev->next = *head_ref;
 free(temp);
}
```

#### c) Deletion of a Specific Node

To delete a specific node by value:

1. If the list is empty, return
2. If the node to be deleted is the only node, delete it and set head to NULL
3. Otherwise:

- Traverse to find the node and keep track of the previous node
- Update the previous node's next to point to the next of the node to be deleted
- If the node to be deleted is the head, update the head pointer
- Delete the node

```c
void deleteNode(struct Node** head_ref, int key) {
 if (*head_ref == NULL) return;

 struct Node* temp = *head_ref;
 struct Node* prev = NULL;

 // If head is to be deleted
 if (temp->data == key) {
 if (temp->next == *head_ref) { // Only one node
 free(temp);
 *head_ref = NULL;
 return;
 }

 // Find last node to update its next pointer
 struct Node* last = *head_ref;
 while (last->next != *head_ref) {
 last = last->next;
 }

 last->next = (*head_ref)->next;
 *head_ref = (*head_ref)->next;
 free(temp);
 return;
 }

 // Traverse to find the node to delete
 do {
 prev = temp;
 temp = temp->next;
 } while (temp != *head_ref && temp->data != key);

 if (temp == *head_ref) {
 printf("Node with value %d not found\n", key);
 return;
 }

 prev->next = temp->next;
 free(temp);
}
```

### 3. Traversal and Display

To traverse a circular linked list:

1. Start from the head node
2. Visit each node until returning to the head node
3. Use a do-while loop to ensure at least one iteration

```c
void displayList(struct Node* head) {
 if (head == NULL) {
 printf("List is empty\n");
 return;
 }

 struct Node* temp = head;

 printf("Circular Linked List: ");
 do {
 printf("%d -> ", temp->data);
 temp = temp->next;
 } while (temp != head);
 printf("(back to head)\n");
}
```

## Applications of Circular Singly Linked Lists

1. **Round-robin Scheduling**: In operating systems, circular lists are used for scheduling processes where each process gets a time slice in rotation.

2. **Multiplayer Games**: In games where players take turns, a circular list can manage the player sequence.

3. **Buffer Management**: Circular buffers implemented using linked lists are used in I/O operations and network data transfer.

4. **Implementation of Advanced Data Structures**: Used as building blocks for more complex structures like circular queues.

5. **Navigation Systems**: Useful for representing circular routes or tours.

## Implementation Example: Circular Queue using Linked List

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node* next;
};

struct Queue {
 struct Node* rear;
};

void enqueue(struct Queue* q, int data) {
 struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
 new_node->data = data;

 if (q->rear == NULL) {
 q->rear = new_node;
 new_node->next = new_node;
 } else {
 new_node->next = q->rear->next;
 q->rear->next = new_node;
 q->rear = new_node;
 }
}

int dequeue(struct Queue* q) {
 if (q->rear == NULL) {
 printf("Queue is empty\n");
 return -1;
 }

 struct Node* front = q->rear->next;
 int data = front->data;

 if (front == q->rear) { // Only one element
 free(front);
 q->rear = NULL;
 } else {
 q->rear->next = front->next;
 free(front);
 }

 return data;
}

void displayQueue(struct Queue* q) {
 if (q->rear == NULL) {
 printf("Queue is empty\n");
 return;
 }

 struct Node* temp = q->rear->next;
 printf("Circular Queue: ");

 do {
 printf("%d ", temp->data);
 temp = temp->next;
 } while (temp != q->rear->next);

 printf("\n");
}
```

## Advantages and Disadvantages

### Advantages:

1. **Efficient Traversal**: Can traverse the entire list starting from any node
2. **Round-robin Applications**: Ideal for applications requiring circular processing
3. **No NULL pointers**: Eliminates NULL pointer checks in some operations
4. **Memory Efficiency**: Similar memory usage to singly linked lists

### Disadvantages:

1. **Complex Operations**: Insertion and deletion operations are more complex
2. **Infinite Loop Risk**: Improper implementation can lead to infinite loops
3. **More Error-Prone**: Requires careful handling of pointers
4. **No Direct Access**: Like all linked lists, no random access to elements

## Memory Management Considerations

When working with circular linked lists:

- Always check for memory allocation failures
- Ensure proper freeing of memory during deletion
- Be cautious of memory leaks in circular references
- Use debugging tools to detect memory issues

## Exam Tips

1. **Understand the Circular Nature**: Remember that the last node points to the first node, not NULL.

2. **Traversal Termination**: Use do-while loops instead of while loops for traversal to handle the circular connection properly.

3. **Edge Cases**: Always handle empty list and single-node list cases separately in your algorithms.

4. **Pointer Management**: Be extremely careful with pointer assignments to avoid breaking the circular chain.

5. **Memory Diagrams**: Practice drawing memory diagrams for various operations to visualize pointer changes.

6. **Time Complexity**: Remember that most operations have O(n) time complexity due to the need to traverse the list.

7. **Comparison Questions**: Be prepared to compare circular linked lists with other list types in terms of memory usage, operation complexity, and applications.
