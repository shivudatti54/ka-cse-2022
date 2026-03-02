# Chapter 4: 4.5 - Stack Data Structure

=====================================================

## Introduction

---

A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning the last element added to the stack will be the first one to be removed. Stacks are often used in computer science for parsing expressions, evaluating postfix notation, and implementing recursive algorithms.

## Definition

---

A stack is a collection of elements that can be added or removed from the top of the stack.

## Types of Stacks

---

### 1. Linear Stack

A linear stack is a stack that can only contain one element at a time.

### 2. Multidimensional Stack

A multidimensional stack is a stack that can contain multiple elements at a time.

## Operations on a Stack

---

### 1. Push

The push operation adds an element to the top of the stack.

### 2. Pop

The pop operation removes an element from the top of the stack.

### 3. Peek

The peek operation returns the top element of the stack without removing it.

### 4. isEmpty

The isEmpty operation checks if the stack is empty.

### 5. size

The size operation returns the number of elements in the stack.

## Implementation of a Stack

---

### Example in Python

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

    def size(self):
        return len(self.stack)
```

### Example Use Cases

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.isEmpty())  # Output: False
print(stack.size())  # Output: 2
```

## Applications of Stacks

---

### 1. Evaluating Postfix Expressions

Stacks are often used to evaluate postfix expressions, which are expressions where operators follow their operands.

### 2. Implementing Recursive Algorithms

Stacks can be used to implement recursive algorithms by pushing the current state onto the stack and popping it when the algorithm completes.

### 3. Parsing XML and HTML

Stacks are used in the parsing of XML and HTML documents to keep track of the current element and its attributes.

## Key Concepts

---

- LIFO principle
- Push and pop operations
- Peek and isEmpty operations
- Size operation
- Multidimensional stacks
- Linear stacks
- Applications of stacks (evaluating postfix expressions, implementing recursive algorithms, parsing XML and HTML)
