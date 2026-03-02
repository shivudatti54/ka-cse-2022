# Singly Linked Lists and Chains

## Overview

A Singly Linked List is a data structure where each node contains data and a pointer to the next node, allowing traversal in only one direction. It supports various operations like insertion, deletion, and searching. Understanding its structure and operations is crucial for efficient programming.

## Key Points

- Singly linked lists support forward traversal only.
- Insertion and deletion at the head are O(1) operations.
- Operations at the end of the list require traversal, making them O(n).
- Always handle edge cases like empty lists and single nodes.
- Freeing memory when deleting nodes is essential in languages like C/C++.
- The two-pointer technique is useful for solving many linked list problems.
- Maintaining a tail pointer can optimize insertion at the end to O(1).

## Important Definitions

- **Node**: A basic element of a linked list, containing data and a pointer to the next node.
- **Head**: The first node of a linked list.
- **Tail**: The last node of a linked list.
- **Traversal**: The process of visiting each node in a linked list.

## Key Formulas / Syntax

- Basic Node Structure: `struct Node { int data; struct Node *next; };`
- Insertion at Beginning: `newNode->next = *head; *head = newNode;`
- Deletion from Beginning: `*head = (*head)->next; free(temp);`

## Comparisons

| Operation        | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Insert at Head   | O(1)            | O(1)             |
| Insert at End    | O(n)            | O(1)             |
| Delete from Head | O(1)            | O(1)             |
| Delete from End  | O(n)            | O(1)             |

## Exam Tips

- Focus on understanding the basic operations and their time complexities.
- Practice handling edge cases like empty lists and single nodes.
- Be familiar with the two-pointer technique and its applications.
- Understand how to optimize insertion at the end using a tail pointer.
- Always consider memory management when dealing with dynamic memory allocation.
