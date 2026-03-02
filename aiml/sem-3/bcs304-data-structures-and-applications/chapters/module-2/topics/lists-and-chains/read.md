# Lists and Chains

## Introduction

Lists and Chains form the foundation of dynamic data structures in computer science. Unlike static arrays that require contiguous memory allocation and fixed size, linked lists (commonly referred to as "chains") provide a flexible mechanism for storing and managing data elements that can grow or shrink during program execution. This dynamic nature makes chains essential for solving real-world programming problems where the number of elements is not known in advance.

In the context of the University of Delhi's Computer Science curriculum, understanding Lists and Chains is crucial because they serve as the building blocks for more complex data structures like stacks, queues, and trees. The concept of chaining—connecting nodes through pointers—represents a paradigm shift from sequential storage (arrays) to linked storage, enabling efficient insertions and deletions without the overhead of shifting elements. This topic becomes particularly important when implementing polynomial arithmetic, sparse matrices, and memory management systems, all of which are covered in subsequent sections of this module.

The significance of linked lists extends beyond academic requirements. In industry, chains are used in operating systems for process scheduling, in file systems for directory structures, and in web browsers for maintaining history (back/forward navigation). Mastering this topic not only helps in acing DU semester examinations but also builds strong fundamentals for technical interviews at top companies.

## Key Concepts

### Definition and Structure of a Chain

A linked list (or chain) is a linear data structure consisting of nodes, where each node contains two parts: the data and a pointer (or reference) to the next node in the sequence. This pointer-based connection eliminates the need for contiguous memory allocation, allowing the list to grow and shrink dynamically.

The basic structure of a node in a singly linked list is:

```
struct Node {
    int data;
    struct Node* next;
};
```

The list is accessed through a head pointer that points to the first node. If the head pointer is NULL, the list is empty. The last node in the list has its next pointer set to NULL, indicating the end of the chain.

### Types of Linked Lists

**Singly Linked List:** Each node contains data and a pointer to the next node. Traversal is possible only in one direction—from head to tail. This is the simplest form of linked list and is commonly used when only forward traversal is required.

**Doubly Linked List:** Each node contains data, a pointer to the next node, and a pointer to the previous node. This bidirectional traversal allows efficient backward movement and makes deletion operations easier since each node knows its predecessor. The structure is:

```
struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};
```

**Circular Linked List:** In this variant, the last node's next pointer points back to the first node (head), forming a circle. Circular linked lists are useful in round-robin scheduling, multiplayer games, and solving problems involving repetition.

### Dynamic Memory Allocation

Linked lists utilize dynamic memory allocation using functions like malloc() and free() in C. When a new node is required, memory is allocated at runtime:

```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
```

This contrasts with arrays where memory is allocated at compile time. The ability to request memory as needed is what makes linked lists truly dynamic.

### Basic Operations on Chains

**Creation:** Initializing an empty list by setting the head pointer to NULL.

**Insertion:** Three scenarios exist—insertion at the beginning (O(1) time), insertion at the end (O(n) time), and insertion at a specific position. Insertion at the beginning requires updating the head pointer, while insertion at the end requires traversing to find the last node.

**Deletion:** Similar to insertion, deletion can be from the beginning, end, or from a specific position. Deleting the first node requires updating the head pointer to point to the second node. Memory must be freed using free() to prevent memory leaks.

**Traversal:** Visiting each node exactly once to process its data. This requires a while loop that continues until the current pointer becomes NULL.

**Searching:** Linear search operation that compares each node's data with the target value until found or end of list is reached (O(n) time complexity).

**Length Calculation:** Counting the number of nodes by traversing the entire list and maintaining a counter.

### Advantages Over Arrays

Linked lists offer several advantages: dynamic size (can grow/shrink as needed), no memory wastage (memory is allocated exactly for required nodes), and efficient insertions/deletions (no shifting of elements required). However, arrays provide faster random access (O(1) vs O(n)), better cache performance due to locality, and simpler implementation for small, fixed-size collections.

### Representation of Chains in C

The complete implementation of a singly linked list involves:

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert at the beginning
void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Function to insert at the end
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

// Function to delete a node
void deleteNode(struct Node** head, int key) {
    struct Node* temp = *head;
    struct Node* prev = NULL;
    
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) return;
    
    prev->next = temp->next;
    free(temp);
}

// Function to display the list
void display(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

## Examples

### Example 1: Reversing a Linked List

**Problem:** Reverse a singly linked list without using extra arrays.

**Solution:**

```c
struct Node* reverse(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;  // Save next node
        current->next = prev;  // Reverse the link
        prev = current;        // Move prev forward
        current = next;        // Move current forward
    }
    return prev;
}
```

**Step-by-step explanation:**
- Initialize three pointers: prev (NULL), current (head), and next (NULL)
- In each iteration, save the next node before breaking the link
- Reverse the current node's pointer to point to previous node
- Move all three pointers one step forward
- When current becomes NULL, prev points to the new head

**Time Complexity:** O(n), Space Complexity: O(1)

### Example 2: Finding Middle Element

**Problem:** Find the middle node of a linked list in one pass.

**Solution using Slow and Fast Pointers:**

```c
struct Node* findMiddle(struct Node* head) {
    if (head == NULL) return NULL;
    
    struct Node* slow = head;
    struct Node* fast = head;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

**Working:** The slow pointer moves one step at a time while the fast pointer moves two steps. When fast reaches the end, slow will be at the middle. For odd-length lists, slow points to the exact middle. For even-length lists, slow points to the second middle element.

### Example 3: Detecting and Removing Duplicates

**Problem:** Remove duplicates from an unsorted linked list.

**Solution:**

```c
void removeDuplicates(struct Node* head) {
    if (head == NULL) return;
    
    struct Node* current = head;
    struct Node* runner = NULL;
    
    while (current != NULL) {
        runner = current;
        while (runner->next != NULL) {
            if (runner->next->data == current->data) {
                struct Node* duplicate = runner->next;
                runner->next = duplicate->next;
                free(duplicate);
            } else {
                runner = runner->next;
            }
        }
        current = current->next;
    }
}
```

**Step-by-step explanation:**
- For each node, traverse the remaining nodes to find duplicates
- When duplicate is found, remove it by adjusting pointers and freeing memory
- Time Complexity: O(n²) - can be optimized to O(n) using a hash table

## Exam Tips

1. **Understand pointer manipulation:** Most exam questions test your understanding of pointers. Practice drawing node diagrams and tracing pointer changes step-by-step.

2. **Time and space complexity:** Be prepared to analyze the time complexity of each operation. Remember: insertion/deletion at beginning is O(1), at end is O(n), and searching is O(n).

3. **Memory leaks:** Always remember to free() memory after deletion. Exams often ask about memory management in linked lists.

4. **Edge cases:** Handle scenarios like empty list, single node, and operations at both ends carefully. These are common sources of bugs.

5. **Difference between array and linked list:** Know when to use each structure. Arrays offer O(1) random access; linked lists offer O(1) insertion/deletion at the beginning.

6. **Tracing through code:** Practice tracing through linked list code by hand. Questions like "What is the output?" or "Draw the final list" are common.

7. **Recursion in linked lists:** Many problems like reversing, finding length, or searching can be solved recursively. Understand the base case and recursive case clearly.

8. **NULL pointer handling:** Always check for NULL before accessing node->next or node->data. Forgetting this causes segmentation faults.