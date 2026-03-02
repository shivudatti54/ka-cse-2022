# **Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

## **Introduction**

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle, meaning the first element added to the queue will be the first one to be removed. Queues are used in various real-world applications such as job scheduling, print queues, and network protocols.

## **Types of Queues**

### 1. Linear Queue

A linear queue is a queue that follows the FIFO principle. It consists of a single array and has two main operations: enqueue (add an element) and dequeue (remove an element).

**Linear Queue Operations**

- **Enqueue**: Adds an element to the end of the queue.
- **Dequeue**: Removes an element from the front of the queue.

**Example:**

```python
class LinearQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

# Create a linear queue
queue = LinearQueue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
```

### 2. Circular Queue

A circular queue is a queue that uses a circular buffer to store elements. It also follows the FIFO principle but has a limited capacity.

**Circular Queue Operations**

- **Enqueue**: Adds an element to the end of the queue, overwriting the oldest element if the queue is full.
- **Dequeue**: Removes an element from the front of the queue, shifting all elements after the removed element to the front of the queue.

**Example:**

```python
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

# Create a circular queue with a capacity of 3
queue = CircularQueue(3)

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
```

### 3. Dynamic Array Queue

A dynamic array queue is a queue that uses a dynamic array as its underlying data structure. It can grow or shrink dynamically as elements are added or removed.

**Dynamic Array Queue Operations**

- **Enqueue**: Adds an element to the end of the queue.
- **Dequeue**: Removes an element from the front of the queue.

**Example:**

```python
class DynamicArrayQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, item):
        if self.size == len(self.array):
            self.array.extend([None] * 10)
        self.array[self.size] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        item = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        return item

# Create a dynamic array queue
queue = DynamicArrayQueue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
```

### 4. Multiple Stacks and Queues

A multiple stacks and queues data structure is a combination of multiple stacks and queues. It allows you to implement a queue using multiple stacks.

**Multiple Stacks and Queues Operations**

- **Push**: Adds an element to the top of a stack.
- **Pop**: Removes an element from the top of a stack.
- **Enqueue**: Adds an element to the end of the queue.
- **Dequeue**: Removes an element from the front of the queue.

**Example:**

```python
class MultipleStacksAndQueues:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.queue = []

    def push_to_stack1(self, item):
        self.stack1.append(item)

    def pop_from_stack1(self):
        if self.stack1:
            return self.stack1.pop()
        return None

    def push_to_stack2(self, item):
        self.stack2.append(item)

    def pop_from_stack2(self):
        if self.stack2:
            return self.stack2.pop()
        return None

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

# Create a multiple stacks and queues data structure
queue = MultipleStacksAndQueues()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)

# Push elements to stack2
queue.push_to_stack2(1)
queue.push_to_stack2(2)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
```

## **Conclusion**

In this study material, we have covered the basics of queues, including linear queues, circular queues, using dynamic arrays, and multiple stacks and queues. We have also provided examples of how to implement these data structures in Python. Understanding these data structures is essential for implementing efficient algorithms and solving real-world problems.
