# Operations: Insert-Delete-Display

## Introduction

This section introduces three essential operations on linked lists: Insert, Delete, and Display.

### Key Points

- **Insert Operation:**
  - Insertion at the beginning: `head = insert(head, value) => head = new Node(value, head)`
  - Insertion at the end: `head = insert(head, value) => lastNode.next = new Node(value, null)`
  - Insertion at a specific position: `head = insert(head, value, pos) => if pos == 0, head = new Node(value, head); else { prev = head; for (i = 0; i < pos - 1; i++) prev = prev.next; prev.next = new Node(value, prev.next); }`
- **Delete Operation:**
  - Deletion at the beginning: `head = delete(head) => newNode = head.next; head = newNode`
  - Deletion at the end: `head = delete(head) => if head.next == null, head = null; else { prev = head; while prev.next != null && prev.next.next != null, prev = prev.next; prev.next = prev.next.next; }`
  - Deletion at a specific position: `head = delete(head, pos) => if pos == 0, head = head.next; else { prev = head; for (i = 0; i < pos - 1; i++) prev = prev.next; prev.next = prev.next.next; }`
- **Display Operation:**
  - Traverse the linked list and print each node's data.

### Important Formulas and Definitions

- Definition: A linked list is a type of data structure consisting of a collection of nodes, each containing a value and a reference (or link) to the next node in the sequence.
- Time complexity:
  - Insert: O(1) for insertion at the beginning, O(n) for insertion at the end, O(n) for insertion at a specific position
  - Delete: O(1) for deletion at the beginning, O(n) for deletion at the end, O(n) for deletion at a specific position
  - Display: O(n)

### Theorems

- There is no specific theorem related to these operations, but it's essential to understand the time and space complexities of each operation to analyze the efficiency of linked lists.
