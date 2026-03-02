# Singly Linked Lists

## Introduction

A singly linked list is a fundamental linear data structure in computer science that consists of a sequence of nodes, where each node contains data and a pointer (or link) to the next node in the sequence. Unlike arrays, linked lists provide dynamic memory allocation, allowing the data structure to grow and shrink during program execution without requiring predefined size limits. This flexibility makes singly linked lists particularly valuable in scenarios where the amount of data is unknown in advance or changes frequently.

In the context of the University of Delhi's Computer Science curriculum, singly linked lists form the foundation for understanding more complex data structures like doubly linked lists, circular linked lists, and various abstract data types including stacks and queues. The concept of linked allocation, where memory is allocated as needed during runtime, represents a paradigm shift from static array-based implementations. This dynamic approach addresses many limitations of contiguous memory structures, including inefficient insertion and deletion operations that require element shifting.

Singly linked lists find extensive applications in real-world computing scenarios such as implementing adjacency lists for graphs, maintaining undo functionality in text editors, managing memory allocation in operating systems, and representing polynomial expressions in mathematical computations. Understanding the intricacies of singly linked list operations—creation, insertion, deletion, traversal, and searching—is essential for developing efficient algorithmic solutions and performing well in DU semester examinations.

## Key Concepts

### Node Structure and Memory Representation

A singly linked list comprises nodes, where each node consists of two components: the data field and the link (or next pointer) field. In C programming, this is typically implemented using a structure definition. The data field can hold a single value or multiple fields depending on the application requirements, while the link field stores the memory address of the next node in the sequence.

```c
struct Node {
    int data;
    struct Node *next;
};
```

The list maintains a pointer to the first node, traditionally called the HEAD or START pointer. The last node in the list contains a NULL pointer in its link field, indicating the end of the list. Memory for each node is dynamically allocated using functions like malloc() in C, which requests memory from the heap during runtime.

### Types of Linked List Operations

The operations on a singly linked list can be categorized into two main types: basic operations and auxiliary operations. Basic operations include creation (initializing an empty list), insertion (adding new nodes), deletion (removing existing nodes), and traversal (visiting each node). Auxiliary operations include searching for a specific element, finding the length of the list, and checking whether the list is empty.

Each operation has specific time complexities that are crucial for algorithm analysis. Traversing the entire list requires O(n) time, where n represents the number of nodes. Similarly, searching for an element in an unsorted list also requires O(n) time. Insertion at the beginning of the list is O(1), while insertion at the end requires O(n) unless a tail pointer is maintained.

### Insertion Operations

Insertion in a singly linked list can be performed at three different positions: the beginning, the end, or a specified position in the middle. Insertion at the beginning involves creating a new node, setting its next pointer to the current head, and updating the head pointer to point to the new node. This operation always takes constant time O(1) regardless of list size.

Insertion at the end requires traversing the entire list to reach the last node, making it O(n) for a list without a tail pointer. However, if a tail pointer is maintained, this operation can be performed in O(1). Insertion at a specific position requires first locating the position by traversing the list, then adjusting the pointers to include the new node in the sequence. Care must be taken to maintain the correct order of pointer modifications to avoid losing access to subsequent nodes.

### Deletion Operations

Deletion operations mirror insertion operations in terms of positioning. Deleting the first node involves saving the head pointer, advancing the head to the second node, and freeing the memory of the original first node. This operation is O(1). Deletion from the end requires traversing to find the second-to-last node and setting its next pointer to NULL, requiring O(n) time.

Deletion from a specific position requires locating the node to be deleted and its predecessor. The predecessor's next pointer is then updated to skip the node being deleted, and the memory is freed. Special care must be taken when deleting the last node or when the list contains only one node. Attempting to delete from an empty list or accessing a NULL pointer results in undefined behavior and potential program crashes.

### Traversal and Display

Traversing a linked list involves starting from the head node and following the next pointers until NULL is encountered. During traversal, each node's data can be processed—for display, calculation, or any other operation. The standard traversal pattern uses a temporary pointer that initially points to the head and advances through the list in a loop that continues until the pointer becomes NULL.

Understanding traversal is fundamental because many operations rely on it as a subroutine. Counting nodes, summing values, finding maximum or minimum elements, and searching all require traversing the list. The time complexity for any operation that examines all nodes is O(n).

## Examples

### Example 1: Creating a Singly Linked List

Problem: Create a singly linked list with nodes containing values 10, 20, and 30, then display all elements.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

int main() {
    struct Node *head = NULL;
    struct Node *second = NULL;
    struct Node *third = NULL;
    
    // Allocate three nodes
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    
    // Assign data and link nodes
    head->data = 10;
    head->next = second;
    
    second->data = 20;
    second->next = third;
    
    third->data = 30;
    third->next = NULL;
    
    // Traverse and display
    struct Node *temp = head;
    printf("List elements: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
    
    return 0;
}
```

Output: List elements: 10 -> 20 -> 30 -> NULL

### Example 2: Inserting a Node at the Beginning

Problem: Given a linked list with values 20 -> 30 -> NULL, insert a node with value 10 at the beginning.

Solution:

```c
struct Node* insertAtBeginning(struct Node *head, int value) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = head;
    return newNode;
}

// Usage
struct Node *head = NULL;
// Assume list 20 -> 30 -> NULL exists
head = insertAtBeginning(head, 10);
// Result: 10 -> 20 -> 30 -> NULL
```

The key insight is that inserting at the beginning requires updating only the head pointer. The new node's next pointer points to the previous first node, and the function returns the new node as the new head.

### Example 3: Deleting a Node with Specific Value

Problem: Delete the first occurrence of value 20 from the list 10 -> 20 -> 30 -> NULL.

Solution:

```c
struct Node* deleteNode(struct Node *head, int value) {
    struct Node *temp = head;
    struct Node *prev = NULL;
    
    // If head node contains the value
    if (temp != NULL && temp->data == value) {
        head = temp->next;
        free(temp);
        return head;
    }
    
    // Search for the node to delete
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }
    
    // If value not found
    if (temp == NULL) {
        printf("Value not found in list\n");
        return head;
    }
    
    // Unlink the node and free memory
    prev->next = temp->next;
    free(temp);
    return head;
}
```

After deletion: 10 -> 30 -> NULL

The algorithm handles two critical cases: when the node to delete is the head (requires head pointer update) and when it's in the middle or end (requires predecessor's next pointer update).

## Exam Tips

1. Understand the difference between static and dynamic memory allocation. In DU exams, questions frequently ask about malloc() and free() functions and their roles in linked list implementations.

2. Always check for NULL pointers before accessing node data or traversing. This is a common source of runtime errors and a frequent exam question.

3. Remember the time complexities: insertion at beginning O(1), insertion at end O(n), deletion at beginning O(1), deletion at end O(n), search O(n), traversal O(n).

4. When drawing linked list diagrams in exams, clearly show the HEAD pointer and NULL terminators. Diagrams typically carry significant marks.

5. The order of pointer modifications matters critically during insertion and deletion. Always update the next pointer of the previous node before updating any other pointers.

6. Be prepared to write complete C programs for creating, inserting, and deleting nodes. Exam questions often require actual code implementation, not just algorithm description.

7. Understand the concept of dummy/sentinel nodes and when they simplify boundary condition handling, especially for operations at both ends of the list.

8. Practice tracing through linked list operations with given sequences of operations. Tracing questions appear frequently in DU examinations.

9. Remember that linked lists do not provide direct access by index. To access the ith element, you must traverse i-1 nodes from the head.

10. When comparing with arrays, emphasize the advantages of linked lists: dynamic size, efficient insertions/deletions without shifting, and no memory wastage. These comparative analysis questions are common.