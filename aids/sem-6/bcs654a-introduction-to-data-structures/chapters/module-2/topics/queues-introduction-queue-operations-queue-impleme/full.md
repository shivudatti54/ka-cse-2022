# **INTRODUCTION TO QUEUES: DATA STRUCTURES AND ALGORITHMS**

## **Table of Contents**

1. [Introduction to Queues](#introduction-to-queues)
2. [Queue Operations](#queue-operations)
3. [Queue Implementation using Arrays](#queue-implementation-using-arrays)
4. [Different Types of Queues](#different-types-of-queues)
   - [Circular Queues](#circular-queues)
   - [Double-Ended Queues](#double-ended-queues)
   - [Priority Queues](#priority-queues)
5. [Applications and Case Studies](#applications-and-case-studies)
6. [Conclusion](#conclusion)
7. [Further Reading](#further-reading)

## **Introduction to Queues**

A queue, also known as a line or a queue data structure, is a basic data structure that follows the First-In-First-Out (FIFO) principle. This means that the element that is added first will be the first one to be removed. Queues are used to manage a line of people waiting for an event or service.

Queues are used in various applications such as:

- Job scheduling and workflow management
- Network protocols (e.g., TCP/IP)
- Print queues
- Online shopping systems
- Airlines and airports

## **Queue Operations**

Queues support the following operations:

- **Enqueue (Add)**: adds an element to the end of the queue
- **Dequeue (Remove)**: removes an element from the front of the queue
- **Peek (Front)**: returns the element at the front of the queue without removing it
- **IsEmpty**: checks if the queue is empty
- **Size (Length)**: returns the number of elements in the queue

### Example Use Case

Suppose we are managing a job scheduling system. We have a queue of jobs, and we want to add a new job to the queue.

| Operation         | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| Enqueue (Add Job) | Add the new job to the end of the queue                     |
| Dequeue (Run Job) | Remove and run the job at the front of the queue            |
| Peek (Front Job)  | Return the job at the front of the queue without running it |
| IsEmpty           | Check if the queue is empty                                 |
| Size (Length)     | Return the number of jobs in the queue                      |

## **Queue Implementation using Arrays**

An array-based queue implementation can be done using a fixed-size array. We can use the following indices to represent the queue:

| Index    | Description        |
| -------- | ------------------ |
| 0        | Front of the queue |
| size - 1 | Rear of the queue  |

Here's a step-by-step implementation of an array-based queue:

1.  Create an array of a fixed size to represent the queue.
2.  Initialize the front and rear indices to 0.
3.  When enqueuing, increment the rear index and check if we have reached the end of the array. If we have, we need to resize the array.
4.  When dequeuing, increment the front index and check if we have reached the beginning of the array. If we have, we need to handle the case where the queue is empty.
5.  When peeking, return the element at the front index without incrementing the front index.

Here's a simple example of an array-based queue implementation in Python:

```python
class ArrayQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = [None] * maxSize
        self.rear = 0
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.maxSize:
            self.maxSize *= 2
            newQueue = [None] * self.maxSize
            for i in range(self.front, self.rear):
                newQueue[i - self.front] = self.queue[i]
            self.queue = newQueue
            self.front = 0
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.maxSize
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size
```

## **Different Types of Queues**

### Circular Queues

A circular queue is a type of queue that follows the FIFO principle and uses a single array or list to store the elements. It is called "circular" because the rear index wraps around to the beginning of the array when it reaches the end.

**Example Use Case**

Suppose we are implementing a DNS resolver. We have a circular queue to store the DNS records for different domains.

| Operation                | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| Enqueue (Add Record)     | Add the new DNS record to the end of the queue                       |
| Dequeue (Resolve Record) | Remove and resolve the DNS record at the front of the queue          |
| Peek (Front Record)      | Return the DNS record at the front of the queue without resolving it |
| IsEmpty                  | Check if the queue is empty                                          |
| Size (Length)            | Return the number of DNS records in the queue                        |

### Double-Ended Queues

A double-ended queue (deque) is a type of queue that allows elements to be added or removed from both the front and rear of the queue. It is also known as a stack or a queue with a twist.

**Example Use Case**

Suppose we are implementing a job scheduler. We have a deque to store the jobs that need to be executed. We can add jobs to the front of the deque and remove them from the rear of the deque.

| Operation         | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| Enqueue (Add Job) | Add the new job to the front of the deque                   |
| Dequeue (Run Job) | Remove and run the job from the rear of the deque           |
| Peek (Front Job)  | Return the job at the front of the deque without running it |
| IsEmpty (Front)   | Check if the deque is empty at the front                    |
| IsEmpty (Rear)    | Check if the deque is empty at the rear                     |
| Size (Length)     | Return the number of jobs in the deque                      |

### Priority Queues

A priority queue is a type of queue that allows the elements to be ordered based on their priority. The element with the highest priority is at the front of the queue.

**Example Use Case**

Suppose we are implementing a medical emergency room. We have a priority queue to store the patients who need to be treated. We can add patients to the queue based on their priority.

| Operation               | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| Enqueue (Add Patient)   | Add the new patient to the front of the queue based on their priority |
| Dequeue (Treat Patient) | Remove and treat the patient at the front of the queue                |
| Peek (Front Patient)    | Return the patient at the front of the queue without treating them    |
| IsEmpty                 | Check if the queue is empty                                           |
| Size (Length)           | Return the number of patients in the queue                            |

## **Applications and Case Studies**

Queues have various applications in real-world systems. Here are a few examples:

- **Web Servers**: Web servers use queues to handle incoming HTTP requests. The request is added to the queue, and the server processes it when it becomes available.
- **Printers**: Printers use queues to manage the print jobs. The print job is added to the queue, and the printer processes it when it becomes available.
- **Air Traffic Control**: Air traffic control uses queues to manage the flights. The flight is added to the queue, and the air traffic controller processes it when it becomes available.
- **Network Protocols**: Network protocols use queues to manage the data packets. The packet is added to the queue, and the network process it when it becomes available.

## **Conclusion**

In conclusion, queues are a fundamental data structure that follows the FIFO principle. They are used in various applications, including job scheduling, network protocols, and print queues. We have discussed the different types of queues, including circular queues, double-ended queues, and priority queues. We have also provided examples of queue implementations using arrays and discussed the applications and case studies of queues.

## **Further Reading**

- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms in Python" by Michael T. Goodrich
- "Queue" by Wikipedia
- "Circular Queue" by Wikipedia
- "Double-Ended Queue" by Wikipedia
- "Priority Queue" by Wikipedia
