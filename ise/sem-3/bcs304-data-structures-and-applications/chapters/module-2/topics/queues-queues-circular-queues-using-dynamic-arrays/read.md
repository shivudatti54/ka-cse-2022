# **Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

## **Queues**

### Definition

A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle, meaning the first element added to the queue will be the first one to be removed.

### Characteristics

- Elements are added to the end of the queue
- Elements are removed from the front of the queue
- Can be implemented using arrays or linked lists

### Example

Suppose we have a line of people waiting for a concert. The person who arrives first will be the first one to enter the concert hall.

### Operations

- **Enqueue**: Add an element to the end of the queue
- **Dequeue**: Remove an element from the front of the queue

### Code Example (Python)

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

# Example usage
q = Queue()
q.enqueue("John")
q.enqueue("Alice")
print(q.dequeue())  # Output: John
print(q.dequeue())  # Output: Alice
```

## **Circular Queues**

### Definition

A circular queue is a type of queue where the last element is connected to the first element, forming a circle.

### Characteristics

- Elements are added to the end of the queue
- Elements are removed from the front of the queue
- Can be implemented using arrays or linked lists

### Example

Suppose we have a conveyor belt that wraps around a circle. The element that is added to the end of the belt will be the first one to be removed.

### Operations

- **Enqueue**: Add an element to the end of the queue
- **Dequeue**: Remove an element from the front of the queue

### Code Example (Python)

```python
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return item

    def is_full(self):
        return self.tail == self.head

    def is_empty(self):
        return self.head == self.tail

# Example usage
cq = CircularQueue(5)
cq.enqueue("John")
cq.enqueue("Alice")
print(cq.dequeue())  # Output: John
print(cq.dequeue())  # Output: Alice
```

## **Using Dynamic Arrays**

### Definition

A dynamic array is a type of array that can grow or shrink at runtime.

### Characteristics

- Can be implemented using pointers or references
- Can be used to implement queues

### Example

Suppose we have a queue implemented using a dynamic array. The array can grow or shrink as elements are added or removed.

### Code Example (Python)

```python
class DynamicArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            self._resize(2 * self.capacity)
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        if self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        return item

    def _resize(self, new_capacity):
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.head + i) % self.capacity]
        self.head = 0
        self.tail = self.size
        self.capacity = new_capacity

    def is_full(self):
        return self.tail == self.head

    def is_empty(self):
        return self.head == self.tail

# Example usage
daq = DynamicArrayQueue()
daq.enqueue("John")
daq.enqueue("Alice")
print(daq.dequeue())  # Output: John
print(daq.dequeue())  # Output: Alice
```

## **Multiple Stacks and Queues**

### Definition

A multiple stack and queue is a data structure that combines the features of multiple stacks and queues.

### Characteristics

- Can be implemented using arrays or linked lists
- Can be used to implement complex data structures

### Example

Suppose we have a stack and queue implementation that allows us to push and pop elements from a stack and enqueue and dequeue elements from a queue.

### Code Example (Python)

```python
class MultipleStackAndQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push_stack(self, item):
        self.stack.append(item)

    def pop_stack(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def enqueue_queue(self, item):
        self.queue.append(item)

    def dequeue_queue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

# Example usage
msaq = MultipleStackAndQueue()
msaq.push_stack("John")
msaq.push_stack("Alice")
print(msaq.pop_stack())  # Output: Alice
print(msaq.dequeue_queue())  # Output: John
```

## **Conclusion**

In this module, we have learned about the different types of queues, including circular queues, dynamic arrays, and multiple stacks and queues. We have also learned about the operations that can be performed on these data structures, such as enqueue and dequeue. By understanding and implementing these data structures, we can solve complex problems in computer science.
