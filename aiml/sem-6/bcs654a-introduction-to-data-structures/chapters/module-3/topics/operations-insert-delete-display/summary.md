# Operations: Insert-Delete-Display

### Introduction

- Linked lists are a linear collection of data elements whose order is not given by their physical placement in memory.
- Operations on linked lists include:
  - Insertion
  - Deletion
  - Display/Traversal

### Insertion

- Insertion at the beginning: `head = new Node(data, head)`
- Insertion at the end: `Node current = head; while (current.next != null) current = current.next; current.next = new Node(data, null)`
- Insertion at a specific position: `Node current = head; i = 0; while (current != null && i < pos - 1) current = current.next; current.next = new Node(data, current.next)`

### Deletion

- Deletion at the beginning: `head = head.next`
- Deletion at the end: `current = head; while (current.next != null) current = current.next; current.next = null`
- Deletion at a specific position: `Node current = head; i = 0; while (current != null && i < pos - 1) current = current.next; current.next = current.next.next`

### Display/Traversal

- In-order traversal: `current = head; while (current != null) { print(current.data); current = current.next }`
- Reverse in-order traversal: `current = tail; while (current != null) { print(current.data); current = current.prev }`

### Important Formulas and Definitions

- Definition: A linked list is a linear collection of data elements whose order is not given by their physical placement in memory.
- Formula for the length of a linked list: `length = 0; current = head; while (current != null) length++;`

### Theorems

- There is no specific theorem for linked lists, but the following theorem is relevant to data structures:
  - The time complexity of insertion and deletion operations in a linked list is O(n), where n is the number of elements in the list.
