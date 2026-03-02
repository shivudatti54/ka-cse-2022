# **8.1 to 8.2: Introduction to Data Structures**

## **8.1: Introduction to Data Structures**

### What are Data Structures?

Data structures are the ways in which we organize and store data in a computer so that it can be efficiently accessed, modified, and manipulated. They provide a way to manage data by grouping it into collections of elements, each of which has a specific value or set of values.

### Types of Data Structures

There are several types of data structures, including:

- **Arrays**: A collection of elements of the same data type stored in contiguous memory locations.
- **Linked Lists**: A dynamic collection of elements, each of which points to the next element in the sequence.
- **Stacks**: A Last-In-First-Out (LIFO) data structure that follows the principle of last element inserted is the first one to be removed.
- **Queues**: A First-In-First-Out (FIFO) data structure that follows the principle of first element inserted is the first one to be removed.
- **Trees**: A hierarchical data structure consisting of nodes, where each node has a value and zero or more child nodes.
- **Graphs**: A non-linear data structure consisting of nodes and edges that connect the nodes.

### Importance of Data Structures

Data structures play a crucial role in programming as they enable efficient storage and retrieval of data. They are used in a wide range of applications, including databases, web browsers, and operating systems.

### Example of Data Structures in Real Life

- **Phonebook**: A phonebook is an example of a data structure as it organizes a collection of names, phone numbers, and addresses in a structured way.
- **Image Editing Software**: Image editing software uses data structures such as matrices and arrays to manipulate and store images.

## **8.2: Types of Data Structures**

### Arrays

#### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations.

#### Characteristics

- **Fixed Size**: Arrays have a fixed size, which is specified by the programmer.
- **Homogeneous**: All elements in an array must be of the same data type.

#### Example

```python
# Define an array
fruits = ['apple', 'banana', 'cherry']

# Access an element in the array
print(fruits[0])  # Output: apple

# Modify an element in the array
fruits[0] = 'mango'
print(fruits[0])  # Output: mango
```

### Linked Lists

#### Definition

A linked list is a dynamic collection of elements, each of which points to the next element in the sequence.

#### Characteristics

- **Dynamic Size**: Linked lists can grow or shrink dynamically as elements are added or removed.
- **Non-Homogeneous**: Linked lists can contain elements of different data types.

#### Example

```python
# Define a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node('apple')
node2 = Node('banana')
node3 = Node('cherry')

# Link nodes together
node1.next = node2
node2.next = node3

# Print the linked list
while node1 is not None:
    print(node1.data)
    node1 = node1.next
```

### Stacks

#### Definition

A stack is a Last-In-First-Out (LIFO) data structure that follows the principle of last element inserted is the first one to be removed.

#### Characteristics

- **LIFO**: Stacks follow the LIFO principle, meaning the last element inserted is the first one to be removed.
- **Dynamic Size**: Stacks can grow or shrink dynamically as elements are added or removed.

#### Example

```python
# Define a stack
class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop an element from the stack
    def pop(self):
        return self.items.pop()

# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push('apple')
stack.push('banana')
stack.push('cherry')

# Pop elements from the stack
print(stack.pop())  # Output: cherry
print(stack.pop())  # Output: banana
print(stack.pop())  # Output: apple
```

### Queues

#### Definition

A queue is a First-In-First-Out (FIFO) data structure that follows the principle of first element inserted is the first one to be removed.

#### Characteristics

- **FIFO**: Queues follow the FIFO principle, meaning the first element inserted is the first one to be removed.
- **Dynamic Size**: Queues can grow or shrink dynamically as elements are added or removed.

#### Example

```python
# Define a queue
class Queue:
    def __init__(self):
        self.items = []

    # Enqueue an element into the queue
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue an element from the queue
    def dequeue(self):
        return self.items.pop(0)

# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue('apple')
queue.enqueue('banana')
queue.enqueue('cherry')

# Dequeue elements from the queue
print(queue.dequeue())  # Output: apple
print(queue.dequeue())  # Output: banana
print(queue.dequeue())  # Output: cherry
```
