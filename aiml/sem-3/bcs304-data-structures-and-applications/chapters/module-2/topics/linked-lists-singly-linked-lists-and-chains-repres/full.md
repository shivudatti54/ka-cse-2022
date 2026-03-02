# **Linked Lists: Singly Linked, Lists and Chains**

## **Introduction**

Linked lists are a fundamental data structure in computer science, consisting of a sequence of nodes, each containing a value and a reference (or link) to the next node in the sequence. This article will delve into the world of linked lists, exploring their history, types, and applications.

## **Historical Context**

The concept of linked lists dates back to the 1960s, when it was first introduced by Charles Bachman, a Canadian computer scientist. Bachman developed the concept of a linked list as a way to efficiently manage data in mainframe computers. The first implementations of linked lists were in assembly languages, where they were used to implement various data structures, such as trees and graphs.

## **Types of Linked Lists**

There are several types of linked lists, including:

### 1. Singly Linked Lists

A singly linked list is the most common type of linked list, where each node only points to the next node in the sequence.

### 2. Doubly Linked Lists

A doubly linked list is a type of linked list where each node points to both the previous and next nodes in the sequence.

### 3. Circularly Linked Lists

A circularly linked list is a type of linked list where the last node points back to the first node, creating a circular structure.

### 4. Multi-Level Linked Lists

A multi-level linked list is a type of linked list where each node can point to multiple other nodes in the sequence.

## **Representing Chains in C**

In C, linked lists can be represented using a structure that contains the value and a pointer to the next node in the sequence.

```c
typedef struct Node {
    int value;
    struct Node* next;
} Node;
```

## **Linked Stacks and Queues**

Linked stacks and queues are data structures that use linked lists to store and retrieve elements. A stack is a Last-In-First-Out (LIFO) data structure, where the last element added is the first one to be removed. A queue is a First-In-First-Out (FIFO) data structure, where the first element added is the first one to be removed.

### Linked Stack

A linked stack can be implemented using a singly linked list, where each node represents an element in the stack.

```c
typedef struct Stack {
    Node* top;
    int size;
} Stack;
```

### Linked Queue

A linked queue can be implemented using a doubly linked list, where each node represents an element in the queue.

```c
typedef struct Queue {
    Node* front;
    Node* rear;
    int size;
} Queue;
```

## **Polynomials and Linked Lists**

Polynomials are mathematical expressions consisting of terms with coefficients and variables. Linked lists can be used to represent polynomials, where each node represents a term in the polynomial.

```c
typedef struct Term {
    int coefficient;
    char variable;
    struct Term* next;
} Term;
```

## **Example Use Cases**

1.  **Database Query Result Sets**

    Linked lists can be used to represent the result sets of database queries. Each node in the linked list represents a row in the result set, and the pointers to the next nodes represent the relationships between the rows.

2.  **Dynamic Memory Allocation**

    Linked lists can be used to implement dynamic memory allocation, where each node in the linked list represents a block of free memory.

3.  **Compilers and Interpreters**

    Linked lists can be used to represent the symbol tables used in compilers and interpreters. Each node in the linked list represents a symbol in the program, and the pointers to the next nodes represent the relationships between the symbols.

## **Case Studies**

1.  **Implementation of a Linked List in C**

        ```c

    #include <stdio.h>
    #include <stdlib.h>

typedef struct Node {
int value;
struct Node\* next;
} Node;

typedef struct LinkedList {
Node\* head;
int size;
} LinkedList;

LinkedList* createLinkedList() {
LinkedList* list = (LinkedList\*) malloc(sizeof(LinkedList));
list->head = NULL;
list->size = 0;
return list;
}

void insertNode(LinkedList* list, int value) {
Node* newNode = (Node\*) malloc(sizeof(Node));
newNode->value = value;
newNode->next = list->head;
list->head = newNode;
list->size++;
}

void printList(LinkedList* list) {
Node* current = list->head;
while (current != NULL) {
printf("%d ", current->value);
current = current->next;
}
printf("\n");
}

int main() {
LinkedList\* list = createLinkedList();
insertNode(list, 1);
insertNode(list, 2);
insertNode(list, 3);
printList(list);
return 0;
}

````

2.  **Implementation of a Circularly Linked List in C**

    ```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node* next;
} Node;

typedef struct CircularLinkedList {
    Node* head;
    int size;
} CircularLinkedList;

CircularLinkedList* createCircularLinkedList() {
    CircularLinkedList* list = (CircularLinkedList*) malloc(sizeof(CircularLinkedList));
    list->head = NULL;
    list->size = 0;
    return list;
}

void insertNode(CircularLinkedList* list, int value) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->value = value;
    newNode->next = list->head;
    list->head = newNode;
}

void printList(CircularLinkedList* list) {
    Node* current = list->head;
    while (1) {
        printf("%d ", current->value);
        current = current->next;
        if (current == list->head) break;
    }
    printf("\n");
}

int main() {
    CircularLinkedList* list = createCircularLinkedList();
    insertNode(list, 1);
    insertNode(list, 2);
    insertNode(list, 3);
    printList(list);
    return 0;
}
````

## **Further Reading**

- "Introduction to Data Structures and Algorithms in Python" by Michael T. Goodrich
- "The C Programming Language" by Brian Kernighan and Dennis Ritchie
- "Data Structures and Algorithms in Java" by Vinay Chacharya
- "Algorithms" by Robert Sedgewick and Kevin Wayne
- "Introduction to Algorithms" by Thomas H. Cormen

This article has provided a comprehensive overview of linked lists, including their history, types, and applications. It has also included examples, case studies, and further reading suggestions to assist in understanding the topic.
