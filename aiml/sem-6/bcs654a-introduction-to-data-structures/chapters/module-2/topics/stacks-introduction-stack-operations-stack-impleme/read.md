# **Stacks: Introduction, Stack Operations, Stack Implementation using Arrays, Applications of Stacks**

## **1. Introduction to Stacks**

### Definition

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It is called a stack because it is similar to a physical stack of plates. Plates are added and removed from the top of the stack.

### Properties

- A stack is a collection of elements that can be added or removed from the top.
- Elements in a stack are added and removed from the top using two operations: push and pop.
- The last element inserted into the stack is the first one to be removed.

### Types of Stacks

- **Array Stack**: A stack implemented using an array.
- **Link Stack**: A stack implemented using linked lists.

### Operations on Stacks

#### Push Operation

The push operation adds an element to the top of the stack.

- Example: `stack.push(5)` adds 5 to the top of the stack.

#### Pop Operation

The pop operation removes the top element from the stack.

- Example: `stack.pop()` removes the top element from the stack.

#### Peek Operation

The peek operation returns the top element of the stack without removing it.

- Example: `stack.peek()` returns the top element of the stack without removing it.

#### isEmpty Operation

The isEmpty operation checks if the stack is empty.

- Example: `stack.isEmpty()` returns true if the stack is empty, false otherwise.

## **2. Stack Operations**

### Push Operation

The push operation is used to add an element to the top of the stack.

- Example: `stack.push(5)` adds 5 to the top of the stack.

### Pop Operation

The pop operation is used to remove the top element from the stack.

- Example: `stack.pop()` removes the top element from the stack.

### Peek Operation

The peek operation is used to return the top element of the stack without removing it.

- Example: `stack.peek()` returns the top element of the stack without removing it.

### isEmpty Operation

The isEmpty operation is used to check if the stack is empty.

- Example: `stack.isEmpty()` returns true if the stack is empty, false otherwise.

## **3. Stack Implementation using Arrays**

### Array Stack Implementation

A stack can be implemented using an array.

- Example:
  ```java
  public class ArrayStack {
  private int[] stack;
  private int top;

      public ArrayStack(int capacity) {
          stack = new int[capacity];
          top = -1;
      }

      public void push(int element) {
          if (top < stack.length - 1) {
              stack[++top] = element;
          } else {
              System.out.println("Stack is full");
          }
      }

      public int pop() {
          if (top >= 0) {
              return stack[top--];
          } else {
              System.out.println("Stack is empty");
              return -1;
          }
      }

      public int peek() {
          if (top >= 0) {
              return stack[top];
          } else {
              System.out.println("Stack is empty");
              return -1;
          }
      }

      public boolean isEmpty() {
          return top == -1;
      }

  }

````

### Example Usage

```java
public class Main {
    public static void main(String[] args) {
        ArrayStack stack = new ArrayStack(5);
        stack.push(5);
        stack.push(10);
        stack.push(15);
        System.out.println(stack.pop()); // prints 15
        System.out.println(stack.peek()); // prints 10
        System.out.println(stack.isEmpty()); // prints false
    }
}
````

## **4. Applications of Stacks**

### Evaluating Postfix Expressions

Stacks can be used to evaluate postfix expressions.

- Example: `E = (A + B) * C` can be evaluated as `((A + B) * C)`.

### Implementing Recursive Functions

Stacks can be used to implement recursive functions iteratively.

- Example: The factorial function can be implemented using a stack.

### Parsing Expressions

Stacks can be used to parse expressions.

- Example: The expression `E = (A + B) * C` can be parsed using a stack.

### Implementing Undo and Redo Functionality

Stacks can be used to implement undo and redo functionality.

- Example: The undo and redo functionality can be implemented using a stack.

### Implementing Backtracking Algorithms

Stacks can be used to implement backtracking algorithms.

- Example: The N-Queens problem can be solved using a stack.

In conclusion, stacks are a fundamental data structure in computer science, and they have numerous applications in programming. Understanding stacks and their operations is essential for any programmer.
