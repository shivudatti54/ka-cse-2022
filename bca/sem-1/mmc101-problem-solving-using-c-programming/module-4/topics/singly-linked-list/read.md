# Singly Linked List


## Table of Contents

- [Singly Linked List](#singly-linked-list)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Node Structure](#node-structure)
  - [Memory Allocation](#memory-allocation)
  - [Basic Operations](#basic-operations)
  - [Important Variations](#important-variations)
- [Examples](#examples)
  - [Example 1: Creating a Linked List from Array Elements](#example-1-creating-a-linked-list-from-array-elements)
  - [Example 2: Inserting a Node at a Specific Position](#example-2-inserting-a-node-at-a-specific-position)
  - [Example 3: Deleting a Node with a Specific Value](#example-3-deleting-a-node-with-a-specific-value)
- [Exam Tips](#exam-tips)

## Introduction

A singly linked list is a fundamental linear data structure in computer science that represents a sequence of nodes, where each node contains data and a pointer to the next node in the sequence. Unlike arrays, linked lists provide dynamic memory allocation, allowing the structure to grow and shrink during runtime without requiring predefined sizes. This flexibility makes linked lists essential for solving problems where the number of elements is unknown in advance or changes frequently.

In the context of C programming, singly linked lists are implemented using self-referential structures and pointers, concepts that were introduced earlier in this module. The ability to manipulate pointers and dynamically allocate memory are critical skills that culminate in understanding linked lists. From an algorithmic perspective, linked lists serve as the foundation for more complex data structures like stacks, queues, and graphs. They are particularly useful in scenarios requiring frequent insertion and deletion operations, where arrays would incur O(n) time complexity.

For University of Delhi examinations, singly linked lists are a frequently tested topic, often appearing in both theoretical questions and practical programming problems. Understanding the underlying mechanics of node allocation, pointer manipulation, and list traversal is essential for scoring well in internal assessments and end semester examinations.

## Key Concepts

### Node Structure

The fundamental building block of a singly linked list is the node, which consists of two components: the data part and the link (or next pointer) part. In C, this is implemented using a self-referential structure where the structure contains a pointer to itself.

```c
struct Node {
    int data;
    struct Node *next;
};
```

The data component stores the actual information, which can be of any valid C data type including integers, floats, characters, or even complex structures. The next pointer stores the memory address of the next node in the sequence, or NULL if the node is the last element in the list. The NULL pointer serves as a sentinel value indicating the end of the list.

### Memory Allocation

Creating nodes in a linked list requires dynamic memory allocation using the malloc() function from the standard library stdlib.h. This allows memory to be allocated at runtime from the heap, rather than the stack. The memory allocated must be properly freed using free() to prevent memory leaks.

```c
struct Node *newNode;
newNode = (struct Node *)malloc(sizeof(struct Node));
```

The casting of malloc's return value to struct Node* is optional in C but recommended for clarity. If malloc fails to allocate memory (due to insufficient heap space), it returns NULL, which must be checked before proceeding.

### Basic Operations

**Creation:** Creating a linked list involves repeatedly allocating new nodes and linking them together. The process begins with initializing the head pointer to NULL (an empty list), then adding nodes one by one.

**Traversal:** To access all elements in a linked list, we start from the head pointer and follow the next pointers until we reach NULL. This requires a temporary pointer that moves through the list while preserving the head pointer.

```c
void display(struct Node *head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

**Insertion:** There are four cases for insertion in a singly linked list:
1. At the beginning (beginning node)
2. At the end (last node)
3. After a given node (specific position)
4. Before a given node

Insertion at the beginning requires updating the head pointer to point to the new node. Insertion at the end requires traversing to the last node (where next is NULL) and updating its next pointer. The time complexity for insertion at the beginning is O(1), while insertion at the end is O(n).

**Deletion:** Similar to insertion, deletion can occur at the beginning, at the end, or at a specific position. Deleting the first node requires updating the head pointer to point to the second node. Deleting the last node requires traversing to find the second-to-last node and setting its next pointer to NULL.

```c
struct Node* deleteFirst(struct Node *head) {
    if (head == NULL) {
        return NULL;
    }
    struct Node *temp = head;
    head = head->next;
    free(temp);
    return head;
}
```

**Search:** Searching for an element requires traversing the list and comparing each node's data with the target value. The time complexity is O(n) in the worst case.

### Important Variations

**Counting Nodes:** A common operation is to count the total number of nodes in the list.

```c
int countNodes(struct Node *head) {
    int count = 0;
    struct Node *temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}
```

**Adding at End:** Creating a list by adding nodes at the end requires maintaining a tail pointer or traversing to the end each time.

```c
void append(struct Node **head, int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    struct Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

## Examples

### Example 1: Creating a Linked List from Array Elements

**Problem:** Given an array of 5 integers, create a linked list where each array element becomes a node's data.

**Step-by-step Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node* createFromArray(int arr[], int n) {
    struct Node *head = NULL, *temp, *newNode;
    int i;
    
    for (i = 0; i < n; i++) {
        newNode = (struct Node *)malloc(sizeof(struct Node));
        newNode->data = arr[i];
        newNode->next = NULL;
        
        if (head == NULL) {
            head = newNode;
        } else {
            temp->next = newNode;
        }
        temp = newNode;
    }
    return head;
}

void display(struct Node *head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        if (temp->next != NULL)
            printf("-> ");
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    struct Node *head = createFromArray(arr, 5);
    display(head);
    return 0;
}
```

**Output:** 10 -> 20 -> 30 -> 40 -> 50

**Explanation:** The createFromArray function iterates through each array element, allocates memory for a new node, assigns the data, and links it to the previous node. The first node becomes the head, and subsequent nodes are attached using a temporary pointer that tracks the last node.

### Example 2: Inserting a Node at a Specific Position

**Problem:** In an existing linked list (10 -> 20 -> 30), insert a new node with value 25 after the node containing 20.

**Step-by-step Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void insertAfter(struct Node *prevNode, int newData) {
    if (prevNode == NULL) {
        printf("Previous node cannot be NULL\n");
        return;
    }
    
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}

void display(struct Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    struct Node *second = (struct Node *)malloc(sizeof(struct Node));
    struct Node *third = (struct Node *)malloc(sizeof(struct Node));
    
    head->data = 10;
    head->next = second;
    
    second->data = 20;
    second->next = third;
    
    third->data = 30;
    third->next = NULL;
    
    printf("Original list: ");
    display(head);
    
    insertAfter(second, 25);
    
    printf("After inserting 25 after 20: ");
    display(head);
    
    return 0;
}
```

**Output:**
Original list: 10 -> 20 -> 30 -> NULL
After inserting 25 after 20: 10 -> 20 -> 25 -> 30 -> NULL

**Explanation:** The insertAfter function takes a pointer to the node after which insertion must occur. We allocate a new node, set its data, make its next pointer point to the node that previously followed the previous node, and then update the previous node's next pointer to point to the new node. The order of these two steps is critical—reversing them would cause us to lose the reference to the rest of the list.

### Example 3: Deleting a Node with a Specific Value

**Problem:** Delete the first occurrence of node containing value 20 from the linked list (10 -> 20 -> 30 -> 40).

**Step-by-step Solution:**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node* deleteNode(struct Node *head, int key) {
    struct Node *temp = head;
    struct Node *prev = NULL;
    
    if (temp != NULL && temp->data == key) {
        head = temp->next;
        free(temp);
        return head;
    }
    
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("Key %d not found in the list\n", key);
        return head;
    }
    
    prev->next = temp->next;
    free(temp);
    return head;
}

void display(struct Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    struct Node *second = (struct Node *)malloc(sizeof(struct Node));
    struct Node *third = (struct Node *)malloc(sizeof(struct Node));
    struct Node *fourth = (struct Node *)malloc(sizeof(struct Node));
    
    head->data = 10;
    head->next = second;
    
    second->data = 20;
    second->next = third;
    
    third->data = 30;
    third->next = fourth;
    
    fourth->data = 40;
    fourth->next = NULL;
    
    printf("Original list: ");
    display(head);
    
    head = deleteNode(head, 20);
    
    printf("After deleting 20: ");
    display(head);
    
    return 0;
}
```

**Output:**
Original list: 10 -> 20 -> 30 -> 40 -> NULL
After deleting 20: 10 -> 30 -> 40 -> NULL

**Explanation:** The deleteNode function handles three scenarios: deletion of the first node (head), deletion of a node in the middle, and deletion of the last node. We maintain two pointers—one to track the current node and one to track the previous node. When the key is found, we bypass the node by updating the previous node's next pointer to skip the current node, then free the memory of the node being deleted.

## Exam Tips

1. **Understand the difference between head and first node**: The head pointer is a pointer variable that stores the address of the first node. It is not the first node itself. Always pass the head pointer by reference (using struct Node**) when modifying the head.

2. **Always check for NULL**: Before accessing any node's data or next pointer, ensure the node is not NULL. Dereferencing a NULL pointer causes segmentation faults and program crashes.

3. **Order of operations matters**: When inserting or deleting nodes, the sequence of pointer updates is critical. For insertion, always link the new node to the rest of the list BEFORE disconnecting the previous node. For deletion, save the reference before freeing.

4. **Time complexity awareness**: Remember that traversal requires O(n), insertion at beginning is O(1), insertion at end is O(n), search is O(n), and deletion of first node is O(1).

5. **Memory management**: Always free dynamically allocated memory using free(). Failing to do so causes memory leaks. After freeing a node, the pointer becomes a dangling pointer—it should either be set to NULL or not be used further.

6. **Drawing helps**: For algorithm questions, draw the linked list visually with boxes representing nodes and arrows representing pointers. This is extremely helpful for debugging and understanding pointer manipulations.

7. **Common functions to memorize**: Be prepared to write functions for createList(), display(), insertAtBegin(), insertAtEnd(), deleteFirst(), deleteLast(), and search().

8. **Difference from arrays**: Understand that linked lists do not provide direct access by index. To access the nth element, you must traverse through n-1 nodes.