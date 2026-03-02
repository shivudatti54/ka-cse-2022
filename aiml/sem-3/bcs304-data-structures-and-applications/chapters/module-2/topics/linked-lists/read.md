# LINKED LISTS

## Introduction

Linked Lists represent one of the most fundamental and versatile data structures in computer science, forming the backbone of dynamic memory management and flexible data storage. Unlike static arrays that allocate contiguous memory blocks, linked lists store elements in nodes that are scattered across memory, connected through pointers or references. This fundamental difference gives linked lists their distinctive advantage: the ability to efficiently insert and delete elements at any position without requiring memory reallocation or data movement.

In the context of the University of Delhi Computer Science curriculum, linked lists serve as a prerequisite understanding for more complex data structures like stacks, queues, trees, and graphs. The dynamic nature of linked lists makes them indispensable in scenarios where the size of data is unknown beforehand or changes frequently. Applications range from operating system memory management (free/busy memory lists) to implementing undo functionality in text editors, maintaining playlists in media players, and representing sparse polynomials in mathematical computations.

The study of linked lists also introduces students to critical concepts in memory management, pointer manipulation, and algorithmic thinking. Understanding how to traverse, search, insert, and delete nodes in a linked list develops skills that are directly applicable to advanced data structures and algorithm design. Given that internal assessments and end-semester examinations at DU frequently include questions on linked list operations, a thorough grasp of this topic is essential for academic success.

## Key Concepts

### Structure of a Linked List Node

A linked list consists of nodes, where each node contains two components: the data field (storing the actual information) and the link field (storing the memory address of the next node). In C programming, this is typically implemented using structures:

```c
struct Node {
    int data;
    struct Node* next;
};
```

The list maintains a pointer to the first node, called the head or start pointer. The last node's link field contains NULL (or nil in some languages) to indicate the end of the list.

### Types of Linked Lists

**Singly Linked List (Linear Linked List):** In this simplest form, each node contains data and a single pointer to the next node. Traversal is possible only in one direction—from the head towards the end. The time complexity for insertion at the beginning is O(1), while insertion at the end requires traversal, making it O(n) without additional tail pointer.

**Doubly Linked List:** Each node contains three fields: data, a pointer to the next node, and a pointer to the previous node. This bidirectional traversal capability allows efficient backward movement, making deletion of previous nodes O(1) instead of O(n). However, it requires additional memory for the extra pointer and more complex pointer manipulation during insertions and deletions.

**Circular Linked List:** In this variant, the last node points back to the first node, forming a circle. A circular singly linked list has the last node's next pointer pointing to the head, while a circular doubly linked list has both ends connected. These structures are particularly useful in round-robin scheduling, circular buffer implementations, and problems requiring continuous rotation through elements.

### Fundamental Operations

**Creation:** Memory is dynamically allocated for each node using malloc() in C. The data field is initialized, and the next pointer is set to NULL (for the last node) or to the next node's address.

**Traversal:** Starting from the head, each node is visited by following next pointers until NULL is encountered. This operation requires O(n) time complexity.

**Insertion:** Can be performed at three positions—beginning, end, or middle (after a given node). Insertion at the beginning requires updating the head pointer; insertion in the middle requires updating two pointers (the previous node's next and the new node's next); insertion at the end requires traversing to the last node unless a tail pointer is maintained.

**Deletion:** Similar to insertion, deletion can occur at the beginning (head update), end (traversal to second-last node), or middle (updating the previous node's next pointer). The freed node's memory should be released using free() to prevent memory leaks.

**Searching:** Linear search traverses the list comparing each element with the target value, requiring O(n) time in the worst case.

**Reversing:** A linked list can be reversed by manipulating pointers without allocating new nodes. The algorithm uses three pointers (previous, current, and next) to reverse the direction of each link.

## Examples

### Example 1: Inserting a Node at the Beginning

Consider a linked list with head pointing to a node containing 10, which points to a node containing 20 (NULL at end). We want to insert a new node with value 5 at the beginning.

**Step-by-step solution:**

Step 1: Create a new node
```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = 5;
```

Step 2: Make the new node point to the current head
```c
newNode->next = head;
```

Step 3: Update the head pointer to point to the new node
```c
head = newNode;
```

**Result:** The list now contains 5 → 10 → 20 → NULL

This operation takes constant time O(1) regardless of list size because we only manipulate two pointers.

### Example 2: Deleting a Node from the Middle

Given a linked list: HEAD → 15 → 25 → 35 → 45 → NULL, delete the node containing 35.

**Step-by-step solution:**

Step 1: Traverse to find the node to delete and its predecessor
- Start at head (15)
- Move to next (25)
- Move to next (35) - this is the target
- Previous node is 25

Step 2: Update the predecessor's next pointer to skip the node being deleted
```c
prev->next = curr->next;  // 25->next = 45
```

Step 3: Free the memory of the deleted node
```c
free(curr);
```

**Result:** The list becomes HEAD → 15 → 25 → 45 → NULL

### Example 3: Reversing a Linked List

Reverse the linked list: HEAD → 5 → 10 → 15 → NULL

**Algorithm using three pointers:**

```c
struct Node *prev = NULL, *curr = head, *next = NULL;

while (curr != NULL) {
    next = curr->next;   // Save next node
    curr->next = prev;   // Reverse the link
    prev = curr;         // Move prev forward
    curr = next;         // Move curr forward
}
head = prev;
```

**Step-by-step execution:**

| Iteration | prev | curr | next | List State |
|-----------|------|------|------|------------|
| Initial   | NULL | 5    | 10   | 5→10→15→NULL |
| 1         | NULL | 5    | 10   | NULL←5 10→15 |
| 2         | 5    | 10   | 15   | NULL←5←10 15 |
| 3         | 10   | 15   | NULL | NULL←5←10←15 |
| End       | 15   | NULL | NULL | NULL←5←10←15 |

**Result:** HEAD → 15 → 10 → 5 → NULL

## Exam Tips

1. **Draw diagrams for pointer manipulations**: In DU examinations, visual representation of linked lists with boxes and arrows helps demonstrate understanding and avoids conceptual errors in pointer-related questions.

2. **Remember time complexities**: Insertion/deletion at beginning is O(1), at end is O(n) without tail pointer, and searching is always O(n). Doubly linked list deletion of previous node is O(1) while singly requires O(n).

3. **Memory management matters**: Always emphasize the use of malloc() for allocation and free() for deallocation. Questions on memory leaks and dangling pointers frequently appear in practical examinations.

4. **Distinguish between head and tail**: Many students confuse head (first node) with tail (last node). Remember that head never changes when inserting at the beginning, but tail changes when inserting at the end.

5. **NULL pointer handling**: Always check for NULL before accessing node->next. Failing to handle NULL results in segmentation faults, a common error in practical exams.

6. **Circular list termination**: In circular linked lists, traversal never naturally terminates. Use a condition that checks if we've returned to the head node or maintain a counter.

7. **Doubly linked list insertion**: When solving insertion in doubly linked lists, remember to update four pointers: new node's next and previous, and the adjacent nodes' next and previous pointers.