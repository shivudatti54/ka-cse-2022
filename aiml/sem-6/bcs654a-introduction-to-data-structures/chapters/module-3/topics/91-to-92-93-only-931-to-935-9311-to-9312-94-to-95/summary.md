# 9.1 to 9.2, 9.3, and 9.4 to 9.5 Revision Notes

## Introduction

- A linked list is a linear collection of data elements, where each element points to the next element.
- Linked lists can be traversed in a linear fashion.

### 9.1

- Definition: A linked list is a dynamic collection of elements, each of which is a separate object.
- Operations:
  - Insertion: O(1) at the beginning and O(n) at the end
  - Deletion: O(1) at the beginning and O(n) at the end
  - Search: O(n)

### 9.2

- Types of Linked Lists:
  - Singly Linked List: Each node has only one link to the next node.
  - Doubly Linked List: Each node has both links to the next and previous nodes.

### 9.3

- Operations on Linked Lists:
  - **9.3.1**: Finding the middle element of a linked list
    - Formula: `mid = (head + tail) / 2`
  - **9.3.2**: Printing a linked list
    - Formula: `print(node.value) while node != null`
  - **9.3.3**: Merging two linked lists
    - Formula: `temp = head1 = head2 = null; while head1 != null || head2 != null, { temp = head1; head1 = head1.next; temp = head2; head2 = head2.next; temp.next = head1; head1 = head2; }`
  - **9.3.4**: Checking if a linked list is empty
    - Formula: `if node == null, return true; return false`
  - **9.3.5**: Counting the number of nodes in a linked list
    - Formula: `count = 0; node = head; while node != null, { count++; node = node.next; } return count`
  - **9.3.11**: Finding the node with a given value
    - Formula: `node = head; while node != null, { if node.value == target, return node; node = node.next; } return null`
  - **9.3.12**: Deleting a node with a given value
    - Formula: `if node.value == target, { node = node.next; return; } else if node.next.value == target, { node.next = node.next.next; return; } else, { return; }`

### 9.4

- Self-Referential Structures:
  - Definition: A data structure that can modify itself.
  - Examples:
    - Linked lists
    - Trees

### 9.5

- Important Formulas and Definitions:
  - Definition of a linked list: A data structure consisting of a sequence of nodes, each of which contains a value and a reference (i.e., "link") to the next node in the sequence.
  - Formula for finding the middle element of a linked list: `mid = (head + tail) / 2`
  - Formula for printing a linked list: `print(node.value) while node != null`
