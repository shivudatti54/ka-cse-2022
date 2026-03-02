# Recursion


## Table of Contents

- [Recursion](#recursion)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Recursion](#definition-of-recursion)
  - [How Recursion Works](#how-recursion-works)
  - [Types of Recursion](#types-of-recursion)
  - [Recursion vs Iteration](#recursion-vs-iteration)
- [Examples](#examples)
  - [Example 1: Factorial Calculation](#example-1-factorial-calculation)
  - [Example 2: Fibonacci Sequence](#example-2-fibonacci-sequence)
  - [Example 3: Sum of Array Elements](#example-3-sum-of-array-elements)
- [Exam Tips](#exam-tips)

## Introduction

Recursion is one of the most powerful and elegant programming techniques where a function calls itself to solve a problem by breaking it down into smaller, more manageable sub-problems. This concept is fundamental to computer science and forms the backbone of many algorithms used in sorting, searching, tree traversals, and combinatorial problems. In the context of problem solving using C programming, recursion provides an intuitive way to express complex problems in a clean, mathematical style.

The importance of recursion in computer science cannot be overstated. It allows programmers to solve problems that would be extremely difficult or impossible to tackle using iterative approaches alone. Many real-world problems have recursive structures - from file systems (folders containing subfolders) to mathematical sequences (Fibonacci numbers) to divide-and-conquer algorithms. Understanding recursion is essential for any computer science student, as it appears prominently in data structures, algorithms, operating systems, and compiler design.

In the University of Delhi's Computer Science curriculum, recursion is taught as a bridge between basic programming constructs and advanced algorithmic thinking. Mastery of recursion demonstrates a student's ability to think recursively - a critical skill for solving complex computational problems.

## Key Concepts

### Definition of Recursion

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. A recursive function consists of two essential components: the BASE CASE (also called the terminating condition) and the RECURSIVE CASE (the part where the function calls itself). The base case prevents infinite recursion by providing a condition that stops the recursive calls, while the recursive case breaks the problem into smaller instances of the same problem.

### How Recursion Works

When a recursive function is called, the following sequence of events occurs:

1. The function receives input (parameters)
2. It checks if the base case is satisfied - if yes, it returns a result
3. If not, it performs some computation and makes a recursive call with modified parameters
4. The recursive call returns a value which is used to compute the final result

Each recursive call creates a new stack frame in memory, storing local variables and the return address. This stack frame persists until the recursive call completes and returns. Understanding this call stack mechanism is crucial for tracing recursive algorithms and avoiding stack overflow errors.

### Types of Recursion

TAIL RECURSION occurs when the recursive call is the last statement in the function. In tail recursion, there is no computation after the recursive call returns, making it possible for compilers to optimize by reusing the same stack frame. However, C compilers typically do not perform this optimization, so tail recursion is not more efficient in C.

HEAD RECURSION occurs when the recursive call is the first operation in the function, before any other processing. The computation happens after all recursive calls return.

TREE RECURSION occurs when a function makes multiple recursive calls within itself, creating a tree-like structure of calls. The classic example is the Fibonacci sequence calculation, where each call branches into two more calls.

NESTED RECURSION occurs when a recursive call is passed as an argument to another recursive call. This type is less common and can be harder to analyze.

### Recursion vs Iteration

Both recursion and iteration repeat computations, but they differ fundamentally. Iteration uses loops (for, while, do-while) and maintains state in variables, while recursion achieves repetition through function calls. Recursion often produces more elegant and readable code for problems with recursive structure, but it incurs the overhead of function call stack management. Iteration is generally more memory-efficient since it doesn't require additional stack space. For problems where both approaches are feasible, iteration is usually preferred in C due to stack limitations.

## Examples

### Example 1: Factorial Calculation

The factorial of a non-negative integer n (denoted as n!) is the product of all positive integers less than or equal to n. Mathematically, n! = n × (n-1) × (n-2) × ... × 2 × 1, with 0! = 1.

```c
#include <stdio.h>

// Function to calculate factorial using recursion
int factorial(int n) {
    // Base case
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case
    return n * factorial(n - 1);
}

int main() {
    int number = 5;
    printf("Factorial of %d is %d\n", number, factorial(number));
    return 0;
}
```

TRACE: factorial(5) = 5 × factorial(4) = 5 × 4 × factorial(3) = 5 × 4 × 3 × factorial(2) = 5 × 4 × 3 × 2 × factorial(1) = 5 × 4 × 3 × 2 × 1 = 120

### Example 2: Fibonacci Sequence

The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

```c
#include <stdio.h>

// Function to find nth Fibonacci number
int fibonacci(int n) {
    // Base cases
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 10;
    printf("Fibonacci sequence up to %d terms:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    return 0;
}
```

OUTPUT: Fibonacci sequence up to 10 terms: 0 1 1 2 3 5 8 13 21 34

NOTE: This implementation demonstrates tree recursion but has exponential time complexity O(2^n). For practical applications, dynamic programming approaches are preferred.

### Example 3: Sum of Array Elements

Recursion can be used to calculate the sum of elements in an array by breaking it down into adding one element to the sum of the remaining elements.

```c
#include <stdio.h>

// Function to find sum of array elements using recursion
int sumArray(int arr[], int size) {
    // Base case: empty array has sum 0
    if (size <= 0) {
        return 0;
    }
    // Recursive case: last element + sum of remaining elements
    return arr[size - 1] + sumArray(arr, size - 1);
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("Sum of array elements: %d\n", sumArray(arr, size));
    return 0;
}
```

OUTPUT: Sum of array elements: 150

TRACE: sumArray([10,20,30,40,50], 5) = 50 + sumArray([10,20,30,40,50], 4) = 50 + 40 + sumArray([10,20,30,40,50], 3) = 50 + 40 + 30 + sumArray([10,20,30,40,50], 2) = 50 + 40 + 30 + 20 + sumArray([10,20,30,40,50], 1) = 50 + 40 + 30 + 20 + 10 + sumArray([10,20,30,40,50], 0) = 50 + 40 + 30 + 20 + 10 + 0 = 150

## Exam Tips

INTERNAL ASSESSMENT AND END SEMESTER EXAM PREPARATION:

1. ALWAYS IDENTIFY THE BASE CASE FIRST: In any recursive solution, the base case is your terminating condition. Without it, your program will result in infinite recursion and stack overflow. Write the base case first, then build the recursive case.

2. VERIFY RECURSIVE CALL PROGRESS: Ensure that each recursive call moves toward the base case by modifying parameters appropriately. For example, if processing n elements, your recursive call should process n-1 elements.

3. DRAW RECURSION TREES FOR TRACE: During exams, when asked to trace a recursive function, draw a tree diagram showing each call and its return value. This helps avoid confusion and demonstrates clear understanding to evaluators.

4. RECURSION DEPTH MATTERS: Remember that C has limited stack memory. Avoid extremely deep recursion (typically more than a few thousand calls) as it may cause stack overflow. For deep recursion, consider using iterative solutions.

5. UNDERSTAND WHEN TO USE RECURSION: Recursion is ideal for problems with recursive structure - tree traversals, combinatorial problems, divide-and-conquer algorithms, and mathematical sequences. For simple repetitive tasks, iteration is often better.

6. ANALYZE COMPLEXITY CAREFULLY: Be prepared to analyze time and space complexity of recursive algorithms. Space complexity is typically O(n) due to stack frames, while time complexity depends on the number of recursive calls.

7. MEMORIZE STANDARD RECURSIVE PATTERNS: Common recursive problems like factorial, Fibonacci, sum of digits, palindrome checking, binary search, and string reversal have standard patterns. Memorize these approaches as they frequently appear in exams.

8. RECURSION IN BINARY SEARCH: Binary search using recursion is a key topic in your module. Remember the key insight: at each step, either search the left half or right half by adjusting the low and high indices, making a recursive call with reduced search space.