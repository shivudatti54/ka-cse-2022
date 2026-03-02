# **Linked Lists Revision Notes**

## **1. Introduction**

- A linked list is a data structure consisting of a sequence of nodes, where each node contains a value and a reference (i.e., "link") to the next node in the sequence.
- Singly linked lists have only one reference to the next node.

## **2. Singly Linked Lists**

- Definition: A collection of nodes, where each node contains a value and a reference to the next node.
- Types:
  - **Singly Linked List**: Each node has a reference to the next node, but not to the previous node.
  - **Doubly Linked List**: Each node has references to both the next and previous nodes.

## **3. Lists and Chains**

- A list is a collection of elements, where each element is a node in a linked list.
- A chain is a linked list where each node has a reference to the next node, but no reference to the previous node.

## **4. Representing Chains in C**

- Use a struct to represent a node, with a value and a pointer to the next node.
- Use a pointer to the head of the list to traverse the list.

## **5. Linked Stacks and Queues**

- A stack is a Last-In-First-Out (LIFO) data structure, where elements are added and removed from the top.
- A queue is a First-In-First-Out (FIFO) data structure, where elements are added to the end and removed from the front.

## **Key Formulas and Definitions**

- **Node**: A single element in a linked list, containing a value and a reference to the next node.
- **Head**: The first node in a linked list.
- **Tail**: The last node in a linked list.
- **Length**: The number of nodes in a linked list.

## **Important Theorems**

- **Traverse and Search**: It is possible to traverse a linked list in O(n) time, where n is the length of the list.
- **Insert and Delete**: It is possible to insert or delete a node in a linked list in O(n) time, where n is the length of the list.
