# Singly Linked Lists

## Introduction

A singly linked list is a fundamental linear data structure in computer science where elements are stored in nodes, and each node contains data along with a pointer to the next node in the sequence. Unlike arrays, linked lists provide dynamic memory allocation, allowing efficient insertion and deletion operations without requiring contiguous memory locations. This flexibility makes singly linked lists essential for solving problems where the size of data structures needs to change frequently or is unknown at compile time.

In the context of the University of Delhi Computer Science curriculum, singly linked lists form the foundation for understanding more complex data structures like doubly linked lists, circular linked lists, and various abstract data types. The concept is particularly important for implementing stacks and queues, polynomial representations, and memory management systems. Understanding the mechanics of node allocation, traversal, insertion, and deletion operations in singly linked lists develops algorithmic thinking skills crucial for programming interviews and real-world software development.

## Key Concepts

### Structure of a Node

A singly linked list consists of nodes where each node contains two fields: a data field to store the actual information and a link field (or next pointer) that stores the memory address of the next node in the sequence. The first node is called the head, and the last node's link field contains NULL (or nullptr in C++) to indicate the end of the list. In C, this structure is typically defined using a struct or typedef structure.

```c
struct Node {
    int data;
    struct Node* next;
};
```

The data field can hold any valid data type including integers, floats, characters, or even complex structures. The pointer field always holds the address of the next node, making the list dynamic and flexible.

### Memory Allocation

Singly linked lists utilize dynamic memory allocation using functions like malloc() in C or new operator in C++. Each node is allocated individually on the heap, and these nodes need not be contiguous in memory. When a node is no longer needed, memory must be explicitly deallocated using free() in C or delete operator in C++ to prevent memory leaks. The total memory consumption of a linked list equals the sum of data size plus pointer size for each node, plus any overhead from memory allocation metadata.

### Traversal Operations

Traversing a singly linked list involves starting from the head node and following the next pointers until NULL is encountered. This is typically implemented using a while loop that continues as long as the current pointer is not NULL. During traversal, each node's data can be processed, printed, or used in computations. The time complexity for traversal is O(n) where n represents the number of nodes in the list.

```c
void traverse(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
}
```

### Insertion Operations

Insertion in a singly linked list can occur at three different positions: at the beginning, at the end, or at a specific position in the middle. Insertion at the beginning requires creating a new node, setting its next pointer to the current head, and updating the head pointer. Insertion at the end requires traversing to the last node and adding a new node after it. Insertion at a specific position requires maintaining a previous pointer while traversing to the target position, then adjusting pointers to include the new node in the sequence. All insertion operations, when properly implemented, maintain the链表的完整性 regardless of the insertion point.

### Deletion Operations

Deletion operations mirror insertion operations in their complexity. Deleting the first node simply requires moving the head pointer to the second node and freeing the old head. Deleting the last node requires traversing to find both the last node and the second-to-last node, setting the second-to-last node's next pointer to NULL, and then freeing the last node. Deleting a node at a specific position requires maintaining both current and previous pointers to properly adjust the link field of the previous node to skip over the deleted node.

### Searching Operations

Searching for an element in a singly linked list requires linear traversal from the head until either the target element is found or the end of the list is reached. The time complexity is O(n) in the worst case, making linked lists less efficient than hash tables or balanced trees for frequent searches. A variation called sentinel search can optimize by adding a dummy node at the beginning, eliminating the need for NULL checks during traversal.

## Examples

### Example 1: Creating and Displaying a Singly Linked List

Problem: Create a singly linked list with nodes containing values 10, 20, 30, and 40, then display all elements.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    struct Node *head = NULL, *newNode, *temp;
    int values[] = {10, 20, 30, 40};
    int n = 4;
    
    for (int i = 0; i < n; i++) {
        newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = values[i];
        newNode->next = NULL;
        
        if (head == NULL) {
            head = newNode;
        } else {
            temp->next = newNode;
        }
        temp = newNode;
    }
    
    printf("Linked List Elements: ");
    temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    
    return 0;
}
```

Output: Linked List Elements: 10 20 30 40

This example demonstrates node creation, memory allocation, and basic traversal. The key insight is maintaining a temporary pointer to the last node for efficient appending during list creation.

### Example 2: Inserting a Node at a Specific Position

Problem: Given a linked list with elements 5 -> 10 -> 15 -> NULL, insert a node with value 12 after the node containing 10.

Solution:

```c
struct Node* insertAfter(struct Node* head, int searchValue, int newValue) {
    struct Node* current = head;
    
    while (current != NULL && current->data != searchValue) {
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Value %d not found\n", searchValue);
        return head;
    }
    
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newValue;
    newNode->next = current->next;
    current->next = newNode;
    
    return head;
}
```

Working: The function traverses until finding node with data 10. A new node with value 12 is created and its next pointer is set to point to the node containing 15. Then the node containing 10's next pointer is updated to point to the new node. The final list becomes: 5 -> 10 -> 12 -> 15 -> NULL.

### Example 3: Deleting a Node from a Singly Linked List

Problem: Delete the node containing value 20 from the list: 10 -> 20 -> 30 -> 40 -> NULL

Solution:

```c
struct Node* deleteNode(struct Node* head, int value) {
    struct Node* current = head;
    struct Node* prev = NULL;
    
    if (head == NULL) {
        return NULL;
    }
    
    if (head->data == value) {
        head = head->next;
        free(current);
        return head;
    }
    
    while (current != NULL && current->data != value) {
        prev = current;
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Value not found\n");
        return head;
    }
    
    prev->next = current->next;
    free(current);
    
    return head;
}
```

After deletion, the list becomes: 10 -> 30 -> 40 -> NULL. This implementation handles three cases: empty list, deletion at head, and deletion at middle or end positions.

## Exam Tips

For DU semester examinations, several critical points must be remembered when answering questions on singly linked lists. First, always draw diagrams to visualize the list structure and pointer modifications—this helps catch logical errors and makes your solution clear to examiners. Second, remember that the time complexity for insertion or deletion at the beginning is O(1), while operations at the end or middle require O(n) traversal time.

Third, when writing code, always check for NULL pointers before dereferencing to avoid segmentation faults—examiners specifically look for these edge case handling capabilities. Fourth, understand the difference between stack memory (automatic allocation) and heap memory (dynamic allocation) when creating nodes, as incorrect memory management leads to memory leaks.

Fifth, for deletion operations, always free the deleted node to prevent memory leaks, though in exam scenarios the conceptual understanding is often sufficient. Sixth, remember that singly linked lists cannot be traversed backward, which distinguishes them from doubly linked lists—a common exam question involves comparing these two structures.

Seventh, when asked to implement functions, always handle the edge cases: empty list, single node list, insertion at the beginning versus middle, and deletion of first node versus last node. Finally, practice writing recursive functions for linked list operations, as recursion-based solutions frequently appear in advanced questions.