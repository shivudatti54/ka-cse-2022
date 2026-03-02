# **Linked Lists: Singly Linked, Lists and Chains**

## **Introduction**

A linked list is a linear data structure where each element is a separate object, known as a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion of elements from any position in the sequence.

## **Singly Linked List**

A singly linked list is a linked list where each node only points to the next node in the sequence. The last node in the sequence points to `NULL`, indicating its absence.

### Properties of a Singly Linked List:

- **Faster insertion and deletion**: Since each node only points to the next node, inserting or deleting a node can be done in O(1) time.
- **Slower searching**: Searching for a specific node in a singly linked list requires traversing the list until the desired node is found, which takes O(n) time.

### Example of a Singly Linked List:

```markdown
+----+ +----+ +----+ +----+
| 5 | --- null | 6 | --- null | 7 | --- null | 8 |
+----+ +----+ +----+ +----+
| |
| |
v v
+----+ +----+ +----+ +----+
| 3 | --- null | 4 | --- null | 5 | --- null | 6 |
+----+ +----+ +----+ +----+
| |
| |
v v
+----+ +----+ +----+ +----+
| 1 | --- null | 2 | --- null | 3 | --- null | 4 |
+----+ +----+ +----+ +----+
```

## **Doubly Linked List**

A doubly linked list is a linked list where each node points to both the next node and the previous node in the sequence. This structure allows for efficient traversal in both forward and backward directions.

### Properties of a Doubly Linked List:

- **Faster insertion and deletion**: Since each node points to both the next and previous nodes, inserting or deleting a node can be done in O(1) time.
- **Faster searching**: Searching for a specific node in a doubly linked list can be done in O(n) time.

### Example of a Doubly Linked List:

```markdown
+----+ +----+ +----+ +----+ +----+
| 5 | --- next---| 6 | --- next---| 7 | --- next---| 8 | --- next---| 9 |
+----+ +----+ +----+ +----+ +----+
| |
| |
v v
+----+ +----+ +----+ +----+ +----+ +----+
| 3 | --- next---| 4 | --- next---| 5 | --- next---| 6 | --- next---| 7 |
+----+ +----+ +----+ +----+ +----+ +----+
| |
| |
v v
+----+ +----+ +----+ +----+ +----+ +----+
| 1 | --- next---| 2 | --- next---| 3 | --- next---| 4 | --- next---| 5 |
+----+ +----+ +----+ +----+ +----+ +----+
```

## **Representing Chains in C**

A chain is a collection of data elements, each of which is a separate object. In C, we can represent a chain using a singly linked list.

### Example of a Chain in C:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Function to insert a new node at the end of the chain
void insertNode(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to print the chain
void printChain(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;
    insertNode(&head, 1);
    insertNode(&head, 2);
    insertNode(&head, 3);
    printChain(head);  // Output: 1 2 3
    return 0;
}
```

## **Linked Stacks and Queues**

A linked stack is a data structure that follows the Last-In-First-Out (LIFO) principle. A linked queue is a data structure that follows the First-In-First-Out (FIFO) principle.

### Linked Stack:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Function to push an element onto the stack
void push(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Function to pop an element from the stack
int pop(Node** head) {
    if (*head == NULL) {
        printf("Stack is empty\n");
        exit(1);
    }
    int data = (*head)->data;
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
    return data;
}

int main() {
    Node* head = NULL;
    push(&head, 1);
    push(&head, 2);
    push(&head, 3);
    printf("%d ", pop(&head));  // Output: 3
    printf("%d ", pop(&head));  // Output: 2
    printf("%d ", pop(&head));  // Output: 1
    return 0;
}
```

### Linked Queue:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Function to enqueue an element
void enqueue(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to dequeue an element
int dequeue(Node** head) {
    if (*head == NULL) {
        printf("Queue is empty\n");
        exit(1);
    }
    int data = (*head)->data;
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
    return data;
}

int main() {
    Node* head = NULL;
    enqueue(&head, 1);
    enqueue(&head, 2);
    enqueue(&head, 3);
    printf("%d ", dequeue(&head));  // Output: 1
    printf("%d ", dequeue(&head));  // Output: 2
    printf("%d ", dequeue(&head));  // Output: 3
    return 0;
}
```
