# **Queues: Introduction, Queue Operations, Queue Implementation using Arrays, Different Types of Queues**

## **1. Introduction to Queues**

A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle, meaning the first element that is added to the queue will be the first one to be removed. Queues are commonly used in many real-world applications such as print queues, job queues, and banking systems.

### Characteristics of a Queue

- Elements are added to the end of the queue.
- Elements are removed from the front of the queue.
- No element can be inserted or removed from anywhere except the front and rear.
- The order of removal is the same as the order of insertion.

### Operations on a Queue

- **Enqueue**: Adding an element to the end of the queue.
- **Dequeue**: Removing an element from the front of the queue.
- **Peek**: Looking at the front element of the queue without removing it.
- **Is Empty**: Checking if the queue is empty.

## **2. Queue Operations**

### Enqueue Operation

The enqueue operation involves adding an element to the end of the queue. This operation can be performed in constant time, making it one of the fastest operations in a queue.

### Dequeue Operation

The dequeue operation involves removing an element from the front of the queue. This operation can also be performed in constant time.

### Peek Operation

The peek operation involves looking at the front element of the queue without removing it. This operation can be performed in constant time.

### Is Empty Operation

The is empty operation involves checking if the queue is empty. This operation can be performed in constant time.

### Example

```markdown
Suppose we have a queue and we add 5 elements to it:
Enqueue(1)
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)

After these operations, the queue is:
1 -> 2 -> 3 -> 4 -> 5

Now we dequeue an element:
Dequeue(1)

After this operation, the queue becomes:
2 -> 3 -> 4 -> 5

We can peak at the front element:
Peek(2)

We can check if the queue is empty:
Is Empty() returns False
```

## **3. Queue Implementation using Arrays**

### Array-Based Queue Implementation

Here is an example implementation of a queue using an array:

```markdown
class Queue:
def **init**(self, size):
self.size = size
self.queue = [None] \* size
self.front = 0
self.rear = 0
self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            raise Exception('Queue is full')
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is empty')
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.count == 0:
            raise Exception('Queue is empty')
        return self.queue[self.front]

    def isEmpty(self):
        return self.count == 0
```

## **4. Different Types of Queues**

### Circular Queues

A circular queue is a type of queue where the wrap around occurs after the last element, i.e., the next element is added at the beginning of the array.

### Double-Ended Queues

A double-ended queue is a type of queue where elements can be added or removed from both ends.

### Priority Queues

A priority queue is a type of queue where elements are ordered based on their priority.

### Example of Circular Queue

```markdown
class CircularQueue:
def **init**(self, size):
self.queue = [None] \* size
self.front = 0
self.rear = 0
self.size = size
self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            raise Exception('Queue is full')
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is empty')
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.count == 0:
            raise Exception('Queue is empty')
        return self.queue[self.front]

    def isEmpty(self):
        return self.count == 0
```

### Example of Double-Ended Queue

```markdown
class DoubleEndedQueue:
def **init**(self):
self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception('Queue is empty')
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            raise Exception('Queue is empty')
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
```

### Example of Priority Queue

```markdown
class PriorityQueue:
def **init**(self):
self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception('Queue is empty')
        return self.queue.pop(0)[0]

    def peek(self):
        if len(self.queue) == 0:
            raise Exception('Queue is empty')
        return self.queue[0][0]

    def isEmpty(self):
        return len(self.queue) == 0
```
