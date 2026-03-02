# Chapter 5: Advanced Data Structures

=====================================

## 5.1: Stacks

---

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. This means the last element added to the stack will be the first one to be removed.

### Key Concepts:

- **Stack Operations:**
  - **Push:** Adding an element to the top of the stack.
  - **Pop:** Removing an element from the top of the stack.
  - **Peek:** Looking at the top element of the stack without removing it.
  - **IsEmpty:** Checking if the stack is empty.
- **Applications:**
  - **Evaluating postfix expressions:**
    - Example: `3 4 + 2 *` can be evaluated as `(3 + (4 * 2))`
  - **Parsing expressions:**
    - Example: Using a stack to parse expressions like `((a + b) * c)`
  - **Undo/Redo functionality:**
    - Example: A text editor that uses a stack to keep track of the last few edits

### Code Example (Python):

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # prints 2
print(stack.pop())    # prints 2
print(stack.is_empty())  # prints False
```

## 5.2: Queues

---

A queue is a linear data structure that follows the FIFO (First In First Out) principle. This means the first element added to the queue will be the first one to be removed.

### Key Concepts:

- **Queue Operations:**
  - **Enqueue:** Adding an element to the end of the queue.
  - **Dequeue:** Removing an element from the front of the queue.
  - **Peek:** Looking at the front element of the queue without removing it.
  - **IsEmpty:** Checking if the queue is empty.
- **Applications:**
  - **Job scheduling:**
    - Example: A printer that uses a queue to manage print jobs
  - **Network communication:**
    - Example: A server that uses a queue to handle incoming requests
  - **Bank teller system:**
    - Example: A bank that uses a queue to manage customer transactions

### Code Example (Python):

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())  # prints 1
print(queue.dequeue())  # prints 1
print(queue.is_empty())  # prints False
```

## 5.3: Trees

---

A tree is a non-linear data structure where each node has at most two children (i.e., left child and right child).

### Key Concepts:

- **Node:**
  - A single element in the tree.
- **Edge:**
  - A connection between two nodes.
- **Tree Operations:**
  - **Insert:** Adding a new node to the tree.
  - **Delete:** Removing a node from the tree.
  - **Search:** Finding a node in the tree.
- **Types of Trees:**
  - **Binary Search Tree (BST):**
    - A tree where each node has a unique key and all keys in the left subtree are less than the node's key, while all keys in the right subtree are greater.
  - **AVL Tree:**
    - A self-balancing BST that ensures the height of the tree remains relatively constant even after insertions and deletions.

### Code Example (Python):

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

# Example usage:
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
print(tree.search(3).key)  # prints 3
```

I hope this comprehensive study material helps you understand the concepts of stacks, queues, and trees.
