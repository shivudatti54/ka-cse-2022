# Introduction to Data Structures

## Module 1: Topic 6.1 to 6.3

### Table of Contents

1. [6.1: Arrays](#61-arrays)
   - Introduction to Arrays
   - Characteristics of Arrays
   - Applications of Arrays
   - Example: Implementing an Array
   - Further Reading

2. [6.2: Linked Lists](#62-linked-lists)
   - Introduction to Linked Lists
   - Characteristics of Linked Lists
   - Types of Linked Lists
   - Applications of Linked Lists
   - Example: Implementing a Singly Linked List
   - Further Reading

3. [6.3: Stacks and Queues](#63-stacks-and-queues)
   - Introduction to Stacks and Queues
   - Characteristics of Stacks and Queues
   - Implementing Stacks and Queues
   - Applications of Stacks and Queues
   - Example: Implementing a Stack using an Array
   - Further Reading

### 6.1: Arrays

Arrays are a fundamental data structure in computer science. They are collections of elements of the same data type stored in contiguous memory locations.

#### Introduction to Arrays

Arrays are a type of data structure that stores a group of elements of the same data type in a single variable. Each element in an array is identified by an index or subscript, which allows for efficient access and manipulation of the elements.

#### Characteristics of Arrays

Arrays have the following characteristics:

- **Fixed Size**: Arrays have a fixed size that cannot be changed dynamically.
- **Contiguous Memory Allocation**: Arrays are stored in contiguous memory locations, which allows for efficient access and manipulation of the elements.
- **Homogeneous Elements**: Arrays store elements of the same data type.
- **Random Access**: Arrays allow for random access to any element in the array.

#### Applications of Arrays

Arrays have numerous applications in computer science, including:

- **Database Management**: Arrays are used to store and manage data in databases.
- **File Systems**: Arrays are used to represent files and directories in file systems.
- **Algorithm Design**: Arrays are used as a fundamental data structure in many algorithm design problems.

#### Example: Implementing an Array

Here is an example of a simple array implementation in Python:

```python
class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, index, element):
        if index < 0 or index >= self.size:
            print("Invalid index")
        else:
            self.array[index] = element

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index")
        else:
            self.array[index] = None

    def print_array(self):
        for element in self.array:
            print(element)

# Create an array of size 5
arr = Array(5)

# Insert elements into the array
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.insert(3, 40)
arr.insert(4, 50)

# Print the array
arr.print_array()
```

#### Further Reading

- "Arrays" by MIT OpenCourseWare
- "The C Programming Language" by Kernighan and Ritchie

### 6.2: Linked Lists

Linked lists are a fundamental data structure in computer science. They are collections of elements, each of which is a separate object, with each element pointing to the next element in the list.

#### Introduction to Linked Lists

Linked lists are a type of data structure that stores a group of elements in separate objects, with each element pointing to the next element in the list.

#### Characteristics of Linked Lists

Linked lists have the following characteristics:

- **Dynamic Size**: Linked lists can grow or shrink dynamically as elements are added or removed.
- **Non-Contiguous Memory Allocation**: Linked lists are stored in non-contiguous memory locations, which allows for efficient insertion and deletion of elements.
- **Heterogeneous Elements**: Linked lists can store elements of different data types.
- **Sequential Access**: Linked lists allow for sequential access to elements in the list.

#### Types of Linked Lists

There are several types of linked lists, including:

- **Singly Linked Lists**: Each element points to the next element in the list.
- **Doubly Linked Lists**: Each element points to both the previous and next elements in the list.
- **Circular Linked Lists**: The last element points back to the first element in the list.

#### Applications of Linked Lists

Linked lists have numerous applications in computer science, including:

- **Database Management**: Linked lists are used to store and manage data in databases.
- **Web Browsers**: Linked lists are used to represent the HTML document tree in web browsers.
- **Algorithm Design**: Linked lists are used as a fundamental data structure in many algorithm design problems.

#### Example: Implementing a Singly Linked List

Here is an example of a simple singly linked list implementation in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Create a linked list
ll = LinkedList()

# Insert elements into the linked list
ll.insert(10)
ll.insert(20)
ll.insert(30)

# Print the linked list
ll.print_list()
```

#### Further Reading

- "Linked Lists" by MIT OpenCourseWare
- "Data Structures and Algorithms" by Robert Sedgewick and Kevin Wayne

### 6.3: Stacks and Queues

Stacks and queues are fundamental data structures in computer science. They are collection of elements that follow the Last-In-First-Out (LIFO) and First-In-First-Out (FIFO) principles, respectively.

#### Introduction to Stacks and Queues

Stacks and queues are data structures that follow the LIFO and FIFO principles, respectively.

#### Characteristics of Stacks and Queues

Stacks have the following characteristics:

- **Last-In-First-Out (LIFO) Principle**: The last element added to the stack is the first one to be removed.
- **Fixed Size**: Stacks have a fixed size that cannot be changed dynamically.

Queues have the following characteristics:

- **First-In-First-Out (FIFO) Principle**: The first element added to the queue is the first one to be removed.
- **Dynamic Size**: Queues can grow or shrink dynamically as elements are added or removed.

#### Implementing Stacks and Queues

Stacks and queues can be implemented using arrays or linked lists. Here is an example of a simple stack implementation using an array:

```python
class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def push(self, element):
        if self.is_full():
            print("Stack is full")
        else:
            self.array[self.top()] = element
            self.top() += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            element = self.array[self.top()]
            self.array[self.top()] = None
            self.top() -= 1
            return element

    def is_full(self):
        return self.top() == self.size

    def is_empty(self):
        return self.top() == 0

    def top(self):
        return self.array[self.top()]

# Create a stack
stack = Stack(5)

# Push elements into the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Pop elements from the stack
print(stack.pop())
print(stack.pop())
```

Queues can be implemented using arrays or linked lists. Here is an example of a simple queue implementation using an array:

```python
class Queue:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full")
        else:
            self.array[self.rear] = element
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            element = self.array[self.front]
            self.array[self.front] = None
            self.front = (self.front + 1) % self.size
            return element

    def is_full(self):
        return self.rear == self.size

    def is_empty(self):
        return self.front == 0

# Create a queue
queue = Queue(5)

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Dequeue elements from the queue
print(queue.dequeue())
print(queue.dequeue())
```

#### Further Reading

- "Stacks and Queues" by MIT OpenCourseWare
- "Data Structures and Algorithms" by Robert Sedgewick and Kevin Wayne
