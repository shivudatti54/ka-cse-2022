# Recursion

## Overview

Recursion is a programming technique where a method calls itself to solve a problem by breaking it down into simpler sub-problems of the same type. It consists of a base case and a recursive case. Recursion is useful for solving complex problems naturally, but can also cause stack overflow and higher memory usage.

## Key Points

- Recursion breaks down a complex problem into simpler sub-problems of the same type.
- A recursive method consists of a base case and a recursive case.
- The base case stops the recursion, while the recursive case calls itself with modified parameters.
- Recursion is useful for tree/graph traversal and solving complex problems naturally.
- Recursion can cause stack overflow and higher memory usage.
- Recursion may be slower than iteration.

## Important Definitions

- **Base Case**: Condition that stops the recursion.
- **Recursive Case**: Method calls itself with modified parameters.
- **Recursion**: Programming technique where a method calls itself to solve a problem.

## Key Formulas / Syntax

```java
public static int factorial(int n) {
 if (n == 0 || n == 1) return 1; // Base case
 return n * factorial(n - 1); // Recursive case
}
```

## Comparisons

| Feature         | Recursion     | Iteration    |
| --------------- | ------------- | ------------ |
| Memory Usage    | Higher        | Lower        |
| Speed           | May be slower | Faster       |
| Code Complexity | Cleaner       | More complex |

## Exam Tips

- Focus on identifying the base case and recursive case in a recursive method.
- Understand the advantages and disadvantages of using recursion.
- Practice solving problems using recursion, such as calculating factorials and Fibonacci numbers.
