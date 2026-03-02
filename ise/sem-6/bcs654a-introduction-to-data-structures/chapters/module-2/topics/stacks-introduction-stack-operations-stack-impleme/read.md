# **Stacks: Introduction, Stack Operations, Stack Implementation using Arrays, Applications of Stacks**

## **Introduction to Stacks**

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed. Stacks are used to store a collection of elements, and they support two primary operations: push and pop.

### Definition:

A stack is a data structure that allows you to add and remove elements from the top of the stack.

### Characteristics:

- Last In, First Out (LIFO) principle
- Elements are added and removed from the top of the stack
- Can be thought of as a vertical pile of plates, where plates are added and removed from the top

## **Stack Operations**

A stack supports two primary operations:

### 1. Push:

The push operation adds an element to the top of the stack.

- Example: `stack.push(10)` adds the element 10 to the top of the stack

### 2. Pop:

The pop operation removes an element from the top of the stack.

- Example: `stack.pop()` removes the top element from the stack

## **Stack Implementation using Arrays**

An array can be used to implement a stack. The top of the stack is represented by the last index of the array.

### Implementation:

```markdown
class Stack {
private int[] array;
private int top;

    public Stack(int size) {
        array = new int[size];
        top = -1;
    }

    public void push(int element) {
        if (top < array.length - 1) {
            array[++top] = element;
        } else {
            System.out.println("Stack is full");
        }
    }

    public int pop() {
        if (top >= 0) {
            return array[top--];
        } else {
            System.out.println("Stack is empty");
            return -1;
        }
    }

}
```

### Example Usage:

```markdown
public class Main {
public static void main(String[] args) {
Stack stack = new Stack(5);
stack.push(10);
stack.push(20);
System.out.println(stack.pop()); // prints 20
System.out.println(stack.pop()); // prints 10
System.out.println(stack.pop()); // prints -1 (Stack is empty)
}
}
```

## **Applications of Stacks**

Stacks have several applications in computer science and real-life scenarios:

### 1. Evaluating Postfix Expressions:

Stacks can be used to evaluate postfix expressions.

- Example: `3 4 +` can be evaluated as `3 + 4`

### 2. Parsing:

Stacks are used in parsing techniques, such as parsing XML or HTML documents.

### 3. Implementing Recursion:

Stacks can be used to implement recursive functions.

- Example: A recursive function can be implemented using a stack to store the function calls.

### 4. Implementing Undo and Redo Functions:

Stacks can be used to implement undo and redo functions in text editors or other applications.

## Conclusion

In conclusion, stacks are a fundamental data structure in computer science. They support two primary operations: push and pop. Arrays can be used to implement stacks, and they have several applications in computer science and real-life scenarios. Understanding stacks is essential for any programmer, and this study material provides a comprehensive introduction to stacks.
