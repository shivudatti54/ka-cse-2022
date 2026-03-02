# Introduction to Data Structures: Linked Lists

## Table of Contents

1. [9.1: Introduction to Linked Lists](#9-1-introduction-to-linked-lists)
2. [9.2: History of Linked Lists and Modern Developments](#9-2-history-of-linked-lists-and-modern-developments)
3. [9.3: Implementing Linked Lists](#9-3-implementing-linked-lists)
   - [9.3.1: Node Structure](#93-1-node-structure)
   - [9.3.2: Singly Linked List Implementation](#93-2-singly-linked-list-implementation)
   - [9.3.3: Self-Referential Linked List Implementation](#93-3-self-referential-linked-list-implementation)
   - [9.3.4: Doubly Linked List Implementation](#93-4-doubly-linked-list-implementation)
   - [9.3.5: Advantages and Disadvantages of Linked Lists](#93-5-advantages-and-disadvantages-of-linked-lists)
4. [9.4: Operations on Linked Lists](#9-4-operations-on-linked-lists)
5. [9.5: Applications and Case Studies](#9-5-applications-and-case-studies)

## 9.1: Introduction to Linked Lists

### Definition

A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next element in the list.

### Types of Linked Lists

1. **Singly Linked List**: Each element points to the next element in the list.
2. **Doubly Linked List**: Each element points to the next and previous elements in the list.
3. **Self-Referential Linked List**: A linked list that contains pointers to its own nodes.

### Benefits

1. **Dynamic Memory Allocation**: Linked lists can efficiently use memory by allocating and deallocating memory as needed.
2. **Efficient Insertion and Deletion**: Linked lists can insert and delete elements at any position in the list, making them suitable for applications that require frequent modifications.

## 9.2: History of Linked Lists and Modern Developments

### Early History

The concept of linked lists dates back to the 1960s, when computer scientists like John McCarthy and Douglas Engelbart developed the first linked list algorithms.

### Modern Developments

1. **Object-Oriented Programming**: Linked lists are commonly used in object-oriented programming languages like Java and C++.
2. **Data Structures in Computer Science**: Linked lists are a fundamental data structure in computer science, used in various applications like databases, file systems, and web browsers.
3. **Algorithms and Complexity**: Linked lists are used to analyze the time and space complexity of algorithms, making them an essential tool in computer science.

## 9.3: Implementing Linked Lists

### 9.3.1: Node Structure

A node in a linked list consists of two parts:

1. **Data**: The actual data stored in the node.
2. **Next**: A pointer to the next node in the list.

### 9.3.2: Singly Linked List Implementation

A singly linked list consists of nodes that point to the next node in the list. Each node has a pointer to the next node, but not to the previous node.

```markdown
+---------------+
| Node A |
+---------------+
| Data: A |
| Next: B |
+---------------+
| Node B |
+---------------+
| Data: B |
| Next: C |
+---------------+
| Node C |
+---------------+
| Data: C |
| Next: NULL |
+---------------+
```

### 9.3.3: Self-Referential Linked List Implementation

A self-referential linked list is a linked list that contains pointers to its own nodes. This implementation is not commonly used in practice.

```markdown
+---------------+
| Node A |
+---------------+
| Data: A |
| Next: B |
+---------------+
| Node B |
+---------------+
| Data: B |
| Next: A |
+---------------+
| Node C |
+---------------+
| Data: C |
| Next: NULL |
+---------------+
```

### 9.3.4: Doubly Linked List Implementation

A doubly linked list consists of nodes that point to the next and previous nodes in the list.

```markdown
+---------------+
| Node A |
+---------------+
| Data: A |
| Prev: NULL |
| Next: B |
+---------------+
| Node B |
+---------------+
| Data: B |
| Prev: A |
| Next: C |
+---------------+
| Node C |
+---------------+
| Data: C |
| Prev: B |
| Next: NULL |
+---------------+
```

### 9.3.5: Advantages and Disadvantages of Linked Lists

Advantages:

- Efficient use of memory
- Fast insertion and deletion of elements

Disadvantages:

- More complex to implement and debug
- Slower access to elements

### 9.3.11: Insertion and Deletion of Elements

Linked lists can insert and delete elements at any position in the list.

```markdown
// Inserting a new node at the beginning of the list
Node* insert(Node* head, int data) {
Node\* newNode = new Node(data);
newNode->next = head;
head = newNode;
return head;
}

// Deleting a node from the list
Node* delete(Node* head, int data) {
if (head == NULL) return NULL;
if (head->data == data) return head->next;
Node\* current = head;
while (current->next != NULL) {
if (current->next->data == data) {
current->next = current->next->next;
return head;
}
current = current->next;
}
return head;
}
```

### 9.3.12: Applications of Linked Lists

Linked lists are used in various applications:

- Database indexing
- File systems
- Web browsers
- Compilers

## 9.4: Operations on Linked Lists

Linked lists support various operations:

- **Insertion**: Adding a new node to the list.
- **Deletion**: Removing a node from the list.
- **Search**: Finding a specific node in the list.
- **Traversal**: Visiting each node in the list.

## 9.5: Applications and Case Studies

Linked lists have numerous applications in various fields:

- **Database Indexing**: Linked lists can be used to index large datasets for efficient querying.
- **File Systems**: Linked lists can be used to manage files and directories in file systems.
- **Web Browsers**: Linked lists can be used to manage web page links and navigate the web.
- **Compilers**: Linked lists can be used to manage syntax trees and parse expressions.

### Case Study: Dynamic Memory Allocation

Linked lists can be used to implement dynamic memory allocation. When a program requires more memory, a new node can be created and inserted at the beginning of the list. When a program no longer requires memory, the node can be deleted from the list.

```markdown
+---------------+
| Node A |
+---------------+
| Data: A |
| Prev: NULL |
| Next: NULL |
+---------------+
```

This implementation is efficient because it allows the program to allocate and deallocate memory as needed.

## Further Reading

- [Data Structures and Algorithms in Python](https://github.com/marcusva/data-structures-and-algorithms-in-python)
- [Introduction to Computer Science](https://mitpress.mit.edu/books/introduction-computer-science)
- [Data Structures for the impatient](https://www.oreilly.com/programming/free/data-structures-for-the-impatient.pdf)
