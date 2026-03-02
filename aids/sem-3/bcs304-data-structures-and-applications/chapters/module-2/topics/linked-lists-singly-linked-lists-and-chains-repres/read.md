# **Linked Lists: Singly Linked, Lists and Chains**

### Introduction

---

A linked list is a linear data structure where each element is a separate object, and each element (called a "node") points to the next node in the sequence. This structure allows for efficient insertion and deletion of elements from any position in the list.

### Singly Linked Lists

---

A singly linked list is a linked list where each node only points to the next node in the sequence. This means that each node can only move forward in the list, and there is no reference to the previous node.

#### Definition

A singly linked list is a data structure consisting of a sequence of nodes, where each node contains a value and a reference (i.e., a "link") to the next node in the sequence.

#### Example

Suppose we have a singly linked list with the following nodes:

- Node 1: value = 5, next = Node 2
- Node 2: value = 10, next = Node 3
- Node 3: value = 15, next = NULL

#### Operations

- Insertion: To insert a new node at the beginning of the list, we need to create a new node and update the next pointer of the first node to point to the new node.
- Deletion: To delete a node from the list, we need to update the next pointer of the previous node to skip over the node to be deleted.

### Lists and Chains

---

A list is a collection of elements, and a chain is a specific type of list where each element is a node in a linked list. In other words, a chain is a linked list where each node points to the next node in the sequence.

#### Definition

A list is a collection of elements, and a chain is a specific type of list where each element is a node in a linked list.

#### Example

Suppose we have a list with the following elements:

- Node 1: value = 5
- Node 2: value = 10
- Node 3: value = 15

This list is equivalent to a chain with three nodes, where each node points to the next node in the sequence.

#### Operations

- Insertion: To insert a new element into the list, we need to create a new node and update the next pointer of the last node to point to the new node.
- Deletion: To delete an element from the list, we need to update the next pointer of the previous node to skip over the node to be deleted.

### Representing Chains in C

---

To represent a chain in C, we can use a struct to define the nodes and a pointer to the head node to keep track of the beginning of the list.

#### Example

```c
typedef struct Node {
    int value;
    struct Node* next;
} Node;

typedef struct List {
    Node* head;
} List;

// Create a new node
Node* createNode(int value) {
    Node* newNode = malloc(sizeof(Node));
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

// Create a new list
List* createList() {
    List* newList = malloc(sizeof(List));
    newList->head = NULL;
    return newList;
}

// Insert a new node into the list
void insertNode(List* list, int value) {
    Node* newNode = createNode(value);
    if (list->head == NULL) {
        list->head = newNode;
    } else {
        Node* current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// Print the list
void printList(List* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}
```

### Linked Stacks and Queues

---

A linked stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first one to be removed. A linked queue is a linear data structure that follows the First-In-First-Out (FIFO) principle, where the first element added to the queue is the first one to be removed.

#### Linked Stack

A linked stack is a linked list where the top node points to the next node in the sequence. To add an element to the stack, we need to create a new node and update the next pointer of the top node to point to the new node. To remove an element from the stack, we need to update the next pointer of the top node to point to the previous node.

#### Linked Queue

A linked queue is a linked list where the front node points to the next node in the sequence. To add an element to the queue, we need to create a new node and update the next pointer of the front node to point to the new node. To remove an element from the queue, we need to update the next pointer of the front node to point to the next node in the sequence.

### Polynomials

---

A polynomial is a mathematical expression consisting of variables and coefficients combined using the operations of addition, subtraction, and multiplication.

#### Definition

A polynomial is a mathematical expression consisting of variables and coefficients combined using the operations of addition, subtraction, and multiplication.

#### Example

Suppose we have a polynomial with the following terms:

a + 2x + 3x^2

This polynomial is equivalent to the expression:

a + 2x + 3x^2

#### Operations

- Addition: To add two polynomials, we need to combine like terms.
- Subtraction: To subtract one polynomial from another, we need to combine like terms.
- Multiplication: To multiply a polynomial by a variable, we need to multiply each term in the polynomial by the variable.

#### Linked Polynomials

---

A linked polynomial is a linked list where each node represents a term in the polynomial. To add two linked polynomials, we need to combine like terms. To subtract one linked polynomial from another, we need to combine like terms. To multiply a linked polynomial by a variable, we need to multiply each term in the polynomial by the variable.

### Operations

---

- Insertion: To insert a new node into the list, we need to create a new node and update the next pointer of the previous node to point to the new node.
- Deletion: To delete a node from the list, we need to update the next pointer of the previous node to skip over the node to be deleted.
- Search: To search for a node in the list, we need to iterate through the list until we find the node we are looking for.
- Insertion at specific position: To insert a new node at a specific position in the list, we need to create a new node and update the next pointer of the previous node to point to the new node.
- Deletion at specific position: To delete a node at a specific position in the list, we need to update the next pointer of the previous node to skip over the node to be deleted.

### Key Concepts

---

- Singly linked lists
- Lists and chains
- Representing chains in C
- Linked stacks and queues
- Polynomials
- Linked polynomials
- Operations
- Key concepts: insertion, deletion, search, insertion at specific position, deletion at specific position

### Practice Problems

---

1. Create a singly linked list with the following nodes: Node 1: value = 5, Node 2: value = 10, Node 3: value = 15.
2. Insert a new node with value = 20 into the list.
3. Delete the node with value = 10 from the list.
4. Create a linked stack with the following elements: Element 1: value = 5, Element 2: value = 10, Element 3: value = 15.
5. Add a new element with value = 20 to the stack.
6. Remove the element with value = 10 from the stack.
