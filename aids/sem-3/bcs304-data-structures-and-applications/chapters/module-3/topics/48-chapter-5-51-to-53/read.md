# Data Structures and Applications

## Chapter 4.8: Stacks and Queues

### 5.1: Introduction to Stacks and Queues

In the field of computer science, a stack and a queue are two fundamental data structures that are used to store and manipulate elements.

### 5.2: Stack

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed.

#### Definition:

A stack is a collection of elements that can be added or removed from the top.

#### Properties:

- **LIFO (Last-In-First-Out) principle**: The last element added to the stack will be the first one to be removed.
- **Limited access**: Access to the elements in a stack is limited to the top element.

#### Operations:

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes the top element from the stack.
- **Peek**: Returns the top element without removing it.

#### Example:

Suppose we have a stack with the following elements:

```
[]
```

We perform the following operations:

- **Push**: Add the element "A" to the stack. The stack becomes:

```
[A]
```

- **Push**: Add the element "B" to the stack. The stack becomes:

```
[A, B]
```

- **Pop**: Remove the top element "B" from the stack. The stack becomes:

```
[A]
```

- **Peek**: Return the top element "A" without removing it. The stack remains:

```
[A]
```

### 5.3: Queue

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed.

#### Definition:

A queue is a collection of elements that can be added or removed from the front.

#### Properties:

- **FIFO (First-In-First-Out) principle**: The first element added to the queue will be the first one to be removed.
- **First-In-First-Out**: The queue is designed to serve the elements in the order they were added.

#### Operations:

- **Enqueue**: Adds an element to the end of the queue.
- **Dequeue**: Removes the front element from the queue.
- **Peek**: Returns the front element without removing it.

#### Example:

Suppose we have a queue with the following elements:

```
[]
```

We perform the following operations:

- **Enqueue**: Add the element "A" to the end of the queue. The queue becomes:

```
[A]
```

- **Enqueue**: Add the element "B" to the end of the queue. The queue becomes:

```
[A, B]
```

- **Dequeue**: Remove the front element "A" from the queue. The queue becomes:

```
[B]
```

- **Peek**: Return the front element "B" without removing it. The queue remains:

```
[B]
```

### Key Concepts

- **Stack**: A linear data structure that follows the LIFO principle.
- **Queue**: A linear data structure that follows the FIFO principle.
- **Push**: Adds an element to the top of the stack or the end of the queue.
- **Pop**: Removes the top element from the stack or the front element from the queue.
- **Peek**: Returns the top element from the stack or the front element from the queue without removing it.
