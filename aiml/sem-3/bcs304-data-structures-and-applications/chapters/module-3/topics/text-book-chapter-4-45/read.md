# **Chapter 4: Data Structures and Applications**

## **4.5: Stacks and Queues**

### Introduction

---

A stack and a queue are two types of data structures that are used to store and retrieve elements in a specific order. A stack follows the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first one to be removed. A queue, on the other hand, follows the First-In-First-Out (FIFO) principle, where the first element added to the queue is the first one to be removed.

### Stack

---

A stack is a data structure that follows the LIFO principle. It is a linear collection of elements, where each element is added and removed from the top of the stack.

**Key Characteristics of a Stack:**

- Last-In-First-Out (LIFO) principle
- Elements are added and removed from the top of the stack
- Can only access the top element

### Queue

---

A queue is a data structure that follows the FIFO principle. It is a linear collection of elements, where elements are added to the end of the queue and removed from the front of the queue.

**Key Characteristics of a Queue:**

- First-In-First-Out (FIFO) principle
- Elements are added to the end of the queue and removed from the front of the queue
- Can access all elements

### Types of Stacks and Queues

---

There are two types of stacks:

- **Basic Stack:** A basic stack is a stack that can only store elements of a single data type.
- **Generic Stack:** A generic stack is a stack that can store elements of any data type.

There are two types of queues:

- **Basic Queue:** A basic queue is a queue that can only store elements of a single data type.
- **Generic Queue:** A generic queue is a queue that can store elements of any data type.

### Operations on Stacks and Queues

---

Stacks and queues support the following operations:

- **Push:** Adds an element to the top of the stack or the end of the queue.
- **Pop:** Removes an element from the top of the stack or the front of the queue.
- **Peek:** Returns the top element of the stack or the front element of the queue without removing it.
- **isEmpty:** Checks if the stack or queue is empty.
- **size:** Returns the number of elements in the stack or queue.

### Examples of Stacks and Queues

---

**Stack Example:**

```
         1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

This is a stack where the elements are pushed onto the stack in the order 1, 2, 3, 4, 5, 6, 7.

**Queue Example:**

```
     1
    / \
   2   3
  / \   \
 4   5   6
```

This is a queue where the elements are added to the front of the queue in the order 1, 2, 3, 4, 5, 6.

### Code Implementation

---

Here is an example implementation of a stack and a queue in Python:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0

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
```

### Conclusion

---

In this chapter, we learned about stacks and queues, two fundamental data structures that are used to store and retrieve elements in a specific order. We also learned about the key characteristics of stacks and queues, types of stacks and queues, operations that can be performed on them, and examples of their usage.
