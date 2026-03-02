# Textbook 2: Ch

## INTRODUCTION TO DATA STRUCTURES

### Module: @#@10012025

### Topic: Textbook 2: Ch

## 1. Introduction

In this topic, we will delve into the world of data structures, a crucial concept in computer science. Data structures are the way we organize and store data in a computer so that we can efficiently retrieve and manipulate it. In this topic, we will explore the concept of stacks, which is represented by the letter "Ch" in the topic title.

## 2. Historical Context

The concept of stacks dates back to the early days of computer science. In 1962, Edsger W. Dijkstra and Peter N. van Emden introduced the concept of a stack in their paper "The Structure of Structured Programs". They described a stack as a Last-In-First-Out (LIFO) data structure, where the last element added to the stack is the first one to be removed.

## 3. Modern Developments

In modern computer science, stacks are used extensively in various applications, such as:

- **Parser implementation**: Stacks are used to parse the syntactic structure of programming languages.
- **Undo/Redo functionality**: Stacks are used to implement the undo and redo functionality in text editors and other applications.
- **Evaluating postfix expressions**: Stacks are used to evaluate postfix expressions, also known as Reverse Polish Notation.

## 4. Stack Data Structure

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning the last element added to the stack will be the first one to be removed.

### **Stack Operations**

There are three primary operations that can be performed on a stack:

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes the top element from the stack.
- **Peek**: Returns the top element from the stack without removing it.

### **Stack Implementation**

There are two primary ways to implement a stack:

- **Array-based implementation**: Uses an array to store the elements of the stack.
- **Linked list-based implementation**: Uses a linked list to store the elements of the stack.

### **Example Implementation (Array-based)**

```python
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def push(self, data):
        if self.top < self.max_size - 1:
            self.top += 1
            self.stack[self.top] = data
        else:
            print("Stack is full")

    def pop(self):
        if self.top != -1:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return data
        else:
            print("Stack is empty")

    def peek(self):
        if self.top != -1:
            return self.stack[self.top]
        else:
            print("Stack is empty")

# Example usage:
stack = Stack(5)
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
```

## 5. Applications of Stacks

Stacks have numerous applications in real-world scenarios, including:

- **Compiler design**: Stacks are used to parse the syntactic structure of programming languages.
- **Game development**: Stacks are used to implement the undo and redo functionality in game editors.
- **Scientific computing**: Stacks are used to evaluate postfix expressions and perform mathematical operations.

## 6. Case Study: Evaluating Postfix Expressions

Postfix expressions, also known as Reverse Polish Notation (RPN), are a way of writing mathematical expressions where operators follow their operands. Stacks are used to evaluate postfix expressions.

### **Example Expression**

The expression `3 4 +` can be evaluated using a stack.

```python
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]

expression = "3 4 +"
result = evaluate_postfix(expression)
print(result)  # Output: 7
```

## 7. Further Reading

- "The Structure of Structured Programs" by Edsger W. Dijkstra and Peter N. van Emden
- "Introduction to Algorithms" by Thomas H. Cormen
- "Data Structures and Algorithms in Python" by Michael T. Goodrich, Robert S. Tarjan, and David R. Musser

This concludes our deep dive into the topic of stacks. We have explored the historical context, modern developments, and applications of stacks. We have also implemented an array-based stack and evaluated postfix expressions using a stack.
