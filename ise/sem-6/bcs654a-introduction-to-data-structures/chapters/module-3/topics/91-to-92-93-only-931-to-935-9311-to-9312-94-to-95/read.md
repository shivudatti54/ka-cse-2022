# **Introduction to Linked Lists: 9.1 to 9.2, 9.3, and 9.4 to 9.5**

## **9.1: Introduction to Linked Lists**

### What is a Linked List?

A linked list is a linear data structure where each element is a separate object, known as a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion of elements from any position in the sequence.

### Key Characteristics of Linked Lists

- Dynamic size: Linked lists can grow or shrink as elements are added or removed.
- Efficient insertion and deletion: Linked lists can insert or delete elements at any position without shifting all elements.
- Variable memory allocation: Each node may require a different amount of memory.

### Advantages of Linked Lists

- Efficient use of memory: Linked lists can use less memory than arrays when elements are inserted or deleted frequently.
- Efficient insertion and deletion: Linked lists can insert or delete elements at any position without shifting all elements.

### Disadvantages of Linked Lists

- Slow search: Linked lists can be slower to search than arrays because each node must be traversed individually.
- More complex implementation: Linked lists require more complex implementation than arrays.

### Example Code (Python)

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create a linked list and insert elements
linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")

# Print the linked list
linked_list.print_list()
```

## **9.2: Singly Linked List**

### Definition

A singly linked list is a type of linked list where each node only contains a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion of elements from any position in the sequence.

### Key Concepts

- **Head**: The first node in the linked list.
- **Tail**: The last node in the linked list.
- **Next**: The reference (or link) to the next node in the sequence.
- **Previous**: The reference (or link) to the previous node in the sequence (not applicable in singly linked lists).

### Operations on Singly Linked Lists

- **Insertion**: Inserting a new element at the beginning, end, or at any position in the sequence.
- **Deletion**: Deleting an element from the beginning, end, or at any position in the sequence.
- **Traversal**: Traversing the linked list to print or access the elements.

### Example Code (Python)

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_head(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create a singly linked list and insert elements
singly_linked_list = SinglyLinkedList()
singly_linked_list.insert_at_head("A")
singly_linked_list.insert_at_head("B")
singly_linked_list.insert_at_tail("C")

# Print the linked list
singly_linked_list.print_list()
```

## **9.3: Self-Referential Structures**

### Definition

A self-referential structure is a data structure that contains references (or pointers) to itself. In the context of linked lists, self-referential structures refer to doubly linked lists or circularly linked lists.

### Key Concepts

- **Doubly Linked List**: A linked list where each node contains references (or links) to the next node and the previous node.
- **Circularly Linked List**: A linked list where the last node points to the first node, creating a circular structure.

### Advantages of Self-Referential Structures

- **Efficient insertion and deletion**: Self-referential structures can insert or delete elements at any position without shifting all elements.
- **Improved search**: Self-referential structures can search for elements more efficiently because each node can access the previous and next nodes.

### Example Code (Python)

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_head(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create a doubly linked list and insert elements
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_at_head("A")
doubly_linked_list.insert_at_head("B")
doubly_linked_list.insert_at_tail("C")

# Print the linked list
doubly_linked_list.print_list()
```

## **9.4: Operations on Linked Lists**

### Insertion

Insertion is the process of adding a new element to the linked list. There are different types of insertion:

- **Insertion at the beginning**: Inserting a new element at the head of the linked list.
- **Insertion at the end**: Inserting a new element at the tail of the linked list.
- **Insertion at a specific position**: Inserting a new element at a specific position in the linked list.

### Deletion

Deletion is the process of removing an element from the linked list. There are different types of deletion:

- **Deletion at the beginning**: Deleting an element from the head of the linked list.
- **Deletion at the end**: Deleting an element from the tail of the linked list.
- **Deletion at a specific position**: Deleting an element from a specific position in the linked list.

### Traversal

Traversal is the process of visiting each element in the linked list. There are different types of traversal:

- **Forward traversal**: Traversing the linked list from head to tail.
- **Backward traversal**: Traversing the linked list from tail to head.
- **Random traversal**: Traversing the linked list in a random order.

### Example Code (Python)

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            if not self.head:
                self.head = None
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    if not current.next:
                        self.head = None
                    break
                current = current.next

    def traverse(self, direction):
        if direction == "forward":
            current = self.head
            while current:
                print(current.data)
                current = current.next
        elif direction == "backward":
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data)
                current = current.prev
        else:
            raise ValueError("Invalid direction")

# Create a linked list and perform operations
linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")

# Traverse the linked list
linked_list.traverse("forward")
print("\nTraversing linked list in reverse order")
linked_list.traverse("backward")
```

## **9.5: Use Cases**

Linked lists have a wide range of use cases in various fields, including:

- **Database query optimization**: Linked lists can be used to represent the order of operations in a database query.
- **File systems**: Linked lists can be used to represent the structure of a file system.
- **Compilers**: Linked lists can be used to represent the parse tree of a program.
- **Algorithms**: Linked lists can be used to implement various algorithms, such as the merge sort and insertion sort algorithms.

### Example Use Case: Implementing a Stack using a Linked List

A stack is a data structure that follows the LIFO (Last-In-First-Out) principle. We can implement a stack using a linked list as follows:

- Define a linked list with a `head` and `tail` node.
- When an element is pushed onto the stack, create a new node and add it to the end of the linked list.
- When an element is popped from the stack, remove the head node from the linked list.
- When the stack is empty, return `None`.

### Example Code (Python)

```python
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return data
        else:
            return None

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Create a stack and perform operations
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

print(stack.pop())  # Output: C
print(stack.pop())  # Output: B
print(stack.pop())  # Output: A
```

This implementation demonstrates how linked lists can be used to implement a stack data structure. The `push` operation adds elements to the end of the linked list, while the `pop` operation removes elements from the head of the linked list.
