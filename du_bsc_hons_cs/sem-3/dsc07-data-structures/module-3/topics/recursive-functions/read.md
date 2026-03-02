# Recursive Functions
## Introduction

Recursion is a fundamental concept in computer science that allows a function to call itself repeatedly until it reaches a base case that stops the recursion. Recursive functions are used to solve problems that can be broken down into smaller sub-problems of the same type. In this topic, we will explore the concept of recursive functions, their importance, and how to implement them.

Recursion is a powerful technique for solving problems, but it can also be less efficient than other methods, such as iteration, due to the overhead of function calls and returns. However, for certain problems, recursion provides a more elegant and intuitive solution.

## Key Concepts

### Base Case

A base case is a condition that stops the recursion. It is a trivial case that can be solved directly without calling the function again. The base case is essential to prevent infinite recursion.

### Recursive Case

A recursive case is a condition that requires the function to call itself to solve the problem. The recursive case breaks down the problem into smaller sub-problems of the same type.

### Recursive Function

A recursive function is a function that calls itself repeatedly until it reaches a base case. The function solves the problem by breaking it down into smaller sub-problems and solving each sub-problem recursively.

### Types of Recursion

There are two types of recursion:

*   **Direct Recursion**: A function calls itself directly.
*   **Indirect Recursion**: A function calls another function, which in turn calls the first function.

## Examples

### Example 1: Factorial Function

The factorial function is a classic example of a recursive function. The factorial of a number `n` is the product of all positive integers less than or equal to `n`.

```c
int factorial(int n) {
    if (n == 0) { // base case
        return 1;
    } else { // recursive case
        return n * factorial(n - 1);
    }
}
```

### Example 2: Fibonacci Series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers.

```c
int fibonacci(int n) {
    if (n == 0 || n == 1) { // base case
        return n;
    } else { // recursive case
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
```

### Example 3: Binary Search

Binary search is an algorithm that finds an element in a sorted array by dividing the array in half and searching for the element in one of the two halves.

```c
int binarySearch(int arr[], int low, int high, int target) {
    if (low > high) { // base case
        return -1;
    } else { // recursive case
        int mid = (low + high) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearch(arr, mid + 1, high, target);
        } else {
            return binarySearch(arr, low, mid - 1, target);
        }
    }
}
```

## Exam Tips

1.  Understand the concept of recursion and how it works.
2.  Identify the base case and the recursive case in a recursive function.
3.  Be able to write a recursive function to solve a problem.
4.  Understand the difference between direct and indirect recursion.
5.  Be able to analyze the time and space complexity of a recursive function.
6.  Practice solving problems using recursion, such as the factorial function, Fibonacci series, and binary search.
7.  Be able to identify and avoid infinite recursion.