# Linked Lists: Singly Linked, Lists and Chains

=====================================================

## Introduction

---

Linked lists are a fundamental data structure in computer science, used to store and manipulate collections of data. In this chapter, we will delve into the world of linked lists, exploring their different types, representations, and applications.

## Historical Context

---

The concept of linked lists dates back to the 1960s, when computer scientists began exploring ways to efficiently manage large amounts of data. The first linked list was developed in 1964 by Ivan Sutherland, a computer scientist and pioneer in the field of computer graphics.

## Types of Linked Lists

---

There are two primary types of linked lists:

### 1. Singly Linked Lists

A singly linked list is a basic type of linked list where each element points to the next element in the list. This means that each node only has a reference to the next node, rather than both the previous and next nodes.

**Example:**

```
Node 1 -> Node 2 -> Node 3 -> ...
```

### 2. Doubly Linked Lists

A doubly linked list is a type of linked list where each element points to both the previous and next elements in the list.

**Example:**

```
Node 1 <-> Node 2 <-> Node 3 <-> ...
```

## Representing Chains in C

---

Chains are a type of linked list that store a collection of linked lists. In C, we can represent chains using a struct and a pointer to the head of the chain.

**Example:**

```c
typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Chain {
    Node* head;
} Chain;
```

## Linked Stacks and Queues

---

Linked stacks and queues are data structures that use linked lists to manage elements. A linked stack follows the LIFO (Last In First Out) principle, where the last element added is the first one removed. A linked queue follows the FIFO (First In First Out) principle, where the first element added is the first one removed.

**Example:**

Linked Stack:

```
Node 1
|
Node 2
|
Node 3
```

Linked Queue:

```
Node 1 -> Node 2 -> Node 3
```

## Polynomials

---

Polynomials can be represented using linked lists, where each node represents a term in the polynomial. The coefficient of each term is stored in the node, and the power of each term is stored in a separate variable.

**Example:**

```
Term 1: 3x^2 + 2x - 1
Term 2: 4x^3 + 2x^2 - 3x + 1
```

## Applications

---

Linked lists have numerous applications in computer science and software development, including:

- **Database query optimization**: Linked lists can be used to optimize database queries by storing results in a linked list and then iterating over the list to retrieve the final result.
- **Graph algorithms**: Linked lists can be used to represent graphs and perform algorithms such as graph traversal and shortest paths.
- **Dynamic memory allocation**: Linked lists can be used to manage dynamic memory allocation by storing free blocks of memory in a linked list.

## Case Studies

---

### Case Study 1: Implementing a Linked List in C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Linked List {
    Node* head;
} Linked List;

Linked List* createLinkedList() {
    Linked List* list = (Linked List*) malloc(sizeof(Linked List));
    list->head = NULL;
    return list;
}

void appendNode(Linked List* list, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = list->head;
    list->head = newNode;
}

void printList(Linked List* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Linked List* list = createLinkedList();
    appendNode(list, 1);
    appendNode(list, 2);
    appendNode(list, 3);
    printList(list);
    return 0;
}
```

### Case Study 2: Implementing a Doubly Linked List in C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

typedef struct Doubly Linked List {
    Node* head;
    Node* tail;
} Doubly Linked List;

Doubly Linked List* createDoublyLinkedList() {
    Doubly Linked List* list = (Doubly Linked List*) malloc(sizeof(Doubly Linked List));
    list->head = NULL;
    list->tail = NULL;
    return list;
}

void appendNode(Doubly Linked List* list, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;
    newNode->prev = list->tail;
    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        newNode->next = list->head;
        list->head->prev = newNode;
        list->head = newNode;
    }
}

void printList(Doubly Linked List* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Doubly Linked List* list = createDoublyLinkedList();
    appendNode(list, 1);
    appendNode(list, 2);
    appendNode(list, 3);
    printList(list);
    return 0;
}
```

## Further Reading

---

- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms" by Robert Sedgewick and Kevin Wayne
- "The C Programming Language" by Brian Kernighan and Dennis Ritchie

## Conclusion

---

In conclusion, linked lists are a fundamental data structure in computer science, used to store and manipulate collections of data. Understanding the different types of linked lists, their representations, and applications is crucial for any software developer or computer scientist. By mastering linked lists, you can efficiently manage large amounts of data and implement complex algorithms.
