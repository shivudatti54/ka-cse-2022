# Singly Linked Lists

## Introduction

A singly linked list is a fundamental linear data structure in computer science where elements are stored in nodes, and each node contains data along with a pointer to the next node in the sequence. Unlike arrays, linked lists provide dynamic memory allocation, allowing the structure to grow and shrink during program execution without requiring contiguous memory blocks. This flexibility makes singly linked lists an essential concept for understanding more complex data structures and algorithmic problem-solving.

In the context of the University of Delhi's Computer Science curriculum, singly linked lists form the foundation for understanding linked representations of data. The concept is crucial because it introduces the fundamental idea of dynamic memory management and pointer-based data structures, which are extensively used in implementing stacks, queues, and graph adjacency lists. Understanding singly linked lists also prepares students for tackling real-world programming challenges where efficient insertion, deletion, and traversal operations are critical.

The significance of singly linked lists extends beyond academic requirements. In practical applications, they are used in operating systems for process scheduling, in file systems for directory structures, and in memory management for free block lists. Mastering this topic develops analytical thinking and problem-solving skills that are transferable to advanced data structures and algorithm design courses.

## Key Concepts

### Node Structure

A singly linked list consists of nodes where each node contains two components: the data field and the link (or next pointer) field. The data field stores the actual information, while the link field stores the memory address of the next node. In C programming, this is typically implemented using a struct:

```c
struct Node {
    int data;
    struct Node* next;
};
```

The list is accessed through a head pointer that points to the first node. If the head pointer is NULL, the list is empty. The last node in the list has its next pointer set to NULL, indicating the end of the list.

### Basic Operations

INSERTION OPERATIONS form the backbone of linked list manipulation. Insertion at the beginning requires creating a new node, setting its next pointer to the current head, and updating the head pointer. Insertion at the end requires traversing to the last node and adjusting pointers. Insertion at a specific position requires maintaining a pointer to the node preceding the insertion point.

DELETION OPERATIONS mirror insertion but require careful memory management. Deleting the first node involves saving the head, moving head to the next node, and freeing the old head. Deleting from the middle or end requires adjusting the next pointer of the previous node to skip over the deleted node.

TRAVERSAL involves starting from the head and following next pointers until NULL is encountered. This operation is fundamental for searching, printing, and performing computations on list elements.

### Memory Allocation

Dynamic memory allocation is achieved using malloc() in C for creating nodes at runtime. Each node is allocated individually from the heap, which allows the list to grow beyond predefined limits. However, this also requires explicit deallocation using free() to prevent memory leaks. The memory addresses of nodes need not be contiguous, which is both an advantage (flexibility) and a disadvantage (no random access).

### Time Complexity Analysis

Understanding time complexity is crucial for algorithm design. Accessing an element by position requires O(n) time in the worst case because traversal from the head is necessary. Searching also requires O(n) time. Insertion and deletion at the beginning are O(1) operations, while at the end they are O(n) unless a tail pointer is maintained. Space complexity is O(n) for storing n elements plus O(n) for the next pointers.

## Examples

### Example 1: Insertion at Beginning

PROBLEM: Insert a new node with value 25 at the beginning of a linked list that currently contains 10 -> 20 -> 30.

SOLUTION:
Step 1: Create a new node with data = 25
Step 2: Set new node's next pointer to point to the current head (node containing 10)
Step 3: Update head pointer to point to the new node

Result: 25 -> 10 -> 20 -> 30

C CODE:
```c
void insertAtBeginning(struct Node** head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = *head;
    *head = newNode;
}
```

### Example 2: Deletion of a Node

PROBLEM: Delete the node containing value 20 from the list 10 -> 20 -> 30 -> 40.

SOLUTION:
Step 1: Traverse to find the node containing 20 and keep track of previous node
Step 2: Previous node (containing 10) should point to the node after 20 (containing 30)
Step 3: Free the memory of the deleted node

Result: 10 -> 30 -> 40

C CODE:
```c
void deleteNode(struct Node** head, int value) {
    struct Node* temp = *head;
    struct Node* prev = NULL;
    
    if (temp != NULL && temp->data == value) {
        *head = temp->next;
        free(temp);
        return;
    }
    
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) return;
    
    prev->next = temp->next;
    free(temp);
}
```

### Example 3: Reversing a Linked List

PROBLEM: Reverse the singly linked list 1 -> 2 -> 3 -> 4 -> NULL to become 4 -> 3 -> 2 -> 1 -> NULL.

SOLUTION:
Step 1: Initialize three pointers: previous (NULL), current (head), and next (NULL)
Step 2: For each node, save the next node, reverse the pointer, and move all pointers one position ahead
Step 3: After loop completes, previous will point to the new head

C CODE:
```c
struct Node* reverseList(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
}
```

## Exam Tips

FOR DU SEMESTER EXAMS, students should pay special attention to the following points:

1. DRAW DIAGRAMS WHENEVER POSSIBLE. Visual representation of linked lists helps in understanding pointer manipulations and prevents errors in examination answers.

2. ALWAYS CHECK FOR NULL POINTERS before accessing node->next or node->data to avoid segmentation faults in code and to demonstrate defensive programming in theoretical answers.

3. UNDERSTAND THE DIFFERENCE BETWEEN malloc AND calloc. malloc allocates uninitialized memory while calloc initializes all bytes to zero. This distinction frequently appears in examination questions.

4. REMEMBER THAT SINGLY LINKED LISTS DO NOT SUPPORT BACKWARD TRAVERSAL. This is a key limitation compared to doubly linked lists and is often tested in comparison questions.

5. PRACTICE WRITING CODE FROM SCRATCH without referring to textbooks. In DU examinations, students are expected to write complete programs or functions for linked list operations.

6. TIME COMPLEXITY QUESTIONS ARE FREQUENTLY ASKED. Memorize the Big-O notation for all basic operations: insertion at beginning O(1), insertion at end O(n), deletion at beginning O(1), deletion at end O(n), search O(n).

7. THE HEAD POINTER MUST BE PASSED BY REFERENCE (or as double pointer) when modifying the list. This common mistake leads to incorrect implementations and is often tested in practical examinations.