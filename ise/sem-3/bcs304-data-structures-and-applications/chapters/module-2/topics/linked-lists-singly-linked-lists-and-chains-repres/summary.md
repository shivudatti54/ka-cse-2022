# **Linked Lists: Revision Notes**

## **3.3 Singly Linked Lists**

- A singly linked list is a linear collection of data elements whose order is not given by their physical placement in memory.
- Each element (or node) points to the next element in the sequence.
- **Definition:** A node contains a data field and a reference (link) to the next node in the sequence.
- **Operations:**
  - Insertion: O(1) at the beginning and middle
  - Deletion: O(1) at the beginning and middle
  - Search: O(n)
  - Traversal: O(n)

## **3.4 Lists and Chains**

- A list is a collection of elements, and a chain is a linked list with a fixed capacity.
- **Definition:** A list is a collection of elements with a fixed number of elements.
- **Operations:**
  - Insertion: O(1) at the beginning and middle
  - Deletion: O(1) at the beginning and middle
  - Search: O(n)
  - Traversal: O(n)

## **3.7 Representing Chains in C**

- To represent a chain in C, use an array of pointers to the first element of each chain.
- **Code Example:**
  ```c
  typedef struct Node {
  int data;
  struct Node\* next;
  } Node;

typedef struct Chain {
Node\* head;
} Chain;

```

**Linked Stacks and Queues**
---------------------------

*   A stack is a LIFO (Last In First Out) data structure.
*   A queue is a FIFO (First In First Out) data structure.
*   **Linked Stack and Queue Operations:**
    *   Stack: push (O(1)), pop (O(1)), peek (O(1))
    *   Queue: enqueue (O(1)), dequeue (O(1)), peek (O(1))

**Important Formulas, Definitions, and Theorems**
-------------------------------------------

*   **Definition of a Node:** A node is a data element with a reference (link) to the next node in the sequence.
*   **Definition of a Linked List:** A linked list is a linear collection of data elements whose order is not given by their physical placement in memory.
*   **Theorem:** A singly linked list can be traversed in O(n) time using a pointer.

Note: This summary is a concise version of the key points. Make sure to review the full chapter for a deeper understanding.
```
