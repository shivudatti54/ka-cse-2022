# **Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

## **What is a Queue?**

A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle, meaning that the first element added to the queue will be the first one to be removed.

### Characteristics of a Queue:

- Elements are added to the end of the queue.
- Elements are removed from the front of the queue.
- No duplicate elements are allowed in a queue.
- A queue is a First-In-First-Out (FIFO) data structure.

### Operations on a Queue:

- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove an element from the front of the queue.
- Peek: Return the element at the front of the queue without removing it.
- isEmpty: Check if the queue is empty.
- size: Return the number of elements in the queue.

**Example of a Queue:**

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Create a queue
q = Queue()

# Enqueue elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Dequeue elements
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
```

## **Circular Queue:**

A circular queue is a type of queue where the last element is connected to the first element, forming a circle.

### Characteristics of a Circular Queue:

- Elements are added to the end of the queue.
- Elements are removed from the front of the queue.
- No duplicate elements are allowed in a circular queue.
- A circular queue is a First-In-First-Out (FIFO) data structure.

### Operations on a Circular Queue:

- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove an element from the front of the queue.
- Peek: Return the element at the front of the queue without removing it.
- isEmpty: Check if the queue is empty.
- size: Return the number of elements in the queue.

## **Using Dynamic Arrays:**

Dynamic arrays are used to implement queues. They are used to store elements in a contiguous block of memory.

### Characteristics of Dynamic Arrays:

- Elements are stored in a contiguous block of memory.
- The size of the array can be changed dynamically.

### Example of a Queue using Dynamic Arrays:

```python
class DynamicArrayQueue:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.size = 0
        self.queue = [None] * self.capacity

    def enqueue(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.queue[self.size] = element
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        element = self.queue[0]
        self.queue[0] = self.queue[self.size - 1]
        self.queue[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        return element

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return self.size == 0

    def _resize(self, new_capacity):
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[i]
        self.capacity = new_capacity
        self.queue = new_queue

# Create a queue
q = DynamicArrayQueue(2)

# Enqueue elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Dequeue elements
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
```

## **Multiple Stacks and Queues:**

A stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle. You can create a multiple stack and queue by combining two stacks and two queues.

### Characteristics of Multiple Stacks and Queues:

- Can be combined to create multiple stacks and queues.
- Can be used to implement various algorithms and data structures.

### Example of Multiple Stacks and Queues:

```python
class MultipleStacksAndQueues:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.queue1 = []
        self.queue2 = []

    def add_to_stack1(self, element):
        self.stack1.append(element)

    def add_to_stack2(self, element):
        self.stack2.append(element)

    def add_to_queue1(self, element):
        self.queue1.append(element)

    def add_to_queue2(self, element):
        self.queue2.append(element)

    def get_from_stack1(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            return None

    def get_from_stack2(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def get_from_queue1(self):
        if self.queue1:
            return self.queue1.pop(0)
        else:
            return None

    def get_from_queue2(self):
        if self.queue2:
            return self.queue2.pop(0)
        else:
            return None

# Create a multiple stacks and queues
msq = MultipleStacksAndQueues()

# Add elements to stacks and queues
msq.add_to_stack1(1)
msq.add_to_stack2(2)
msq.add_to_queue1(3)
msq.add_to_queue2(4)

# Get elements from stacks and queues
print(msq.get_from_stack1())  # Output: 1
print(msq.get_from_stack2())  # Output: 2
print(msq.get_from_queue1())  # Output: 3
print(msq.get_from_queue2())  # Output: 4
```
