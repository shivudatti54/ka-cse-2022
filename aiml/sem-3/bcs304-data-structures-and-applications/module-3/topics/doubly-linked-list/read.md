# Doubly Linked List


## Table of Contents

- [Doubly Linked List](#doubly-linked-list)
- [1. Introduction and Formal Definition](#1-introduction-and-formal-definition)
- [2. Node Structure Representation](#2-node-structure-representation)
- [3. Theoretical Analysis: Advantages Over Singly Linked List](#3-theoretical-analysis-advantages-over-singly-linked-list)
  - [Theorem: Deletion Given Node Pointer](#theorem-deletion-given-node-pointer)
  - [Comparative Complexity Analysis](#comparative-complexity-analysis)
- [4. Implementation of Core Operations](#4-implementation-of-core-operations)
  - [4.1 Node Creation - O(1)](#41-node-creation---o1)
  - [4.2 Insertion at Beginning - O(1)](#42-insertion-at-beginning---o1)
  - [4.3 Insertion at End - O(1) with Tail Pointer](#43-insertion-at-end---o1-with-tail-pointer)
  - [4.4 Insertion at Specific Position - O(n)](#44-insertion-at-specific-position---on)
  - [4.5 Deletion from Beginning - O(1)](#45-deletion-from-beginning---o1)
  - [4.6 Deletion from End - O(1) with Tail Pointer](#46-deletion-from-end---o1-with-tail-pointer)
  - [4.7 Deletion at Position - O(n)](#47-deletion-at-position---on)
  - [4.8 Delete Given Node - O(1) [Key Advantage]](#48-delete-given-node---o1-key-advantage)
  - [4.9 Search Operation - O(n)](#49-search-operation---on)
  - [4.10 Forward Traversal - O(n)](#410-forward-traversal---on)
  - [4.11 Reverse Traversal - O(n)](#411-reverse-traversal---on)
  - [4.12 Reversing the List - O(n)](#412-reversing-the-list---on)
- [5. Circular Doubly Linked List](#5-circular-doubly-linked-list)
- [6. Practical Applications](#6-practical-applications)
- [7. Comprehensive Complexity Analysis](#7-comprehensive-complexity-analysis)
- [8. Assessment](#8-assessment)
  - [Multiple Choice Questions](#multiple-choice-questions)

## 1. Introduction and Formal Definition

A **Doubly Linked List (DLL)** is a linear data structure consisting of a collection of nodes, where each node contains three components:

1. **Data Field** — The information or value stored in the node
2. **Forward Pointer (next)** — A reference to the successor node in the sequence
3. **Backward Pointer (prev)** — A reference to the predecessor node in the sequence

This bidirectional linking enables traversal in both forward and backward directions, providing significant algorithmic advantages over singly linked lists at the cost of additional memory overhead.

**Formal Definition:**

Let a DLL be represented as a sequence of nodes N₀, N₁, N₂, ..., Nₙ₋₁ where:

- For each node Nᵢ (where 0 < i < n-1): Nᵢ.next = Nᵢ₊₁ and Nᵢ.prev = Nᵢ₋₁
- The head node N₀ satisfies: N₀.prev = NULL
- The tail node Nₙ₋₁ satisfies: Nₙ₋₁.next = NULL

## 2. Node Structure Representation

```c
struct Node {
    int data;              // Data element
    struct Node *next;    // Pointer to successor node
    struct Node *prev;    // Pointer to predecessor node
};
```

**Memory Layout Visualization:**

```
Address:    0x100       0x108       0x110       0x118       0x120
           ┌─────────┬─────────┬─────────┐
           │  NULL   │   10    │  0x120  │ ◄── Node 0 (HEAD)
           └─────────┴─────────┴─────────┘
                        ▲
                        │ prev
           ┌────────────┼────────────┐
           │            ▼            │
           │  ┌─────────┬─────────┐  │
           │  │  0x100  │   20    │  │
           │  │         │  0x130  │  │
           │  └─────────┴─────────┘  │
           │           ▲             │
           │           │ prev        │
           │  ┌────────┴─────────┐   │
           │  │                   ▼   │
           │  │  ┌─────────┬─────────┐  │
           │  │  │  0x108  │   30    │  │
           │  │  │  NULL   │         │  │
           │  │  └─────────┴─────────┘  │
           │  │          Node 2 (TAIL)  │
           │  └─────────────────────────┘
```

## 3. Theoretical Analysis: Advantages Over Singly Linked List

### Theorem: Deletion Given Node Pointer

**Statement:** Deletion of a node in a doubly linked list, when a pointer to that node is provided, executes in O(1) time complexity.

**Proof:**
Given a pointer `P` to node N in a doubly linked list, the deletion requires only constant-time pointer updates:

1. Update N.prev.next → N.next (O(1))
2. Update N.next.prev → N.prev (O(1))
3. Free(N) (O(1))

Total: 3 constant-time operations = O(1)

In contrast, a singly linked list requires O(n) traversal to find the predecessor node since only forward pointers exist.

### Comparative Complexity Analysis

| Operation           | Singly Linked List | Doubly Linked List   | Reasoning                       |
| ------------------- | ------------------ | -------------------- | ------------------------------- |
| Traversal Direction | Forward only       | Bidirectional        | DLL has prev pointers           |
| Insert before node  | O(n)               | O(1)                 | Direct access to predecessor    |
| Delete given node   | O(n)               | O(1)                 | Predecessor accessible via prev |
| Delete from end     | O(n)               | O(1)\*               | \*Requires tail pointer         |
| Memory per node     | O(1)               | O(1) + extra pointer | 50% more memory overhead        |

**Space Complexity:**

- Per node: O(1) additional memory (one extra pointer compared to SLL)
- Total list: O(n) where n is the number of nodes

## 4. Implementation of Core Operations

### 4.1 Node Creation - O(1)

```c
struct Node* createNode(int data) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}
```

### 4.2 Insertion at Beginning - O(1)

```c
void insertAtBeginning(struct Node **head, struct Node **tail, int data) {
    struct Node *newNode = createNode(data);

    if (*head == NULL) {
        *head = *tail = newNode;
        return;
    }

    newNode->next = *head;
    (*head)->prev = newNode;
    *head = newNode;
}
```

**Proof of Correctness:** The algorithm maintains the invariant that all existing nodes remain linked via their next and prev pointers while establishing the new node as the head. The new head's prev is implicitly NULL, and the previous head's prev now correctly points to the new head.

### 4.3 Insertion at End - O(1) with Tail Pointer

```c
void insertAtEnd(struct Node **head, struct Node **tail, int data) {
    struct Node *newNode = createNode(data);

    if (*head == NULL) {
        *head = *tail = newNode;
        return;
    }

    newNode->prev = *tail;
    (*tail)->next = newNode;
    *tail = newNode;
}
```

**Without tail pointer:** Time complexity degrades to O(n) as traversal to the last node is required.

### 4.4 Insertion at Specific Position - O(n)

```c
void insertAtPosition(struct Node **head, struct Node **tail, int data, int position) {
    if (position == 0) {
        insertAtBeginning(head, tail, data);
        return;
    }

    struct Node *newNode = createNode(data);
    struct Node *temp = *head;

    // Traverse to position - 1
    for (int i = 0; i < position - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Position %d out of bounds\n", position);
        free(newNode);
        return;
    }

    // Insert between temp and temp->next
    newNode->next = temp->next;
    newNode->prev = temp;

    if (temp->next != NULL) {
        temp->next->prev = newNode;
    } else {
        // Inserting at tail
        *tail = newNode;
    }
    temp->next = newNode;
}
```

### 4.5 Deletion from Beginning - O(1)

```c
void deleteFromBeginning(struct Node **head, struct Node **tail) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = *head;
    *head = (*head)->next;

    if (*head != NULL) {
        (*head)->prev = NULL;
    } else {
        // List becomes empty
        *tail = NULL;
    }
    free(temp);
}
```

### 4.6 Deletion from End - O(1) with Tail Pointer

```c
void deleteFromEnd(struct Node **head, struct Node **tail) {
    if (*tail == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = *tail;
    *tail = (*tail)->prev;

    if (*tail != NULL) {
        (*tail)->next = NULL;
    } else {
        *head = NULL; // List became empty
    }
    free(temp);
}
```

### 4.7 Deletion at Position - O(n)

```c
void deleteAtPosition(struct Node **head, struct Node **tail, int position) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }

    if (position == 0) {
        deleteFromBeginning(head, tail);
        return;
    }

    struct Node *temp = *head;
    for (int i = 0; i < position && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Position out of bounds\n");
        return;
    }

    // Update predecessor's next
    if (temp->prev != NULL) {
        temp->prev->next = temp->next;
    }

    // Update successor's prev
    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    } else {
        // Deleting tail
        *tail = temp->prev;
    }

    free(temp);
}
```

### 4.8 Delete Given Node - O(1) [Key Advantage]

```c
void deleteNode(struct Node **head, struct Node **tail, struct Node *node) {
    if (node == NULL) return;

    // Update head if deleting first node
    if (node == *head) {
        *head = node->next;
    }

    // Update tail if deleting last node
    if (node == *tail) {
        *tail = node->prev;
    }

    // Bypass the node in the linked structure
    if (node->prev != NULL) {
        node->prev->next = node->next;
    }
    if (node->next != NULL) {
        node->next->prev = node->prev;
    }

    free(node);
}
```

### 4.9 Search Operation - O(n)

```c
struct Node* search(struct Node *head, int key) {
    struct Node *current = head;
    while (current != NULL) {
        if (current->data == key) {
            return current;  // Found
        }
        current = current->next;
    }
    return NULL;  // Not found
}
```

### 4.10 Forward Traversal - O(n)

```c
void printForward(struct Node *head) {
    printf("Forward: ");
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d <-> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

### 4.11 Reverse Traversal - O(n)

```c
void printReverse(struct Node *tail) {
    printf("Reverse: ");
    struct Node *temp = tail;
    while (temp != NULL) {
        printf("%d <-> ", temp->data);
        temp = temp->prev;
    }
    printf("NULL\n");
}
```

### 4.12 Reversing the List - O(n)

```c
void reverseList(struct Node **head, struct Node **tail) {
    struct Node *current = *head;
    struct Node *temp = NULL;

    // Swap prev and next pointers for all nodes
    while (current != NULL) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;  // Move to next (originally prev)
    }

    // Swap head and tail pointers
    if (temp != NULL) {
        temp = *head;
        *head = *tail;
        *tail = temp;
    }
}
```

## 5. Circular Doubly Linked List

A **Circular Doubly Linked List** connects the tail's next to the head and head's prev to the tail, forming a circular structure.

**Structure:**

```
┌─────────────────────────────────┐
│                                 │
│    ┌──────┐    ┌──────┐         │
│    │  10  │ ⇄  │  20  │ ⇄ ...   │
│    └──────┘    └──────┘         │
│      ▲                        │
│      │                        │
│      └────────────────────────┘
```

**Advantages:** Eliminates NULL checks for traversal, useful for round-robin scheduling.

## 6. Practical Applications

1. **Browser History Navigation** — Forward and backward navigation in web browsers
2. **Music Player Playlists** — Next and previous track functionality
3. **Undo/Redo Operations** — Text editors maintaining operation history
4. **LRU Cache Implementation** — Efficient insertion and deletion at both ends
5. **Deque (Double-Ended Queue)** — O(1) operations at both ends
6. **Polynomial Representation** — Sparse polynomials using doubly linked structures
7. **Operating System Process Scheduling** — Circular ready queue management

## 7. Comprehensive Complexity Analysis

| Operation             | Time Complexity   | Space Complexity | Notes               |
| --------------------- | ----------------- | ---------------- | ------------------- |
| Insert at beginning   | O(1)              | O(1)             |                     |
| Insert at end         | O(1)\* / O(n)\*\* | O(1)             | \*With tail pointer |
| Insert at position    | O(n)              | O(1)             |                     |
| Delete from beginning | O(1)              | O(1)             |                     |
| Delete from end       | O(1)\* / O(n)\*\* | O(1)             | \*With tail pointer |
| Delete at position    | O(n)              | O(1)             |                     |
| Delete given node     | O(1)              | O(1)             | Major advantage     |
| Search                | O(n)              | O(1)             |                     |
| Reverse traversal     | O(n)              | O(1)             | O(n)\* in SLL       |
| Reverse list          | O(n)              | O(1)             |                     |

_Total space: O(n)_

## 8. Assessment

### Multiple Choice Questions

**Question 1:** In a doubly linked list with head pointer 'head' and tail pointer 'tail', what is the time complexity of deleting a node when a pointer to that node is provided?

(A) O(n)  
(B) O(1)  
(C) O(log n)  
(D) O(n²)

**Answer:** (B) O(1)

**Explanation:** The doubly linked list maintains a prev pointer to the predecessor, allowing direct access without traversal. Deletion requires updating only three pointers (prev->next, next->prev, and free), each in constant time.

---

**Question 2:** Consider inserting elements [10, 20, 30, 40] at the beginning of an empty doubly linked list. After performing deleteFromEnd twice, then inserting 50 at the beginning, what will be the forward traversal output?

(A) 10 <-> 20 <-> NULL  
(B) 50 <-> 10 <-> NULL  
(C) 50 <-> 10 <-> 20 <-> NULL  
(D) 50 <-> 30 <-> NULL

**Answer:** (B) 50 <-> 10 <-> NULL

**Explanation:**

- Insert 10: 10
- Insert 20: 20 <-> 10
- Insert 30: 30 <-> 20 <-> 10
- Insert 40: 40 <-> 30 <-> 20 <-> 10
- Delete from end twice: 40 <-> 30
- Insert 50 at beginning: 50 <-> 40 <-> 30

After second deletion: 40 <-> 30. After inserting 50 at beginning: 50 <-> 40 <-> 30.

Wait, let's recalculate: After insert [10,20,30,40] at beginning → 40↔30↔20↔10. Delete from end twice → 40↔30. Insert 50 at beginning → 50↔40↔30. Forward traversal: 50, 40, 30.

**Correction:** (B) 50 <-> 40 <-> 30 <-> NULL

---

**Question 3:** What is the primary advantage of using a circular doubly linked list over a linear doubly linked list?

(A) Lower memory consumption  
(B) O(1) insertion at both ends without special cases  
(C) Faster search operations  
(D) Automatic sorting of elements

**Answer:** (B) O(1) insertion at both ends without special cases

**Explanation:** In a circular DLL, both head and tail are directly accessible, and the structure naturally wraps around, eliminating boundary conditions (NULL checks) during circular traversal. This simplifies implementation and ensures O(1) operations at both ends.

---

**Question 4:** A doubly linked list stores integers. The list currently contains: HEAD ↔ 5 ↔ 10 ↔ 15 ↔ 20 ↔ TAIL. If we call deleteNode() on the node containing 15, how many pointer updates occur?

(A) 2  
(B) 3  
(C) 4  
(D) 5

**Answer:** (C) 4

**Explanation:** Deleting node 15 requires updating:

1. 10->next = 20 (node before 15)
2. 20->prev = 10 (node after 15)
3. Setting deleted node's pointers to NULL before free (optional but recommended)
4. Updating head/tail if necessary (not in this case)

The critical pointer updates are 10->next and 20->prev, totaling 2 direct updates. In practice, boundary checks and nullifications bring the total operations to approximately 4.

---

**Question 5:** In a doubly linked list implementation of a browser's back-forward navigation, which data structure operation is analogous to clicking the "Back" button?

(A) Traversal using next pointer  
(B) Traversal using prev pointer  
(C) Insertion at head  
(D) Deletion at tail

**Answer:** (B) Traversal using prev pointer

**Explanation:** Browser history maintains a doubly linked list where the current page is the head. Clicking "Back" moves to the previous node via the prev pointer, while "Forward" uses the next pointer.
