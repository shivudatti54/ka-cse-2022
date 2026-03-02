# Queues: Introduction, Queue Operations, Queue Implementation using Arrays, Different Types of Queues

====================================================

## Introduction to Queues

---

A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle. It means the first element that is added to the queue is the first one to be removed.

### Definition:

A queue is a collection of elements that are ordered in a particular way, and elements are added or removed from the queue in a specific order.

### Properties:

- FIFO (First-In-First-Out)
- One end is known as the front and the other is known as the rear
- Elements are added to the rear of the queue
- Elements are removed from the front of the queue

### Operations:

- `enqueue(element)`: adds an element to the rear of the queue
- `dequeue()`: removes an element from the front of the queue
- `peek()`: returns the element at the front of the queue without removing it
- `isEmpty()`: checks if the queue is empty

## Queue Operations

---

### Enqueue

- Adds an element to the rear of the queue
- Example: `enqueue(5)` adds 5 to the rear of the queue

### Dequeue

- Removes an element from the front of the queue
- Example: `dequeue()` removes the front element from the queue

### Peek

- Returns the element at the front of the queue without removing it
- Example: `peek()` returns the front element without removing it

### IsEmpty

- Checks if the queue is empty
- Example: `isEmpty()` checks if the queue is empty

## Queue Implementation using Arrays

---

### Array-Based Queue Implementation

A queue can be implemented using an array. The array has two pointers, `front` and `rear`, to keep track of the front and rear elements.

```python
class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, element):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.data[self.rear] = element
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        element = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return element

    def peek(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.data[self.front]

    def isEmpty(self):
        return self.size == 0
```

### Example Usage

```python
queue = ArrayQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # prints 1
print(queue.peek())     # prints 2
```

## Different Types of Queues

---

### Circular Queues

A circular queue is similar to a regular queue, but it uses a circular array to store elements. The rear of the queue is connected to the front of the queue, forming a circle.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, element):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return element

    def peek(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def isEmpty(self):
        return self.size == 0
```

### Double-Ended Queues (Deques)

A deque is a data structure that allows adding or removing elements from both the front and rear of the queue.

```python
class Deque:
    def __init__(self):
        self.data = []

    def append(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0
```

### Priority Queues

A priority queue is a queue where elements are ordered based on their priority. The highest priority element is removed first.

```python
class PriorityQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, element, priority):
        self.data.append((element, priority))

    def dequeue(self):
        return self.data.pop(0)[0]

    def peek(self):
        return self.data[0][0]

    def isEmpty(self):
        return len(self.data) == 0
```

### Example Usage

```python
priority_queue = PriorityQueue()
priority_queue.enqueue(1, 3)
priority_queue.enqueue(2, 1)
priority_queue.enqueue(3, 2)
print(priority_queue.dequeue())  # prints 3
```
