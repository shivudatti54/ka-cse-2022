# Recursion

## Table of Contents

- [Recursion](#recursion)
- [Introduction](#introduction)
- [Components of Recursion](#components-of-recursion)
- [How Recursion Works](#how-recursion-works)
- [Example: Factorial](#example-factorial)
- [Example: Fibonacci](#example-fibonacci)
- [Advantages and Disadvantages](#advantages-and-disadvantages)
- [Comparison with Iteration](#comparison-with-iteration)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Recursion is a fundamental programming technique where a method calls itself to solve a problem by breaking it down into simpler sub-problems of the same type. This technique is useful for solving complex problems naturally, but it can also cause stack overflow and higher memory usage. In this chapter, we will explore the concept of recursion, its components, and its applications.

## Components of Recursion

A recursive method consists of two essential components:

1. **Base Case**: A condition that stops the recursion. It is the smallest possible input that can be solved directly.
2. **Recursive Case**: A method calls itself with modified parameters. The recursive case breaks down the problem into smaller sub-problems until it reaches the base case.

## How Recursion Works

To understand how recursion works, let's consider the execution stack of recursive calls. When a method calls itself, a new stack frame is created, and the method's parameters are pushed onto the stack. The method executes until it reaches the base case, at which point the recursion stops, and the method returns. The stack frames are then popped off the stack, and the final result is returned.

## Example: Factorial

The factorial of a number `n` is the product of all positive integers less than or equal to `n`. We can write a recursive method to calculate the factorial as follows:

```java
public static int factorial(int n) {
 // Base case
 if (n == 0 || n == 1) {
 return 1;
 }
 // Recursive case
 return n * factorial(n - 1);
}
```

For example, `factorial(5)` would return `120`, which is the product of all positive integers less than or equal to `5`.

## Example: Fibonacci

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. We can write a recursive method to generate the Fibonacci sequence as follows:

```java
public static int fibonacci(int n) {
 // Base case
 if (n <= 1) {
 return n;
 }
 // Recursive case
 return fibonacci(n - 1) + fibonacci(n - 2);
}
```

For example, `fibonacci(5)` would return `5`, which is the fifth number in the Fibonacci sequence.

## Advantages and Disadvantages

Recursion has several advantages and disadvantages:

**Advantages**

- Clean and elegant code
- Solves complex problems naturally
- Good for tree/graph traversal

**Disadvantages**

- Can cause stack overflow
- Higher memory usage
- May be slower than iteration

## Comparison with Iteration

Recursion and iteration are two different approaches to solving problems. The following table compares the two:

| Feature         | Recursion     | Iteration    |
| --------------- | ------------- | ------------ |
| Memory Usage    | Higher        | Lower        |
| Speed           | May be slower | Faster       |
| Code Complexity | Cleaner       | More complex |

## Real-World Applications

Recursion has several real-world applications, including:

- Tree/graph traversal
- Parsing expressions
- Solving complex problems naturally

## Exam Tips

- Focus on identifying the base case and recursive case in a recursive method.
- Understand the advantages and disadvantages of using recursion.
- Practice solving problems using recursion, such as calculating factorials and Fibonacci numbers.

## Key Takeaways

- Recursion is a programming technique where a method calls itself to solve a problem.
- A recursive method consists of a base case and a recursive case.
- Recursion is useful for solving complex problems naturally, but it can also cause stack overflow and higher memory usage.
- Recursion has several advantages and disadvantages, and it is essential to understand when to use it.
