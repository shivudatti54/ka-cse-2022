# **8.1 Linked Lists and 8.2 Stacks and Queues**

## **Introduction**

In this section, we will explore two fundamental data structures in computer science: Linked Lists and Stacks and Queues.

## **8.1 Linked Lists**

### Definition

A Linked List is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next element in the sequence.

### Characteristics

- Each element is called a node, and it contains a value and a reference (or link) to the next node in the sequence.
- Linked Lists can be either singly linked or doubly linked. A singly linked list has only one reference to the next node, while a doubly linked list has references to both the next and previous nodes.

### Types of Linked Lists

- **Singly Linked List**: Each node only points to the next node in the sequence.
- **Doubly Linked List**: Each node points to both the next and previous nodes in the sequence.

### Operations

- **Insertion**: Inserting a new node at a specific position in the sequence.
- **Deletion**: Removing a node from the sequence at a specific position.
- **Traversal**: Traversing the sequence from the beginning to the end.

### Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

# Example usage:
linked_list = LinkedList()
linked_list.insert('A')
linked_list.insert('B')
linked_list.insert('C')
linked_list.traverse()  # Output: A B C
```

## **8.2 Stacks and Queues**

### Definition

A Stack is a Last-In-First-Out (LIFO) data structure, meaning the last element added is the first one to be removed. A Queue is a First-In-First-Out (FIFO) data structure, meaning the first element added is the first one to be removed.

### Characteristics

- **Stacks**:
  - Last-In-First-Out (LIFO) order
  - Elements are added and removed from the top of the stack
- **Queues**:
  - First-In-First-Out (FIFO) order
  - Elements are added to the end of the queue and removed from the front of the queue

### Operations

- **Stack**:
  - **Push**: Add an element to the top of the stack
  - **Pop**: Remove an element from the top of the stack
  - **Peek**: Get the top element without removing it
- **Queue**:
  - **Enqueue**: Add an element to the end of the queue
  - **Dequeue**: Remove an element from the front of the queue
  - **Peek**: Get the front element without removing it

### Example

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

# Example usage:
stack = Stack()
stack.push('A')
stack.push('B')
print(stack.pop())  # Output: B
print(stack.peek())  # Output: A

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
print(queue.dequeue())  # Output: A
print(queue.peek())  # Output: B
```

### Key Concepts

- Linked Lists: Linear collection of data elements with references to the next element
- Stacks: LIFO data structure for adding and removing elements from the top
- Queues: FIFO data structure for adding and removing elements from the front
