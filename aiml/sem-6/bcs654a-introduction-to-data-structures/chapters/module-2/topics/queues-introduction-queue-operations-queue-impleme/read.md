# Queues: Introduction, Queue Operations, and Different Types of Queues

===========================================================

## Introduction to Queues

---

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. Queues are also known as "lines" or "buffers" because they represent a line of people waiting to be served.

### Definition:

A queue is a collection of elements that are ordered in a way that the first element added to the queue is the first one to be removed.

### Characteristics:

- FIFO (First-In-First-Out) principle
- Elements are added and removed from the end of the queue
- Elements are removed in the order they were added

### Operations:

- `enqueue`: adds an element to the end of the queue
- `dequeue`: removes an element from the front of the queue
- `isEmpty`: checks if the queue is empty
- `size`: returns the number of elements in the queue

## Queue Operations

---

### Enqueue Operation:

The `enqueue` operation adds an element to the end of the queue. This operation is usually implemented using an array and involves shifting all elements to the right to make room for the new element.

### Dequeue Operation:

The `dequeue` operation removes an element from the front of the queue. This operation is usually implemented using an array and involves shifting all elements to the left to fill the gap created by the removed element.

### Example:

Suppose we have a queue implemented using an array and we want to add the elements 1, 2, and 3 to the queue.

| Index | Element |
| ----- | ------- |
| 0     | -       |
| 1     | -       |
| 2     | -       |
| 3     | -       |

After adding the elements using `enqueue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 0     | 1       |
| 1     | 2       |
| 2     | 3       |
| 3     | -       |

After removing the element using `dequeue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 0     | 2       |
| 1     | 3       |
| 2     | -       |
| 3     | -       |

## Queue Implementation using Arrays

---

Here is an example of a queue implementation using an array in Python:

```python
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, element):
        if self.size == self.max_size:
            print("Queue is full")
            return
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return temp

    def display(self):
        for i in range(self.size):
            print(self.queue[i], end=" ")

# Example usage:
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # prints: 1 2 3
q.dequeue()
q.display()  # prints: 2 3
```

## Different Types of Queues

---

### Circular Queues

---

A circular queue is a type of queue where the last element is connected to the first element, forming a circle.

### Characteristics:

- FIFO principle
- Elements are added and removed from the end of the queue
- Elements are removed in the order they were added
- No need to worry about overflow or underflow

### Operations:

- `enqueue`: adds an element to the end of the queue
- `dequeue`: removes an element from the front of the queue
- `isEmpty`: checks if the queue is empty
- `size`: returns the number of elements in the queue

### Example:

Suppose we have a circular queue and we want to add the elements 1, 2, and 3 to the queue.

| Index | Element |
| ----- | ------- |
| 0     | -       |
| 1     | -       |
| 2     | -       |
| 3     | -       |
| 4     | -       |

After adding the elements using `enqueue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 0     | 1       |
| 1     | 2       |
| 2     | 3       |
| 3     | -       |
| 4     | -       |

After removing the element using `dequeue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 1     | 2       |
| 2     | 3       |
| 3     | -       |
| 0     | 1       |
| 4     | -       |

### Double-Ended Queues

---

A double-ended queue is a type of queue where elements can be added and removed from both ends.

### Characteristics:

- FIFO principle
- Elements can be added and removed from both ends
- Elements are removed in the order they were added
- No need to worry about overflow or underflow

### Operations:

- `enqueue`: adds an element to the end of the queue
- `dequeue`: removes an element from the front of the queue
- `isEmpty`: checks if the queue is empty
- `size`: returns the number of elements in the queue

### Example:

Suppose we have a double-ended queue and we want to add the elements 1 and 2 to the queue.

| Index | Element |
| ----- | ------- |
| 0     | -       |
| 1     | -       |

After adding the elements using `enqueue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 0     | 1       |
| 1     | 2       |

After removing the element from the front using `dequeue`, the queue becomes:

| Index | Element |
| ----- | ------- |
| 0     | 2       |
| 1     | -       |

### Priority Queues

---

A priority queue is a type of queue where elements are ordered based on their priority.

### Characteristics:

- Elements are ordered based on their priority
- Elements are removed in the order of their priority
- No need to worry about overflow or underflow

### Operations:

- `enqueue`: adds an element to the queue with a specified priority
- `dequeue`: removes an element from the queue with the highest priority
- `isEmpty`: checks if the queue is empty
- `size`: returns the number of elements in the queue

### Example:

Suppose we have a priority queue and we want to add the elements 1 and 2 to the queue with priorities 2 and 1, respectively.

| Index | Element | Priority |
| ----- | ------- | -------- |
| 0     | -       | -        |
| 1     | -       | -        |

After adding the elements using `enqueue`, the queue becomes:

| Index | Element | Priority |
| ----- | ------- | -------- |
| 0     | 1       | 2        |
| 1     | 2       | 1        |

After removing the element with the highest priority using `dequeue`, the queue becomes:

| Index | Element | Priority |
| ----- | ------- | -------- |
| 0     | 2       | 1        |
| 1     | -       | -        |
