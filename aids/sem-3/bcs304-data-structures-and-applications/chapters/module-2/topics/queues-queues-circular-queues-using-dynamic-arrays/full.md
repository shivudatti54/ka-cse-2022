# **Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

## **Introduction**

A queue is a fundamental data structure that follows the FIFO (First-In-First-Out) principle, meaning the first element added to the queue will be the first one to be removed. Queues are widely used in various applications, including operating systems, network protocols, and algorithms. In this section, we will delve into the world of queues, exploring their types, implementations, and applications.

## **Historical Context**

The concept of a queue dates back to the 17th century, when French mathematician Blaise Pascal used a queue to model a line of people waiting to enter a salon. The term "queue" was coined from the French word "file," referring to a line of people waiting to be served. In the 19th century, mathematicians like Emile Borel and Henri Lebesgue developed queuing theory, which laid the foundation for modern queue data structures.

## **Queue Data Structure**

A queue is a linear data structure that follows the FIFO principle. It consists of a sequence of elements, known as nodes or entries, which are added to the end of the queue and removed from the front of the queue. Queues can be implemented using various data structures, including arrays, linked lists, and trees.

## **Types of Queues**

### 1. Single Queue

A single queue is the most basic type of queue, where elements are added to the end and removed from the front.

### 2. Circular Queue

A circular queue is a type of queue where the last element is connected to the first element, forming a circle. This implementation is useful when the queue is implemented using an array.

### 3. Double Queue

A double queue is a queue that consists of two queues, one for adding elements and another for removing elements.

### 4. Multi-Queue

A multi-queue is a queue that consists of multiple queues, each with its own set of elements.

## **Implementing Queues Using Dynamic Arrays**

Dynamic arrays can be used to implement queues by modifying the array to accommodate the increasing or decreasing number of elements.

### Example: Implementing a Queue Using a Dynamic Array

```python
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0
```

## **Implementing Queues Using Multiple Stacks**

Multiple stacks can be used to implement queues by using two stacks, one for adding elements and another for removing elements.

### Example: Implementing a Queue Using Multiple Stacks

```python
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
```

## **Applications of Queues**

Queues have numerous applications in various fields, including:

1.  **Operating Systems**: Queues are used to manage processes and threads, ensuring that the operating system can efficiently allocate resources.
2.  **Network Protocols**: Queues are used to manage network packets, ensuring that data is transmitted in the correct order.
3.  **Algorithms**: Queues are used to solve problems, such as job scheduling and resource allocation.
4.  **Database Systems**: Queues are used to manage transactions, ensuring that data is processed in the correct order.

## **Case Studies**

### Case Study 1: Bank Teller System

A bank teller system uses a queue to manage customers. When a customer enters the bank, they are added to the end of the queue. When a teller becomes available, they remove the first customer from the queue and process their transaction.

### Case Study 2: Job Scheduling System

A job scheduling system uses a queue to manage jobs. When a job is submitted, it is added to the end of the queue. The system then executes the jobs in the order they were added to the queue.

## **Conclusion**

In this section, we explored the world of queues, including their types, implementations, and applications. We discussed the historical context of queues and their importance in various fields. We also provided examples of implementing queues using dynamic arrays and multiple stacks. Finally, we highlighted the applications of queues in operating systems, network protocols, algorithms, and database systems.
