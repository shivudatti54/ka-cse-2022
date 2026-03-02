# INTRODUCTION TO DATA STRUCTURES

## Module: @#@10012025

## Topic: 6.1 to 6.3

**Table of Contents**

- [6.1: Arrays](#6-1-array)
- [6.2: Linked Lists](#6-2-linked-lists)
- [6.3: Stacks and Queues](#6-3-stacks-and-queues)

### 6.1: Arrays

An array is a fundamental data structure in computer science that stores a collection of elements of the same data type in contiguous memory locations.

#### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations. The elements are identified by their indices, which are used to access and manipulate the data.

#### Characteristics

- **Fixed size**: The size of an array is fixed at the time of its creation.
- **Homogeneous**: All elements in an array must be of the same data type.
- **Contiguous memory allocation**: Array elements are stored in contiguous memory locations.

#### Example

```python
# Creating an array of integers
int_array = [1, 2, 3, 4, 5]

# Accessing elements
print(int_array[0])  # Output: 1
print(int_array[1])  # Output: 2

# Modifying elements
int_array[0] = 10
print(int_array[0])  # Output: 10
```

#### Applications

- **Database indexing**: Arrays are used to implement index structures for databases, allowing for efficient storage and retrieval of data.
- **Image processing**: Arrays are used to represent images, with each pixel stored in a contiguous memory location.

### 6.2: Linked Lists

A linked list is a dynamic data structure that consists of nodes, each containing a value and a reference (or link) to the next node in the sequence.

#### Definition

A linked list is a dynamic data structure consisting of nodes, each containing a value and a reference (or link) to the next node in the sequence.

#### Characteristics

- **Dynamic size**: The size of a linked list is dynamic and can be modified at runtime.
- **Heterogeneous**: Linked lists can store elements of different data types.
- **Non-contiguous memory allocation**: Linked list elements are stored in non-contiguous memory locations.

#### Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Accessing elements
current = head
while current:
    print(current.value)
    current = current.next
```

#### Applications

- **Database query result sets**: Linked lists are used to implement result sets for database queries, allowing for efficient storage and retrieval of data.
- **Dynamic memory allocation**: Linked lists are used to manage dynamic memory allocation in operating systems.

### 6.3: Stacks and Queues

A stack and a queue are two fundamental data structures that follow the Last-In-First-Out (LIFO) and First-In-First-Out (FIFO) principles, respectively.

#### Stacks

A stack is a Last-In-First-Out (LIFO) data structure that follows the principle that the last element added to the stack is the first one to be removed.

#### Definition

A stack is a LIFO data structure that stores elements in a particular order, with the last element added to the top of the stack being the first one to be removed.

#### Characteristics

- **LIFO principle**: The last element added to the stack is the first one to be removed.
- **Fixed order**: Elements in a stack follow a fixed order, with the top element being the most accessible.

#### Example

```python
# Creating a stack
stack = []

# Pushing elements
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
```

#### Queues

A queue is a First-In-First-Out (FIFO) data structure that follows the principle that the first element added to the queue is the first one to be removed.

#### Definition

A queue is a FIFO data structure that stores elements in a particular order, with the first element added to the queue being the first one to be removed.

#### Characteristics

- **FIFO principle**: The first element added to the queue is the first one to be removed.
- **Variable order**: Elements in a queue follow a variable order, with the end element being the most accessible.

#### Example

```python
# Creating a queue
queue = []

# Enqueueing elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeueing elements
print(queue.pop(0))  # Output: 1
print(queue.pop(0))  # Output: 2
print(queue.pop(0))  # Output: 3
```

#### Applications

- **Undo/Redo functionality**: Stacks and queues are used to implement undo/redo functionality in text editors and other applications.
- **Job scheduling**: Queues are used to manage job scheduling in operating systems, with jobs being added to the queue and executed in the order they were added.

### Further Reading

- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms in Python" by Michael T. Goodrich
- "Computer Organization and Design" by David A. Patterson and John L. Hennessy
