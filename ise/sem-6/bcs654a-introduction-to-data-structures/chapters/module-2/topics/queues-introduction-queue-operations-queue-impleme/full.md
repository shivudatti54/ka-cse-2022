# **Queues: Introduction, Queue Operations, Queue Implementation using Arrays, Different Types of Queues: Circular Queues, Double-Ended Queues, Priority Q**

## **Introduction**

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It is a collection of elements that are ordered in a sequence, and elements are added to the end of the queue and removed from the front. Queues are used in many applications, including job scheduling, print queues, and banking systems.

## **Queue Operations**

A queue supports the following operations:

1.  **Enqueue**: Adds an element to the end of the queue.
2.  **Dequeue**: Removes an element from the front of the queue.
3.  **Peek**: Returns the element at the front of the queue without removing it.
4.  **IsEmpty**: Checks if the queue is empty.
5.  **Size**: Returns the number of elements in the queue.

## **Queue Implementation using Arrays**

Here is a basic implementation of a queue using an array in Python:

```python
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_size:
            print("Queue is full")
            return
        self.queue[self.rear] = item
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

    def peek(self):
        if self.size == 0:
            print("Queue is empty")
            return
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
```

## **Different Types of Queues**

### Circular Queues

A circular queue is a type of queue where the last element is connected to the first element, forming a circle. This type of queue is used when the maximum number of elements is fixed, and the element that is removed from the front of the queue needs to be added to the end of the queue.

Here is an implementation of a circular queue in Python:

```python
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_size:
            print("Queue is full")
            return
        self.queue[self.rear] = item
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

    def peek(self):
        if self.size == 0:
            print("Queue is empty")
            return
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
```

### Double-Ended Queues

A double-ended queue is a type of queue where elements can be added to both the beginning and the end of the queue. This type of queue is used when the user needs to add elements to both ends of the queue.

Here is an implementation of a double-ended queue in Python:

```python
class DoubleEndedQueue:
    def __init__(self):
        self.queue = []

    def add_front(self, item):
        self.queue.insert(0, item)

    def add_rear(self, item):
        self.queue.append(item)

    def remove_front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        return self.queue.pop(0)

    def remove_rear(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        return self.queue.pop()

    def peek_front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        return self.queue[0]

    def peek_rear(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)
```

### Priority Queues

A priority queue is a type of queue where elements are ordered based on their priority. This type of queue is used when the user needs to prioritize certain elements.

Here is an implementation of a priority queue in Python:

```python
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        item = self.queue.pop(0)
        return item[0]

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        return self.queue[0][0]

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)
```

## **Applications of Queues**

Queues have many applications in various fields, including:

1.  **Job Scheduling**: Queues can be used to schedule tasks in a system.
2.  **Print Queues**: Queues can be used to manage print jobs in a print server.
3.  **Banking Systems**: Queues can be used to manage customer transactions in a bank.
4.  **Job Scheduling**: Queues can be used to schedule tasks in a system.
5.  **Network Protocols**: Queues can be used to manage network packets.

## **Case Study**

Suppose we have a bank with several branches, and each branch has a limited number of tellers. The bank has a system to manage customer transactions, which uses a queue to manage the transactions.

The system has the following requirements:

1.  The system should be able to handle a large number of transactions.
2.  The system should be able to prioritize transactions based on the type of transaction (e.g., deposits, withdrawals, etc.).
3.  The system should be able to manage the tellers' workload.

The system can use a priority queue to manage the transactions. The tellers are assigned a priority based on their workload, and the transactions are prioritized based on the type of transaction.

## **Conclusion**

Queues are a fundamental data structure in computer science, and they have many applications in various fields. Understanding queues and how to implement them can help you solve many real-world problems.

## **Further Reading**

1.  "Introduction to Algorithms" by Thomas H. Cormen
2.  "Data Structures and Algorithms in Python" by Michael T. Goodrich
3.  "Queues and Stacks" by Donald E. Knuth
4.  "Algorithm Design" by Robert Sedgewick and Kevin Wayne
5.  "Data Structures and Algorithms" by MIT OpenCourseWare
