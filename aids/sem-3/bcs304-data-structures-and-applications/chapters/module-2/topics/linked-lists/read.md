# Linked Lists

## Introduction

Linked Lists represent one of the most fundamental and versatile dynamic data structures in computer science. Unlike static arrays that require contiguous memory allocation and fixed size declaration, linked lists provide a flexible mechanism for storing and managing collections of elements that can grow or shrink dynamically during program execution. In the context of the University of Delhi Computer Science curriculum, linked lists form the backbone of understanding dynamic memory management and pointer-based data structures.

The significance of linked lists extends far beyond their immediate practical applications. They serve as the foundation for implementing other complex data structures such as stacks, queues, graphs (adjacency lists), and hash tables. Understanding linked lists deeply prepares students to grasp more advanced concepts in data structures and algorithms, making it an essential topic for anyone pursuing computer science at the undergraduate level.

In real-world applications, linked lists are used extensively in operating systems for process scheduling, in file systems for directory structures, in web browsers for managing browser history (back and forward navigation), and in music players for creating playlists. The dynamic nature of linked lists makes them indispensable when the number of elements is unknown beforehand or when frequent insertions and deletions are required.

## Key Concepts

### Definition and Structure

A linked list is a linear data structure where elements (called nodes) are stored in separate memory locations and connected through pointers. Each node contains two components: the data (which stores the actual information) and the link (which stores the memory address of the next node). This fundamental difference from arrays—where elements are stored in contiguous memory locations—gives linked lists their unique properties and advantages.

The first node in a linked list is called the HEAD, and the last node typically points to NULL to indicate the end of the list. The head pointer serves as the entry point to the entire list, and losing reference to the head effectively loses access to the entire data structure.

### Types of Linked Lists

SINGLY LINKED LISTS represent the simplest form where each node contains data and a single pointer pointing to the next node. Navigation is strictly forward-only, from the head to the tail. This type is memory-efficient as it requires only one pointer per node.

DOUBLY LINKED LISTS enhance the singly linked list by adding a previous pointer to each node, allowing traversal in both forward and backward directions. While this requires additional memory for the extra pointer, it simplifies operations like deletion (since we can easily access the previous node) and is particularly useful in applications requiring bidirectional traversal.

CIRCULAR LINKED LISTS modify the basic structure by connecting the last node back to the first, forming a circle. In a circular singly linked list, the last node points to the first node; in a circular doubly linked list, both the first node's previous pointer and last node's next pointer connect to form a complete circle. These are particularly useful in round-robin scheduling and cyclic buffering.

### Node Representation in C

In C programming, a node is typically implemented using a structure. For a singly linked list node:

```c
struct Node {
    int data;
    struct Node *next;
};
```

The data field can be modified to store any type of information—integers, characters, floats, or even complex structures. The next pointer stores the memory address of the next node or NULL if it is the last node.

### Operations on Linked Lists

TRAVERSAL involves visiting each node sequentially to process or display its contents. Starting from the head, we follow the next pointers until we reach NULL. The time complexity is O(n) where n is the number of nodes.

INSERTION can be performed at three positions: at the beginning (O(1) operation), at the end (O(n) operation without tail pointer), or at a specific position in the middle. Each insertion requires dynamic memory allocation using malloc() and careful pointer manipulation to maintain list integrity.

DELETION mirrors insertion with operations at the beginning, end, or middle position. Proper memory management is crucial—we must free the memory of the deleted node using free() to prevent memory leaks. Deletion from the beginning is O(1), while deletion from end or middle is O(n).

SEARCHING performs a linear traversal comparing each node's data with the target value. The worst-case time complexity is O(n), making it less efficient than binary search available in sorted arrays, but unlike arrays, linked lists don't require elements to be stored contiguously.

### Memory Allocation and Deallocation

Dynamic memory allocation is fundamental to linked lists. In C, we use malloc() to allocate memory for new nodes and free() to deallocate memory when nodes are removed. The proper sequence for creating a node is: allocate memory, initialize data, set next pointer to NULL, and then integrate into the list.

Memory leaks occur when allocated memory is not properly freed, leading to reduced available memory over time. In embedded systems or long-running applications, memory leaks can cause system failure. Conversely, using freed memory (dangling pointers) leads to undefined behavior and security vulnerabilities.

## Examples

### Example 1: Creating and Traversing a Singly Linked List

Problem: Create a linked list with nodes containing values 10, 20, and 30, then display all elements.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

int main() {
    // Create three nodes
    struct Node *head = (struct Node*)malloc(sizeof(struct Node));
    struct Node *second = (struct Node*)malloc(sizeof(struct Node));
    struct Node *third = (struct Node*)malloc(sizeof(struct Node));
    
    // Assign data and links
    head->data = 10;
    head->next = second;
    
    second->data = 20;
    second->next = third;
    
    third->data = 30;
    third->next = NULL;
    
    // Traverse and print
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
    
    // Free memory
    free(head);
    free(second);
    free(third);
    
    return 0;
}
```

Output: 10 -> 20 -> 30 -> NULL

### Example 2: Insertion at the Beginning

Problem: Insert a new node with value 5 at the beginning of an existing list (10 -> 20 -> NULL).

Solution:

```c
struct Node* insertAtBeginning(struct Node *head, int value) {
    // Create new node
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    
    // Point new node to current head
    newNode->next = head;
    
    // Update head to new node
    return newNode;
}
```

After calling insertAtBeginning(head, 5), the list becomes: 5 -> 10 -> 20 -> NULL

The key insight is that we first link the new node to the existing list (newNode->next = head) before updating head. If we did this in reverse order, we would lose reference to the entire list.

### Example 3: Deleting a Node from Middle

Problem: Delete the first occurrence of node with value 20 from the list (10 -> 20 -> 30 -> NULL).

Solution:

```c
struct Node* deleteNode(struct Node *head, int value) {
    // Handle empty list
    if (head == NULL) return NULL;
    
    // If head node contains the value
    if (head->data == value) {
        struct Node *temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    // Search for the node to delete
    struct Node *current = head;
    while (current->next != NULL && current->next->data != value) {
        current = current->next;
    }
    
    // If value found
    if (current->next != NULL) {
        struct Node *temp = current->next;
        current->next = temp->next;
        free(temp);
    }
    
    return head;
}
```

After deletion, the list becomes: 10 -> 30 -> NULL

## Exam Tips

For University of Delhi semester examinations, the following points are essential for scoring well in linked list questions:

1. DRAW DIAGRAMS FREQUENTLY: Visual representation helps understand pointer manipulation. examiners appreciate clear diagrams showing before and after states of linked list operations.

2. ALWAYS CHECK FOR NULL: Before accessing->next or->data, verify the pointer is not NULL. This is the most common source of runtime errors and segmentation faults in linked list implementations.

3. UNDERSTAND THE DIFFERENCE BETWEEN ARRAY AND LINKED LIST: Arrays provide O(1) random access but O(n) insertion/deletion; linked lists provide O(1) insertion/deletion at known positions but O(n) for access. Choose based on use case.

4. MEMORY MANAGEMENT IS CRUCIAL: Always pair malloc() with free(). In exam questions, mention that dynamically allocated memory must be freed to prevent memory leaks.

5. TIME COMPLEXITY MEMORIZATION: Insertion at beginning: O(1), Insertion at end with tail: O(1), without tail: O(n). Search: O(n). Deletion at beginning: O(1), Deletion at end: O(n).

6. PRACTICE POINTER MANIPULATION: The core of linked list operations is pointer manipulation. Understand that changing ->next changes what node comes next in the sequence.

7. DOUBLY LINKED LIST DELETION IS SIMPLER: Remember that in doubly linked lists, we can directly access the previous node, making deletion O(1) if we have the node pointer, unlike singly linked lists requiring traversal.

8. EDGE CASES MATTER: Always consider and handle edge cases—empty list, single node, insertion at beginning/end, deletion of first/last node.