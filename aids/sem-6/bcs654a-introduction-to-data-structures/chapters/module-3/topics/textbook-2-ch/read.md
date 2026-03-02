# **Introduction to Linked Lists**

## **What is a Linked List?**

A linked list is a linear data structure where each element is a separate object, and each element (called a node) points to the next node in the list. This structure allows for efficient insertion and deletion of nodes at any position in the list.

## **Key Characteristics of Linked Lists**

- **Dynamic Memory Allocation**: Linked lists can grow or shrink dynamically as elements are added or removed.
- **Efficient Insertion and Deletion**: Inserting or deleting a node at a specific position in the list can be done in O(1) time.
- **No Head Node**: Unlike arrays, linked lists do not require a head node, making them more memory-efficient.

## **Types of Linked Lists**

There are two primary types of linked lists:

- **Singly Linked List**: Each node points to the next node in the list.
- **Doubly Linked List**: Each node points to both the next and previous nodes in the list.

### Singly Linked List

A singly linked list is the most basic type of linked list, where each node points to the next node in the list.

## **Singly Linked List Node Structure**

- **Node**: Each node has the following components:
  - **data**: The actual data stored in the node.
  - **next**: A reference (or "link") to the next node in the list.

## **Example of a Singly Linked List**

Suppose we have a singly linked list with the following nodes:

- Node 1: `data = 10`, `next = Node 2`
- Node 2: `data = 20`, `next = Node 3`
- Node 3: `data = 30`, `next = Node 4`
- Node 4: `data = 40`, `next = NULL`

### Self-Referential Linked List

A self-referential linked list is a linked list where each node points to its own next node.

## **Self-Referential Linked List Example**

Suppose we have a self-referential linked list with the following nodes:

- Node 1: `data = 10`
- Node 1.next: `Node 1` (self-referential)
- Node 2: `data = 20`
- Node 2.next: `Node 3`
- Node 3: `data = 30`
- Node 3.next: `Node 4`
- Node 4: `data = 40`
- Node 4.next: `Node 1` (self-referential)

### Operations on Linked Lists

Linked lists support the following operations:

- **Insertion**: Inserting a new node at a specific position in the list.
- **Deletion**: Deleting a node from the list.
- **Traversal**: Traversing the list to access each node's data.

**Example Code in Python**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Example usage
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.traverse()  # Output: 10, 20, 30
linked_list.delete(20)
linked_list.traverse()  # Output: 10, 30
```

This study material provides a comprehensive introduction to linked lists, including their definition, key characteristics, types, and operations. It also includes examples and code snippets in Python to illustrate the concepts.
