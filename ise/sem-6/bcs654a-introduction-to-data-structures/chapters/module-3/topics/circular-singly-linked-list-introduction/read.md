# Introduction to Linked Lists

## What is a Linked List?

A **linked list** is a linear data structure where elements are stored in a non-contiguous manner, unlike arrays. Each element, called a **node**, contains two parts:

1. **Data** - The actual value or information
2. **Pointer/Reference** - A link to the next node in the sequence

The first node is called the **head**, and the last node (which points to NULL/nothing) is called the **tail**.

```
[Data | Next] → [Data | Next] → [Data | Next] → NULL
   ↑ Head                                  ↑ Tail
```

## Why Linked Lists Over Arrays?

| Aspect             | Arrays                          | Linked Lists                     |
| ------------------ | ------------------------------- | -------------------------------- |
| Memory Allocation  | Static (compile-time)           | Dynamic (run-time)               |
| Memory Efficiency  | May have unused allocated space | Efficient - allocates as needed  |
| Insertion/Deletion | Expensive (shifting required)   | Efficient (pointer manipulation) |
| Access             | Random access (O(1))            | Sequential access (O(n))         |
| Memory Usage       | Contiguous block                | Non-contiguous (scattered)       |

**When to use linked lists:**

- When the number of elements is unknown
- When frequent insertions/deletions are required
- When memory efficiency is crucial

## Self-Referential Structures

In C, linked lists are implemented using self-referential structures - structures that contain pointers to instances of themselves.

```c
struct Node {
    int data;           // Data part
    struct Node* next;  // Pointer to next node
};
```

This structure contains:

- `data`: stores the actual value
- `next`: a pointer to another structure of the same type

## Types of Linked Lists

1. **Singly Linked List**: Each node points only to the next node
2. **Doubly Linked List**: Each node points to both next and previous nodes
3. **Circular Linked List**: The last node points back to the first node

## Basic Operations on Singly Linked Lists

### 1. Node Creation

```c
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

### 2. Insertion Operations

#### Insert at Beginning

```c
void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
```

Visualization:

```
Before: [Head] → [A | Next] → [B | Next] → NULL

Step 1: Create new node [C | Next]
Step 2: newNode->next = current head → [C | Next] → [A | Next] → [B | Next] → NULL
Step 3: Update head to point to newNode → Head → [C | Next] → [A | Next] → [B | Next] → NULL
```

#### Insert at End

```c
void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    struct Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

#### Insert after a Specific Node

```c
void insertAfterNode(struct Node* prevNode, int data) {
    if (prevNode == NULL) {
        printf("Previous node cannot be NULL");
        return;
    }

    struct Node* newNode = createNode(data);
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}
```

### 3. Deletion Operations

#### Delete from Beginning

```c
void deleteFromBeginning(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* temp = *head;
    *head = (*head)->next;
    free(temp);
}
```

#### Delete from End

```c
void deleteFromEnd(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }

    if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }

    struct Node* temp = *head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    free(temp->next);
    temp->next = NULL;
}
```

#### Delete a Specific Node

```c
void deleteNode(struct Node** head, int key) {
    struct Node* temp = *head;
    struct Node* prev = NULL;

    // If head node itself holds the key
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }

    // Search for the key to be deleted
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If key was not present in list
    if (temp == NULL) return;

    // Unlink the node from linked list
    prev->next = temp->next;
    free(temp);
}
```

### 4. Display/Traversal

```c
void displayList(struct Node* head) {
    struct Node* temp = head;
    printf("Linked List: ");
    while (temp != NULL) {
        printf("%d → ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

## Implementation of Stack using Linked List

```c
// Stack structure
struct Stack {
    struct Node* top;
};

// Push operation
void push(struct Stack* stack, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = stack->top;
    stack->top = newNode;
}

// Pop operation
int pop(struct Stack* stack) {
    if (stack->top == NULL) {
        printf("Stack Underflow\n");
        return -1;
    }

    struct Node* temp = stack->top;
    int popped = temp->data;
    stack->top = stack->top->next;
    free(temp);
    return popped;
}
```

## Implementation of Queue using Linked List

```c
// Queue structure
struct Queue {
    struct Node *front, *rear;
};

// Enqueue operation
void enqueue(struct Queue* queue, int data) {
    struct Node* newNode = createNode(data);

    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
        return;
    }

    queue->rear->next = newNode;
    queue->rear = newNode;
}

// Dequeue operation
int dequeue(struct Queue* queue) {
    if (queue->front == NULL) {
        printf("Queue Underflow\n");
        return -1;
    }

    struct Node* temp = queue->front;
    int dequeued = temp->data;
    queue->front = queue->front->next;

    if (queue->front == NULL) {
        queue->rear = NULL;
    }

    free(temp);
    return dequeued;
}
```

## Concatenating Two Lists

```c
void concatenateLists(struct Node** list1, struct Node* list2) {
    if (*list1 == NULL) {
        *list1 = list2;
        return;
    }

    struct Node* temp = *list1;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = list2;
}
```

## Reversing a List Without Creating New Nodes

```c
void reverseList(struct Node** head) {
    struct Node* prev = NULL;
    struct Node* current = *head;
    struct Node* next = NULL;

    while (current != NULL) {
        next = current->next;  // Store next node
        current->next = prev;  // Reverse current node's pointer
        prev = current;        // Move pointers one position ahead
        current = next;
    }
    *head = prev;
}
```

Visualization of reversal process:

```
Original: [1 | ] → [2 | ] → [3 | ] → NULL

Step 1: prev=NULL, current=[1], next=[2]
        [1 | ] → NULL (prev becomes [1])

Step 2: prev=[1], current=[2], next=[3]
        [2 | ] → [1 | ] → NULL

Step 3: prev=[2], current=[3], next=NULL
        [3 | ] → [2 | ] → [1 | ] → NULL

Final: Head points to [3]
```

## Static Allocation vs Linked Allocation

| Parameter         | Static Allocation (Arrays) | Linked Allocation (Linked Lists) |
| ----------------- | -------------------------- | -------------------------------- |
| Memory            | Fixed size, contiguous     | Dynamic size, non-contiguous     |
| Memory Efficiency | May waste memory           | Efficient memory utilization     |
| Insertion         | O(n) time complexity       | O(1) at beginning, O(n) at end   |
| Deletion          | O(n) time complexity       | O(1) at beginning, O(n) at end   |
| Access            | Random access, O(1)        | Sequential access, O(n)          |
| Flexibility       | Fixed capacity             | Grows/shrinks as needed          |

## Exam Tips

1. **Memory Diagrams**: Always draw memory diagrams for insertion/deletion operations
2. **Edge Cases**: Remember to handle empty list and single-node cases
3. **Memory Management**: Always free memory after deletion to prevent leaks
4. **Pointer Manipulation**: Practice pointer reassignment sequences
5. **Time Complexity**: Be prepared to analyze time complexity of operations
6. **Comparison Questions**: Know when to use arrays vs linked lists
7. **Code Tracing**: Practice tracing through linked list operations step-by-step
