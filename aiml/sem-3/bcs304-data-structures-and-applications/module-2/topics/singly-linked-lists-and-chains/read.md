# Singly Linked Lists and Chains


## Table of Contents

- [Singly Linked Lists and Chains](#singly-linked-lists-and-chains)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Formal Definition](#formal-definition)
  - [Node Structure in C](#node-structure-in-c)
  - [Insertion Operations](#insertion-operations)
  - [Deletion Operations](#deletion-operations)
  - [Traversal Operation](#traversal-operation)
  - [Search Operation](#search-operation)
  - [List Reversal](#list-reversal)
  - [Merge Two Sorted Lists](#merge-two-sorted-lists)
- [Relationship to Queue Implementation](#relationship-to-queue-implementation)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

A **singly linked list** (also called a **chain**) is a fundamental linear data structure consisting of nodes where each node contains a data element and a pointer (link) to the next node in the sequence. The first node is called the **head** (or front), and the last node points to **NULL** to indicate the end of the list. This structure is particularly crucial in the context of queues because it provides an elegant solution for implementing dynamic queues where the size can grow and shrink arbitrarily during program execution.

In the broader context of the Queues module, linked lists serve as the underlying structure for implementing **linked queues** - a variant of queues that uses dynamic memory allocation. Unlike array-based queues that suffer from fixed capacity limitations or the "wraparound" complexity of circular queues, linked queues can efficiently enqueue elements without any capacity restrictions. The ability to add elements at the rear and remove from the front in O(1) time makes singly linked lists ideal for this purpose. Furthermore, understanding chains is prerequisite to studying **linked stacks and queues** as indicated in the module's sibling topics.

## Key Concepts

### Formal Definition

A singly linked list (chain) is defined as a sequence of nodes L = {n₁, n₂, ..., nₖ} where each node nᵢ contains:

- **Data field**: An element of type T, denoted as nᵢ.data
- **Link field**: A pointer to the next node, denoted as nᵢ.link

The list is characterized by a **head pointer** that references the first node n₁, and the link field of the last node nₖ contains NULL (or nullptr in C++).

### Node Structure in C

```c
typedef struct Node {
    int data;
    struct Node* next;
} Node;
```

### Insertion Operations

**1. Insert at Beginning (Push Front)**

- Create a new node with the given data
- Set new node's next pointer to current head
- Update head pointer to new node
- **Time Complexity**: O(1) - constant time regardless of list size
- **Space Complexity**: O(1)

```c
Node* insertAtBeginning(Node* head, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = head;
    return newNode;  // Returns new head
}
```

**2. Insert at End (Push Back)**

- Traverse to the last node (or handle empty list case)
- Create new node and attach after last node
- **Time Complexity**: O(n) - requires traversal
- **Space Complexity**: O(1)

**3. Insert at Position**

- Traverse to the (k-1)th position
- Adjust pointers to insert new node
- **Time Complexity**: O(n) worst case, O(1) if position is known

### Deletion Operations

**1. Delete from Beginning**

- Store current head in temporary pointer
- Move head to next node
- Free the old head memory
- **Time Complexity**: O(1)

```c
Node* deleteFromBeginning(Node* head) {
    if (head == NULL) return NULL;
    Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}
```

**2. Delete from End**

- Traverse to find second-to-last node
- Free the last node
- Set second-to-last node's next to NULL
- **Time Complexity**: O(n)

**3. Delete by Value**
This operation removes the first occurrence of a specified value from the list:

```c
Node* deleteByValue(Node* head, int value) {
    if (head == NULL) return NULL;

    // Case 1: Delete at head
    if (head->data == value) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    // Case 2: Search and delete elsewhere
    Node* current = head;
    while (current->next != NULL && current->next->data != value) {
        current = current->next;
    }

    // If value found
    if (current->next != NULL) {
        Node* temp = current->next;
        current->next = temp->next;
        free(temp);
    }

    return head;
}
```

### Traversal Operation

Traversing a linked list visits each node exactly once, performing an operation (such as printing):

```c
void traverse(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
```

**Time Complexity**: O(n) - must visit every node

### Search Operation

```c
int search(Node* head, int key) {
    int position = 0;
    Node* current = head;
    while (current != NULL) {
        if (current->data == key) {
            return position;  // Found at position
        }
        current = current->next;
        position++;
    }
    return -1;  // Not found
}
```

**Time Complexity**: O(n) worst case, O(1) best case (found at head)

### List Reversal

Reversing a singly linked list inverts the direction of all pointers:

```c
Node* reverse(Node* head) {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;

    while (current != NULL) {
        next = current->next;  // Save next node
        current->next = prev;  // Reverse the link
        prev = current;        // Move prev forward
        current = next;        // Move current forward
    }
    return prev;  // New head
}
```

**Proof of Correctness**: The algorithm uses three pointers to reverse each link. After processing all nodes, `prev` points to the original last node (now the new head), and all links point to the previous node. Time complexity: O(n), Space complexity: O(1).

### Merge Two Sorted Lists

```c
Node* mergeSortedLists(Node* l1, Node* l2) {
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;

    Node* result = NULL;

    if (l1->data <= l2->data) {
        result = l1;
        result->next = mergeSortedLists(l1->next, l2);
    } else {
        result = l2;
        result->next = mergeSortedLists(l1, l2->next);
    }
    return result;
}
```

**Time Complexity**: O(m + n) where m and n are list lengths

## Relationship to Queue Implementation

The connection between singly linked lists and queues is fundamental. A **linked queue** uses a singly linked list with two pointers:

- **front pointer**: Points to the node for dequeue operations
- **rear pointer**: Points to the node for enqueue operations

This implementation provides O(1) time complexity for both enqueue and dequeue operations, unlike array-based queues that require O(n) for front element removal or complex wraparound logic in circular arrays. The singly linked list structure naturally supports FIFO (First-In-First-Out) access patterns required by queues.

## Examples

**Example 1: Building a List and Performing Operations**

Consider building a list by inserting elements 10, 20, 30 at the beginning:

```
After insertAtBeginning(10):  HEAD → [10|NULL]
After insertAtBeginning(20):  HEAD → [20]→[10|NULL]
After insertAtBeginning(30):  HEAD → [30]→[20]→[10|NULL]
```

Now delete value 20:

```
HEAD → [30]→[20]→[10|NULL]
         ↑
    current here, current->next.data == 20
After deletion: HEAD → [30]→[10|NULL]
```

**Example 2: Reversal Step-by-Step**

Initial: HEAD → [A]→[B]→[C]→[NULL]

| Step | prev | current | next | Action               |
| ---- | ---- | ------- | ---- | -------------------- |
| 0    | NULL | A       | B    | current->next = NULL |
| 1    | A    | B       | C    | current->next = A    |
| 2    | B    | C       | NULL | current->next = B    |
| 3    | C    | NULL    | -    | Loop exits           |

Final: HEAD → [C]→[B]→[A]→[NULL]

## Exam Tips

1. **Complexities**: Remember - insertion/deletion at head is O(1); operations at tail or middle are O(n). Search is always O(n).

2. **Memory Leaks**: Always free() nodes after deletion. In exam questions, mention the need for proper deallocation when asked about memory management.

3. **Pointer Manipulation**: For reversing a list, always draw the diagram. The key invariant is: after processing k nodes, `prev` points to the reversed portion.

4. **Queue Connection**: Understand that linked queues require maintaining both front and rear pointers to achieve O(1) enqueue/dequeue.

5. **Cycle Detection**: In practice, linked lists can form cycles. For singly linked lists, Floyd's tortoise-and-hare algorithm detects cycles in O(n) time and O(1) space.

6. **Edge Cases**: Always consider empty list, single node, and operations at boundaries when analyzing algorithms.

7. **Proof by Induction**: For linked list algorithms, use induction - prove base case (empty/single node) and inductive step (if it works for k nodes, it works for k+1).
