# Doubly Linked List

## Overview

A doubly linked list is a linked list where each node contains data, a pointer to the next node, and a pointer to the previous node, allowing bidirectional traversal. This data structure is useful when frequent insertions and deletions are needed at arbitrary positions.

## Key Points

- Each node has three components: data, next pointer, and previous pointer.
- Bidirectional traversal is possible, allowing efficient insertion and deletion at any position.
- Doubly linked lists have advantages over singly linked lists in terms of insertion and deletion operations.
- A tail pointer can be used to improve the efficiency of insertion and deletion at the end of the list.
- Doubly linked lists require more memory than singly linked lists due to the extra pointer.

## Important Definitions

- **Node**: A single element in the doubly linked list, containing data and pointers to the next and previous nodes.
- **Head**: The first node in the doubly linked list.
- **Tail**: The last node in the doubly linked list.
- **Bidirectional Traversal**: The ability to traverse the list in both forward and backward directions.

## Key Formulas / Syntax

- `struct Node { int data; struct Node *next; struct Node *prev; };`
- `void insertAtBeginning(struct Node **head, int data) { ... }`
- `void deleteNode(struct Node **head, struct Node **tail, struct Node *node) { ... }`

## Comparisons

| Feature                     | Singly Linked List | Doubly Linked List   |
| --------------------------- | ------------------ | -------------------- |
| Traversal                   | Forward only       | Both directions      |
| Delete node (given pointer) | O(n)               | O(1)                 |
| Insert before node          | O(n)               | O(1)                 |
| Delete from end             | O(n)               | O(1)\*               |
| Memory per node             | Less               | More (extra pointer) |

## Exam Tips

- Focus on the advantages and disadvantages of doubly linked lists compared to singly linked lists.
- Understand the time and space complexities of various operations in doubly linked lists.
- Practice implementing insertion, deletion, and traversal operations in doubly linked lists.
