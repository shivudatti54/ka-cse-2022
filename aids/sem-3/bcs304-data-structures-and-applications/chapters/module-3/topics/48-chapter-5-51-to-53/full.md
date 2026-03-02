**4.8 Chapter-5: 5.1 to 5.3**
**DATA STRUCTURES AND APPLICATIONS**
**Module: 8Hours**

# **5.1: Stacks**

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed.

## **History**

The concept of a stack has been around for centuries, dating back to the ancient Egyptians. The word "stack" comes from the idea of a pile of objects, and the first stack data structure was implemented using a deck of cards. In the 1950s, the concept of a stack was formalized using a mathematical model.

## **Properties**

A stack data structure has the following properties:

- **Last-In-First-Out (LIFO)**: The last element added to the stack will be the first one to be removed.
- **Ordered**: Elements in a stack are ordered based on the order of insertion.
- **Dynamic**: The size of a stack can change dynamically during execution.

## **Operations**

A stack data structure supports the following operations:

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes the top element from the stack.
- **Peek**: Returns the top element of the stack without removing it.
- **IsEmpty**: Returns a boolean indicating whether the stack is empty.

## **Example**

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

# Create a new stack
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Peek at the top element
print(stack.peek())  # Output: 3

# Pop elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

# Check if the stack is empty
print(stack.is_empty())  # Output: True
```

# **5.2: Queues**

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

## **History**

The concept of a queue has been around for centuries, dating back to ancient civilizations. The word "queue" comes from the French word "queue," meaning "tail," which refers to the end of a line.

## **Properties**

A queue data structure has the following properties:

- **First-In-First-Out (FIFO)**: The first element added to the queue will be the first one to be removed.
- **Ordered**: Elements in a queue are ordered based on the order of insertion.
- **Dynamic**: The size of a queue can change dynamically during execution.

## **Operations**

A queue data structure supports the following operations:

- **Enqueue**: Adds an element to the end of the queue.
- **Dequeue**: Removes the front element from the queue.
- **Peek**: Returns the front element of the queue without removing it.
- **IsEmpty**: Returns a boolean indicating whether the queue is empty.

## **Example**

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

# Create a new queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Peek at the front element
print(queue.peek())  # Output: 1

# Dequeue elements from the queue
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3

# Check if the queue is empty
print(queue.is_empty())  # Output: True
```

# **5.3: Linked Lists**

A linked list is a linear data structure where each element points to the next element. This allows for efficient insertion and deletion of elements at any position.

## **History**

The concept of a linked list has been around since the 1960s, when it was first proposed by Ivan Sutherland. The first linked list was implemented using a deck of cards.

## **Properties**

A linked list data structure has the following properties:

- **Dynamic**: The size of a linked list can change dynamically during execution.
- **Ordered**: Elements in a linked list are ordered based on the order of insertion.
- **Efficient insertion and deletion**: Linked lists allow for efficient insertion and deletion of elements at any position.

## **Operations**

A linked list data structure supports the following operations:

- **Insert**: Adds an element to the linked list.
- **Delete**: Removes an element from the linked list.
- **Search**: Returns an element if it exists in the linked list, or None otherwise.
- **Print**: Prints the elements of the linked list.

## **Example**

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
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Create a new linked list
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

# Print the linked list
linked_list.print_list()  # Output: 1 2 3

# Delete an element from the linked list
linked_list.delete(2)

# Print the linked list
linked_list.print_list()  # Output: 1 3

# Search for an element in the linked list
print(linked_list.search(1))  # Output: True
```

## **Further Reading**

- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms in Python" by Michael T. Goodrich
- "The C Programming Language" by Brian Kernighan and Dennis Ritchie
